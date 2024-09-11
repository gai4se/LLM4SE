# Large Language Model for Software Engineering

The collection is actively updated with the help of an internal literature search engine.

# Table of Contents

| [Code Model List](#model-list) |
| [Popular Code Model List](#popular-model-list) |
| [Paper List](#paper-list) |
| [Paper Stats](#paper-stats) |
| [Recent Preprints](./arxiv.md) |

<a name="model-list"></a>

## Model List

### 2024 (616 Models as of March 6 2024)

<details>
<summary>Click to expand!</summary>


|  |  |  |
|:--------:|:--------:|:--------:|
|   Kquant03/TechxGenus-starcoder2-15b-instruct-GGUF   |   bartowski/starcoder2-15b-instruct-exl2   |   bartowski/starcoder2-15b-exl2   |
|   bigcode/starcoder2-15b   |   bigcode/starcoder2-7b   |   bartowski/starcoder2-15b-instruct-GGUF   |
|   semantixai/LloroV2   |   bognix/digits-recognition-app   |   Hadiboo/boguey   |
|   brescia/IndoBERT   |   ajibawa-2023/OpenHermes-2.5-Code-290k-13B   |   TechxGenus/starcoder2-15b-instruct   |
|   abideen/starcoder2-chat   |   TechxGenus/starcoder2-7b-instruct   |   TechxGenus/starcoder2-3b-instruct   |
|   bartowski/Magic-Dolphin-7b-GGUF   |   alibidaran/Gemma2_Python_instruction   |   solidrust/Magic-Dolphin-7b-AWQ   |
|   TechxGenus/CodeGemma-7b-GPTQ   |   TechxGenus/CodeGemma-2b-GPTQ   |   bartowski/Magic-Dolphin-7b-exl2   |
|   senseable/moe-x33   |   InferenceIllusionist/Magic-Dolphin-7b   |   codellama/CodeLlama-34b-Instruct-hf   |
|   codellama/CodeLlama-13b-Instruct-hf   |   codellama/CodeLlama-7b-Instruct-hf   |   Mollel/swahili_LLaMA_7Bv0.1_GGUF   |
|   budecosystem/code-millenials-34b   |   macadeliccc/Orca-SOLAR-4x10.7b   |   ed001/datascience-coder-6.7b   |
|   Locutusque/Orca-2-13b-SFT-v6   |   Orkhan/llama-2-7b-absa   |   bigcode/starcoder2-3b   |
|   arzeth/opencsg-starcoder2-15b-v0.1-GGUF   |   ajibawa-2023/Code-290k-6.7B-Instruct   |   ajibawa-2023/Code-13B   |
|   ajibawa-2023/Python-Code-33B   |   ajibawa-2023/Code-290k-13B   |   codellama/CodeLlama-70b-Instruct-hf   |
|   m-a-p/OpenCodeInterpreter-CL-70B   |   opencsg/opencsg-phi-2-v0.1   |   opencsg/opencsg-stable-code-3b-v1   |
|   bartowski/OpenCodeInterpreter-GM-7B-exl2   |   solidrust/Hercules-2.5-Mistral-7B-AWQ   |   solidrust/Hercules-3.1-Mistral-7B-AWQ   |
|   opencsg/opencsg-starcoder2-15b-v0.1   |   opencsg/opencsg-starcoder2-7b-v0.1   |   opencsg/opencsg-starcoder2-3b-v0.1   |
|   opencsg/opencsg-codeLlama-13b-v0.2   |   opencsg/opencsg-codeLlama-7b-v0.2   |   bartowski/Hercules-3.1-Mistral-7B-GGUF   |
|   opencsg/opencsg-CodeLlama-34b-v0.2   |   mlx-community/OpenCodeInterpreter-SC2-7B-4bit   |   mlx-community/OpenCodeInterpreter-SC2-3B-4bit   |
|   mlx-community/starcoder2-7b-4bit   |   JPAiversion/ImageFX   |   Lotem/check   |
|   parsi-ai-nlpclass/ParsbertHallu   |   m-a-p/OpenCodeInterpreter-DS-1.3B   |   m-a-p/OpenCodeInterpreter-DS-6.7B   |
|   m-a-p/OpenCodeInterpreter-DS-33B   |   m-a-p/OpenCodeInterpreter-CL-7B   |   m-a-p/OpenCodeInterpreter-CL-13B   |
|   m-a-p/OpenCodeInterpreter-CL-34B   |   m-a-p/OpenCodeInterpreter-SC2-3B   |   m-a-p/OpenCodeInterpreter-SC2-7B   |
|   m-a-p/OpenCodeInterpreter-SC2-15B   |   OrionStarAI/Orion-14B-Chat-Plugin   |   OrionStarAI/Orion-14B-Chat-RAG   |
|   OrionStarAI/Orion-14B-LongChat   |   OrionStarAI/Orion-14B-Chat-Int4   |   OrionStarAI/Orion-14B-Base-Int4   |
|   OrionStarAI/Orion-14B-Chat   |   OrionStarAI/Orion-14B-Base   |   bartowski/OpenHermes-2.5-Code-290k-13B-exl2   |
|   nold/starcoder2-15b-GGUF   |   Enderchef/JarvisAI   |   nold/starcoder2-7b-GGUF   |
|   LoneStriker/OpenHermes-2.5-Code-290k-13B-8.0bpw-h8-exl2   |   LoneStriker/OpenHermes-2.5-Code-290k-13B-6.0bpw-h6-exl2   |   LoneStriker/OpenHermes-2.5-Code-290k-13B-5.0bpw-h6-exl2   |
|   LoneStriker/OpenHermes-2.5-Code-290k-13B-4.0bpw-h6-exl2   |   LoneStriker/OpenHermes-2.5-Code-290k-13B-3.0bpw-h6-exl2   |   LoneStriker/OpenHermes-2.5-Code-290k-13B-GGUF   |
|   aneesarom/Helmet-Violation-Detection   |   nold/starcoder2-3b-GGUF   |   second-state/StarCoder2-7B-GGUF   |
|   second-state/StarCoder2-15B-GGUF   |   second-state/StarCoder2-3B-GGUF   |   Locutusque/Hercules-3.1-Mistral-7B   |
|   mlx-community/starcoder2-15b-4bit   |   mlx-community/starcoder2-3b-4bit   |   ritwikraha/khabib_sketch_LoRA   |
|   BeannRL/RocketLeagueWallpapers   |   MaziyarPanahi/OpenCodeInterpreter-DS-6.7B-GGUF   |   TechxGenus/CodeGemma-7b   |
|   defog/sqlcoder   |   LeanAI/llama-2-7b-emw-2   |   nuprl/EditCoder-6.7b-v1   |
|   mlx-community/math-phi-v1   |   CISCai/OpenCodeInterpreter-DS-6.7B-SOTA-GGUF   |   MBZUAI/MobiLlama-08B   |
|   MBZUAI/MobiLlama-1B   |   MBZUAI/MobiLlama-05B   |   bjornbundgaard/Mistral-16bit-merged   |
|   mlx-community/gemma-2b-coder   |   brittlewis12/OpenCodeInterpreter-DS-1.3B-GGUF   |   patrickbdevaney/WizardLM-1b-GGUF   |
|   andythetechnerd03/BERT-tiny_AI-Human   |   shareAI/CodeLLaMA-chat-13b-Chinese   |   rxploit/CodeGenRxp   |
|   PipableAI/pip-sql-1.3b   |   xiangxinai/Xiangxin-3B   |   bartowski/Code-290k-6.7B-Instruct-exl2   |
|   TechxGenus/CodeGemma-2b   |   bartowski/OpenCodeInterpreter-DS-33B-exl2   |   Kryptone/RVCollection-Revamped   |
|   LoneStriker/OpenCodeInterpreter-DS-33B-8.0bpw-h8-exl2   |   LoneStriker/OpenCodeInterpreter-DS-33B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-33B-5.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-DS-33B-4.65bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-33B-4.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-33B-3.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-13B-8.0bpw-h8-exl2   |   LoneStriker/OpenCodeInterpreter-CL-13B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-13B-5.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-13B-4.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-13B-3.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-13B-GGUF   |
|   bartowski/OpenCodeInterpreter-CL-13B-exl2   |   LoneStriker/OpenCodeInterpreter-DS-33B-GGUF   |   LoneStriker/OpenCodeInterpreter-DS-6.7B-8.0bpw-h8-exl2   |
|   LoneStriker/OpenCodeInterpreter-DS-6.7B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-6.7B-5.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-6.7B-4.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-DS-6.7B-3.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-DS-6.7B-GGUF   |   LoneStriker/OpenCodeInterpreter-CL-70B-3.5bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-70B-2.65bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-70B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-70B-5.0bpw-h6-exl2   |
|   second-state/WizardCoder-Python-7B-v1.0-GGUF   |   LoneStriker/OpenCodeInterpreter-CL-34B-8.0bpw-h8-exl2   |   second-state/CodeLlama-13B-Instruct-GGUF   |
|   LoneStriker/OpenCodeInterpreter-CL-70B-4.65bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-34B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-70B-4.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-34B-5.0bpw-h6-exl2   |   second-state/phi-2-GGUF   |   LoneStriker/OpenCodeInterpreter-CL-70B-3.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-34B-4.65bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-70B-2.4bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-34B-4.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-34B-3.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-70B-GGUF   |   LoneStriker/OpenCodeInterpreter-CL-7B-8.0bpw-h8-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-7B-6.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-7B-5.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-7B-4.0bpw-h6-exl2   |
|   LoneStriker/OpenCodeInterpreter-CL-7B-3.0bpw-h6-exl2   |   LoneStriker/OpenCodeInterpreter-CL-7B-GGUF   |   mlx-community/OpenCodeInterpreter-DS-33B-hf-4bit-mlx   |
|   mlx-community/OpenCodeInterpreter-DS-6.7B-4bit   |   aryachakraborty/GEMMA-2B-NL-SQL   |   nisten/BigCodeLlama-92b   |
|   bartowski/OpenCodeInterpreter-CL-7B-exl2   |   bartowski/OpenCodeInterpreter-DS-6.7B-exl2   |   Hugi-R/OpenCodeInterpreter-DS-33B-GGUF   |
|   brittlewis12/OpenCodeInterpreter-DS-6.7B-GGUF   |   MaziyarPanahi/Llama-2-7b-hf-codealpaca-8bit   |   antoniomae/XTTS_V2_CPU_working   |
|   antoniomae/coquixtts   |   ozayezerceli/TinyLama-1.1b-CypherGen   |   JiZha/Bailing-SQL   |
|   stabilityai/stable-code-3b   |   mrm8488/phi-2-coder   |   MAISAAI/gemma-2b-coder   |
|   SameerArz/Sameer-google-gemma-7b   |   bigscience/bloomz-7b1   |   second-state/CodeLlama-70b-Instruct-hf-GGUF   |
|   ranamhamoud/storytellai   |   ThatFkrDurk666/idk   |   ba8im/phi-2-bash-v3   |
|   ba8im/phi-2-bash-v2   |   Kauru/DialoGPT-medium-Ranni   |   claudios/cotext-1-ccg   |
|   lamm-mit/BioinspiredLLM   |   codesage/codesage-base   |   codesage/codesage-large   |
|   codesage/codesage-small   |   ba8im/phi-2-bash-v1   |   Miras-P/KazDALLE   |
|   ba8im/phi-2-bash-v0   |   bartowski/Hercules-3.1-Mistral-7B-exl2   |   Kukedlc/NeuralMaxime-7B-DPO   |
|   arunp77/Machine-learning   |   erfanzar/LinguaMatic-Tiny   |   bartowski/speechless-thoughts-mistral-7b-v1.0-exl2   |
|   shibing624/code-autocomplete-distilgpt2-python   |   madroid/phi2-4bit-mlx   |   bartowski/speechless-sparsetral-mistral-16x7b-MoE-exl2   |
|   ValiantLabs/Fireplace-13b   |   LunaticPython161/starcoderbase-3b   |   emre/java_8m_methods_doc2vec   |
|   DamienDrash/CodeLlama-70B-Instruct   |   Juanfco/Jotaefe   |   bartowski/OpenMath-CodeLlama-7b-Python-hf-exl2   |
|   uukuguy/speechless-thoughts-mistral-7b-v1.0   |   bartowski/OpenMath-Mistral-7B-v0.1-hf-exl2   |   nold/OpenMath-Mistral-7B-v0.1-hf-GGUF   |
|   PipableAI/pip-SQL-1B   |   nvidia/OpenMath-Llama-2-70b   |   nvidia/OpenMath-CodeLlama-34b-Python-hf   |
|   nvidia/OpenMath-CodeLlama-34b-Python   |   nvidia/OpenMath-CodeLlama-13b-Python-hf   |   nvidia/OpenMath-CodeLlama-13b-Python   |
|   nvidia/OpenMath-CodeLlama-7b-Python-hf   |   nvidia/OpenMath-CodeLlama-7b-Python   |   nvidia/OpenMath-Mistral-7B-v0.1-hf   |
|   nvidia/OpenMath-Mistral-7B-v0.1   |   nvidia/OpenMath-CodeLlama-70b-Python-hf   |   nvidia/OpenMath-CodeLlama-70b-Python   |
|   nvidia/OpenMath-Llama-2-70b-hf   |   hamel/code-llama-test   |   nold/CroissantLLMChat-v0.1-GGUF   |
|   edumunozsala/aguila-7b-instructft-bactrian-x   |   alvarophylipe/portuguese-fake-news-classification   |   uukuguy/speechless-thoughts-mistral-7b   |
|   Palmono/Baharai   |   bigcode/starcoder   |   croissantllm/CroissantLLMBase   |
|   croissantllm/CroissantLLMChat-v0.1   |   PipableAI/pip-SQL-7B   |   tyson0420/stack_codellama-7b-inst   |
|   MH0386/phi-2-napoleon-bonaparte   |   nold/CroissantLLMBase-GGUF   |   OEvortex/HelpingAI-unvelite-GGUF   |
|   tyson0420/stack_llama_fil_ai   |   Agra2002/finetuned_bertuncased_sentiment   |   SJ182120/codellama_trial_v1   |
|   MaziyarPanahi/sqlcoder-7b-GGUF   |   edumunozsala/TinyLlama-1431k-python-coder   |   exzread/MIT-AI   |
|   Locutusque/Hercules-2.0-Mistral-7B   |   Locutusque/Hercules-2.5-Mistral-7B   |   uukuguy/speechless-sparsetral-mistral-16x7b-MoE   |
|   netcat420/MHENN5-GGUF   |   bartowski/Hercules-2.5-Mistral-7B-exl2   |   bartowski/Hercules-2.0-Mistral-7B-exl2   |
|   lamm-mit/ProteinMechanicsDiffusionDesign   |   nextai-team/apollo-v1-7b   |   nextai-team/Moe-2x7b-QA-Code   |
|   andrewrreed/test-mlops-tagging   |   Gfdegi/cs   |   gonglinyuan/ast_t5_base   |
|   Jack00555/nerwww   |   nextai-team/Moe-4x7b-reason-code-qa   |   HyunaZ/az00   |
|   GobinathR/language-training   |   surya47/medclip-roco   |   nuprl/MultiPLCoder-1b   |
|   maidacundo/phi-moe-loras   |   SRK2203/star   |   saridormi/commit-message-quality-codebert   |
|   microsoft/phi-1   |   microsoft/phi-1_5   |   microsoft/phi-2   |
|   uukuguy/speechless-mistral-hermes-code-7b   |   defog/sqlcoder-7b   |   Rapando/TBL_KPIs   |
|   LLM360/CrystalCoder   |   OEvortex/lite-hermes-GGUF   |   mlx-community/OphiHermes-2.5   |
|   smashmaster/MysteryBox   |   MaziyarPanahi/Hercules-1.0-Mistral-7B-GGUF   |   Sharathhebbar24/code_gpt2   |
|   nextai-team/Moe-3x7b-QA-Code-Inst   |   MaziyarPanahi/Hercules-2.0-Mistral-7B-GGUF   |   MaziyarPanahi/TinyMistral-248M-v2.5-Instruct-GGUF   |
|   fort-capital/phi-2   |   croissantllm/CroissantLLM_training_logs   |   OEvortex/HelpingAI-Lite-GGUF   |
|   mlx-community/phi-2-dpo-7k   |   TheDevilsDaughter/TheDevilsDaughter   |   AISE-TUDelft/BinT5-NoFunName   |
|   AISE-TUDelft/BinT5-C   |   AISE-TUDelft/BinT5-Stripped   |   AISE-TUDelft/BinT5-Decom   |
|   AISE-TUDelft/BinT5-Demi   |   philomath-1209/programming-language-identification   |   zeppdev/phi2-url   |
|   mlx-community/CodelLama7B-inst-dpo-7k-mlx   |   mlx-community/CodeLlama-13b-Instruct-hf-4bit-MLX   |   mlx-community/CodeLlama-7b-Python-4bit-MLX   |
|   MaziyarPanahi/CodeLlama-34b-Instruct-hf-GGUF   |   MaziyarPanahi/CodeLlama-34b-hf-GGUF   |   MaziyarPanahi/CodeLlama-34b-Python-hf-GGUF   |
|   croissantllm/CroissantCool   |   croissantllm/base_185k   |   croissantllm/base_180k   |
|   croissantllm/base_170k   |   croissantllm/base_175k   |   croissantllm/base_160k   |
|   croissantllm/base_165k   |   croissantllm/base_150k   |   croissantllm/base_155k   |
|   croissantllm/base_140k   |   croissantllm/base_145k   |   croissantllm/base_130k   |
|   croissantllm/base_135k   |   croissantllm/base_120k   |   croissantllm/base_125k   |
|   croissantllm/base_110k   |   croissantllm/base_115k   |   croissantllm/base_105k   |
|   croissantllm/base_95k   |   croissantllm/base_100k   |   croissantllm/base_85k   |
|   croissantllm/base_90k   |   croissantllm/base_75k   |   croissantllm/base_80k   |
|   croissantllm/base_65k   |   croissantllm/base_70k   |   croissantllm/base_60k   |
|   croissantllm/base_50k   |   croissantllm/base_55k   |   croissantllm/base_40k   |
|   croissantllm/base_45k   |   croissantllm/base_30k   |   croissantllm/base_35k   |
|   croissantllm/base_20k   |   croissantllm/base_25k   |   croissantllm/base_10k   |
|   croissantllm/base_15k   |   croissantllm/base_5k   |   orion-penner/phi-2-test   |
|   cpans/idcard_ocr   |   Grex69/sqllaama   |   opencsg/opencsg-starcoder-v0.1   |
|   Salesforce/codegen25-7b-multi   |   Salesforce/codegen25-7b-instruct   |   Salesforce/codegen25-7b-mono   |
|   Trelis/CodeLlama-70b-Instruct-hf-function-calling-v3   |   nicocolas/phixtral-2x2_8   |   kroonen/CodeLLaMa-70b-Python-GGUF   |
|   kit-mcse/CodeBERT-Java   |   opencsg/opencsg-CodeLlama-13b-v0.1   |   opencsg/opencsg-CodeLlama-7b-v0.1   |
|   opencsg/opencsg-CodeLlama-34b-v0.1   |   bulentnuran/Votran   |   mlx-community/CodeLlama-70b-hf-4bit-MLX   |
|   TheBloke/CodeLlama-70B-Python-GPTQ   |   TheBloke/CodeLlama-70B-Python-AWQ   |   TheBloke/CodeLlama-70B-Python-GGUF   |
|   TheBloke/CodeLlama-70B-Instruct-GPTQ   |   Artefact2/CodeLlama-70b-Instruct-hf-GGUF   |   Locutusque/Hercules-1.0-Mistral-7B   |
|   TheBloke/CodeLlama-70B-Instruct-AWQ   |   TheBloke/CodeLlama-70B-Instruct-GGUF   |   TheBloke/CodeLlama-70B-hf-GPTQ   |
|   TheBloke/CodeLlama-70B-hf-AWQ   |   TheBloke/CodeLlama-70B-hf-GGUF   |   LoneStriker/CodeLlama-70b-hf-3.5bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-hf-2.65bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-hf-6.0bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-hf-5.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-hf-4.65bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-hf-4.0bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-hf-3.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-hf-2.4bpw-h6-exl2   |   kye/Atom-Z-Tiny-7B   |   LoneStriker/CodeLlama-70b-Instruct-hf-3.5bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-Instruct-hf-2.65bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Instruct-hf-6.0bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Instruct-hf-5.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-Instruct-hf-4.65bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Instruct-hf-4.0bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Instruct-hf-3.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-Instruct-hf-2.4bpw-h6-exl2   |   Plaban81/Moe-4x7b-math-reason-code   |   dhanikitkat/8-emotions-predictor   |
|   nisten/BigCodeLlama-92b-GGUF   |   LoneStriker/CodeLlama-70b-Python-hf-6.0bpw-h6-exl2   |   mlx-community/CodeLlama-34b-Instruct-hf-4bit   |
|   marcel/phi-2-openhermes-30k   |   mlx-community/CodeLlama-7b-Instruct-hf-4bit-MLX   |   LoneStriker/CodeLlama-70b-Python-hf-5.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-Python-hf-4.65bpw-h6-exl2   |   nisten/BigCodeLlama-169b   |   LoneStriker/CodeLlama-70b-Python-hf-4.0bpw-h6-exl2   |
|   LoneStriker/CodeLlama-70b-Python-hf-3.5bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Python-hf-2.65bpw-h6-exl2   |   LoneStriker/CodeLlama-70b-Python-hf-GGUF   |
|   mlx-community/CodeLlama-70b-Python-hf-4bit-MLX   |   mlx-community/CodeLlama-70b-Instruct-hf-4bit-MLX   |   codellama/CodeLlama-70b-Python-hf   |
|   mlx-community/CodeLlama-13b-Python-4bit-MLX   |   LoneStriker/CodeLlama-70b-Instruct-hf-GGUF   |   codellama/CodeLlama-70b-hf   |
|   codellama/CodeLlama-7b-hf   |   codellama/CodeLlama-13b-hf   |   codellama/CodeLlama-34b-hf   |
|   codellama/CodeLlama-7b-Python-hf   |   codellama/CodeLlama-13b-Python-hf   |   codellama/CodeLlama-34b-Python-hf   |
|   HuggingFaceM4/VLM_WebSight_finetuned   |   Locutusque/TinyMistral-248M-v2.5-Instruct   |   Locutusque/TinyMistral-248M-v2.5   |
|   nold/phi-2-GGUF   |   MaziyarPanahi/sqlcoder-7b-Mistral-7B-Instruct-v0.1-GGUF   |   budecosystem/code-millenials-3b   |
|   MaziyarPanahi/speechless-mistral-six-in-one-7b-orth-1.0-Mistral-7B-Instruct-v0.1-GGUF   |   MaziyarPanahi/speechless-code-mistral-7b-v2.0-Mistral-7B-Instruct-v0.1-GGUF   |   MaziyarPanahi/speechless-code-mistral-orca-7b-v1.0-Mistral-7B-Instruct-v0.1-GGUF   |
|   Phanh2532/GAMA-Code-Generator-1.2   |   Phanh2532/GAMA-Code-Generator-1.0   |   bartowski/Hercules-1.0-Mistral-7B-exl2   |
|   jartine/WizardCoder-Python-34B-V1.0-llamafile   |   jartine/phi-2-llamafile   |   rrawen/Digitalfriend   |
|   omo-vxlot/ddpm-ema-pokemonv2-128   |   MaziyarPanahi/speechless-code-mistral-7b-v1.0-Mistral-7B-Instruct-v0.1-GGUF   |   MaziyarPanahi/phi-2-GGUF   |
|   jorgefalcon/llama-2-7b-datetime-regex-patterns   |   Luizinftr/TESTE   |   zaq-hack/Orion-14B-LongChat-bpw600-h6-exl2   |
|   sakren/audio-emotion-recognition   |   BhoneMyintSwe/Handwritten-classification   |   Norway/auria   |
|   AI4Ev3r/Traffic-Signs-Detection   |   JinbiaoZhu/llama-2-7b-robotplanning   |   sosoai/Orion-14B-Chat-RAG-safetensors   |
|   sosoai/Orion-14B-Chat-safetensors   |   Amartya77/RLHF_PPOppo_model   |   jtatman/tinymistral-v2-pycoder-instruct-248m   |
|   blueapple8259/TinyCode-python   |   medxiaorudan/CodeLlama_CPP_FineTuned   |   Qvi/Junkyu   |
|   mrm8488/mamba-coder   |   LoneStriker/code-millenials-34b-8.0bpw-h8-exl2   |   LoneStriker/code-millenials-34b-6.0bpw-h6-exl2   |
|   LoneStriker/code-millenials-34b-5.0bpw-h6-exl2   |   LoneStriker/code-millenials-34b-4.65bpw-h6-exl2   |   LoneStriker/code-millenials-34b-4.0bpw-h6-exl2   |
|   LoneStriker/code-millenials-34b-3.0bpw-h6-exl2   |   LoneStriker/code-millenials-34b-GGUF   |   jannatulferdaws/dl-project1   |
|   bartowski/code-millenials-34b-exl2   |   bartowski/code-millenials-13b-exl2   |   Herve12/remove-bg   |
|   Or4cl3-1/CSUMLM   |   mlabonne/phixtral-3x2_8   |   shadowml/phixtral-3x2_8   |
|   AmiaoinBJ/gsgsgs   |   iproskurina/bloom-7b1-gptq-4bit   |   iproskurina/bloom-1b7-gptq-4bit   |
|   iproskurina/bloom-3b-gptq-4bit   |   brittlewis12/stable-code-3b-GGUF   |   Locutusque/Qwen-14B-llamafied   |
|   SinaLab/Offensive-Hebrew   |   Seowoong-Chang/Book-Streak-Maker   |   cassanof/CommitMessageBackwards   |
|   SinaLab/ArBanking77   |   monsterapi/mistral_7b_HalfEpoch_DolphinCoder   |   afrideva/tinyllama-python-GGUF   |
|   philschmid/CodeLlama-7b-hf   |   rahuldshetty/tinyllama-python   |   rahuldshetty/tinyllama-python-gguf   |
|   smallcloudai/Refact-1_6-base   |   WizardLM/WizardCoder-Python-34B-V1.0   |   WizardLM/WizardCoder-15B-V1.0   |
|   WizardLM/WizardCoder-Python-13B-V1.0   |   WizardLM/WizardCoder-Python-7B-V1.0   |   WizardLM/WizardCoder-3B-V1.0   |
|   WizardLM/WizardCoder-1B-V1.0   |   LLM360/CrystalChat   |   parsak/phi-2-code-instruct-gguf   |
|   Zangs3011/mistral_7b_2EPOCH_DolphinCoder   |   Zangs3011/mistral_7b_3Epoch_DolphinCoder   |   TheBloke/stable-code-3b-GPTQ   |
|   TheBloke/stable-code-3b-GGUF   |   MaziyarPanahi/sqlcoder-7b-Mistral-7B-Instruct-v0.1   |   Abzu/CodeLlama-7b-hf   |
|   LoneStriker/Code-290k-13B-8.0bpw-h8-exl2   |   LoneStriker/Code-290k-13B-6.0bpw-h6-exl2   |   LoneStriker/Code-290k-13B-4.0bpw-h6-exl2   |
|   LoneStriker/Code-290k-13B-3.0bpw-h6-exl2   |   MaziyarPanahi/speechless-mistral-six-in-one-7b-orth-1.0-Mistral-7B-Instruct-v0.1   |   MaziyarPanahi/speechless-code-mistral-7b-v2.0-Mistral-7B-Instruct-v0.1   |
|   MaziyarPanahi/speechless-code-mistral-orca-7b-v1.0-Mistral-7B-Instruct-v0.1   |   mlx-community/stable-code-3b-mlx   |   bartowski/Code-290k-13B-exl2   |
|   TheBloke/Code-290k-13B-GPTQ   |   TheBloke/Code-290k-13B-AWQ   |   TheBloke/Code-290k-13B-GGUF   |
|   minkhantycc/letstalk   |   MaziyarPanahi/speechless-code-mistral-7b-v1.0-Mistral-7B-Instruct-v0.1   |   Kazilsky/Petal_Model   |
|   alibidaran/llama-2-7b-sql_generator_2   |   alibidaran/llama-2-7b-instruction_code   |   afrideva/phi-2-code-instruct-GGUF   |
|   bartowski/speechless-mistral-dolphin-orca-platypus-samantha-7b-exl2   |   lxuechen/phi-2-sft   |   lxuechen/phi-2-dpo   |
|   mlabonne/phixtral-4x2_8   |   FelixChao/vicuna-33b-coder   |   uukuguy/speechless-nl2sql-ds-6.7b   |
|   enyasantos/galaxy-classification-v01   |   enyasantos/galaxy-classification-v02   |   MaziyarPanahi/Llama-2-7b-hf-codealpaca-4bit   |
|   mlabonne/phixtral-2x2_8   |   mlx-community/phi-2-hf-4bit-mlx   |   Juanfco/Juanpancho   |
|   Flexy0/VeoAI-Small   |   0xnu/AGTD-v0.1   |   MuGeminorum/hoyoGPT   |
|   marcel/phixtral-4x2_8-gates-poc   |   parsak/phi-2-code-instruct   |   not-lain/PyGPT   |
|   Jiban4/BrainBox   |   TitleOS/CodePhi2   |   matthewnorton/mamba-phi   |
|   TheBloke/phixtral-4x2_8-GPTQ   |   jacobhoffmann/CodeLLaMA-2-13B-TestGen-Dart_v0.2-GGUF   |   shadowml/phixtral-4x2_8odd   |
|   shadowml/phixtral-4x2_8odo   |   bigscience/bloomz-7b1-mt   |   baotoan2002/GPT-2   |
|   Skier8402/code-search-net-tokenizer   |   budecosystem/code-millenials-13b   |   budecosystem/code-millenials-1b   |
|   kirstus/CodeLlama-7b-Instruct-hf   |   mero24424/cali72mero   |   ashutoshsharma58/indian_food_image_detection   |
|   acedev003/llama-2-coder-7b   |   edumunozsala/unsloth-llama-2-7B-python-coder   |   ziffir/LiteLLama-460M-1T   |
|   yuuko-eth/UniNER-7B-all-GGUF   |   daniellnichols/spack-llama-13b   |   daniellnichols/spack-llama-7b   |
|   Zienab/wav2vec   |   uukuguy/speechless-coder-ds-6.7b   |   maybprince/movie_suggestion   |
|   noahtren/phi-2   |   gnsepili/phi-1_5-finetuned-code   |   CravenMcin22/Cherub   |
|   Manoj21k/microsoft-phi-2-finetuned   |   kroonen/phi-2-GGUF   |   star-inc/machina   |
|   BucketOfFish/simplified_phi2   |   claudios/VulBERTa-MLP-VulDeePecker   |   TheBloke/phi-2-dpo-GPTQ   |
|   claudios/VulBERTa-MLP-ReVeal   |   claudios/VulBERTa-MLP-MVD   |   claudios/VulBERTa-MLP-Draper   |
|   TheBloke/phi-2-dpo-GGUF   |   claudios/VulBERTa-MLP-D2A   |   claudios/VulBERTa-MLP-Devign   |
|   JingyaoLi/MoTCoder-15B-v1.0   |   erfanzar/LinguaMatic-GPT4   |   SnypzZz/Llama2-13b-Language-translate   |
|   WizardLM/WizardCoder-33B-V1.1   |   bartowski/WizardCoder-33B-V1.1-exl2   |   LoneStriker/WizardCoder-33B-V1.1-8.0bpw-h8-exl2   |
|   TheBloke/WizardCoder-33B-V1.1-GPTQ   |   jncraton/phi-2-ct2-int8   |   LoneStriker/WizardCoder-33B-V1.1-6.0bpw-h6-exl2   |
|   AbdallahNasir/book-review-sentiment-classification   |   LoneStriker/WizardCoder-33B-V1.1-5.0bpw-h6-exl2   |   LoneStriker/WizardCoder-33B-V1.1-4.65bpw-h6-exl2   |
|   TheBloke/WizardCoder-33B-V1.1-AWQ   |   LoneStriker/WizardCoder-33B-V1.1-4.0bpw-h6-exl2   |   LoneStriker/WizardCoder-33B-V1.1-3.0bpw-h6-exl2   |
|   TheBloke/WizardCoder-33B-V1.1-GGUF   |   zahrach0724/Attendify-v2   |   mlx-community/CodeLlama-7b-Python-hf-8bit-mlx   |
|   mlx-community/CodeLlama-7b-Python-hf-4bit-mlx   |   winyap1516/mygpt   |   mlx-community/CodeLlama-7b-Python-hf-4bit   |
|   LoneStriker/tora-70b-v1.0-5.0bpw-h6-exl2   |   LoneStriker/tora-70b-v1.0-4.65bpw-h6-exl2   |   LoneStriker/tora-70b-v1.0-4.0bpw-h6-exl2   |
|   LoneStriker/tora-70b-v1.0-3.0bpw-h6-exl2   |   LoneStriker/tora-70b-v1.0-2.4bpw-h6-exl2   |   ed001/datascience-coder-1.3b   |
|   bigscience/bloom-7b1   |   mvdaaaaaaaalun/code_debug   |   dtnhan/codeGen_auto   |
|   bigcode/astraios-fft   |   bigcode/astraios-adapterp   |   bigcode/astraios-ia3   |
|   bigcode/astraios-adapterh   |   bigcode/astraios-parallel   |   bigcode/astraios-ptuning   |
|   bigcode/astraios-lora   |   bigcode/astraios-3b-fft   |   bigcode/astraios-7b-ptuning   |
|   bigcode/astraios-7b-parallel   |   bigcode/astraios-7b-ia3   |   bigcode/astraios-7b-fft   |
|   bigcode/astraios-7b-adapterh   |   bigcode/astraios-7b-lora   |   bigcode/astraios-7b-adapterp   |
|   bigcode/astraios-3b-parallel   |   bigcode/astraios-3b-ia3   |   bigcode/astraios-3b-lora   |
|   bigcode/astraios-3b-ptuning   |   bigcode/astraios-3b-adapterh   |   bigcode/astraios-3b-adapterp   |
|   bigcode/astraios-1b-adapterp   |   bigcode/astraios-1b-ptuning   |   bigcode/astraios-1b-lora   |
|   bigcode/astraios-1b-ia3   |   bigcode/astraios-1b-parallel   |   bigcode/astraios-1b-fft   |
|   bigcode/astraios-1b-adapterh   |


</details>



### 2023 (887 Models)

<details>
<summary>Click to expand!</summary>


|  |  |  |
|:--------:|:--------:|:--------:|
|   Shiyad/englishteacher   |   nchen909/codellm-7b-v4   |   uukuguy/speechless-codellama-34b-v2.0   |
|   uukuguy/speechless-coding-7b-16k-tora   |   uukuguy/speechless-code-mistral-7b-v1.0   |   uukuguy/speechless-tora-code-7b-v1.0   |
|   uukuguy/speechless-coder-ds-1.3b   |   teilomillet/MiniMerlin-3B   |   Saugatkafley/opt-350m-sft   |
|   parsak/codegen-350M-mono-lora-instruction   |   Vipitis/santacoder-finetuned-Shadertoys-fine   |   monsterapi/codellama_7b_DolphinCoder   |
|   monsterapi/gpt2_137m_DolphinCoder   |   monsterapi/mistral_7b_DolphinCoder   |   monsterapi/llama2_7b_DolphinCoder   |
|   monsterapi/falcon_7b_DolphinCoder   |   mehdi108090/new_model   |   kumar9/super-cool-model   |
|   prashrex/WizardCoder3b-gguf   |   prashrex/Santacoder-gguf   |   prashrex/WizardCoder1b-gguf   |
|   diamond0/dummy-model   |   Olast42/Find_out   |   NoCrypt/fast-repo   |
|   Lipu124/Spd1   |   dnnsdunca/Groglins   |   MexIvanov/zephyr-python-ru   |
|   MexIvanov/zephyr-python-ru-merged   |   mrm8488/llama-2-coder-7b   |   HuggingAlgorithms/figr-mistral7b-html   |
|   Andrecarlos9987/leo-santana   |   erfanzar/LinguaMatic-Coder-INST-1B-GGUF   |   erfanzar/LinguaMatic-Coder-INST-1B   |
|   erfanzar/LinguaMatic-1B-GGUF   |   baolongzhanshi007/first_model   |   liyoo/IntegratedModel_PairClassification   |
|   satanicsmores/SoftDisXFusionXRealistechX   |   hoolatech/keras-dummy-sequential-demo   |   bartowski/CodeNinja-1.0-OpenChat-7B-exl2   |
|   beowolx/CodeNinja-1.0-OpenChat-7B-GGUF   |   beowolx/CodeNinja-1.0-OpenChat-7B   |   LoneStriker/CodeNinja-1.0-OpenChat-7B-8.0bpw-h8-exl2   |
|   LoneStriker/CodeNinja-1.0-OpenChat-7B-6.0bpw-h6-exl2   |   LoneStriker/CodeNinja-1.0-OpenChat-7B-5.0bpw-h6-exl2   |   LoneStriker/CodeNinja-1.0-OpenChat-7B-4.0bpw-h6-exl2   |
|   TheBloke/CodeNinja-1.0-OpenChat-7B-GPTQ   |   LoneStriker/CodeNinja-1.0-OpenChat-7B-3.0bpw-h6-exl2   |   TheBloke/CodeNinja-1.0-OpenChat-7B-AWQ   |
|   TheBloke/CodeNinja-1.0-OpenChat-7B-GGUF   |   MexIvanov/zephyr-python-ru-gguf   |   mlx-community/phi-2-4bit   |
|   zhzhang93/test-model   |   erfanzar/LinguaMatic-1B   |   mlx-community/phi-2   |
|   SuryanshThePro/AI_0_beta_alpha   |   BOBBYBEAR1/BIOB   |   somehumanperson1/phi2pytorch   |
|   dpogreb/ai   |   erfanzar/LinguaMatic-2.7B-GGUF   |   erfanzar/LinguaMatic-Tiny-GGUF   |
|   andrijdavid/phi-2-GGUF   |   erfanzar/LinguaMatic-2.7B   |   rubble/HelpCode   |
|   Locutusque/Orca-2-13b-SFT-v4   |   TKDKid1000/phi-1_5-GGUF   |   TheBloke/phi-2-GPTQ   |
|   TheBloke/phi-2-GGUF   |   afrideva/phi-2-GGUF   |   fatihMaull/Camellia   |
|   muktadiur/Llama-2-7b-chat-hf-fine-tuned   |   robinsyihab/Sidrap-7B-v2   |   wassname/phi-2-GPTQ_w_hidden_states   |
|   GeneralGost/Enchanted_Gost_Models   |   Vipitis/santacoder-finetuned-Shadertoys   |   Locutusque/Orca-2-13b-SFT_v5   |
|   TheBloke/Orca-2-13B-SFT_v5-GPTQ   |   TheBloke/Orca-2-13B-SFT_v5-AWQ   |   TheBloke/Orca-2-13B-SFT_v5-GGUF   |
|   model-hub/phi-2   |   wassname/phi-2-w_hidden_states   |   protectai/CodeBERTa-language-id-onnx   |
|   aaptknews/BHARAT-AI   |   ajibawa-2023/Code-33B   |   TheBloke/Code-33B-GPTQ   |
|   TheBloke/Code-33B-AWQ   |   TheBloke/Code-33B-GGUF   |   CNXT/CHaTx   |
|   speechlessai/speechless-mistral-six-in-one-7b-orth-1.0   |   uukuguy/speechless-mistral-six-in-one-7b-orth-1.0   |   youdiniplays/my_translation_model   |
|   kumar9/word-auto-filled   |   WebraftAI/synapsellm-7b-mistral-v0.4-preview3   |   WebraftAI/synapsellm-7b-mistral-v0.5-preview2   |
|   KnutJaegersberg/GPT-JX-3b   |   WebraftAI/synapsellm-7b-mistral-v0.5-preview   |   WebraftAI/synapsellm-7b-mistral-v0.4-preview2   |
|   ammarnasr/codegen-350M-mono-java   |   huutmmt/imagetotext   |   uukuguy/speechless-code-mistral-7b-v2.0   |
|   maxwellinked/maxwellinked   |   halima014/llama-2-7b-int4-python-code-20k   |   lxe/Cerebras-GPT-2.7B-Alpaca-SP   |
|   TheBloke/Code-13B-GPTQ   |   TheBloke/Code-13B-AWQ   |   TheBloke/Code-13B-GGUF   |
|   monsterapi/falcon_7b_OpenPlatypus   |   jimjonesbabyfreshout/JefeHuggingface   |   kazma1/simcse-RobertLarge-job   |
|   damerajee/Py-Genius.gguf   |   ramgpt/ramgpt-13b-awq-gemm   |   ramgpt/ramgpt-13b   |
|   monsterapi/mistral_7b_norobots   |   Mreeb/Medi-llama-2-7b-custom1000   |   mayanksony/codellama-7b-instruct-6bit   |
|   OpenNMT/phi-1-ct2-int8   |   WebraftAI/synapsellm-7b-mistral-v0.4-preview   |   michaelfeil/ct2fast-phi-1   |
|   dotfantasy/godot-code   |   cyberghostM/ghost   |   sokada/codegen25-7b-multi-gguf-with-dummy-tokenizer   |
|   WebraftAI/synapsellm-7b-mistral-v0.3-preview   |   maddes8cht/smallcloudai-Refact-1_6B-fim-gguf   |   XAgentTeam/XAgentLLaMa-34B-preview   |
|   ngocminhta/Llama-2-vitd-tinycode   |   monsterapi/falcon_7b_3epoch_norobots   |   LazarusNLP/bloomz-7b1-mt-fp32   |
|   LazarusNLP/bloomz-1b7-fp32   |   LazarusNLP/bloomz-560m-fp32   |   LazarusNLP/bloom-1b7-fp32   |
|   kyriacou2009/TVR-1   |   NeuraCorp1212/AI_for_SmallMoleculeDesign   |   speechlessai/speechless-coding-7b-16k-tora   |
|   maddes8cht/syzymon-long_llama_3b_instruct-gguf   |   maddes8cht/syzymon-long_llama_3b_v1_1-gguf   |   Skuli/test   |
|   AlessandraAbreu/AI-LA   |   01GangaPutraBheeshma/colab_code_generator_FT_code_gen_UT   |   blueUmbrella/panda   |
|   tarudesu/gendec-with-distilmbert   |   Alpha316/ATLAS   |   Frazic/udever-bloom-3b-sentence   |
|   Vipitis/santacoder-finetuned-the-stack-glsl   |   frankminors123/Chinese-CodeLlama-7B-PT   |   maddes8cht/stabilityai-stablecode-instruct-alpha-3b-gguf   |
|   Myrax3000/starcoderbase1b-personal-copilot-A100-ibanity-lib   |   AlexWortega/taskGPT2-xl-v0.2a   |   XAgentTeam/XAgentLlama-7B-preview   |
|   cppowboy/XAgentLLaMa-7B-preview   |   bartowski/zephyr_7b_norobots-exl2   |   bartowski/mistral_7b_norobots-exl2   |
|   TheBloke/zephyr_7b_norobots-GPTQ   |   TheBloke/zephyr_7b_norobots-AWQ   |   TheBloke/zephyr_7b_norobots-GGUF   |
|   TheBloke/mistral_7b_norobots-GPTQ   |   TheBloke/zephyr_7b_norobots-fp16   |   TheBloke/mistral_7b_norobots-fp16   |
|   TheBloke/mistral_7b_norobots-GGUF   |   TheBloke/mistral_7b_norobots-AWQ   |   ajibawa-2023/Python-Code-13B   |
|   flax-community/gpt-neo-125M-apps   |   lvzixin/test   |   monsterapi/gpt2_124m_norobots   |
|   monsterapi/zephyr_7b_norobots   |   monsterapi/falcon_7b_norobots   |   monsterapi/llama2_7b_norobots   |
|   anycores/whisper_tiny_v1.1_intel   |   Keynote-Technology/KAI-7B-Instruct-v0.1   |   Keynote-Technology/KAI-7B-v0.1   |
|   Keynote-Technology/TinyKAI-0.7B-v0.1   |   Keynote-Technology/TinyKAI-3B-v0.1   |   NurtureAI/llama-2-7b-int4-gptq-python   |
|   Keynote-Technology/TinyKAI-1B-v0.1   |   uukuguy/speechless-codellama-dolphin-orca-platypus-13b   |   uukuguy/speechless-codellama-dolphin-orca-platypus-34b   |
|   uukuguy/speechless-codellama-34b-v1.9   |   uukuguy/speechless-code-mistral-orca-7b-v1.0   |   uukuguy/speechless-mistral-dolphin-orca-platypus-samantha-7b   |
|   Techhacker/Simplar   |   uukuguy/speechless-mistral-six-in-one-7b   |   FreddyM/Modeloafinclasiftexto   |
|   emny/admisi-indobert-qna-v2   |   afrideva/bloom-560m-GGUF   |   core-outline/llama-2-7b-chat-hf   |
|   bartowski/sqlcoder-7b-exl2   |   TheBloke/sqlcoder-7B-GPTQ   |   TheBloke/sqlcoder-7B-AWQ   |
|   TheBloke/sqlcoder-7B-GGUF   |   bartowski/Python-Code-13B-exl2   |   TheBloke/Python-Code-33B-GPTQ   |
|   TheBloke/Python-Code-33B-GGUF   |   TheBloke/Python-Code-33B-AWQ   |   TheBloke/Python-Code-13B-GPTQ   |
|   TheBloke/Python-Code-13B-GGUF   |   TheBloke/Python-Code-13B-AWQ   |   TheBloke/speechless-mistral-dolphin-orca-platypus-samantha-7B-GPTQ   |
|   speechlessai/speechless-codellama-34b-v1.0   |   TheBloke/speechless-mistral-dolphin-orca-platypus-samantha-7B-GGUF   |   TheBloke/speechless-mistral-dolphin-orca-platypus-samantha-7B-AWQ   |
|   Keynote-Technology/TinyIguana   |   bartowski/speechless-mistral-dolphin-orca-platypus-samantha-7b-exl2-broken   |   monsterapi/zephyr-7b-alpha_metamathqa   |
|   Amaraa0404/AI-First   |   or4cl3ai/SquanchNastyAI   |   cfahlgren1/wasm-sqlcoder-7b-q4f32_1   |
|   cfahlgren1/wasm-glaive-coder-7b-q4f32_1   |   erfanzar/LinguaMatic   |   TheBloke/CodeLlama-13B-Python-AWQ   |
|   TheBloke/CodeLlama-13B-Instruct-AWQ   |   TheBloke/CodeLlama-13B-AWQ   |   TheBloke/CodeLlama-34B-Instruct-AWQ   |
|   TheBloke/CodeLlama-34B-AWQ   |   TheBloke/CodeLlama-7B-AWQ   |   TheBloke/CodeLlama-7B-Instruct-AWQ   |
|   TheBloke/CodeLlama-34B-Python-AWQ   |   TheBloke/CodeLlama-7B-Python-AWQ   |   TheBloke/WizardCoder-Python-7B-V1.0-AWQ   |
|   TheBloke/WizardCoder-Python-34B-V1.0-AWQ   |   TheBloke/WizardCoder-Python-13B-V1.0-AWQ   |   TheBloke/Llama-2-Coder-7B-AWQ   |
|   TheBloke/Lemur-70B-Chat-v1-AWQ   |   TheBloke/ARIA-70B-V2-AWQ   |   TheBloke/Pandalyst-7B-V1.1-AWQ   |
|   TheBloke/Pandalyst_13B_V1.0-AWQ   |   TheBloke/speechless-code-mistral-7B-v1.0-AWQ   |   TheBloke/speechless-tora-code-7B-v1.0-AWQ   |
|   TheBloke/speechless-codellama-34b-v2.0-AWQ   |   TheBloke/tora-13B-v1.0-AWQ   |   TheBloke/tora-70B-v1.0-AWQ   |
|   TheBloke/tora-7B-v1.0-AWQ   |   TheBloke/tora-code-13B-v1.0-AWQ   |   TheBloke/tora-code-34b-v1.0-AWQ   |
|   TheBloke/tora-code-7B-v1.0-AWQ   |   TheBloke/Pandalyst-7B-v1.2-AWQ   |   TheBloke/vicuna-33B-coder-AWQ   |
|   TheBloke/Mistral-7B-codealpaca-lora-AWQ   |   TheBloke/KAI-7B-beta-AWQ   |   TheBloke/KAI-7B-Instruct-AWQ   |
|   smallcloudai/Refact-1_6B-fim   |   TheBloke/KAI-7B-Instruct-GPTQ   |   bartowski/KAI-7B-Instruct-exl2   |
|   TheBloke/KAI-7B-Instruct-GGUF   |   TheBloke/KAI-7B-beta-GPTQ   |   TheBloke/KAI-7B-beta-GGUF   |
|   D4ve-R/codepilot-mistral-7b   |   ghostdanny/bobby   |   ASHu2/codellama-13b-instruct-hf-q8_0.gguf   |
|   monsterapi/zephyr-7b-beta-CTranslate2-bfloat16   |   GeneralGost/monitor   |   0xOracle/mistral-7b-fraud-test-finetuned   |
|   Mreeb/Medi-llama-2-7b-custom100   |   izhx/udever-bloom-560m   |   izhx/udever-bloom-1b1   |
|   izhx/udever-bloom-3b   |   izhx/udever-bloom-7b1   |   nadiamaqbool81/llama-2-7b-int4-python-code-510   |
|   AISE-TUDelft/ML4SE23_G1_WizardCoder-SCoT-1B-V1.0   |   ML4SE2023-G1-WizardCoder/ML4SE23_G1_WizardCoder-SCoT-1B-V1.0   |   AlfredPros/CodeLlama-7b-Instruct-Solidity   |
|   monsterapi/mistral_7b_WizardLMEvolInstruct70k   |   monsterapi/zephyr_7b_WizardLMEvolInstruct70k   |   cecep31/pilput   |
|   pangxiang/gpt4mm   |   aiplanet/effi-13b-quant   |   teleprint-me/refact-1.6b-fim-gguf   |
|   oblivious/Refact-1.6B-fim-GGUF   |   Ama-Weerasinghe/Clip-model   |   EloimEssaim/yolov8n   |
|   nuprl/MultiPLCoder-15b   |   rohansaraswat/RoadSafetyModel   |   wilson989/speechless-codellama-34b-v2.0-GGUF   |
|   Nondzu/Mistral-7B-codealpaca-lora   |   Overthrow4232/cat_and_dog_breed_classifier   |   bartowski/Mistral-7B-codealpaca-lora-exl2   |
|   LoneStriker/Mistral-7B-codealpaca-lora-8.0bpw-h6-exl2   |   LoneStriker/Mistral-7B-codealpaca-lora-5.0bpw-h6-exl2   |   LoneStriker/Mistral-7B-codealpaca-lora-4.0bpw-h6-exl2   |
|   LoneStriker/Mistral-7B-codealpaca-lora-3.0bpw-h6-exl2   |   LoneStriker/Mistral-7B-codealpaca-lora-6.0bpw-h6-exl2   |   TheBloke/Mistral-7B-codealpaca-lora-GPTQ   |
|   TheBloke/Mistral-7B-codealpaca-lora-GGUF   |   rohansaraswat/CNN_Detection_Model   |   monsterapi/gpt2_124m_WizardLMEvolInstruct70k   |
|   monsterapi/gptj_6b_WizardLMEvolInstruct70k   |   monsterapi/llama2_7b_WizardLMEvolInstruct70k   |   Plaban81/codegen-finetuned-python   |
|   mllakers/marioooo   |   ML4SE2023-G1-WizardCoder/ML4SE23_G1_WizardCoder-SCoT-350M-V1.0   |   boinc/111   |
|   AzuleAI/VoiceLine   |   yofitofi/shlomper   |   thanhnew2001/bloom7b1   |
|   thanhnew2001/ct2-bloom-7b1   |   lucas347/extend_audio   |   ziqin/test   |
|   TheBloke/vicuna-33B-coder-GPTQ   |   TheBloke/vicuna-33B-coder-GGUF   |   Vichayturen/RefereeGLM   |
|   replit/replit-code-v1_5-3b   |   HiTZ/GoLLIE-13B   |   HiTZ/GoLLIE-34B   |
|   onepunya/liv001   |   ashwincv0112/codellama-python7b   |   SakshiRathi77/wav2vec2-large-xlsr-300m-hi-kagglex   |
|   LoneStriker/speechless-code-mistral-7b-v1.0-recalibrate-8.0bpw-h6-exl2   |   LoneStriker/speechless-code-mistral-7b-v1.0-recalibrate-6.0bpw-h6-exl2   |   TheBloke/Pandalyst-7B-v1.2-GPTQ   |
|   TheBloke/Pandalyst-7B-v1.2-GGUF   |   Kx15/ai-text-portfolio   |   TSjB/NLLB-201-600M-QM-V1   |
|   VatsaDev/NanoPhi   |   pipizhao/Pandalyst-7B-V1.2   |   pipizhao/Pandalyst-7B-V1.1   |
|   pipizhao/Pandalyst_13B_V1.0   |   TheBloke/tora-code-7B-v1.0-GPTQ   |   TheBloke/tora-code-7B-v1.0-GGUF   |
|   TheBloke/tora-code-34b-v1.0-GPTQ   |   TheBloke/tora-code-34b-v1.0-GGUF   |   TheBloke/tora-code-13B-v1.0-GPTQ   |
|   TheBloke/tora-code-13B-v1.0-GGUF   |   TheBloke/tora-7B-v1.0-GPTQ   |   TheBloke/tora-7B-v1.0-GGUF   |
|   TheBloke/tora-70B-v1.0-GPTQ   |   TheBloke/tora-70B-v1.0-GGUF   |   TheBloke/tora-13B-v1.0-GPTQ   |
|   TheBloke/tora-13B-v1.0-GGUF   |   TheBloke/speechless-codellama-34b-v2.0-GPTQ   |   erfanzar/EasyDelCollection   |
|   monsterapi/llama2_70B_dolly15k_mergedweights   |   defog/sqlcoder2   |   LoneStriker/speechless-code-mistral-7b-v1.0-6.0bpw-h6-exl2   |
|   LoneStriker/speechless-code-mistral-7b-v1.0-4.0bpw-h6-exl2   |   LoneStriker/speechless-code-mistral-7b-v1.0-5.0bpw-h6-exl2   |   LoneStriker/speechless-code-mistral-7b-v1.0-8.0bpw-h6-exl2   |
|   LoneStriker/speechless-code-mistral-7b-v1.0-3.0bpw-h6-exl2   |   TheBloke/speechless-codellama-34b-v2.0-GGUF   |   TheBloke/speechless-tora-code-7B-v1.0-GPTQ   |
|   TheBloke/speechless-tora-code-7B-v1.0-GGUF   |   OpenLemur/lemur-70b-chat-v1   |   OpenLemur/lemur-70b-v1   |
|   TheBloke/speechless-code-mistral-7B-v1.0-GPTQ   |   TheBloke/speechless-code-mistral-7B-v1.0-GGUF   |   monsterapi/Falcon_40B_dolly15k   |
|   monsterapi/Falcon_180B_dolly15k   |   Babu/code-llama-Html-responsive   |   bigcode/santacoder   |
|   TheBloke/sqlcoder2-GGUF   |   monsterapi/llama2_70B_dolly15k   |   vijayfound/ludwig-llama2-demo   |
|   UDE-SE/CodeBERTForReturnTypeClassification   |   UDE-SE/BERTForReturnTypeClassification   |   TheBloke/sqlcoder2-GPTQ   |
|   Faradaylab/ARIA-70B-V2   |   JackCloudman/tora-code-34b-v1.0-GGUF   |   HiTZ/GoLLIE-7B   |
|   vedica1011/llama-2-7b-int4-python-code-20k   |   Diego-0121/OCR_ImaText   |   JackCloudman/tora-code-13b-1.0-4bit-128g   |
|   LeanAI/llama-2-7b-CH1-cav1-3   |   llm-agents/tora-70b-v1.0   |   llm-agents/tora-13b-v1.0   |
|   llm-agents/tora-code-7b-v1.0   |   llm-agents/tora-code-13b-v1.0   |   llm-agents/tora-code-34b-v1.0   |
|   llm-agents/tora-7b-v1.0   |   Mxode/Pythia-70m-C-Language-KnowledgeExtract   |   Dimensity/Complexity-1B   |
|   willyninja30/ARIA-70B-French   |   smallcloudai/starcoderbase-7b   |   smallcloudai/starcoderbase-3b   |
|   smallcloudai/starcoderbase-1b   |   morph-labs/rift-coder-v0-7b-gguf   |   joernio/codetidal5   |
|   amtsal/resnet18_finetunewithcifar10   |   mlsoft/PVQ   |   openerotica/CodeLlama-13b-GPTQ-ERP   |
|   bgsach/WizardCoder-Python-7B-V1.0-ct2-int8_float16   |   bgsach/WizardCoder-Python-13B-V1.0-ct2-float16   |   bgsach/WizardCoder-Python-7B-V1.0-ct2-float16   |
|   bgsach/WizardCoder-Python-7B-V1.0-ct2-int8   |   bgsach/WizardCoder-Python-13B-V1.0-ct2-int8_float16   |   robinsyihab/Sidrap-7B-v1   |
|   openerotica/CodeLlama-34b-GPTQ-ERP   |   xtradereturn/MQL4-Reworking   |   subu4444/angular-ut-generator   |
|   aswin1906/llama-7b-sql-2k   |   TheBloke/Pandalyst_13B_V1.0-GPTQ   |   Ahada/Olivia   |
|   TheBloke/Pandalyst_13B_V1.0-GGUF   |   TheBloke/Pandalyst-7B-V1.1-GPTQ   |   TheBloke/Pandalyst-7B-V1.1-GGUF   |
|   LeeEric/openbuddy-codellama2-34b-v11.1-GGUF   |   showpiece/donut4cover_of_books   |   RamNaamSatyaHai/whisper-small-ft-hindi   |
|   morph-labs/rift-coder-v0-7b   |   TheBloke/WizardCoder-Python-13B-V1.0-GGML   |   TheBloke/Lemur-70B-Chat-v1-GGML   |
|   TheBloke/CodeLlama-13B-GGML   |   TheBloke/CodeLlama-13B-Python-GGML   |   TheBloke/CodeLlama-13B-Instruct-GGML   |
|   TheBloke/CodeLlama-7B-Python-GGML   |   TheBloke/CodeLlama-7B-GGML   |   TheBloke/CodeLlama-7B-Instruct-GGML   |
|   TheBloke/Octocoder-GPTQ   |   TheBloke/Octocoder-GGML   |   TheBloke/stablecode-instruct-alpha-3b-GGML   |
|   TheBloke/stablecode-completion-alpha-3b-4k-GGML   |   TheBloke/stablecode-completion-alpha-3b-4k-GPTQ   |   TheBloke/sqlcoder-GGUF   |
|   TheBloke/sqlcoder-GPTQ   |   TheBloke/ARIA-70B-V2-GPTQ   |   TheBloke/ARIA-70B-V2-GGUF   |
|   TheBloke/WizardCoder-Python-7B-V1.0-GPTQ   |   TheBloke/WizardCoder-Python-7B-V1.0-GGUF   |   TheBloke/Llama-2-Coder-7B-GPTQ   |
|   TheBloke/Llama-2-Coder-7B-GGUF   |   TheBloke/Lemur-70B-Chat-v1-GPTQ   |   TheBloke/Lemur-70B-Chat-v1-GGUF   |
|   TheBloke/WizardCoder-Python-13B-V1.0-GGUF   |   TheBloke/WizardCoder-Python-13B-V1.0-GPTQ   |   TheBloke/WizardCoder-Python-34B-V1.0-GPTQ   |
|   TheBloke/WizardCoder-Python-34B-V1.0-GGUF   |   TheBloke/CodeLlama-34B-GPTQ   |   TheBloke/CodeLlama-34B-Instruct-GPTQ   |
|   TheBloke/CodeLlama-34B-Python-GPTQ   |   TheBloke/CodeLlama-13B-GPTQ   |   TheBloke/CodeLlama-13B-Instruct-GPTQ   |
|   TheBloke/CodeLlama-13B-Python-GPTQ   |   TheBloke/CodeLlama-7B-GPTQ   |   TheBloke/CodeLlama-34B-Instruct-GGUF   |
|   TheBloke/CodeLlama-7B-Python-GPTQ   |   TheBloke/CodeLlama-34B-Python-GGUF   |   TheBloke/CodeLlama-13B-Python-GGUF   |
|   TheBloke/CodeLlama-34B-GGUF   |   TheBloke/CodeLlama-7B-Instruct-GPTQ   |   TheBloke/CodeLlama-13B-GGUF   |
|   TheBloke/CodeLlama-13B-Instruct-GGUF   |   TheBloke/CodeLlama-7B-Python-GGUF   |   TheBloke/CodeLlama-7B-GGUF   |
|   TheBloke/CodeLlama-7B-Instruct-GGUF   |   tahniat/Classifier_bias_TahniatKhan   |   bigscience/bloom-560m   |
|   bigscience/bloom-1b1   |   jmoney54378256438905/CodeLlama-13b-Instruct-4.65bpw   |   victor/CodeLlama-34b-Instruct-hf   |
|   TSjB/mbart-large-52-qm-ru-v2   |   Techiehill/Himagiri   |   syzymon/long_llama_code_7b   |
|   pszemraj/bart-base-code-instructiongen   |   nisten/glaive-coder-7b-q4f16_2-mlc   |   aswin1906/gpt2-medium-wiki   |
|   luffycodes/higgs-llama-vicuna-ep25-70b   |   glaiveai/glaive-coder-7b   |   monsterapi/opt1.3B_codeinstruct   |
|   monsterapi/llama7B_alpaca-lora   |   monsterapi/opt125M_alpaca   |   monsterapi/OpenPlatypus_LLAMA2_7b   |
|   monsterapi/OpenPlatypus_Falcon_7b   |   monsterapi/codellama7b_codealpaca20k   |   monsterapi/llama2_SQL_Answers_finetuned   |
|   monsterapi/falcon-7b-python-code-instructions-18k-alpaca   |   monsterapi/gpt2_alpaca-lora   |   monsterapi/CodeAlpaca_LLAMA2_7B   |
|   shareAI/CodeLlama-13b-English-Chat   |   nomsgadded/opt_RestaurantReview   |   Faradaylab/Aria_7b_v2   |
|   Faradaylab/ARIA-CODE   |   Harshit0722/dolly-fine-tuned-on-med-data   |   Siddhanta19/nc-backup   |
|   ZahrizhalAli/phi-1_5-code-generation   |   ZahrizhalAli/llama-7b-code-generation   |   dwjj/bloom-560m   |
|   olanigan/llama-7b-codealpaca   |   bugdaryan/WizardCoderSQL-15B-V1.0-QLoRA   |   mlabonne/codellama-2-7b   |
|   monsterapi/llama2-code-generation   |   monsterapi/llama2-7b-tiny-codes-code-generation   |   Indiarti/test_llm   |
|   Cyborg-AI/model   |   Vesper27/TEST   |   lepin2001/catsordogs   |
|   abhinavkulkarni/codellama-CodeLlama-13b-Instruct-hf-w4-g128-awq   |   bugdaryan/WizardCoderSQL-15B-V1.0   |   miojizzy/mhr_recognize_classify_model_whole   |
|   FinchResearch/Gurkha-copilot-1b   |   PetraAI/Nashmi   |   Moses25/Llama2-Moses-7b-chat   |
|   bigcode/starcoderbase-1b   |   waleko/codereviewer-finetuned-msg   |   muhtasham/santacoder-finetuned-the-stack-cobol   |
|   michaelfeil/ct2fast-CodeLlama-34b-hf   |   michaelfeil/ct2fast-CodeLlama-13b-hf   |   michaelfeil/ct2fast-CodeLlama-7b-hf   |
|   teleprint-me/codellama-7b-python-gguf   |   teleprint-me/llama-2-7b-chat-gguf   |   abhinavkulkarni/codellama-CodeLlama-7b-Python-hf-w4-g128-awq   |
|   abhinavkulkarni/codellama-CodeLlama-7b-Instruct-hf-w4-g128-awq   |   abhinavkulkarni/codellama-CodeLlama-13b-Python-hf-w4-g128-awq   |   rombodawg/WizardCoder-Python-7B-V1.0_Sharded_1.5gb   |
|   rombodawg/WizardCoder-Python-13B-V1.0_Sharded_1.5gb   |   JCTN/fast-repo   |   f4th4n/coba   |
|   Faradaylab/Aria-40B   |   OtterDev/otterchat   |   Chirayu/nl2cql   |
|   dubdoo/dubdoo_stories_test_first   |   JetBrains-Research/cmg-race-with-history   |   Faradaylab/ARIA_7B   |
|   ccore/core-prompt-reverser-opt-1.3b   |   Transform72/PandasSolver   |   DataLinguistic/DataLinguistic-34B-V1.0   |
|   premai-io/CodeLlama-34b-Instruct-hf   |   edumunozsala/llama-2-7b-int4-GPTQ-python-code-20k   |   seeklhy/codes-15b   |
|   seeklhy/codes-7b   |   seeklhy/codes-3b   |   seeklhy/codes-1b   |
|   SymeCloud/Llama2-7b-Chat-GGUF   |   madhan2301/llama-2-7b-chuk-test   |   JetBrains-Research/cmg-race-without-history   |
|   xianglingjing/llama-2-7b-int4-text-to-sql   |   shailja/fine-tuned-codegen-2B-Verilog   |   shailja/fine-tuned-codegen-6B-Verilog   |
|   shailja/fine-tuned-codegen-16B-Verilog   |   luxspacescience/turtleYOLONAS   |   bigscience/bloom-3b-intermediate   |
|   hessertaboada/ludwig-webinar   |   Fduv/DeciCoder-FineTuned-CodeAlpaca   |   JetBrains-Research/cmg-codereviewer-with-history   |
|   HarshSinyal/Constitution-India-Falcon-Sharded-7B   |   FinchResearch/Nines-llama2-7b   |   FinchResearch/Sherman-copilot-1b   |
|   WillemVH/E   |   RicardoLee/Llama2-chat-13B-Chinese-withCode3W-LoRA   |   willyninja30/ARIA_CODE_fr-instruct   |
|   Mediocreatmybest/WizardCoder-Python-13B-V1.0_8bit_nf4   |   JamalSQ/PiddingAI   |   AhmedSSoliman/Llama2-CodeGen-PEFT-QLoRA   |
|   FinchResearch/GTamaraw3-1b   |   piratos/ct2fast-codellama-13b-instruct-hf   |   Faradaylab/aria-code-light-llama2-python   |
|   FinchResearch/GTamaraw-1b   |   vodkaslime/codellama-7b-hf   |   Chirayu/nl2kql   |
|   Petercottontail1/Beavis   |   Spectre29/MaliciousWeb   |   shuvom/falcon-med-FT-v1.114   |
|   rtlabs/StableCode-3B   |   SY0719/llama2-ss   |   jeekzhang/duanzai_punchline_ner_model   |
|   Lilithchouy/xxxx   |   vodkaslime/test-repo-stablecode   |   thr10/th-ins-coder-v1   |
|   ammarnasr/codegen-350M-mono-rust   |   ammarnasr/codegen-350M-mono-ruby   |   ammarnasr/codegen-350M-mono-swift   |
|   karthick1/TestNlpScoring   |   saurabhharak/intent-fine-tuned-model-roberta-base   |   bigcode/starcoderplus   |
|   TheBloke/starcoder-GPTQ   |   TheBloke/starcoderplus-GPTQ   |   TheBloke/minotaur-15B-GPTQ   |
|   TheBloke/Redmond-Hermes-Coder-GPTQ   |   TheBloke/Codegen25-7B-mono-GPTQ   |   SoniR/config   |
|   bigcode/octocoder   |   Nan-Do/python-assistant-3b   |   RicardoLee/Llama2-chat-7B-Chinese-withCode3W-LoRA   |
|   JetBrains-Research/cmg-codereviewer-without-history   |   JetBrains-Research/cmg-codet5-with-history   |   JetBrains-Research/cmg-codet5-without-history   |
|   bigcode/santacoderpack   |   Orgilbold09/Orikore   |   sadiqj/camlcoder   |
|   oItsMineZ/oItsMineZ-so-vits-svc-4.0-PreTrained-Model   |   Chirayu/nl2mongo   |   Chirayu/nl2pandas   |
|   Francesco-A/code-search-net-tokenizer   |   justinmeans/stablecode-completion-alpha-3b-4k-coreml   |   stabilityai/stablecode-completion-alpha-3b-4k   |
|   stabilityai/stablecode-instruct-alpha-3b   |   stabilityai/stablecode-completion-alpha-3b   |   edumunozsala/llama-2-7b-int4-python-code-20k   |
|   vishnun/codenlbert-tiny   |   mrutyunjay-patil/keywordGen-v2   |   Hossein69/test1   |
|   mrutyunjay-patil/keywordGen-v1   |   syzymon/long_llama_3b_instruct   |   syzymon/long_llama_3b_v1_1   |
|   AbdulSami/bert-base-cased-cefr   |   vishnun/codenlbert-sm   |   winstxnhdw/replit-code-v1-3b-ct2-int8   |
|   paralleldynamix/paralleldynamix-model101   |   emre/llama-2-13b-code-122k   |   emre/llama-2-13b-code-chat   |
|   Sakuna/LLaMaCoderAll   |   iamtarun/pycompetitive-codegen350M-qlora   |   iamtarun/codegen-350M-mono-4bit-qlora   |
|   bigscience/bloom   |   killmealreadypls228/Mickella_theCat   |   michaelfeil/ct2fast-starcoderbase-1b   |
|   michaelfeil/ct2fast-starcoderbase-7b   |   michaelfeil/ct2fast-starcoderbase-3b   |   vijaysekhar/summarization_finetuned_model   |
|   vishnun/lora-NLIGraph   |   GenerativeMagic/Llama-Engineer-Evol-7b-GGML   |   GenerativeMagic/Llama-Engineer-Evol-7b   |
|   bigcode/starcoderbase-7b   |   TitanML/ct2-int8-bloomz-7b1-mt   |   bigscience/bloomz-p3   |
|   bigscience/bloomz-mt   |   KshitizPandya/GenzTranscribe-small-hi   |   bigcode/starpii   |
|   replit/replit-code-v1-3b   |   UncoverAI/LiveModelX   |   Martin2203/starcoder-peft-2   |
|   prabhuzz00/LORA   |   MrAiran/GPT2-1B-Spanish-NSFW   |   yhyhy3/med-orca-instruct-33b   |
|   yhyhy3/med-orca-instruct-33b-GPTQ   |   AlexWortega/wortegaLM-1b   |   satzkumar/BoatAI   |
|   u2003158/saved_model   |   huolongguo10/check_sec_tiny   |   huolongguo10/check_sec   |
|   Ralpone/AITest   |   MOONBOW2/EVA   |   ahmadnajm/KurdGPT   |
|   SerchOnodera117/Lora-chan   |   avnishkr/falcon-QAMaster   |   aniketr/mrl-resnet50   |
|   digitalmax1/max   |   Daniil-plotnikov/Glazastik_Chat   |   PledgeVentures/COSMO   |
|   Daniil-plotnikov/glazastik   |   kryox64/stock-x   |   TK192828/Bangable-Inanimate-Insanity-2-Microphone   |
|   felixdae/cs324-length-control   |   yhyhy3/open_llama_7b_v2_med_instruct   |   mvasiliniuc/iva-codeint-kotlin-small   |
|   mvasiliniuc/iva-codeint-swift-small   |   mrtimmydontplay/netsec   |   TheBloke/bloomz-176B-GPTQ   |
|   RHP27042002/AI_NFT_generator   |   PetchP/distilwangchanberta-base-att-spm-uncased   |   Binaryy/blender-bot-distill-finetuned   |
|   openkg/knowlm-13b-lora   |   openkg/knowlm-13b-diff   |   UncoverAI/ImageClassificationX   |
|   gvij/gpt-j-code-alpaca-instruct   |   Fsoft-AIC/Codebert-docstring-inconsistency   |   gvij/open-llama-7b-code-alpaca-instruct   |
|   bigscience/bloom-1b7-intermediate   |   FabriLluvia/BOT   |   matthoffner/santacoder-metal   |
|   matthoffner/WizardCoder-mlc-llm   |   erfanzar/llama-chat   |   TheBloke/Redmond-Hermes-Coder-GGML   |
|   NousResearch/Redmond-Hermes-Coder   |   bigcode/starcoderbase-3b   |   Cr4yfish/zipnerf   |
|   JacobHenry/Pleasantnoise   |   nayralabs/test   |   rizkyds/bert-phb   |
|   michaelfeil/ct2fast-starcoder   |   mroppokhan/Glamare.shopify   |   Berev/MegaChatger   |
|   zjunlp/zhixi-13b-lora   |   Sp1786/mutliclass-sentiment-analysis-bert   |   Neupane9Sujal/Text_Summarization   |
|   ssj1989/open_llama_001   |   erfanzar/Mpt-7B-Assistant   |   onesubmit/onesubmit   |
|   fazni/predicting-role-based-on-skills   |   leons-esposa02/BeedTesting.AI   |   papahawk/keya-560m   |
|   Or4cl3/Or4cl3   |   pavanBuduguppa/asr_inverse_text_normalization   |   zjunlp/zhixi-13b-diff-fp16   |
|   zjunlp/zhixi-13b-diff   |   pavanBuduguppa/chat_to_speech_transcription   |   ChilNik/PR_digits   |
|   devers93/Dodo   |   ArturStepanenko/pythonV6   |   TheBloke/minotaur-15B-GGML   |
|   mrm8488/falcoder-7b   |   codeparrot/starcoder-self-instruct   |   openaccess-ai-collective/minotaur-15b   |
|   piratos/ct2fast-starcoderplus   |   aliyadetect/road_detection   |   bumstern/segmentation_model_russian_data   |
|   Brendar/MaBePa_STS   |   bigscience/bloom-560m-intermediate   |   up201806461/bert-java-bfp_single   |
|   up201806461/bert-java-bfp_combined   |   wangluping2023/llama-plus-7b   |   xared1001/bloom-7b1_pytorch   |
|   bigcode/starcoderplus-megatron   |   neethubehanan28/t5_squad_v1   |   UnstableLlama/alpaca_lora_open_llama_3b_watermarked   |
|   rajkanbu/sampleapp   |   ireneli1024/biobart-v2-base-finetuned-pubmed-train   |   Sourabh2/List-notes-summarizer   |
|   OdiaGenAI/odiagenAI-bengali-lora-model-v1   |   rustformers/bloomz-ggml   |   rustformers/bloom-ggml   |
|   TheBloke/starcoder-GGML   |   TheBloke/starcoderplus-GGML   |   HuggingFaceH4/starchat-alpha   |
|   DebeshSahoo/text2sql-finetune   |   bigcode/gpt_bigcode-santacoder   |   sirbrentmichaelskoda/Auto-GBT-Dream-Team-Model   |
|   teknium/Replit-v1-CodeInstruct-3B-fp16   |   teknium/Replit-v2-CodeInstruct-3B   |   teknium/Replit-v1-CodeInstruct-3B   |
|   dhhd255/EfficientNet_ParkinsonsPred   |   kevinpro/Vicuna-13B-CoT   |   michaelfeil/ct2fast-starchat-alpha   |
|   mantra-coding/alBERTo   |   michaelfeil/ct2fast-starcoderbase   |   bigcode/tiny_starcoder_py   |
|   jiezhou1996/test   |   Soliai/Soli   |   michaelfeil/ct2fast-gpt_bigcode-santacoder   |
|   dushigao/yolov4   |   mishasadhaker/codet5_large_typescript   |   sahil2801/instruct-codegen-16B   |
|   omegaodin/replit-replit-code-v1-3b   |   kkhan/gpt2-medium-iba-txt   |   4bit/Replit-v1-CodeInstruct-3B   |
|   bigscience/bloomz-560m   |   bigscience/bloomz-1b1   |   bigscience/bloomz-1b7   |
|   bigscience/bloomz-3b   |   bigscience/bloomz   |   betelguesestudios/ChatDBD   |
|   azizp128/emotion-predictor-indobert   |   zirui3/starcoder-ft-zh   |   zchflyer/test11   |
|   EnterNameBros/DialoGPT-small-Senko-san-ver-2   |   dev2bit/es2bash-mt5   |   omegaodin/gpt2   |
|   AsakusaRinne/LLamaSharpSamples   |   NeoDim/starcoder-GGML   |   NeoDim/starcoderbase-GGML   |
|   NeoDim/starchat-alpha-GGML   |   christinacdl/moderate_severe_depression_model   |   Fredithefish/CrimsonPajama   |
|   OdiaGenAI/odiagenAI-model-v1   |   NatLee/openpose-keras-model   |   pratikcha/DummyModelTest   |
|   brandit/atharv.1   |   BlackBull/yeet   |   wandisun/generate_testcase   |
|   pszemraj/bart-large-code-instructiongen   |   erichilarysmithsr/Quality-of-Life-Games   |   AlexWortega/wortegaLM   |
|   bigcode/starcoder-megatron   |   bigcode/starcoderbase-megatron   |   bigscience/bloom-1b7   |
|   bigcode/starcoderbase   |   APJ23/MultiHeaded_Sentiment_Analysis_Model   |   lentan/replit   |
|   bigcode/starencoder   |   jitesh/emotion-english   |   TinaLiHF/fined-tuned-T5small   |
|   tmnam20/codebert-code-summarization   |   tabbleman/test   |   HelloImSteven/AppleScript-Summarizer   |
|   duncan93/video   |   alexpaul/QI-Large-v1   |   JeanL-0/ChatAnswering-PTBR   |
|   jitroy07/BOT   |   Rirou360/test   |   RafMuz/alpaca7B-lora   |
|   Akhil0-o/saved_model_links   |   TrippingFollowing39/AMOGUS   |   Akhil0-o/saved_model_body   |
|   MrRainbow/RainbowGPT   |   Akhil0-o/Phishing_detection   |   Ilangraterol/Dataset_model   |
|   AlexWortega/instruct_rugptlarge   |   MLRush/chinese-chat-30m   |   MLRush/chinese-lm-30m   |
|   ParsaKgvr/mmdGPT   |   ParsaKgvr/mmdBERT   |   dorkai/codeX-1.0   |
|   Phonecharger/WLAsw1   |   MatthiasPi/ActiveLearningModel-WAR-WassersteinActiveRegression   |   Wannita/baseline_codecompletion   |
|   ybelkada/bloom-1b7-8bit   |   kelly233/test_model   |   bigscience/bloom-3b   |
|   lambdasec/santafixer   |   ybelkada/bloom-560m-8bit   |   PromptKing/GTA5_PROCESS_LEARNING_AI   |
|   Qrstud/ANCs   |   HTP/CHaTx   |   LYFCJJ/anythingv45-cjj-diffusers   |
|   hakurei/instruct-12b   |   Dirus/GPTOWN   |   TeamGZG/toxic-comment-classification-project   |
|   MarTinSForZZa/Innerversal   |   newsrx/bloomz-7b1   |   0x7o/pyGPT-50M   |
|   dhnchandan/huggingface   |   RomanTeucher/PythonCoder   |   edbeeching/llama-se-rl-adapter   |
|   TheEeeeLin/test   |   olivierdehaene/optimized-santacoder   |   Mauquoi-00/Teenage_Gender_Classification   |
|   Esly35i/Esmoli   |   zee2221/ai_me   |   urmom12349823/AItext   |
|   manstepharder/hangi   |   Sentdex/GPyT   |   akone/bloomgpt   |
|   Wannita/PyCoder   |   mazeratti/creative   |   AlexWortega/instruct_rugptMedium   |
|   vernin/maylora   |   valooo/test   |   amongusrickroll68/MeloMind   |
|   amongusrickroll68/TextImagine-1.0-March-2023   |   badmatr11x/distilroberta-base-offensive-hateful-speech-text-multiclassification   |   Ar4ikov/gpt2-650k-stable-diffusion-prompt-generator   |
|   bigscience/distill-bloom-1b3   |   CAUKiel/JavaBERT   |   Ashokajou51/NonToxicCivilBert   |
|   namikazi25/DCNN_on_CIFAR_10   |   mdoshi2612/fake-news-detector   |   shibing624/code-autocomplete-gpt2-base   |
|   aarnphm/multi-length-text-classification-pipeline   |   NITINNANNAPANENI/Ll   |   rockmiin/ml-codeparrot   |
|   Naina07/Fine_tune   |   bigscience/distill-bloom-1b3-10x   |   razent/cotext-1-cc   |
|   omarelsayeed/wav2vec2_ar_anz2   |   whybeyoung/test   |   KonghaYao/MagicPrompt_SD_V1   |
|   zabir-alnazi/fatima-fellowship-ai-gen-detector   |   Abdullah007/image-classification-ResNet50   |   AlexWortega/instruct_rugptSmall   |
|   sjiang1/codecse   |   daeunj/828A   |   Ajibola/PaViT   |
|   changwh5/BigBiGAN-MNIST-150epoch   |   Azarthehulk/Image_preprocessing_basics   |   nishakathiriya/DR-model   |
|   AcrossTheUniverseZ/ATUZGenerator   |   Roy029/sno_empty   |   imharesh/Shabbat   |
|   rapples/png2emb   |   marlenezw/AutoVC_Voice_Conversion   |   mrm8488/santacoder-finetuned-the-stack-clojure   |
|   BrendaTellez/sounds   |   BrendaTellez/SoundClassificationCNNRNN   |   samkenxstream/AlgoSilicon   |
|   samkenxstream/HierarchyMartialsAI   |   ilahazs/rokashibasakiv1   |   bigscience/bloom-1b1-intermediate   |
|   bigscience/bloom-7b1-intermediate   |   bigscience/bloomz-7b1-p3   |   mrm8488/santacoder-finetuned-the-stack-swift   |
|   Neighhhbor/Test_model   |   muhtasham/santacoder-finetuned-the-stack-assembly   |   zkep/detr   |
|   loubnabnl/santacoder-code-to-text   |   mrm8488/santacoder-finetuned-the-stack-bash-shell   |   Thyral/Testing   |
|   noahshinn/santacoder-ts   |   el-profesor/code_t5   |   K8778/universe   |
|   CarperAI/diff-codegen-6b-v2   |   CarperAI/diff-codegen-2b-v2   |   CarperAI/diff-codegen-350m-v2   |
|   96harsh56/bert_test2   |   aminian/ML-final-project   |   microsoft/codereviewer   |
|   facebook/incoder-1B   |   facebook/incoder-6B   |   MrFitzmaurice/roberta-finetuned-topic-5   |
|   mble/nameToStdName   |   aadvari/movie-recommender   |   aparnabhat/kannada-ner   |
|   Kaliel456/Lynn   |   bigcode/santacoder-megatron   |


</details>

### 2022 (38 Models)

<details>
<summary>Click to expand!</summary>

|                                                                  |                                                      |                                          |
| :---------------------------------------------------------------: | :---------------------------------------------------: | :--------------------------------------: |
|            mrm8488/bloom-560m-finetuned-the-stack-rust            |           smallcloudai/codify_medium_multi           |       smallcloudai/codify_3b_multi       |
|                     anjandash/JavaBERT-small                     |                anjandash/JavaBERT-mini                |              saikatc/NatGen              |
|                       Nokia/nlgp-docstring                       |             alecsharpie/codegen_350m_html             |       alecsharpie/codegen_350m_css       |
|                   CarperAI/diff-codegen-350m-v1                   |         giulio98/codegen-350M-multi-xlcost-v2         |    giulio98/codegen-350M-multi-xlcost    |
|                        Nokia/nlgp-natural                        |        model-attribution-challenge/bloom-560m        |          CarperAI/FIM-NeoX-1.3B          |
|               model-attribution-challenge/bloom-2b5               |           huggingface/CodeBERTa-language-id           | codeparrot/codeparrot-small-code-to-text |
|                          moyix/csrc_774m                          |    codeparrot/unixcoder-java-complexity-prediction    | codeparrot/codeparrot-small-text-to-code |
|                 bigscience/bloom-optimizer-states                 |        model-attribution-challenge/bloom-350m        |          little-star/good_model          |
|                 codeparrot/codeparrot-small-multi                 |             bigscience/bloom-intermediate             |        bigscience/tr11-176B-logs        |
|                    codeparrot/codeparrot-small                    |            huggingface/CodeBERTa-small-v1            |          codeparrot/codeparrot          |
|                         lvwerra/test_card                         |                razent/spbert-mlm-base                |        razent/spbert-mlm-wso-base        |
|                      razent/spbert-mlm-zero                      |                  razent/cotext-2-cc                  |           razent/cotext-1-ccg           |
| ietz/distilroberta-base-finetuned-jira-qt-issue-titles-and-bodies | ietz/distilroberta-base-finetuned-jira-qt-issue-title |                                          |

</details>

### 2021 (2 Models)

<details>
<summary>Click to expand!</summary>

|                    |                    |  |
| :-----------------: | :-----------------: | :-: |
| mrm8488/codeBERTaJS | mrm8488/CodeBERTaPy |  |

</details>

## Benchmark List

| Year | Name                                                                                                           |
| ---- | --------------------------------------------------------------------------------------------------------------- |
| 2024  | [BigCodeBench](https://bigcode-bench.github.io/) |
| 2024  | [HumanEval+](https://evalplus.github.io/leaderboard.html) |
| 2024  | [SWE-Bench](https://www.swebench.com) |

## Paper List

**Survey Papers**

| Year | Title                                                                                                           |
| ---- | --------------------------------------------------------------------------------------------------------------- |
| 2024 | [Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/pdf/2409.02977) |
| 2024 | [Robustness, Security, Privacy, Explainability, Efficiency, and Usability of Large Language Models for Code](https://arxiv.org/pdf/2403.07506.pdf) |
| 2023 | [Source Code Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2305.19915)  |
| 2023 | [A Survey of Trojans in Neural Models of Source Code: Taxonomy and Techniques](https://arxiv.org/pdf/2305.03803.pdf)  |
| 2023 | [Towards an Understanding of Large Language Models in Software Engineering Tasks](https://arxiv.org/abs/2308.11396) |
| 2023 | [A Survey of Large Language Models for Code: Evolution, Benchmarking, and Future Trends](https://arxiv.org/abs/2311.10372) |
| 2023 | [Large Language Models for Software Engineering: Survey and Open Problems](https://arxiv.org/abs/2310.03533) |
| 2023 | [Large Language Models for Software Engineering: A Systematic Literature Review](https://arxiv.org/abs/2308.10620) |
| 2023 | [Software Testing with Large Language Model: Survey, Landscape, and Vision](https://arxiv.org/pdf/2307.07221.pdf)  |

**Complete Paper List**

<details>
<summary>Click to expand!</summary>

| Year-Id | Title                                                                                                                                                                     | Venue Name |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
|2024-03        |[Re(gEx\|DoS)Eval: Evaluating Generated Regular Expressions and their Proneness to DoS Attacks](https://joannacss.github.io/preprints/icse_nier24-preprint.pdf)      |ICSE-NIER      |
|2024-02        |[Understanding Regular Expression Denial of Service (ReDoS): Insights from LLM-Generated Regexes and Developer Forums.](https://github.com/s2e-lab/redos-study)      |ICPC      |
|2024-01        |[Using Large Language Models to Generate JUnit Tests: An Empirical Study.](https://s2e-lab.github.io/preprints/ease24-preprint.pdf)      |EASE      |
|2023-33        |[Flakify: A Black-Box, Language Model-Based Predictor for Flaky Tests.](https://doi.org/10.1109/TSE.2022.3201209)      |TSE      |
|2023-32        |[Do Pretrained Language Models Indeed Understand Software Engineering Tasks?](https://doi.org/10.1109/TSE.2023.3308952) |TSE     |
|2023-31        |[CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models.](https://doi.org/10.1109/ICSE48619.2023.00085)  |ICSE   |
|2023-30        |[Impact of Code Language Models on Automated Program Repair.](https://doi.org/10.1109/ICSE48619.2023.00125)    |ICSE   |
|2023-29        |[Automated Repair of Programs from Large Language Models.](https://doi.org/10.1109/ICSE48619.2023.00128)       |ICSE   |
|2023-28        |[Automated Program Repair in the Era of Large Pre-trained Language Models.](https://doi.org/10.1109/ICSE48619.2023.00129)|ICSE   |
|2023-27        |[Recommending Root-Cause and Mitigation Steps for Cloud Incidents using Large Language Models.](https://doi.org/10.1109/ICSE48619.2023.00149)    |ICSE   |
|2023-26        |[Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction.](https://doi.org/10.1109/ICSE48619.2023.00194)        |ICSE   |
|2023-25        |[On the Applicability of Language Models to Block-Based Programs.](https://doi.org/10.1109/ICSE48619.2023.00199)       |ICSE     |
|2023-24        |[The Devil is in the Tails: How Long-Tailed Code Distributions Impact Large Language Models.](https://doi.org/10.1109/ASE56229.2023.00157)       |ASE    |
|2023-23        |[CAT-LM Training Language Models on Aligned Code And Tests.](https://doi.org/10.1109/ASE56229.2023.00193)      |ASE    |
|2023-22        |[Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases.](https://doi.org/10.1109/ASE56229.2023.00076)       |ASE    |
|2023-21        |[The Plastic Surgery Hypothesis in the Era of Large Language Models.](https://doi.org/10.1109/ASE56229.2023.00047)     |ASE      |
|2023-20        |[An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair.](https://doi.org/10.1109/ASE56229.2023.00181)     |ASE    |
|2023-19        |[SMT Solver Validation Empowered by Large Pre-Trained Language Models.](https://doi.org/10.1109/ASE56229.2023.00180)   |ASE      |
|2023-18        |[Towards Autonomous Testing Agents via Conversational Large Language Models.](https://doi.org/10.1109/ASE56229.2023.00148)       |ASE    |
|2023-17        |[Model-Agnostic Syntactical Information for Pre-Trained Programming Language Models.](https://doi.org/10.1109/MSR59073.2023.00036)       |MSR    |
|2023-16        |[Large Language Models and Simple, Stupid Bugs.](https://doi.org/10.1109/MSR59073.2023.00082)  |MSR    |
|2023-15        |[She Elicits Requirements and He Tests: Software Engineering Gender Bias in Large Language Models.](https://doi.org/10.1109/MSR59073.2023.00088) |MSR    |
|2023-14        |[Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair.](https://doi.org/10.1145/3611643.3616271)   |FSE    |
|2023-13        |[Multilingual Code Co-evolution using Large Language Models.](https://doi.org/10.1145/3611643.3616350) |FSE    |
|2023-12        |[Baldur: Whole-Proof Generation and Repair with Large Language Models.](https://doi.org/10.1145/3611643.3616243)       |FSE      |
|2023-11        |[On the Usage of Continual Learning for Out-of-Distribution Generalization in Pre-trained Language Models of Code.](https://doi.org/10.1145/3611643.3616244)     |FSE    |
|2023-10        |[Grace: Language Models Meet Code Edits.](https://doi.org/10.1145/3611643.3616253)     |FSE    |
|2023-9 |[Assess and Summarize: Improve Outage Understanding with Large Language Models.](https://doi.org/10.1145/3611643.3613891)      |FSE      |
|2023-8 |[Getting pwn'd by AI: Penetration Testing with Large Language Models.](https://doi.org/10.1145/3611643.3613083)        |FSE    |
|2023-7 |[Assisting Static Analysis with Large Language Models: A ChatGPT Experiment.](https://doi.org/10.1145/3611643.3613078) |FSE    |
|2023-6 |[A Language Model of Java Methods with Train/Test Deduplication.](https://doi.org/10.1145/3611643.3613090)     |FSE    |
|2023-5 |[Extending Source Code Pre-Trained Language Models to Summarise Decompiled Binarie.](https://doi.org/10.1109/SANER56733.2023.00033)      |SANER  |
|2023-4 |[Large Language Models: The Next Frontier for Variable Discovery within Metamorphic Testing?](https://doi.org/10.1109/SANER56733.2023.00070)     |SANER  |
|2023-3 |[How Robust Is a Large Pre-trained Language Model for Code Generationƒ A Case on Attacking GPT2.](https://doi.org/10.1109/SANER56733.2023.00076) |SANER  |
|2023-2 |[Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models.](https://doi.org/10.1145/3597926.3598067)       |ISSTA  |
|2023-1 |[Harnessing Large Language Models for Simulink Toolchain Testing and Developing Diverse Open-Source Corpora of Simulink Models for Metric and Evolution Analysis.](https://doi.org/10.1145/3597926.3605233)      |ISSTA  |
| 2022-27 | [Fast Changeset-based Bug Localization with BERT](https://doi.org/10.1145/3510003.3510042)                                                                                   | ICSE          |
| 2022-26 | [An Empirical Study on the Usage of Transformer Models for Code Completion](https://doi.org/10.1109/TSE.2021.3128234)                                                        | TSE           |
| 2022-25 | [DualSC: Automatic Generation and Summarization of Shellcode via Transformer and Dual Learning](https://doi.org/10.1109/SANER53432.2022.00052)                               | SANER         |
| 2022-24 | [Source Code Summarization with Structural Relative Position Guided Transformer](https://doi.org/10.1109/SANER53432.2022.00013)                                              | SANER         |
| 2022-23 | [Aspect-Based API Review Classification: How Far Can Pre-Trained Transformer Model Go?](https://doi.org/10.1109/SANER53432.2022.00054)                                       | SANER         |
| 2022-22 | [Can Identifier Splitting Improve Open-Vocabulary Language Model of Code?](https://doi.org/10.1109/SANER53432.2022.00130)                                                    | SANER         |
| 2022-21 | [Evaluation of Context-Aware Language Models and Experts for Effort Estimation of Software Maintenance Issues](https://doi.org/10.1109/ICSME55016.2022.00020)                | ICSME         |
| 2022-20 | [Automating code review activities by large-scale pre-training](https://dl.acm.org/doi/10.1145/3540250.3549081)                                                              | FSE           |
| 2022-19 | [VulCurator: A Vulnerability-fixing Commit Detector](https://doi.org/10.1145/3540250.3558936)                                                                                | FSE           |
| 2022-18 | [AutoPruner: Transformer-based Call Graph Pruning](https://doi.org/10.1145/3540250.3549175)                                                                                  | FSE           |
| 2022-17 | [Can pre-trained code embeddings improve model performance? Revisiting the use of code embeddings in software engineering tasks](https://doi.org/10.1007/s10664-022-10118-5) | EMSE          |
| 2022-16 | [Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding](https://doi.org/10.1145/3510003.3510062)                                                    | ICSE          |
| 2022-15 | [Jigsaw: Large Language Models meet Program Synthesis](https://doi.org/10.1145/3510003.3510203)                                                                              | ICSE          |
| 2022-14 | [Natural Attack for Pre-trained Models of Code](https://doi.org/10.1145/3510003.3510146)                                                                                     | ICSE          |
| 2022-13 | [Using Pre-Trained Models to Boost Code Review Automation](https://doi.org/10.1145/3510003.3510621)                                                                          | ICSE          |
| 2022-12 | [What Do They Capture? - A Structural Analysis of Pre-Trained Language Models for Source Code](https://doi.org/10.1145/3510003.3510050)                                      | ICSE          |
| 2022-11 | [A Light Bug Triage Framework for Applying Large Pre-trained Language Model](https://doi.org/10.1145/3551349.3556898)                                                        | ASE           |
| 2022-10 | [AST-Probe: Recovering abstract syntax trees from hidden representations of pre-trained language models](https://doi.org/10.1145/3551349.3556900)                            | ASE           |
| 2022-9  | [Compressing Pre-trained Models of Code into 3 MB](https://doi.org/10.1145/3551349.3556964)                                                                                  | ASE           |
| 2022-8  | [PRCBERT: Prompt Learning for Requirement Classification using BERT-based Pretrained Language Models](https://doi.org/10.1145/3551349.3560417)                               | ASE           |
| 2022-7  | [Prompt-tuned Code Language Model as a Neural Knowledge Base for Type Inference in Statically-Typed Partial Code](https://doi.org/10.1145/3551349.3556912)                   | ASE           |
| 2022-6  | [Few-shot training LLMs for project-specific code-summarization](https://doi.org/10.1145/3551349.3559555)                                                                    | ASE           |
| 2022-5  | [Diet code is healthy: simplifying programs for pre-trained models of code](https://doi.org/10.1145/3540250.3549094)                                                         | FSE           |
| 2022-4  | [Discrepancies among pre-trained deep neural networks: a new threat to model zoo reliability](https://doi.org/10.1145/3540250.3560881)                                       | FSE           |
| 2022-3  | [Effective and scalable fault injection using bug reports and generative language models](https://doi.org/10.1145/3540250.3558907)                                           | FSE           |
| 2022-2  | [An extensive study on pre-trained models for program understanding and generation](https://doi.org/10.1145/3533767.3534390)                                                 | ISSTA         |
| 2022-1  | [Using pre-trained language models to resolve textual and semantic merge conflicts (experience paper)](https://doi.org/10.1145/3533767.3534396)                              | ISSTA         |
| 2021-7  | [Studying the Usage of Text-To-Text Transfer Transformer to Support Code-Related Tasks](https://doi.org/10.1109/ICSE43902.2021.00041)                                        | ICSE          |
| 2021-6  | [Traceability Transformed: Generating more Accurate Links with Pre-Trained BERT Models](https://doi.org/10.1109/ICSE43902.2021.00040)                                        | ICSE          |
| 2021-5  | [Code Prediction by Feeding Trees to Transformers](https://doi.org/10.1109/ICSE43902.2021.00026)                                                                             | ICSE          |
| 2021-4  | [Traceability Transformed: Generating more Accurate Links with Pre-Trained BERT Models](https://doi.org/10.1109/ICSE43902.2021.00040)                                        | ICSE          |
| 2021-3  | [DeepMemory: Model-based Memorization Analysis of Deep Neural Language Models](https://doi.org/10.1109/ASE51524.2021.9678871)                                                | ASE           |
| 2021-2  | [What do pre-trained code models know about code?](https://doi.org/10.1109/ASE51524.2021.9678927)                                                                            | ASE           |
| 2021-1  | [Does reusing pre-trained NLP model propagate bugs?](https://doi.org/10.1145/3468264.3473494)                                                                                | FSE           |
| 2020-3  | [Achieving Reliable Sentiment Analysis in the Software Engineering Domain using BERT](https://doi.org/10.1109/ICSME46990.2020.00025)                                         | ICSME         |
| 2020-2  | [Sentiment Analysis for Software Engineering: How Far Can Pre-trained Transformer Models Go?](https://doi.org/10.1109/ICSME46990.2020.00017)                                 | ICSME         |
| 2020-1  | [Multi-task Learning based Pre-trained Language Model for Code Completion](https://doi.org/10.1145/3324884.3416591)                                                          | ASE           |

</details>

<a name="paper-stats"></a>

## Paper Stats

### Venue Stats

| Venue | Count |
| ----- | ----- |
| ICSE  | 17    |
| FSE   | 17     |
| ASE   | 16     |
| ISSTA | 4     |
| TSE   | 3     |
| TOSEM | 0     |
| EMSE  | 1     |
| ICSME | 3     |
| SANER | 7     |
| MSR   | 3     |

### Year Stats

| Venue | Count |
| ----- | ----- |
| 2023  | 33    |
| 2022  | 27    |
| 2021  | 7     |
| 2020  | 3     |

## Considered Venues

Powered by an automation tool, mainteners routinary check for new LLM4SE papers that appear in the venues below:

### Conferences

- Software Engineering Domain:
  - **ICSE**: International Conference on Software Engineering
  - **FSE**: The ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
  - **ASE**: IEEE/ACM International Conference on Automated Software Engineering
  - **ISSTA**: International Symposium on Software Testing and Analysis
  - **ICSME**: IEEE International Conference on Software Maintenance and Evolution
  - **MSR**: IEEE Working Conference on Mining Software Repositories
  - **SANER**: IEEE International Conference on Software Analysis, Evolution, and Reengineering

### Journals

- Software Engineering Domain:
  - **TSE**: IEEE Transactions on Software Engineering
  - **TOSEM**: ACM Transactions on Software Engineering and Methodology
  - **EMSE**: Empirical Software Engineering

### Contribution

The easiest way to contribute is to submit a paper with verified information via GitHub issues. Only url of the paper should be already enough. The mainteiner will add accordingly and keep you updated in the issue conversation.

Alternatively, you can create a pull request. For that, you need to strictly follow the format.

Any other suggestion to improve this repository is also highly welcomed via GitHub issues.

### Contributors

<p align="left"><a href="https://github.com/maxxbw54"><img src="https://avatars.githubusercontent.com/maxxbw54?v=4" width="50px" alt="maxxbw54" /></a>  <a href="https://github.com/thanhlecongg"><img src="https://avatars.githubusercontent.com/thanhlecongg?v=4" width="50px" alt="thanhlecongg" /></a></a>  <a href="https://github.com/Xin-Zhou-smu"><img src="https://avatars.githubusercontent.com/Xin-Zhou-smu?v=4" width="50px" alt="Xin-Zhou-smu" /></a>  </p>
