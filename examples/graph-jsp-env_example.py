from jsp_instance_utils.instances import ft06, ft06_makespan
from graph_jsp_env.disjunctive_graph_jsp_env import DisjunctiveGraphJspEnv
import numpy as np


def main():
    env = DisjunctiveGraphJspEnv(
        jps_instance=ft06,
        reward_function_parameters={
            "scaling_divisor": ft06_makespan
        },
    )

    done = False
    info = {}
    while not done:
        # get valid action mask. sample expects it to be a numpy array of type int8
        mask = np.array(env.valid_action_mask()).astype(np.int8)
        action = env.action_space.sample(mask=mask)
        state, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

    # console rendering
    env.render(show=["gantt_console", "graph_console"])
    print(f"makespan: {info['makespan']}")


if __name__ == '__main__':
    main()
