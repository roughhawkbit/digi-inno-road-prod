# digi-inno-road-prod
Project "Do innovation roadmaps lead to productivity and growth?" for Oxford Brookes University Business School, funded by The Productivity Institute.

## Data Security
To avoid Jupyter notebook outputs being committed to GitHub, run the following command in terminal:
```
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'
```

You may need to re-run `git init` for the changes to take effect.
