# Large Language Model for Software Engineering

The collection is actively updated with the help of an internal literature search engine.

# Table of Contents

| [Code Model List](#model-list) |
| [Paper List](#paper-list) |
| [Paper Stats](#paper-stats) |

<a name="model-list"></a>
## Model List

| Year-Id | Model Name    | Paper                            | # of Parameters /Model Size | Open Source?                                             |
|---------|---------------|----------------------------------|-----------------------------|----------------------------------------------------------|
| 2023-3  | CodeT5+       | [link](https://arxiv.org/abs/2305.07922) | [220M, 770M, 2B, 6B, 16B]   | [source](https://github.com/salesforce/CodeT5/tree/main/CodeT5%2B) |
| 2023-2  | StarCoder     | [link](https://arxiv.org/abs/2305.06161) | [15B]                       | [source](https://github.com/bigcode-project/starcoder)             |
| 2023-1  | CodeGeeX      | [link](https://arxiv.org/abs/2303.17568) | [13B]                       | [source](https://github.com/THUDM/CodeGeeX)                        |
| 2022-2  | InCoder       | [link](https://arxiv.org/abs/2204.05999) | [1.3B/2.62GB, 6B(26.6GB)]   | [source](https://github.com/dpfried/incoder)                       |
| 2022-1  | CodeGen       | [link](https://arxiv.org/abs/2203.13474) | [350M, 2B, 6B, 16B]         | [source](https://github.com/salesforce/CodeGen)                    |
| 2021-1  | CodeT5        | [link](https://arxiv.org/abs/2109.00859) | [770M/892MB]                | [source](https://github.com/salesforce/CodeT5)                     |
| 2020-2  | GraphCodeBERT | [link](https://arxiv.org/abs/2009.08366) |                             | [source](https://github.com/microsoft/CodeBERT#graphcodebert)      |
| 2020-1  | CodeBERT      | [link](https://arxiv.org/abs/2002.08155) |                             | [source](https://github.com/microsoft/CodeBERT)                    |


<a name="paper-list"></a>
## Paper List

<details>
<summary>Click to expand!</summary>
  
| Year-Id | Title        | Venue Name(Type) |
|---------|---------------------------------------------------------------------------------------------------------------------------------|------------|
| 2023-1  | [Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning](https://10.1109/TSE.2023.3255177)              | TSE(J)        |
| 2022-27 | [Fast Changeset-based Bug Localization with BERT](https://doi.org/10.1145/3510003.3510042)       | ICSE(C)       |
| 2022-26  | [An Empirical Study on the Usage of Transformer Models for Code Completion](https://doi.org/10.1109/TSE.2021.3128234)              | TSE(J)        |
| 2022-25  | [DualSC: Automatic Generation and Summarization of Shellcode via Transformer and Dual Learning](https://doi.org/10.1109/SANER53432.2022.00052)       | SANER(C)        |
| 2022-24  | [Source Code Summarization with Structural Relative Position Guided Transformer](https://doi.org/10.1109/SANER53432.2022.00013)       | SANER(C)        |
| 2022-23  | [Aspect-Based API Review Classification: How Far Can Pre-Trained Transformer Model Go?](https://doi.org/10.1109/SANER53432.2022.00054)       | SANER(C)        |
| 2022-22  | [Can Identifier Splitting Improve Open-Vocabulary Language Model of Code?](https://doi.org/10.1109/SANER53432.2022.00130)       | SANER(C)        |
| 2022-21  | [Evaluation of Context-Aware Language Models and Experts for Effort Estimation of Software Maintenance Issues](https://doi.org/10.1109/ICSME55016.2022.00020)       | ICSME(C)        |
| 2022-20 | [Automating code review activities by large-scale pre-training](https://dl.acm.org/doi/10.1145/3540250.3549081)                                                                                    | FSE(C)        |
| 2022-19 | [VulCurator: A Vulnerability-fixing Commit Detector](https://doi.org/10.1145/3540250.3558936)       | FSE(C)        |
| 2022-18 | [AutoPruner: Transformer-based Call Graph Pruning](https://doi.org/10.1145/3540250.3549175)       | FSE(C)        |
| 2022-17 | [Can pre-trained code embeddings improve model performance? Revisiting the use of code embeddings in software engineering tasks](https://doi.org/10.1007/s10664-022-10118-5)    | EMSE(J)       |
| 2022-16 | [Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding](https://doi.org/10.1145/3510003.3510062)       | ICSE(C)       |
| 2022-15 | [Jigsaw: Large Language Models meet Program Synthesis](https://doi.org/10.1145/3510003.3510203)       | ICSE(C)       |
| 2022-14 | [Natural Attack for Pre-trained Models of Code](https://doi.org/10.1145/3510003.3510146)       | ICSE(C)       |
| 2022-13 | [Using Pre-Trained Models to Boost Code Review Automation](https://doi.org/10.1145/3510003.3510621)       | ICSE(C)       |
| 2022-12 | [What Do They Capture? - A Structural Analysis of Pre-Trained Language Models for Source Code](https://doi.org/10.1145/3510003.3510050)       | ICSE(C)       |
| 2022-11 | [A Light Bug Triage Framework for Applying Large Pre-trained Language Model](https://doi.org/10.1145/3551349.3556898)       | ASE(C)        |
| 2022-10 | [AST-Probe: Recovering abstract syntax trees from hidden representations of pre-trained language models](https://doi.org/10.1145/3551349.3556900)       | ASE(C)        |
| 2022-9  | [Compressing Pre-trained Models of Code into 3 MB](https://doi.org/10.1145/3551349.3556964)       | ASE(C)        |
| 2022-8  | [PRCBERT: Prompt Learning for Requirement Classification using BERT-based Pretrained Language Models](https://doi.org/10.1145/3551349.3560417)       | ASE(C)        |
| 2022-7  | [Prompt-tuned Code Language Model as a Neural Knowledge Base for Type Inference in Statically-Typed Partial Code](https://doi.org/10.1145/3551349.3556912)       | ASE(C)        |
| 2022-6  | [Few-shot training LLMs for project-specific code-summarization](https://doi.org/10.1145/3551349.3559555)       | ASE(C)        |
| 2022-5  | [Diet code is healthy: simplifying programs for pre-trained models of code](https://doi.org/10.1145/3540250.3549094)       | FSE(C)        |
| 2022-4  | [Discrepancies among pre-trained deep neural networks: a new threat to model zoo reliability](https://doi.org/10.1145/3540250.3560881)       | FSE(C)        |
| 2022-3  | [Effective and scalable fault injection using bug reports and generative language models](https://doi.org/10.1145/3540250.3558907)       | FSE(C)        |
| 2022-2  | [An extensive study on pre-trained models for program understanding and generation](https://doi.org/10.1145/3533767.3534390)       | ISSTA(C)      |
| 2022-1  | [Using pre-trained language models to resolve textual and semantic merge conflicts (experience paper)](https://doi.org/10.1145/3533767.3534396)       | ISSTA(C)      |
| 2021-7 | [Studying the Usage of Text-To-Text Transfer Transformer to Support Code-Related Tasks](https://doi.org/10.1109/ICSE43902.2021.00041)       | ICSE(C)       |
| 2021-6 | [Traceability Transformed: Generating more Accurate Links with Pre-Trained BERT Models](https://doi.org/10.1109/ICSE43902.2021.00040)       | ICSE(C)       |
| 2021-5 | [Code Prediction by Feeding Trees to Transformers](https://doi.org/10.1109/ICSE43902.2021.00026)       | ICSE(C)       |
| 2021-4  | [Traceability Transformed: Generating more Accurate Links with Pre-Trained BERT Models](https://doi.org/10.1109/ICSE43902.2021.00040)  | ICSE(C)       |
| 2021-3  | [DeepMemory: Model-based Memorization Analysis of Deep Neural Language Models](https://doi.org/10.1109/ASE51524.2021.9678871) | ASE(C)        |
| 2021-2  | [What do pre-trained code models know about code?](https://doi.org/10.1109/ASE51524.2021.9678927) | ASE(C)        |
| 2021-1  | [Does reusing pre-trained NLP model propagate bugs?](https://doi.org/10.1145/3468264.3473494)       | FSE(C)        |
| 2020-3  | [Achieving Reliable Sentiment Analysis in the Software Engineering Domain using BERT](https://doi.org/10.1109/ICSME46990.2020.00025)       | ICSME(C)        |
| 2020-2  | [Sentiment Analysis for Software Engineering: How Far Can Pre-trained Transformer Models Go?](https://doi.org/10.1109/ICSME46990.2020.00017)       | ICSME(C)        |
| 2020-1  | [Multi-task Learning based Pre-trained Language Model for Code Completion](https://doi.org/10.1145/3324884.3416591)       | ASE(C)        |
  
</details>

<a name="paper-stats"></a>
## Paper Stats


### Venue Stats

| Venue | Count |
|-------|-------|
| ICSE  |   10   |
| FSE   |   7    |
| ASE   |   9    |
| ISSTA |   2    |
| TSE   |   2    |
| TOSEM |   0    |
| EMSE  |    1   |
| ICSME  |    3   |
| SANER  |    4   |
| MSR  |    0   |

### Year Stats

| Venue | Count |
|-------|-------|
| 2023  |   1    |
| 2022  |   27    |
| 2021   |   7    |
| 2020 |    3   |

## Considered Venues
Powered by an automation tool, mainteners routinary check for new program repair papers that appear in the venues below:

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

<p align="left"><a href="https://github.com/maxxbw54"><img src="https://avatars.githubusercontent.com/maxxbw54?v=4" width="50px" alt="maxxbw54" /></a>&nbsp;&nbsp;<a href="https://github.com/thanhlecongg"><img src="https://avatars.githubusercontent.com/thanhlecongg?v=4" width="50px" alt="thanhlecongg" /></a></a>&nbsp;&nbsp;</p>




