

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

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.
[screenshot]: resources/readme_images/screenshot.png


