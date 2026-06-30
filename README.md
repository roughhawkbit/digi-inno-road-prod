# digi-inno-road-prod
Project "Do innovation roadmaps lead to productivity and growth?" for Oxford Brookes University Business School, funded by [The Productivity Institute](https://www.productivity.ac.uk/).

## Data Security
To avoid Jupyter notebook outputs being committed to GitHub, run the following command in terminal:
```
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'
```

You may need to re-run `git init` for the changes to take effect.

## Interaction between codebase & analysis

The [Jupyter notebooks](https://jupyter.org/) in the [analysis](./analysis/) folder are where exploratory data science is best conducted, including initial development of methods. As these methods become established, however, it is best to migrate them into the codebase in the [innoprod](./innoprod/) folder; this enables:
1. consistent re-use across multiple notebooks, thereby facilitating (a) focus of notebooks on specific questions, (b) simpler version control of notebooks, and (c) avoiding situations where tweaks to methods must be manually copy/pasted across notebooks or where methods become inconsistent.
2. rigourous (unit) testing of methods within the [tests](./tests/) folder.
