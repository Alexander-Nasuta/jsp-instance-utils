import numpy as np
from JSSEnv.envs import JssEnv

# in this example we create the instance file instead of downloading it, because https://jobshop.jjvh.nl/ is
# sometimes down. You can also download the instance from https://jobshop.jjvh.nl/ or use the download utils of
# the package.
#
# Note: this repo also contains .txt files with instances from https://jobshop.jjvh.nl/ in the resources folder. So that
#       is an alternative to downloading the instances from the website.


# setup the jsp instance
instance_text = """6	6 
2	1	0	3	1	6	3	7	5	3	4	6
1	8	2	5	4	10	5	10	0	10	3	4
2	5	3	4	5	8	0	9	1	1	4	7
1	5	0	5	2	5	3	3	4	8	5	9
2	9	1	3	4	5	5	4	0	3	3	1
1	3	3	3	5	9	0	10	4	4	2	1
"""
jsp_std_path = "ft06.txt"
# write the instance to a file
with open(jsp_std_path, "w") as f:
    f.write(instance_text)

# create the environment
env = JssEnv(env_config={'instance_path': jsp_std_path})

# reset the environment
obs = env.reset()

# perform a random action till the environment is done
done = False
while not done:
    # sample a random action
    mask = env.unwrapped.legal_actions.astype(np.int8)
    action = env.action_space.sample(mask=mask)
    # take a step in the environment
    obs, reward, done, info = env.step(action)

    # render the environment

env.render()
print(f"makespan: {env.unwrapped.last_time_step}")

if __name__ == '__main__':
    pass
