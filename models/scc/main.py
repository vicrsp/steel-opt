from .data import Cast, Charge, Machine, SCCData, Stage, SteelGrade
from .model import build_instance

STAGES = [
    Stage(
        id=1,
        machines=[
            Machine(id=1, transportation_time={3: 5, 4: 7}),
            Machine(id=2, transportation_time={3: 7, 4: 5}),
        ],
    ),
    Stage(
        id=2,
        machines=[
            Machine(id=3, transportation_time={5: 8, 6: 10}),
            Machine(id=4, transportation_time={5: 10, 6: 8}),
        ],
    ),
    Stage(id=3, machines=[Machine(id=5, setup_time=20), Machine(id=6, setup_time=20)]),
]

STEEL_GRADES = {
    SteelGrade(
        id=1,
        route=[STAGES[0], STAGES[1], STAGES[2]],
        processing_duration={
            STAGES[0].machines[0].id: 30,
            STAGES[0].machines[1].id: 28,
            STAGES[1].machines[0].id: 25,
            STAGES[1].machines[1].id: 27,
            STAGES[2].machines[0].id: 15,
            STAGES[2].machines[1].id: 18,
        },
    )
}

SMALL_TEST_DATA = SCCData(
    casts={
        1: Cast(
            id=1,
            charges=[
                Charge(id=1, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=2, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=3, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=4, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=5, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=6, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
            ],
        ),
        2: Cast(
            id=2,
            charges=[
                Charge(id=7, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=8, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=9, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=10, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=11, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
                Charge(id=12, release_time=0, due_date=5, steel_grade=STEEL_GRADES[0]),
            ],
        ),
    },
    stages={stage.id: stage for stage in STAGES},
    penalty_tardiness=1,
    penalty_earliness=1,
    penalty_idle_time=1,
    penalty_cast_break=100,
    max_wait_time=300,
)


data = SMALL_TEST_DATA
model = build_instance(data)
