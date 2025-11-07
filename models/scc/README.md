# The steelmaking-contiunous-casting (SCC) scheduling problem 
## Problem description

For a steelmaking plant, a production schedule consists in the processing steps a charge undergoes from steelmaking to the casting stage, where the slabs are produced. In the steelmaking process, the molten steel received from the blast furnace is charged into a BOF (Basyc Oxygen Furnace) along with scrap. In this step, oxygen is blown in order to reduce the initial carbon content and increase the molten steel temperature, based on the steel grade being produced. After that, the molten steel is tapped into a steel landel and proceeds to the secondary refining stages, which can include a (1) stirring station, (2) ladle furnace and (3) vaccum degassing. (1) is usually applied to obtain a better homgeneization of the molten steel, (2) can be used to adjust the molten steel temperature up to a certain degree using electrical energy and add alloying materials to achieve the desired steel quality and (3) is applied when it is desired to achieve an ultra-low carbon content. The steel grade is used to define which routes a charge must undergo to achieve the casting stage within the specifications. Finally, the continuos casting process is reached, where the molten steel is loaded into a tundish and then solidified into a water-cooled mold into slabs. The tundish is important to allow a continuouts flow of steel into the mould.

The steelmaking-contiunous-casting (SCC) scheduling is usually represented as a hybrid flow-shop scheduling problem. A cast represent the final product and contains at least one charge. Each charge can be seen as a job to be produced into several machines. Each machine belongs to a stage and a job can be produced by at most one machine within each stage. Moreover, it is necessary to resepect the order of the processing stages and consider transportation and setup times between each one of them. The charges must reach the caster sequentially, such that a continuos flow of molten steel feed to them. 

Fiding an optimal schedule is considered a NP-hard problem and state-of-the-art exact solvers have difficulties in solving large instances of this problem in a reasonable amount of time. 

## Implementation

The MILP model described in this paper is implemented: 

Hong, J., Moon, K., Lee, K., Lee, K., & Pinedo, M. L. (2021). An iterated greedy matheuristic for scheduling in steelmaking-continuous casting process. International Journal of Production Research, 60(2), 623–643. https://doi.org/10.1080/00207543.2021.1975839

## Getting started
