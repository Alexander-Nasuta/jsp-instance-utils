from jsp_instance_utils.instances import ft06, ft06_makespan
from jsp_instance_utils.jsp_or_tools_solver import solve_jsp

makespan, status, *_ = solve_jsp(jsp_instance=ft06, plot_results=True)

assert status == "OPTIMAL"
assert makespan == ft06_makespan

print(f"makespan: {makespan} ({status} solution)")

if __name__ == '__main__':
    pass