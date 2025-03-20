from jsp_instance_utils.instances import ft06, ft06_makespan
from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv
import numpy as np


def main():
    env = DisjunctiveGraphJspEnv(
        jsp_instance=ft06,
        c_lb=ft06_makespan,
        reward_function="makespan"
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
    env.render()
    print(f"makespan: {env.get_makespan()}")


if __name__ == '__main__':
    main()
