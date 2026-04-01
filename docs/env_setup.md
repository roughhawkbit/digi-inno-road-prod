# Environment setup

The code in this repository requires installation of [pip](https://pypi.org/project/pip/) and of [Conda](https://docs.conda.io/projects/conda/en/latest/index.html#) (e.g., [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)).

## Using conda

Your terminal should activate the conda base during initialisation. If not, run `source {path_to_conda}/Scripts/activate base`

Then run `conda init`, following any instructions to close and re-open the terminal window, if instructed.

If it's your first time using this repository, run `conda env create -f environment.yml` and accept all Terms of Service, assuming you are happy to do so!

Whenever starting a session running the code, use `conda activate innoprod` first.

### Resolving Pylance errors
If using Visual Studio Code (VSC) as your Integrated Development Environment (IDE), you may notice yellow zigzagged lines under Python import statements. Hovering over the lines will display an error message that the import could not be resolved (Pylance). In the bottom-right of your window, there should be a button saying something like "3.13.5 (base)". Click on this and a selection box should open at the top of the window. Choose the option similar to "Python 3... (innoprod)" and the warnings should disappear.

## PyTorch
Using PyTorch on many systems may require installation of the Cuda Toolkit.

On a Windows machine with ARM64 architecture, instead install Windows ML:
```
pip install wasdk-Microsoft.Windows.AI.MachineLearning[all] wasdk-Microsoft.Windows.ApplicationModel.DynamicDependency.Bootstrap onnxruntime-windowsml
```
and then
```
python scripts/install_windowsml.py
```

C++ build tools and Rust are also required: https://blogs.windows.com/windowsdeveloper/2025/04/23/pytorch-arm-native-builds-now-available-for-windows/

This needs to be completed before attempting to install pytorch.

At time of writing (25 March 2026), PyTorch failed to install correctly via conda but succeeded via pip:

```
pip install torch
```

There was also a conflict between libiomp5md.dll files: manually removing the copy of this file in ~/miniconda3/envs/innoprod/Library/bin resolved the issue.