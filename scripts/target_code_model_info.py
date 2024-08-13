from transformers import AutoConfig, AutoModel
from huggingface_hub import HfApi

def get_model_information(model):

    print("Collecting information for model: {0}".format(model.modelId))

    # Get the model configuration
    config = AutoConfig.from_pretrained(model.modelId)

    # Get the model architecture
    model_arch = AutoModel.from_pretrained(model.modelId)
    
    # Get the model size in bytes
    model_size_bytes = sum(p.numel() for p in model_arch.parameters() if p.requires_grad) * 4  # Assuming float32
    
    # Convert the model size to megabytes (MB)
    model_size_mb = model_size_bytes / (1024 ** 2)
    
    # Get the total number of model parameters
    num_params = sum(p.numel() for p in model_arch.parameters())

    info_dict={'date': model.lastModified, 'model size (MB)': model_size_mb, 'num params': num_params, 'model id': model.modelId}

    return info_dict
    



def retrieve_all_huggingface_models(filtering_language):
    return list(HfApi().list_models(language=filtering_language))


def group_models_by_year(model_list):
    year_dict = {}

    for model in model_list:
        year = int(model.lastModified.split('-')[0])
        if year not in year_dict.keys():
            year_dict[year] = []
        year_dict[year].append(model)
    

    for year in range(2025, 2014, -1):
        if year in year_dict:
            year_dict[year] = sorted(year_dict[year], key=lambda x: x.lastModified, reverse=True)

            print("### {} {}\n".format(year,len(year_dict[year])))


def print_model_list(model_list):

    model_info_dict = {}

    for model in model_list:
        model_info=get_model_information(model)
        model_info_dict[model_info['date']]=model_info

    # sort model_info_dict by date
    print('| Date | Model Name  | # of Parameters /Model Size | Huggingface  |')

    for date, model_info in model_info_dict.items():
        # | Year-Id | Model Name  | # of Parameters /Model Size | Huggingface  |
        
        # Print the model information
        print("| {0} | {1} | TBA | {2}/{3} | {4} |".format(model_info['date'], model_info['model name'], model_info['num params'], model_info['model size (MB)'], '[link](https://huggingface.co/{})'.format(model_info['model id'])))


if __name__ == "__main__":

    filtering_language = "code"
    model_list = retrieve_all_huggingface_models(filtering_language)
    group_models_by_year(model_list)

    print_model_list(model_list)
