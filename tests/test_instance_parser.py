import pytest

from jsp_instance_utils.instance_parser import parse_jps_standard_specification, parse_jps_taillard_specification

ft06_standard_format_str = f"""6	6 
2	1	0	3	1	6	3	7	5	3	4	6
1	8	2	5	4	10	5	10	0	10	3	4
2	5	3	4	5	8	0	9	1	1	4	7
1	5	0	5	2	5	3	3	4	8	5	9
2	9	1	3	4	5	5	4	0	3	3	1
1	3	3	3	5	9	0	10	4	4	2	1"""

ft06_taillard_fromat_string = f"""6	6
1	3	6	7	3	6
8	5	10	10	10	4
5	4	8	9	1	7
5	5	5	3	8	9
9	3	5	4	3	1
3	3	9	10	4	1
3	1	2	4	6	5
2	3	5	6	1	4
3	4	6	1	2	5
2	1	3	4	5	6
3	2	5	6	1	4
2	4	6	1	5	3"""


def test_instance_parser_std():
    import tempfile
    import numpy as np
    import os

    f = tempfile.NamedTemporaryFile(mode='w', delete=False)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(ft06_standard_format_str)
        fpath = f.name

    instance_numpy, _ = parse_jps_standard_specification(fpath)

    ft06_expected = np.array([[[2, 0, 1, 3, 5, 4],
                               [1, 2, 4, 5, 0, 3],
                               [2, 3, 5, 0, 1, 4],
                               [1, 0, 2, 3, 4, 5],
                               [2, 1, 4, 5, 0, 3],
                               [1, 3, 5, 0, 4, 2]],

                              [[1, 3, 6, 7, 3, 6],
                               [8, 5, 10, 10, 10, 4],
                               [5, 4, 8, 9, 1, 7],
                               [5, 5, 5, 3, 8, 9],
                               [9, 3, 5, 4, 3, 1],
                               [3, 3, 9, 10, 4, 1]]
                              ])

    assert (ft06_expected == instance_numpy).all()

    # remove file
    os.remove(fpath)


def test_instance_parser_taillard_on_invalid_instance():
    with pytest.raises(AssertionError):
        import tempfile
        import os

        f = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(ft06_taillard_fromat_string)  # invalid format
            fpath = f.name

        instance_numpy, _ = parse_jps_standard_specification(fpath)

        # remove file
        os.remove(fpath)


def test_instance_parser_taillard():
    import tempfile
    import numpy as np
    import os

    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    try:
        f.write(ft06_taillard_fromat_string)
        fpath = f.name

        f.close()

    finally:
        os.remove(fpath)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(ft06_taillard_fromat_string)
        fpath = f.name

    instance_numpy, _ = parse_jps_taillard_specification(fpath)

    ft06_expected = np.array([[[2, 0, 1, 3, 5, 4],
                               [1, 2, 4, 5, 0, 3],
                               [2, 3, 5, 0, 1, 4],
                               [1, 0, 2, 3, 4, 5],
                               [2, 1, 4, 5, 0, 3],
                               [1, 3, 5, 0, 4, 2]],

                              [[1, 3, 6, 7, 3, 6],
                               [8, 5, 10, 10, 10, 4],
                               [5, 4, 8, 9, 1, 7],
                               [5, 5, 5, 3, 8, 9],
                               [9, 3, 5, 4, 3, 1],
                               [3, 3, 9, 10, 4, 1]]
                              ])

    assert (ft06_expected == instance_numpy).all()

    # remove file
    os.remove(fpath)


def test_instance_parser_talliard_on_invalid_instance():
    with pytest.raises(AssertionError):
        import tempfile
        import os

        f = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(ft06_standard_format_str)  # invalid format
            fpath = f.name

        instance_numpy, _ = parse_jps_taillard_specification(fpath)

        # remove file
        os.remove(fpath)