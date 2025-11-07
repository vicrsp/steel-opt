from pydantic import BaseModel


class Machine(BaseModel):
    id: int
    setup_time: int = 0
    transportation_time: dict[int, int] = {}


class Stage(BaseModel):
    id: int
    machines: list[Machine]


class SteelGrade(BaseModel):
    id: int
    route: list[Stage]
    processing_duration: dict[int, int]

    @property
    def route_sequence(self) -> tuple[Stage, Stage]:
        if len(self.route) < 2:
            return ()
        stages = [stage for stage in self.route]
        return tuple((stages[i], stages[i + 1]) for i in range(len(stages) - 1))


class Charge(BaseModel):
    id: int
    release_time: int
    due_date: int
    steel_grade: SteelGrade


class Cast(BaseModel):
    id: int
    charges: list[Charge]

    @property
    def charges_sequence(self) -> list[tuple[int, int]]:
        if len(self.charges) < 2:
            return []
        # return the pairs of consecutive charges in the cast
        charge_ids = [charge.id for charge in self.charges]
        return [(charge_ids[i], charge_ids[i + 1]) for i in range(len(charge_ids) - 1)]


class SCCData(BaseModel):
    casts: dict[int, Cast] = {}
    stages: dict[int, Stage] = {}
    penalty_tardiness: int
    penalty_earliness: int
    penalty_idle_time: int
    penalty_cast_break: int
    max_wait_time: int

    @property
    def charge_indexes(self) -> list[int]:
        """Return a list of all charge IDs."""
        return [charge.id for cast in self.casts.values() for charge in cast.charges]

    @property
    def machine_indexes(self) -> list[int]:
        """Return a list of all machine IDs."""
        return [
            machine.id for stage in self.stages.values() for machine in stage.machines
        ]

    @property
    def machine_indexes_per_stage(self) -> dict[int, list[int]]:
        """Return a mapping of stage IDs to their machine IDs."""
        return {
            stage.id: [machine.id for machine in stage.machines]
            for stage in self.stages.values()
        }

    @property
    def transportation_times(self) -> dict[tuple[int, int], int]:
        """Return a mapping of (from_machine_id, to_machine_id) to transportation time."""
        times = {}
        for stage in self.stages.values():
            for machine in stage.machines:
                for to_machine_id, time in machine.transportation_time.items():
                    times[(machine.id, to_machine_id)] = time
        return times

    @property
    def index_first_stage(self) -> int:
        """Return the ID of the first stage."""
        if not self.stages:
            raise ValueError("No stages defined in SCCData.")
        return min(self.stages.keys())

    @property
    def index_last_stage(self) -> int:
        """Return the ID of the last stage."""
        if not self.stages:
            raise ValueError("No stages defined in SCCData.")
        return max(self.stages.keys())
