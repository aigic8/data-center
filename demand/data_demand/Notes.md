# Server Power Models

## Server Power Model High level analysis

On the higher level, there are three main power models for servers. 

- `additive based:` In this model we calculate average power consumption of each part and calculate the whole power consumption as the summation of these parts.

- `utilization based:` In this model, we use the utilization of each item in the server and add it to the main power consumption model.

- `task based:` In this method, we estimate the power consumption based on the task we have. In this method we assume a fixed power consumption and add the additional power consumption based on the tasks in the hand.

- `vm based:` The power consumption of the system is divided to the system itself and the vms that run on the system. For each component the additional is added.
