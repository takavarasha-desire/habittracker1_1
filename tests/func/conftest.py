import pytest
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
    h1 = Habit('walking', 'Daily')
    session.add(h1)
    session.commit()
    yield session


def test_databasee(datasett):
    # Get the session from the fixture
    session = datasett

    # Basic checking
    assert len(session.query(Habit).all()) == 1
    assert len(session.query(HabitHistory).all()) == 0
