Title: Yan's paper is accepted in Bioinformatics! 🎉
Category: news
Date: 2023-09-01
Slug: yanhu-bioinfo-acceptance
Tags: paper
Summary: Yan's work **Towards precise PICO extraction from abstracts of randomized controlled trials using a section-specific learning approach** has been accepted and published by **Bioinformatics**


Yan's work **Towards precise PICO extraction from abstracts of randomized controlled trials using a section-specific learning approach** has been accepted and published by **Bioinformatics**, PMID: [37669123](https://pubmed.ncbi.nlm.nih.gov/37669123/) PMCID: PMC10500081, DOI: https://doi.org/10.1093/bioinformatics/btad542.

## Abstract

### Motivation
Automated extraction of population, intervention, comparison/control, and outcome (PICO) from the randomized controlled trial (RCT) abstracts is important for evidence synthesis. Previous studies have demonstrated the feasibility of applying natural language processing (NLP) for PICO extraction. However, the performance is not optimal due to the complexity of PICO information in RCT abstracts and the challenges involved in their annotation.

### Results
We propose a two-step NLP pipeline to extract PICO elements from RCT abstracts: (i) sentence classification using a prompt-based learning model and (ii) PICO extraction using a named entity recognition (NER) model. First, the sentences in abstracts were categorized into four sections namely background, methods, results, and conclusions. Next, the NER model was applied to extract the PICO elements from the sentences within the title and methods sections that include >96% of PICO information. We evaluated our proposed NLP pipeline on three datasets, the EBM-NLPmod dataset, a randomly selected and re-annotated dataset of 500 RCT abstracts from the EBM-NLP corpus, a dataset of 150 Coronavirus Disease 2019 (COVID-19) RCT abstracts, and a dataset of 150 Alzheimer’s disease (AD) RCT abstracts. The end-to-end evaluation reveals that our proposed approach achieved an overall micro F1 score of 0.833 on the EBM-NLPmod dataset, 0.928 on the COVID-19 dataset, and 0.899 on the AD dataset when measured at the token-level and an overall micro F1 score of 0.712 on EBM-NLPmod dataset, 0.850 on the COVID-19 dataset, and 0.805 on the AD dataset when measured at the entity-level.