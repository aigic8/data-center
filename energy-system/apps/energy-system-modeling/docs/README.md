# Energy Systems

- [Energy Systems](#energy-systems)
  - [PV System](#pv-system)
    - [Choosing Panels](#choosing-panels)
    - [Choosing Inverters](#choosing-inverters)
      - [Result](#result)
    - [Designing System](#designing-system)
  - [Wind Turbine Model](#wind-turbine-model)
    - [Modeling](#modeling)
    - [Change of Height (Power law)](#change-of-height-power-law)
  - [To DOs](#to-dos)

## PV System

### Choosing Panels

- The common PV brands for commercial applications are:
  - `SunPower`
  - `LG Solar`
  - `REC Group`
  - `Canadian Solar`
  - `Trina Solar`
  - `Longi Solar`
  - `Jinko Solar`
- Common PV Size for these applications is `450W` panels

### Choosing Inverters

- The common inverter models are:
  - `SMA Solar Technology`
  - `Fronius`
  - `SunGrow`

#### Result

- We go only for `Sunny Power` brand (`SMA`)
  - We use `CORE 1` and `CORE 2` configurations and pricing for different configurations
    - The pricing of CORE 2: 6471.60 euro ([source](https://www.mg-solar-shop.com/sma-sunny-tripower-core2-solar-inverter-sma-stp-110-60))

### Designing System

- The Max Power of Inverter should match panels
- The Voltage of panels should match the inverter's

## Wind Turbine Model

### Modeling

I've only seen one modeling method of wind turbine. Though there is also a more sophisticated library
in python, since the model is easy to program and accurate enough, I'd use it. It can be found in various
articles like these ones:

- <https://www.sciencedirect.com/science/article/abs/pii/S0360544217301548>
- <https://www.sciencedirect.com/science/article/abs/pii/S0196890418309415> (contains good data)
- <https://www.mdpi.com/1996-1073/15/10/3579> (contains good data) (good source for structuring the function)

### Change of Height (Power law)

Power law is used to change the height of wind speed, the source of the formula is from the following article:

- <https://www.mdpi.com/1996-1073/15/10/3579>

## To DOs

- [ ] Check if other inverter brands has hybrid inverters for their batteries (Sunny Power does not!)
- [ ] Automate weather data retrieval for a location
- [ ] Design the PVSystem (Choose Panels and Inverters) based on the panels in Sandia Database
- [ ] Use multiple configuration inverters in the following steps
  - `20kW`
  - `40kW`
  - `80kW`
  - `100kW`
  - `200kW`
  - `300kW`
- Check if inverters has enough inputs
- [ ] add degradation rates for pv and wind turbines
- [ ] choose turbine models and document the process
