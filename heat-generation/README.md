# Heat Generation

## Sandbox

There are two models for heat generation:

- static
- dynamic

### Static Heat Generation Model

Considers a static heat generation regardless of servers utiliztaion

### Dynamic Heat Generation Model

Considers heat generation of the servers based on the utilization of them (cpu, gpu, and ...)

#### Sources

- [https://doi.org/10.1016/j.enbuild.2014.10.058](https://doi.org/10.1016/j.enbuild.2014.10.058)
  - data
    - important data for cpu, hdd and power supply heat generation
    - important data for u-value and server and rack
    - important data on the sizing of the data center
  - quotes
    - The efficiency and heat generation of the server power supply unit (PSU) change independently according to the CPU utilization [29]. However, with general server operation (i.e., 50%–90% utilization), the efficiency does not change a great deal, so variations in the PSU efficiency and heat generation were not considered in this study.
    - Independent server cooling fans are installed in a general server. Recent high-density servers have applied variable airflow control (which maintains a minimum server airflow to conserve server cooling fan energy [27]) and a CPU die temperature between 75 and 90 ◦C (wherein CPU reliability is guaranteed [35]) [32,36,37]. Thus, a general heat-sink attached air-cooled server model
    - PIT = 1.566 × 10^−5 + 42.29u_cpu + 0.379T_die + 0.03002T^2_die

#### Notes

- GPU and CPU heat generation is sufficient to be calculated and other parts can be neglected (source: https://doi.org/10.1016/j.enbuild.2014.10.058)
