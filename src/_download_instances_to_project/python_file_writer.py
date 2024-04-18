import json
import os
import pathlib as pl
import pprint

import numpy as np

from jsp_instance_utils.instance_parser import parse_jps_taillard_specification


def parse_instance_details(instance_details_file_path: pl.Path) -> dict:
    """
    reads 'jps_instance_details/benchmark_details.json' file and returns it as a dictionary.

    make sure to download the instance details beforehand (run 'download_benchmark_instances_details' once)

    :return: the 'jps_instance_details/benchmark_details.json'-file as a python dictionary
    """
    with open(instance_details_file_path) as f:
        details_dict = json.load(f)
    return details_dict


if __name__ == '__main__':
    resources_path = pl.Path(os.path.abspath(__file__)).parent.parent.parent \
        .joinpath("resources")
    details_path = resources_path.joinpath("jps_instance_details").joinpath("benchmark_details.json")
    details = parse_instance_details(
        instance_details_file_path=details_path
    )

    jsp_instances_path = pl.Path(os.path.abspath(__file__)).parent.parent.parent \
        .joinpath("resources") \
        .joinpath("jsp_instances")

    jsp_taillard_path = jsp_instances_path.joinpath("taillard")

    header = f"""import numpy as np
    
    """

    file_strings = [header]

    for instance_name, instance_details in details.items():

        instance_ta_path = jsp_taillard_path.joinpath(f"{instance_name}.txt")
        instance_numpy, _ = parse_jps_taillard_specification(instance_ta_path)
        # Set print options
        np.set_printoptions(threshold=np.inf)

        instance_data_py = f"""
{instance_name} = np.array({np.array2string(instance_numpy, separator=', ')})

{instance_name}_makespan = {instance_details['upper_bound']}
{instance_name}_makespan_is_optimal = {instance_details['lb_optimal']}
        """

        file_strings.append(instance_data_py)

    file_string = "".join(file_strings)
    python_res_file = resources_path.joinpath("instances.py")
    print(file_string)

    with open(python_res_file, "w+") as f:
        f.writelines(file_string)
