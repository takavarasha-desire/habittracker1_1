from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer, create_engine
from sqlalchemy import String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URI


class HabitTrackerError(Exception):
    pass


class HabitNotCreated(HabitTrackerError):
    pass


Base = declarative_base()


class Habit(Base):
    """
    Model class to represent a habit.
    """
    __tablename__ = 'habits'
    habitid = Column(Integer, primary_key=True)
    activity = Column(String, unique=True)
    periodicity = Column(String)
    creation_date = Column(Date)
    completed = Column(Boolean)
    completed_at = Column(DateTime)
    streak = Column(Integer, default=0)
    date_broken = Column(Date)
    broken_count = Column(Integer, default=0)
    next_run = Column(DateTime)

    def __init__(self, activity, periodicity):
        self.activity = activity
        self.periodicity = periodicity
        self.creation_date = datetime.today()
        self.completed = False
        self.completed_at = None
        self.streak: int = 0
        self.date_broken = None
        self.broken_count: int = 0
        self.next_run: Optional[datetime] = None
        self.period: timedelta = timedelta(days=0)
        self._schedule_next_run()

    def __repr__(self):
        return "Habit(habitid='{self.habitid}',"\
               "activity='{self.activity}',"\
               "periodicity='{self.periodicity}',"\
               "creation_date='{self.creation_date}'" \
               "completed='{self.completed}'," \
               "completed_at='{self.completed_at})"\
               "streak='{self.streak}',"\
               "date_broken='{self.date_broken}'"\
               "broken_count='{self.broken_count}'"\
               "next_run='{self.next_run})".format(self=self)

    @property
    def can_complete(self) -> bool:
        assert self.next_run is not None, "must run _schedule_next_run before"
        return self.next_run <= datetime.now()

    @property
    def overdue(self) -> bool:
        assert self.next_run is not None
        return (self.next_run + timedelta(days=1)) <= datetime.now()

    def complete(self):
        self.streak += 1
        self.completed = True
        self.completed_at = datetime.now()
        self._schedule_next_run()

    def _broken(self):
        self.completed = False
        self.streak = 0
        self.broken_count += 1
        self.date_broken = datetime.today()

    def check_if_broken_and_update(self):  # checked on next completion
        self._broken()
        self._schedule_next_run()

    def _schedule_next_run(self) -> None:  # this method must be called upon creation
        if self.periodicity == "Daily":
            self.period = timedelta(days=1)
        if self.periodicity == "Weekly":
            self.period = timedelta(days=7)
        if self.periodicity == "Monthly":
            self.period = timedelta(days=30)
        if self.periodicity == "Annually":
            self.period = timedelta(days=365)
        self.next_run = datetime.now() + self.period


class HabitHistory(Base):
    """
    Model class to track all the states of the habit class.
    """
    __tablename__ = 'habits_history'
    historyid = Column(Integer, primary_key=True)
    habitid = Column(Integer)
    activity = Column(String)
    periodicity = Column(String)
    creation_date = Column(Date)
    completed = Column(Boolean)
    completed_at = Column(DateTime)
    streak = Column(Integer)
    date_broken = Column(Date)
    broken_count = Column(Integer)
    next_run = Column(DateTime)

    def __init__(self, habitid, activity, periodicity, creation_date,
                 completed, completed_at, streak,
                 date_broken, broken_count, next_run):
        self.habitid = habitid
        self.activity = activity
        self.periodicity = periodicity
        self.creation_date = creation_date
        self.completed = completed
        self.completed_at = completed_at
        self.streak = streak
        self.date_broken = date_broken
        self.broken_count = broken_count
        self.next_run = next_run

    def __repr__(self):
        return "Habit(historyid= {self.historyid}, " \
               "habitid= '{self.habitid}', "\
               "activity= '{self.activity}', "\
               "periodicity= '{self.periodicity}', "\
               "creation_date= '{self.creation_date}' " \
               "completed= '{self.completed}', " \
               "completed_at='{self.completed_at}) "\
               "streak= '{self.streak}', "\
               "date_broken= '{self.date_broken}' "\
               "broken_count= '{self.broken_count}' "\
               "next_run= '{self.next_run})".format(self=self)


engine = create_engine(DB_URI)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
