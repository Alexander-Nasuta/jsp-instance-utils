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
