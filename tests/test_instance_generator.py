

def test_instance_generator():
    from jsp_instance_utils.jsp_instance_generator import generate_jsp_instance

    jsp_instance = generate_jsp_instance(n_jobs=10, n_machines=15, min_processing_time=1, max_processing_time=14)

    assert jsp_instance.shape == (2, 10, 15)

    machine_order = jsp_instance[0]
    processing_times = jsp_instance[1]

    for row in machine_order:
        assert len(row) == len(set(row))
        assert max(row) == 14

    for row in processing_times:
        assert max(row) <= 14
        assert min(row) >= 1


