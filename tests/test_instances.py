def test_ft06():
    from jsp_instance_utils.instances import ft06
    import numpy as np

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

    assert (ft06_expected == ft06).all()