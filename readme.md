# Arup 2023 Hackathon
## Context
In Hong Kong, land piles are simple and do not offer much opportunity for innovation. Therefore, I propose that we focus on offshore piles, which are typically tubular piles driven using a hydraulic hammer. Calculating the pile capacity is generally straightforward, using an $\alpha$ and $\beta$ method.
For our purposes, let's assume that the geological conditions are typical for Hong Kong offshore sites, with two layers comprising Marine Deposit Overlaying Alluvium.
| Soils | Unit Weight | $s_u$                    | $\phi$ |
| ----- | ----------- | ------------------------ | ------ |
| MD    | 16          | $s_u=0.2\cdot \sigma_v'$ | 0      |

## Aim

Our main objectives for the Arup 2023 Hackathon are as follows:

- Develop an automated checking process using `CalcBuilder` or `DesignCheck` to improve efficiency and accuracy.
- Investigate the use of `AutoReporting` and determine if this can be incorporated into our current workflow to streamline reporting.
- Explore the use of `Speckle` as a central hub for sharing model information and improving collaboration among team members.
- Develop a unified approach for calculating pile capacity using (CPT) data, as well as for calculating soil springs `p-y`, `t-z`, and `Q-z` curves. This will help us to more accurately design offshore piles and ensure their long-term stability and reliability.


## To-dos

- [ ] Unified CPT Approach using Python
  - [ ] Ultimate Bearing Capacity of the piles 
  - [ ] Generating soil springs
- [ ] Generating handle calculation using either `CalBuilder` or `ArupCompute` with python API
- [ ] Report Generation 
- [ ] Write Geometry into `Speckle`, this can either be done using `Rhino` or `Grasshopper`
- [ ] GUI Development (Dazhong Li - Likely will start with `Plotly Dash`)
- [ ] Implement elementary calculation `DesignCheck` and publish 

## Reference


