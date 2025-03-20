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
