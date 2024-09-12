
# PyDaddy 

[![Documentation Status](https://readthedocs.org/projects/pydaddy/badge/?version=latest)](https://pydaddy.readthedocs.io/en/latest/?badge=latest) [![](https://img.shields.io/github/license/tee-lab/PyDaddy) ](https://github.com/tee-lab/PyDaddy/blob/master/LICENSE.txt) [![](https://img.shields.io/badge/arXiv-preprint-red)](https://arxiv.org/abs/2205.02645)


Discovering stochastic dynamical equations from ecological time series data, together with an easy to use Python package.

### Citation to the manuscript
Nabeel, A., Karichannavar, A., Palathingal, S., Jhawar, J., Bruckner, B., Danny Raj, M., & Guttal, V., "Discovering stochastic dynamical equations from ecological time series data", arXiv preprint [arXiv:2205.02645](https://arxiv.org/abs/2205.02645), to appear in <strong>The American Naturalist</strong>. 

### Citation to the package

Nabeel, A., Karichannavar, A., Palathingal, S., Jhawar, J., Bruckner, David B., Danny Raj, M., & Guttal, V. (2024). PyDaddy: A Python Package for Discovering SDEs from Time Series Data (Version 1.1.1) [Computer software]. https://github.com/tee-lab/PyDaddy   

### Authors and Contact Details

#### Corresponding Authors
Arshed Nabeel, IISc Mathematics Initiative and Centre for Ecological Sciences, Indian Institute of Science, Bengaluru, Karnatata, 560012, India.
Email: arshed@iisc.ac.in and arshed.nabeel@gmail.com 

Danny Raj M, Dept of Applied Mechanics and Biomedical Engineering, IIT Madras, Chennai, 600036, India.
Email: danny@iitm.ac.in

Vishwesha Guttal, Centre for Ecological Sciences, Indian Institute of Science, Bengaluru, Karnatata, 560012, India. 
Email: guttal@iisc.ac.in

#### Code and Data Contributors
Codes and package were written by Arshed Nabeel and Ashwin Karichannavar. 

The package uses two datasets from previously published papers, which are also made available as part of the package. 

* Fish dataset: Jhawar, Jitesh, et al. "Noise-induced schooling of fish." Nature Physics 16.4 (2020): 488-493. https://www.nature.com/articles/s41567-020-0787-y

* Cell migration dataset: Brückner, David B., et al. "Stochastic nonlinear dynamics of confined cell migration in two-state systems." Nature Physics 15.6 (2019): 595-601. https://www.nature.com/articles/s41567-019-0445-4

### Overview of the study and package

<strong>PyDaddy</strong> is an open source package which is a key contribution of the manuscript Nabeel et al, [arXiv:2205.02645](https://arxiv.org/abs/2205.02645). The basic scientific premise for this package is to discover the nature of stochasticity in ecological time series datasets. It is well known that the stochasticity can affect the dynamics of ecological systems in counter-intuitive ways. Without understanding the equations (typically, in the form of stochastic differential equations or SDEs, in short) that govern the dynamics of populations or ecosystems, it's challenging to determine the impact of randomness on real datasets. In this manuscript and accompanying package, we introduce a methodology for discovering equations (SDEs) that transforms time series data of state variables into stochastic differential equations. This approach merges traditional stochastic calculus with modern equation-discovery techniques. We showcase the generality of our method through various applications and discuss its limitations and potential pitfalls, offering diagnostic measures to address these challenges.

<strong>PyDaddy</strong> is a comprehensive and easy to use python package to discover data-derived stochastic differential equations from time series data. PyDaddy takes the time series of state variable $x$, scalar or 2-dimensional vector, as input and discovers an SDE of the form:

$$ \frac{dx}{dt} = f(x) + g(x) \cdot \eta(t) $$

where $\eta(t)$ is Gaussian white noise. The function $f$ is called the _drift_, and governs the deterministic part of the dynamics. $g^2$ is called the _diffusion_ and governs the stochastic part of the dynamics.



| ![](https://github.com/tee-lab/PyDaddy/blob/master/resources/PyDaddyExample.jpg?raw=true) |
| :---: |
| An example summary plot generated by PyDaddy, for a vector time series dataset. |

PyDaddy also provides a range of functionality such as equation-learning for the drift and diffusion functions using sparse regresssion, a suite of diagnostic functions, etc.. For more details on how to use the package, check out the [example notebooks](./notebooks) and [documentation](https://pydaddy.readthedocs.io/).

### Workflow and Documentation
The workflow of the package is summarised by the schematic given below - which is also the Fig 1 of the manuscript (https://arxiv.org/abs/2205.02645). 

A detailed workflow of the package along with detailed instructions on various features are included as Supplementary Information Section S2 of the manuscript. 

Detailed documentation of the PyDaddy package can be found at [ documentation](https://pydaddy.readthedocs.io/).

| ![](https://github.com/tee-lab/PyDaddy/blob/master/resources/PyDaddySchematic.jpg?raw=true) |
| :---: |
| Schematic illustration of PyDaddy functionality. |

### Getting Started Without Package Installation

We provide a number of easy to use scripts for the ease of learning and using the package, and with an aim that our manuscript is easily reproducible. 

First, we emphasise that PyDaddy can be executed online on [Google Colab](https://colab.research.google.com/), without having to install it on your local machine. To run PyDaddy on Colab, open a notebook on Colab. Paste the following code on a notebook cell and run it:

    %pip install git+https://github.com/tee-lab/PyDaddy.git

This sets up PyDaddy in the notebook environment.

### Example Scripts/Jupyter Notebooks
There are several <strong>example scripts / Jupyter notebooks</strong> provided, which can be used to familiarize yourself with various features and functionalities of PyDaddy. These can be executed on Colab.

- <strong>Notebook 1</strong>: [Getting started with scalar data](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/1_getting_started.ipynb): Introduction to the basic functionalities of PyDaddy, using a 1-dimensional dataset.
- <strong>Notebook 2</strong>: [Getting started with vector data](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/2_getting_started_vector.ipynb): Introduction to the basic functionalities of PyDaddy on 2-dimensional datasets.
- <strong>Notebook 3</strong>: [Advanced function fitting](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/3_advanced_function_fitting.ipynb): PyDaddy can discover analytical expressions for the drift and diffusion functions. This notebook describes how to customize the fitting procedure to obtain best results.
- <strong>Notebook 4</strong>: [Recovering SDEs from synthetic time series](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/4_sdes_from_simulated_timeseries.ipynb): This notebook generates a simulated time series from a user-specified SDE, and uses PyDaddy to recover the drift and diffusion functions from the simulated time series.
- <strong>Notebook 5</strong>: [Exporting data](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/5_exporting_data.ipynb): Demonstrates how to export the recovered drift and diffusion data as CSV files or Pandas data-frames.
- <strong>Notebook 6</strong>: [Fitting non-polynomial functions](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/6_non_poly_function_fitting.ipynb): PyDaddy fits polynomial functions to drift and diffusion by default. This behaviour can be customized, this notebook illustrates how to do this.
- <strong>Notebook 9</strong>: [Demonstration with a 3-dimensional system] An example to demonstrate that, in principle, the method of stochastic equation discovery can be extended to higher dimensions. 

(See below for Notebooks 7 and 8).

### Real datasets and Scripts/Jupyter Notebooks
There are also two notebooks that use PyDaddy to discover SDEs from real-world datasets.

* <strong>Fish Schooling Dataset </strong>: The fish data (<strong>Folder: pydaddy/data/fish_data</strong>) contains a subset of the fish schooling dataset presented in the manuscript. The dataset contains the 2D polarisation vector time series of a fish school (15 fish). The full dataset is available at https://zenodo.org/records/3632470. For more details about the dataset, see https://doi.org/10.1038/s41567-020-0787-y 
   * <strong>Notebook 7</strong>: [Example analysis - fish schooling](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/7_example_fish_school.ipynb): An example analysis of a fish schooling dataset (Jhawar et. al., Nature Physics, 2020) using PyDaddy. 

* <strong>Cell Migration Dataset </strong>: The confine cell migration dataset (<strong>Folder: pydaddy/data/cell_data</strong>) contains tracked trajectories of 149 cells, tracked for upto 300 time steps each, with one data point every 15 minutes. The data is provided as a plain text file. Each row corresponds to the time series of one cell. For more details about the dataset, see https://doi.org/10.1038/s41567-019-0445-4.
   * <strong>Notebook 8</strong>: [Example analysis - cell migration](https://colab.research.google.com/github/tee-lab/PyDaddy/blob/colab/notebooks/8_example_cell_migration.ipynb): An example analysis of a confined cell migration dataset (Brückner et. al., Nature Physics, 2019) using PyDaddy.
   
### Folder structure
The zipped folder whose link is given below is structured as follows: <strong>(TO BE DONE)</strong>

### Package Installation
PyDaddy is available both on PyPI and Anaconda Cloud, and can be installed on any system with a Python 3 environment. If you don't have Python 3 installed on your system, we recommend using [Anaconda](https://www.anaconda.com) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). See the PyDaddy [package documentation](https://pydaddy.readthedocs.io/) for detailed installation instructions.

#### Using pip
![PyPI](https://img.shields.io/pypi/v/pydaddy?color=blue) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/pydaddy) ![PyPI - Status](https://img.shields.io/pypi/status/pydaddy)

To install the latest stable release version of PyDaddy, use:

	pip install pydaddy

To install the latest development version of PyDaddy, use:

    pip install git+https://github.com/tee-lab/PyDaddy.git

#### Using anaconda
![](https://anaconda.org/tee-lab/pydaddy/badges/version.svg) ![](https://anaconda.org/tee-lab/pydaddy/badges/latest_release_date.svg) ![](https://anaconda.org/tee-lab/pydaddy/badges/platforms.svg)

To install using `conda`, [Anaconda](https://www.anaconda.com) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) need to be installed first. Once this is done, use the following command.

    conda install -c tee-lab pydaddy
    
<!---
   *Click [here](https://github.com/tee-lab/PyDaddy/archive/master.zip) to download source repository zip file.*
--->

### Detailed Package Documentation
For more information about PyDaddy, check out the [package documentation](https://pydaddy.readthedocs.io/).

### Citation
If you are using this package in your research, please cite the repository and the associated [paper](https://arxiv.org/abs/2205.02645) as follows:

Nabeel, A., Karichannavar, A., Palathingal, S., Jhawar, J., Bruckner, David B., Danny Raj, M., & Guttal, V. (2024). PyDaddy: A Python Package for Discovering SDEs from Time Series Data (Version 1.1.1) [Computer software]. https://github.com/tee-lab/PyDaddy, DOI: To Do. 

Nabeel, A., Karichannavar, A., Palathingal, S., Jhawar, J., Bruckner, B., Danny Raj, M., & Guttal, V., "Discovering stochastic dynamical equations from ecological time series data", arXiv preprint [arXiv:2205.02645](https://arxiv.org/abs/2205.02645), to appear in <strong>The American Naturalist</strong>. 


### Licence
PyDaddy is distributed under the [**GNU General Public License v3.0**](./LICENSE.txt).

