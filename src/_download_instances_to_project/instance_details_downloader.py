import requests
import bs4
import json
import logging
import pathlib as pl

from typing import Dict

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def download_benchmark_instances_details(target_dir: pl.Path) -> None:
    """
    scrapes additional information of benchmark instances from

        http://jobshop.jjvh.nl

    and save them in as in .json-format in the target_dir directory.

    :return: None
    """
    url = 'http://jobshop.jjvh.nl/'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    jsp_instance_details = {}
    for row in soup.findAll("tr", attrs={"class": "hideRow"}):
        instance_name = row.find('a', attrs={"class": "instance"}).getText()
        log.info(f"parsing instance '{instance_name}'")
        lower_bound = int(row.find('div', attrs={"class": "lb"}).getText())
        upper_bound = int(row.find('div', attrs={"class": "ub"}).getText())

        _, jobs, machines, *_ = row.find_all('td')

        jobs = int(jobs.getText())
        machines = int(machines.getText())

        # the number of solutions is the last div in a row
        no_solutions = None
        for no_solutions in row.find_all('div'): pass
        if no_solutions:
            no_solutions = int(no_solutions.getText())
        else:
            log.warning(f"could not parse the number of solutions for instance {instance_name}.")

        data = {
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "jobs": jobs,
            "machines": machines,
            "n_solutions": no_solutions,
            "lb_optimal": no_solutions > 0
        }
        jsp_instance_details[instance_name] = data
        log.info(f"adding {data} with key '{instance_name}' to details")

    jsp_instance_details_path = target_dir.joinpath("jps_instance_details")
    jsp_instance_details_path.mkdir(parents=True, exist_ok=True)

    jsp_instance_details_file_path = jsp_instance_details_path.joinpath("benchmark_details.json")
    log.info(f"saving details to .json file ('{jsp_instance_details_file_path}')")

    with open(jsp_instance_details_file_path, 'w') as fp:
        json.dump(jsp_instance_details, fp, indent=4)

    log.info(f"successfully saved details to .json file ('{jsp_instance_details_file_path}')")


def parse_instance_details(instance_details_file_path: pl.Path) -> Dict:
    """
    reads 'jps_instance_details/benchmark_details.json' file and returns it as a dictionary.

    make sure to download the instance details beforehand (run 'download_benchmark_instances_details' once)

    :return: the 'jps_instance_details/benchmark_details.json'-file as a python dictionary
    """
    with open(instance_details_file_path) as f:
        details_dict = json.load(f)
    return details_dict


def get_jps_instance_details(instance_details_file_path: pl.Path, instance: str) -> Dict:
    """
    looks up the details-entry that corresponds to the specified instance in the
    'jps_instance_details/benchmark_details.json'-file and returns them as a python dictionary.

    :param instance: the name of instance (example: 'ft06'). see: http://jobshop.jjvh.nl/index.php
    :return:
    """
    return parse_instance_details(instance_details_file_path=instance_details_file_path)[instance]


if __name__ == '__main__':
    import os
    resources_path = pl.Path(os.path.abspath(__file__)).parent.parent.parent \
        .joinpath("resources")

    download_benchmark_instances_details(target_dir=resources_path)

    details_path = resources_path.joinpath("jps_instance_details").joinpath("benchmark_details.json")
    details = parse_instance_details(
        instance_details_file_path=details_path
    )
    details_ft10 = get_jps_instance_details(
        instance_details_file_path=details_path,
        instance="ft10"
    )
    log.info(f"EXAMPLE: details for ft06: {details['ft06']}")
    log.info(f"EXAMPLE: details for ft06: {details_ft10}")