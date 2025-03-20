# Usage

To get started, you need to install the package. You can do this by running the following command:

```bash
pip install jsp-instance-utils
```
Then you can import instances from the package and use them in your code. For example, to load an instance from the package.
Here is an example of how to load the `ft06` instance from the package:
```
from jsp_instance_utils.instances import ft06
from jsp_instance_utils.instances import ft06_makespan
from jsp_instance_utils.instances import ft06_makespan_is_optimal
```
or you can do it in a more compact way:
```
from jsp_instance_utils.instances import ft06, ft06_makespan, ft06_makespan_is_optimal
```

The individual instances follow the naming in the Table of isntances.
The `_makespan`-suffix indicates yields the lowest makespan of the instance that is known (cf. the cited literature).
For small instances this is the optimal makespan, for larger instances it is the best known makespan.
The `_makespan_is_optimal`-suffix indicates whether the `_makespan`-value is optimal or not.
So `ft06` refers to the instance (in the format of this software package), `ft06_makespan` to the best known makespan, and `ft06_makespan_is_optimal` to whether the best known makespan is optimal or not.
The `ft06` instance is a small instance with 6 jobs and 6 machines and was introduced by Fisher and Thompson in 1963.

Here is another example of how to load the `ta01` instance from the package:
```
from jsp_instance_utils.instances import ta01, ta01_makespan, ta01_makespan_is_optimal
```
The `ta01` instance is a instance with 10 jobs and 10 machines and was introduced by Taillard in 1993.

## Format of the Instances

```{note}
The machines are indexed starting from 0.
```

The instances in this package are represented as numpy arrays with shape `(n_jobs, n_machines, 2)`.
here is a small example:

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
This format is useful, because the individual matrices can easily be extracted.
Here is an example:

```python
machine_matrix, processing_time_matrix = custom_jsp_instance
```
That way `machine_matrix` would be:

```python
np.array([
    [0, 1, 2, 3],
    [0, 2, 1, 3]
])
```
and `processing_time_matrix` would be:

```python
np.array([
    [11, 3, 3, 12],
    [5, 16, 7, 4]
])
```

Here is a complete runnable example of how to load the `ft06` instance from the package and how to extract the machine matrix and the processing time matrix:

```python
from jsp_instance_utils.instances import ft06, ft06_makespan, ft06_makespan_is_optimal

machine_matrix, processing_times = ft06

print(f"""
The machine matrix of instance 'ft06' is:
{machine_matrix}

The processing times of instance 'ft06' are:
{processing_times}

The lowest known makespan of instance 'ft06' is:
{ft06_makespan}
The lowest known makespan is a {'optimal' if ft06_makespan_is_optimal else 'not necessarily optimal'} solution.
""")
    
```

This code snippet returns the following output:

![ft06_screenshot](https://github.com/Alexander-Nasuta/jsp-instance-utils/blob/main/docs/source/_static/ft06_screenshot.png)

Analogously, you can load the `ta01` instance from the package and extract the machine matrix and the processing time matrix:

```python
from jsp_instance_utils.instances import ta01, ta01_makespan, ta01_makespan_is_optimal

machine_matrix, processing_times = ta01

print(f"""
The machine matrix of instance 'ft06' is:
{machine_matrix}

The processing times of instance 'ft06' are:
{processing_times}

The lowest known makespan of instance 'ft06' is:
{ta01_makespan}
The lowest known makespan is a {'optimal' if ta01_makespan_is_optimal else 'not necessarily optimal'} solution.
""")
```

This code snippet yields the following output:

![ta01_screenshot](https://github.com/Alexander-Nasuta/jsp-instance-utils/blob/main/docs/source/_static/ta01-screenshot.png)

## Reinforcement Learning Environments

For the usage of the instances in reinforcement learning environments, we provide a wrapper class that can be used to create a reinforcement learning environment please check out the {ref}`Table of Instances` of this project. 
