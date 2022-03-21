import pytest
from datetime import datetime, date
from habit.habit_model import Habit, HabitHistory, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='function')
def setup_database():

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope='function')
def dataset(setup_database):

    session = setup_database

    # create habits
    h1 = Habit('dancing', 'Daily')
    h2 = Habit('jogging', 'Weekly')
    h3 = Habit('cleaning the garage', 'Monthly')
    h4 = Habit('visiting the dentist', 'Annually')
    session.add(h1)
    session.add(h2)
    session.add(h3)
    session.add(h4)
    session.commit()

    # habits history
    data = [
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 1, 12, 49, 0, 0), 1, None, 0,
                     datetime(2022, 1, 2, 12, 45, 0, 0)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 2, 12, 50), 2, None, 0,
                     datetime(2022, 1, 3, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 3, 14, 45), 3, None, 0,
                     datetime(2022, 1, 4, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 4, 18, 45), 4, None, 0,
                     datetime(2022, 1, 5, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 5, 14, 45), 5, None, 0,
                     datetime(2022, 1, 6, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 6, 22, 52), 6, None, 0,
                     datetime(2022, 1, 7, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 7, 14, 45), 7, None, 0,
                     datetime(2022, 1, 8, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), False,
                     None, 0, date(2022, 1, 8), 1,
                     datetime(2022, 1, 9, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 9, 12, 45), 1, None, 1,
                     datetime(2022, 1, 10, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 10, 12, 45), 2, None, 1,
                     datetime(2022, 1, 11, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 11, 12, 45), 3, None, 1,
                     datetime(2022, 1, 12, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 12, 12, 45), 4, None, 1,
                     datetime(2022, 1, 13, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 13, 12, 45), 5, None, 1,
                     datetime(2022, 1, 14, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 14, 17, 45), 6, None, 1,
                     datetime(2022, 1, 15, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 15, 13, 45), 7, None, 1,
                     datetime(2022, 1, 16, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 16, 12, 45), 8, None, 1,
                     datetime(2022, 1, 17, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 17, 13, 45), 9, None, 1,
                     datetime(2022, 1, 18, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 18, 13, 45), 10, None, 1,
                     datetime(2022, 1, 19, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     True, datetime(2022, 1, 19, 20, 45), 11, None, 1,
                     datetime(2022, 1, 20, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 20, 19, 45), 12, None, 1,
                     datetime(2022, 1, 21, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 21, 18, 45), 13, None, 1,
                     datetime(2022, 1, 22, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 22, 14, 45), 14, None, 1,
                     datetime(2022, 1, 23, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 23, 13, 45), 15, None, 1,
                     datetime(2022, 1, 24, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 24, 13, 45), 16, None, 1,
                     datetime(2022, 1, 25, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 25, 14, 45), 17, None, 1,
                     datetime(2022, 1, 26, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31), True,
                     datetime(2022, 1, 26, 14, 45), 18, None, 1,
                     datetime(2022, 1, 27, 12, 45)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     True, datetime(2022, 1, 27, 16, 45), 19, None, 1,
                     datetime(2022, 1, 28, 12, 45, 0, 0)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     True, datetime(2022, 1, 28, 15, 45, 0, 0), 20, None, 1,
                     datetime(2022, 1, 29, 12, 45, 0, 0)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     False, None, 0, date(2022, 1, 29), 2,
                     datetime(2022, 1, 30, 12, 45, 0, 0)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     True, datetime(2022, 1, 30, 16, 45, 0, 0), 1, None, 2,
                     datetime(2022, 1, 31, 12, 45, 0, 0)),
        HabitHistory(1, "dance", "Daily", date(2021, 12, 31),
                     True, datetime(2022, 1, 31, 13, 45, 0, 0), 2, None, 2,
                     datetime(2022, 2, 1, 12, 45, 0, 0)),
        HabitHistory(2, "jogging", "Weekly", date(2022, 1, 1),
                     True, datetime(2022, 1, 1, 12, 45, 0, 0), 1, None, 0,
                     datetime(2022, 1, 8, 12, 45, 0, 0)),
        HabitHistory(2, "jogging", "Weekly", date(2022, 1, 1),
                     True, datetime(2022, 1, 8, 12, 50, 0, 0), 2, None, 0,
                     datetime(2022, 1, 15, 12, 45, 0, 0)),
        HabitHistory(2, "jogging", "Weekly", date(2022, 1, 1),
                     False, None, 0, datetime(2022, 1, 15), 1,
                     datetime(2022, 1, 22, 17, 45, 0, 0)),
        HabitHistory(2, "jogging", "Weekly", date(2022, 1, 1), True,
                     datetime(2022, 1, 2, 12, 45, 0, 0), 1, None, 1,
                     datetime(2022, 1, 3, 12, 45, 0, 0)),
        HabitHistory(3, "cleaning the garage", "Monthly",
                     date(2022, 1, 1), True,
                     datetime(2022, 1, 2, 15, 45, 0, 0), 1, None, 0,
                     datetime(2022, 2, 3, 12, 45, 0, 0)),
        HabitHistory(4, "visiting the dentist", "Annually",
                     date(2022, 1, 1), True,
                     datetime(2022, 1, 2, 16, 0, 0, 0), 1, None, 0,
                     datetime(2023, 1, 3, 16, 0, 0, 0))
    ]
    for d in data:
        session.add(d)
        session.commit()
    yield session


def test_database(dataset):
    # Get the session from the fixture
    session = dataset

    # Basic checking
    assert len(session.query(Habit).all()) == 4
    assert len(session.query(HabitHistory).all()) == 37
