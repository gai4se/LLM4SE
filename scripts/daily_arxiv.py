import requests
import xml.etree.ElementTree as ET
import json 
import datetime

base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

def search_arxiv_papers(keywords, max_results):
    # Join the keywords with 'AND' to create the search query
    # abs:%22large+language+model%22+AND+abs:%22program+repair%22
    encoded_keywords = ["abs:%22{}%22".format(k) for k in keywords]
    query = '+AND+'.join(encoded_keywords)
    # Construct the API query URL

    url = f"https://export.arxiv.org/api/query?search_query={query}&sortBy=lastUpdatedDate&sortOrder=descending&max_results={max_results}"
    try:
        # Send a GET request to the Arxiv API
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors
        # Parse the XML response
        root = ET.fromstring(response.content)

        results = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            paper_id = entry.find('{http://www.w3.org/2005/Atom}id').text
            short_id = paper_id.split("/")[-1]
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            updated_date = entry.find('{http://www.w3.org/2005/Atom}updated').text

            results.append((short_id, title, summary, updated_date))
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_daily_papers(keyword_sets, max_results=10):
    content = {}
    for keywords in keyword_sets:
        search_results = search_arxiv_papers(keywords, max_results)
        print(search_results)
        for result in search_results:
            paper_id, paper_title, paper_summary, updated_date = result
            updated_date = updated_date.split("T")[0]
            ver_pos = paper_id.find('v')
            if ver_pos == -1:
                paper_key = paper_id
            else:
                paper_key = paper_id[0:ver_pos]   
    
            paper_url = arxiv_url + 'abs/' + paper_key
            code_url            = base_url + paper_id
            # source code link    
            r = requests.get(code_url).json()
            repo_url = None
            if "official" in r and r["official"]:
                repo_url = r["official"]["url"]
            
            content[paper_key] = {
                "id": paper_id, 
                 "url": paper_url,
                 "code_url": repo_url,
                 "title": paper_title,
                 "updated_date": updated_date
            }
    return content

def sort_papers(papers):
    sorted_dict = dict(sorted(papers.items(), key=lambda x: datetime.datetime.strptime(x[1]["updated_date"], '%Y-%m-%d'), reverse=True))
    return sorted_dict

def json_to_md(json_data, md_filename, maximum_papers=20):
    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-','.')
    
    data = json_data

    # write data into README.md
    with open(md_filename, 'w') as f:
        f.write("## Updated on " + DateNow + "\n")
        f.write("<details>\n")
        f.write("  <summary>Table of Contents</summary>\n")
        f.write("  <ol>\n")
        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            kw = keyword.replace(' ','-')      
            f.write(f"    <li><a href=#{kw}>{keyword}</a></li>\n")
        f.write("  </ol>\n")
        f.write("</details>\n\n")
        
        for category, papers in data.items():
            content = sort_papers(papers)
            kw = category.replace(' ','-') 
            f.write(f'<h2 id="{kw}"> {category} </h2>\n\n')
            # f.write(f'## {category}\n\n')
            f.write('| Title | ArXiv Link | GitHub Link | Last Update |\n')
            f.write('| --- | --- | --- | --- |\n')
            idx = 0
            for paper_id, paper_info in content.items():
                title = paper_info["title"].replace("\n", " ")
                arxiv_link = paper_info["url"]
                github_link = paper_info["code_url"]
                updated_date = paper_info["updated_date"]
                f.write(f'| {title} | [{paper_id}]({arxiv_link}) | {github_link} | {updated_date} |\n')
                idx += 1
                if idx > maximum_papers:
                    break
            f.write('\n')

def update_json_file(filename, data_dict):
    '''
    daily update json file using data_dict
    '''
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
            
    json_data = m.copy() 
    
    # update papers in each keywords         
    for keyword in data_dict.keys():
        papers = data_dict[keyword]
        
        if keyword in json_data.keys():
            json_data[keyword].update(papers)
        else:
            json_data[keyword] = papers
    
    with open(filename,"w") as f:
        json.dump(json_data,f)
    
    return json_data


def main():
    max_queries = 30
    max_display = 30
    md_file = "arxiv.md"
    json_file = "papers/arxiv/data.json"
    # # Open the JSON file
    with open('config/arxiv_keywords.json') as file:
        # Load the contents of the file
        data = json.load(file)
        
    contents = {}
    
    total_data = 0
    for topic_info in data:
        topic = topic_info["topic"]
        keyword_sets = topic_info["keyword_sets"]
        contents[topic] = get_daily_papers(keyword_sets, max_queries)
        total_data += len(contents[topic])
    
    if total_data == 0:
        raise ValueError("Data is empty")
    
    json_to_md(contents, md_file, max_display)
    
if __name__ == "__main__":
    main()