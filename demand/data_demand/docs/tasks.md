# Tasks

## Next Time

- [ ] calc the CPU power
- [ ] find the GPU power usage of different GPU models
- [ ] create baseline for GPU power when in IDLE mode
- [ ] create the baseline for CPU power usage
- [ ] create time probability of for hours of day

## Overall

- [ ] read some articles on data driven design of data center demand model
- [ ] create the base GPU demand of instances
  - By combining the data of sensors and start and end time of each instance we can easily create the GPU demand of each instance
  also we should take into consideration the GPU model, which can be effective of the power usage
- [ ] create the base GPU demand of tasks
  - by combining (& grouping) tasks we can easily find the gpu usage of each task and using the end and start time of each
    we can have a good idea
- [ ] create the base GPU demand of jobs
  - same as tasks but only for jobs
- [ ] model power usage (specifics are subject to change)
  - [ ]  the average gpu utilization and gpu model for each task in each time-frame
  - [ ] find the power usage characteristics of each gpu model used in the data
  - [ ] find the the gpu power usage model
- [ ] find some characteristics of user task submissions
- [ ] model cpu demand
