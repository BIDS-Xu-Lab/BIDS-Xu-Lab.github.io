Title: Xu Zuo's paper has been accepted by JCO Clinical Cancer Informatics! 🎉
Category: news
Date: 2024-03-15
Slug: xu-jco-acceptance
Tags: paper
Summary: Xu Zuo's paper **Extracting Systemic Anticancer Therapy and Response Information from Clinical Notes following the RECIST Definition** has been accepted by **JCO Clinical Cancer Informatics**!


Xu Zuo's paper **Extracting Systemic Anticancer Therapy and Response Information from Clinical Notes following the RECIST Definition** has been accepted by **JCO Clinical Cancer Informatics**!

## Abstract
 
**OBJECTIVE**: The Response Evaluation Criteria in Solid Tumors (RECIST) guidelines provide a standardized approach for evaluating the response of cancer to treatment, allowing for consistent comparison of treatment efficacy across different therapies and patients. However, collecting such information from electronic health records (EHRs) manually can be extremely labor-intensive and time-consuming due to the complexity and volume of clinical notes. The aim of this study is to apply natural language processing (NLP) techniques to automate the process of extracting the necessary information for cancer treatment and efficacy assessment, reducing the need for manual data collection, and improving the consistency and reliability of the results.

**METHODS**: We proposed a complex, hybrid NLP system that automates the process of extracting, linking, and summarizing anticancer therapy and associated RECIST-like responses from narrative clinical text. The system consists of multiple machine learning/deep learning-based and rule-based modules for diverse NLP tasks such as named entity recognition, assertion classification, relation extraction, and text normalization, to address different challenges associated with anticancer therapy and response information extraction. We then evaluated the system performances on two independent test sets from different institutions to demonstrate its effectiveness and generalizability.

**RESULTS**: In the entity extraction step, two domain-specific language models, BioBERT and BioClinicalBERT, achieved high performance in identifying therapy mentions, as well as extracting and categorizing RECIST responses.  In the relation extraction step, our best-performing model achieved 0.66 in linking therapy and RECTIST response mentions. After relation normalization that removed duplicated relations, our highest end-to-end performance reached 0.74, implying that our system has fairly good performance with potential space for improvements.

**CONCLUSION**: We developed, implemented, and tested an information extraction system from clinical notes for cancer treatment and efficacy assessment information. We expect this system will support future cancer research, particularly oncological studies that focus on efficiently assessing the effectiveness and reliability of cancer therapeutics.