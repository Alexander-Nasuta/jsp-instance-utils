

def test_ft06_instance():
    from jsp_instance_utils.instances import ft06
    from jsp_instance_utils.jsp_or_tools_solver import solve_jsp

    makespan, status, *_ = solve_jsp(jsp_instance=ft06)

    assert status == "OPTIMAL"
    assert makespan == 55