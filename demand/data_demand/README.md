# Data Demand

## Ideas

- [ ] Also doing data center reliability analysis for each scenario

## Todos

- [x] find the good articles with the keyword "high level data center power modeling gpu"
- [x] find the good articles with the keyword "gpu data center demand"
- [x] check out `GPUCloudSim` tool from article
- [x] organize articles in the directory
- [ ] make a basic load with [GPUCloudSim](https://github.com/weisselbiad/gpucloudsim)
- [ ] check out [CloudSimPlus](https://github.com/cloudsimplus/cloudsimplus)
- [ ] check out query `GPU server power model data center`
- [ ] check the articles for utilization based modeling in review article 1 (table 7) in `r001`
- [ ] check reliability analysis for data center (like `r001`)
- [ ] check out keyword `heterogeneous gpu data-center power model`
- [ ] complete the list of papers in this document
- [ ] rename papers to articles

### Archive

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
  - [ ] the average gpu utilization and gpu model for each task in each time-frame
  - [ ] find the power usage characteristics of each gpu model used in the data
  - [ ] find the the gpu power usage model
- [ ] find some characteristics of user task submissions
- [ ] model cpu demand

## Find the keywords in the researches

- Current keywords
  - energy consumption
    - energy consumption and management
    - Servers power consumption models (additive, base-active, regression, and server utilization based model)
  - reliability
    - reliability assessment
    - Data center reliability analysis
    - QoS and SLA of data center
    - Tier classification of data center
    - Service availability and service reliability
    - Reliability modeling approach

## Papers

- `data`
  - articles
    - `a001_mit-gpu-data`: a paper explaining the dataset of MIT gpus
    - **IMPORTAT**: three datasets are in this paper that need to be explored
    -
- `dc-gpu`
  - articles
    - `p001_heterogeneous_cloud_dc`: a paper on gpu models
      - references to `GPUCloudSim`
    - `p002_dl_dc_characteristics`: a paper on a gpu models in an actual data center (venus, earth, neptune, ...)
      - actual real-world data
    - `p003_deep_learning_wl_scheduling_ARCHIVE`: _maybe later_
      - only downloaded because bought the file
    - `p004_agnostic_gpu_energy_dc`: _TODO later_
    - `p005_gpu_cloud_sim`: the structure of GPUCloudSim
  - reviews
    - `r001_dc_energy_reliability`: review different gpu models
      - references different articles for utilization based, additive, .... models
      - great classification for modeling technics
- `dc-cpu`
  - articles
  - reviews
    - `r001_dc_power_survey`: different models for data center power modeling
      - different formulas for different types of models
      - cpu power models (specially utilization based)
- `cpu-models`
  - articles
    - `p001_cpu_non_linear_model`: non-linear cpu power model
      - non-linearity
      - the problem with this paper is that it considers everything a vm, which may be not true on K8s
    - `p002_cpu_linear_model`: linear power model
      - linear
      - the power model is used in the current model
  - reviews
