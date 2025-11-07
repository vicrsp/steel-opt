import pyomo.environ as pyo

from .data import SCCData


class SCCModel:
    def __init__(self, data: SCCData):
        self.model = self.build_instance(data)

    def build_instance(self, data: SCCData) -> pyo.ConcreteModel:
        """Create an instance of the SCC model."""
        model = pyo.ConcreteModel()
        self.add_decision_variables(model, data)
        self.add_constraints(model, data)
        self.add_objective_function(model, data)
        return model

    def create_sets(self, model: pyo.ConcreteModel, data: SCCData) -> None:
        """Create sets for the model."""
        model.CASTS = pyo.Set(initialize=data.casts.keys())
        model.CHARGES = pyo.Set(initialize=data.charge_indexes)
        model.MACHINES = pyo.Set(initialize=data.machine_indexes)
        model.STAGES = pyo.Set(initialize=[stage.id for stage in data.stages])
        model.STAGE_MACHINES = pyo.Set(
            initialize=[
                (stage.id, machine.id)
                for stage in data.stages.values()
                for machine in stage.machines
            ]
        )

    def create_parameters(self, model: pyo.ConcreteModel, data: SCCData) -> None:
        """Create parameters for the model."""
        model.PENALTY_TARDINESS = pyo.Param(initialize=data.penalty_tardiness)
        model.PENALTY_EARLINESS = pyo.Param(initialize=data.penalty_earliness)
        model.PENALTY_IDLE_TIME = pyo.Param(initialize=data.penalty_idle_time)
        model.PENALTY_CAST_BREAK = pyo.Param(initialize=data.penalty_cast_break)
        model.MAX_WAIT_TIME = pyo.Param(initialize=data.max_wait_time)

        model.TRANSPORTATION_TIME = pyo.Param(
            model.MACHINES * model.MACHINES,
            initialize=lambda m,
            from_machine,
            to_machine: data.transportation_times.get((from_machine, to_machine), 0),
        )

    def add_decision_variables(self, model: pyo.ConcreteModel, data: SCCData) -> None:
        """Add decision variables to the model."""
        model.x = pyo.Var(
            model.CHARGES * model.CHARGES * model.STAGES, domain=pyo.Binary
        )
        model.y = pyo.Var(
            model.MACHINES * model.CHARGES * model.STAGES, domain=pyo.Binary
        )
        model.c_time = pyo.Var(
            model.CHARGES * model.STAGES, domain=pyo.NonNegativeReals
        )
        model.w_time = pyo.Var(
            model.CHARGES * model.STAGES, domain=pyo.NonNegativeReals
        )
        model.u_time = pyo.Var(model.CHARGES, domain=pyo.NonNegativeReals)
        model.tardiness = pyo.Var(model.CHARGES, domain=pyo.NonNegativeReals)
        model.earliness = pyo.Var(model.CHARGES, domain=pyo.NonNegativeReals)

    def add_objective_function(self, model: pyo.ConcreteModel, data: SCCData) -> None:
        """Add objective function to the model."""
        model.obj = pyo.Objective(expr=lambda m: 3 * m.x + 4 * m.y, sense=pyo.minimize)

    def add_constraints(model: pyo.ConcreteModel, data: SCCData) -> None:
        """Add constraints to the model."""
        model.con1 = pyo.Constraint(expr=lambda m: 2 * m.x + m.y <= 20)
        model.con2 = pyo.Constraint(expr=lambda m: 4 * m.x + 5 * m.y <= 40)
