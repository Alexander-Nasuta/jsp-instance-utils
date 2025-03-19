

<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
   <!--
  <a href="https://cybernetics-lab.de/">
    <img src="https://github.com/Alexander-Nasuta/graph-jsp-env/raw/master/resources/readme_images/logo.png">
  </a>
   -->

  <h1 align="center">
     Job Shop Scheduling Problem Benchmark Instances
  </h1>


</div>


- **Github**: https://github.com/Alexander-Nasuta/jsp-instance-utils/

- **PyPi**: https://pypi.org/project/jsp-instance-utils/


# About The Project
This project contains all Job Shop Scheduling Problem (JSP) benchmark instances from http://jobshop.jjvh.nl/ and some utility functions to work with JSP instances.
The project contains a parser to read the instances in the `.txt` files with JPS instances in `taillard` and `standard` format.
For more info about the formatting see: http://jobshop.jjvh.nl/explanation.php
The benchmark instances can be imported as a numpy array.
The instances have the shape `(2, n_jobs, n_machines)`, where the last dimension contains the processing time and the release time of the job on the machine.
So the instance-numpy-array consists of two numpy arrays, the first array contains the order of the machines and the second array contains the processing times of the tasks on the machines.
here is a minimal example of how to define a instance:

```python
import numpy as np
custom_jsp_instance = np.array([
    [
        [0, 1, 2, 3],  # job 0 (machine0, machine1, machine2, machine3)
        [0, 2, 1, 3]  # job 1 (machine0, machine1, machine2, machine3)
    ],
    [
        [11, 3, 3, 12],  # task durations of job 0
        [5, 16, 7, 4]  # task durations of job 1
    ]
])

```
# Installation

Install the package with pip:
```
   pip install jsp-instance-utils
```

# Importing a JSP instance OR-tools Solver
`jsp-instance-utils` contains provides a implementation of the OR-tools solver for the JSP in the numpy array format provided by `jsp-instance-utils`.
The following example shows how to import and solve the ft06 instance with the OR-tools solver:

```python
from jsp_instance_utils.instances import ft06
from jsp_instance_utils.jsp_or_tools_solver import solve_jsp

makespan, status, *_ = solve_jsp(jsp_instance=ft06, plot_results=True)

assert status == "OPTIMAL"
assert makespan == 55
```

The code above yields the following output, if the `plot_results` flag is set to `True`:

![](https://raw.githubusercontent.com/Alexander-Nasuta/jsp-instance-utils/main/resources/ft06-or-tools.png)

# Available Instances

All instances are available in the `jsp_instance_utils.instances` module.
You can also find them on this website: http://jobshop.jjvh.nl/

# More Examples
For more examples you can have a look at the test files in the `tests` directory.

## Development Setup

If you want to check out the code and implement new features or fix bugs, you can set up the project as follows:

### Clone the Repository

clone the repository in your favorite code editor (for example PyCharm, VSCode, Neovim, etc.)

using https:
```shell
git clone https://github.com/Alexander-Nasuta/graph-jsp-env
```
or by using the GitHub CLI:
```shell
gh repo clone Alexander-Nasuta/graph-jsp-env
```

if you are using PyCharm, I recommend doing the following additional steps:

- mark the `src` folder as source root (by right-clicking on the folder and selecting `Mark Directory as` -> `Sources Root`)
- mark the `tests` folder as test root (by right-clicking on the folder and selecting `Mark Directory as` -> `Test Sources Root`)
- mark the `resources` folder as resources root (by right-clicking on the folder and selecting `Mark Directory as` -> `Resources Root`)

at the end your project structure should look like this:

todo

### Create a Virtual Environment (optional)

Most Developers use a virtual environment to manage the dependencies of their projects.
I personally use `conda` for this purpose.

When using `conda`, you can create a new environment with the name 'my-graph-jsp-env' following command:

```shell
conda create -n my-graph-jsp-env python=3.11
```

Feel free to use any other name for the environment or an more recent version of python.
Activate the environment with the following command:

```shell
conda activate jsp-instance-utils
```

Replace `jsp-instance-utils` with the name of your environment, if you used a different name.

You can also use `venv` or `virtualenv` to create a virtual environment. In that case please refer to the respective documentation.

### Install the Dependencies

To install the dependencies for development purposes, run the following command:

```shell
pip install -r requirements_dev.txt
pip install tox
```

The testing package `tox` is not included in the `requirements_dev.txt` file, because it sometimes causes issues when
using github actions.
Github Actions uses an own tox environment (namely 'tox-gh-actions'), which can cause conflicts with the tox environment on your local machine.

Reference: [Automated Testing in Python with pytest, tox, and GitHub Actions](https://www.youtube.com/watch?v=DhUpxWjOhME).

### Install the Project in Editable Mode

To install the project in editable mode, run the following command:

```shell
pip install -e .
```

This will install the project in editable mode, so you can make changes to the code and test them immediately.

### Run the Tests

This project uses `pytest` for testing. To run the tests, run the following command:

```shell
pytest
```

For testing with `tox` run the following command:

```shell
tox
```

Tox will run the tests in a separate environment and will also check if the requirements are installed correctly.

### Building and Publishing the Project to PyPi

In order to publish the project to PyPi, the project needs to be built and then uploaded to PyPi.

To build the project, run the following command:

```shell
python -m build
```

It is considered good practice use the tool `twine` for checking the build and uploading the project to PyPi.
By default the build command creates a `dist` folder with the built project files.
To check all the files in the `dist` folder, run the following command:

```shell
twine check dist/**
```

If the check is successful, you can upload the project to PyPi with the following command:

```shell
twine upload dist/**
```

### Documentation
This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).



## Contact

If you have any questions or feedback, feel free to contact me via [email](mailto:alexander.nasuta@wzl-iqs.rwth-aachen.de) or open an issue on repository.



# License

Distributed under the MIT License. See `LICENSE.txt` for more information.
[screenshot]: resources/readme_images/screenshot.png


