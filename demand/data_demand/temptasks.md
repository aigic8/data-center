# Tasks

## Todos

- [x] find the good articles with the keyword "high level data center power modeling gpu"
- [x] find the good articles with the keyword "gpu data center demand"
- [x] check out `GPUCloudSim` tool from article
- [x] organize articles in the directory
- [ ] install `Idea`
- [ ] do an active usage of GPUCouldSim
- [ ] check out query `GPU server power model data center`
- [ ] check the articles for utilization based modeling in review article 1 (table 7) in `r001`
- [ ] check reliability analysis for data center (like `r001`)
- [ ] check out keyword `heterogeneous gpu data-center power model`
- [ ] complete the list of papers in this document
- [ ] rename papers to articles

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

- `dc-gpu`
  - papers
    - `p001_heterogeneous_cloud_dc`: a paper on gpu models
      - references to `GPUCloudSim`
    - `p002_dl_dc_characteristics`: a paper on a gpu models in an actual data center (venus, earth, neptune, ...)
      - actual real-world data
    - `p003_deep_learning_wl_scheduling_ARCHIVE`: _maybe later_
      - only downloaded because bought the file
    - `p004_agnostic_gpu_energy_dc.pdf`: _TODO later_
  - reviews
    - `r001_dc_energy_reliability`: review different gpu models
      - references different papers for utilization based, additive, .... models
      - great classification for modeling technics
- `dc-cpu`
  - papers
  - reviews
    - `r001_dc_power_survey.pdf`: different models for data center power modeling
      - different formulas for different types of models
      - cpu power models (specially utilization based)
- `cpu-models`
  - papers
    - `p001_cpu_non_linear_model.pdf`: non-linear cpu power model
      - non-linearity
      - the problem with this paper is that it considers everything a vm, which may be not true on K8s
    - `p002_cpu_linear_model.pdf`: linear power model
      - linear
      - the power model is used in the current model
  - reviews
