import pytest
from datetime import datetime, timedelta
from habit.habit_model import Habit, HabitHistory, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='function')
def setup_databasee():

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope='function')
def datasett(setup_databasee):

    session = setup_databasee

    # create habits
    overdue_habit = Habit('walking', 'Daily')
    overdue_habit.next_run = datetime.now() - timedelta(days=1)
    due_habit = Habit('work_out', 'Daily')
    due_habit.next_run = datetime.now()

    session.add(overdue_habit)
    session.add(due_habit)
    session.commit()
    yield session


def test_databasee(datasett):
    # Get the session from the fixture
    session = datasett

    # Basic checking
    assert len(session.query(Habit).all()) == 2
    assert len(session.query(HabitHistory).all()) == 0
