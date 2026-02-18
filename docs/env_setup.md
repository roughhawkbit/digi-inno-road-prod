# Environment setup

The code in this repository requires installation of [pip](https://pypi.org/project/pip/) and of [Conda](https://docs.conda.io/projects/conda/en/latest/index.html#) (e.g., [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)).

## Using conda

Your terminal should activate the conda base during initialisation. If not, run `source {path_to_conda}/Scripts/activate base`

Then run `conda init`, following any instructions to close and re-open the terminal window, if instructed.

If it's your first time using this repository, run `conda env create -f environment.yml` and accept all Terms of Service, assuming you are happy to do so!

Whenever starting a session running the code, use `conda activate innoprod` first.

### Resolving Pylance errors
If using Visual Studio Code (VSC) as your Integrated Development Environment (IDE), you may notice yellow zigzagged lines under Python import statements. Hovering over the lines will display an error message that the import could not be resolved (Pylance). In the bottom-right of your window, there should be a button saying something like "3.13.5 (base)". Click on this and a selection box should open at the top of the window. Choose the option similar to "Python 3... (innoprod)" and the warnings shoudl disappear.
