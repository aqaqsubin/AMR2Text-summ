# Work in progress
# Guided Neural Language Generation for Abstractive Summarization Using AMR

This repository contains code for our EMNLP 2018 paper "[Guided Neural Language Generation for Abstractive Summarization Using AMR](https://arxiv.org/abs/1808.09160)"

# Obtaining the Dataset

We used the [Abstract Meaning Representation Annotation Release 2.0](https://catalog.ldc.upenn.edu/LDC2017T10) which contains manually annotated document and summary AMR.

# Preprocessing the Data

For preprocessing, clone the [AMR preprocessing](https://github.com/sheffieldnlp/AMR-Preprocessing) repository.

```
git clone https://github.com/sheffieldnlp/AMR-Preprocessing
```

Run the AMR linearizing where the input is the system summary AMR from Liu's summarizer ($F) and the AMR raw dataset ($AMR). Here we use the test dataset. Run the preprocessing on the training, and validation dataset if you want to train the model.

```
export F=/<path to test summarizer output>/summ_ramp_10_passes_len_edges_exp_0
export OUTPUT=/<path to test preprocessed output>
export AMR=/<path to AMR>/amr-release-2.0-amrs-test-proxy.txt
python var_free_amrs.py -is_dir -f $F -output_path $OUTPUT --custom_parentheses --no_semantics --delete_amr_var --with_side -side_file $AMR
```

# Training New Model

# Generation with New Model


<!--
Find the raw input = AMR 2.0
- amr-release-2.0-amrs-training-proxy.txt
- amr-release-2.0-amrs-test-proxy.txt
- amr-release-2.0-amrs-dev-proxy.txt

Process the raw input (we have to look into the other repository and find the right argument, look into the paper for clue)
-->
