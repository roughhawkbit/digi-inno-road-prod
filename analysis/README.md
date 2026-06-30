# Analysis

This repository contains a series of [Jupyter notebooks](https://jupyter.org/) for data exploration, processing, and analysis. 

## Notebook organisation
There are several key phases in notebook development, although the separation between the two is often transitional rather than a clean break:
1. Exploration of data & methods
2. Notebooks that drive decision-making
3. Rigourous pipeline for producing results

Notebooks in the final phase could be migrated to a pipeline tool, such as [Luigi](https://luigi.readthedocs.io/en/stable/), within a different context, but in this project we are constrained by the single option available for heavy computing power: [Google Colab](https://colab.research.google.com/), which focuses on Jupyter notebooks and which offers runtimes such as GPUs and TPUs. 

In order to organise the notebooks so that the structure can be easily navigated, adopt the following naming convention:
* Pipeline notebooks start with a number for ordering and then a short hyphen delimited description. E.g., `1.0-initial-analysis.ipynb`.
* Decision notebooks start with a `d` and then a short hyphen delimited description. E.g., `d-use-org-size-category-for-firm-size.md`.They should also be linked to the corresponding document in the [decisions](../decisions/) folder, where possible.
* Exploratory notebooks start with an `x` and then a short hyphen delimited description. E.g., `x-data-wrangling.md`.

## Interaction with codebase
See the main repository [READ-ME file](../README.md#interaction-between-codebase--analysis) for how to use these notebooks in this folder together with the codebase elsewhere in the repository.

## Development environment

Difference between local machine and Google Colab
