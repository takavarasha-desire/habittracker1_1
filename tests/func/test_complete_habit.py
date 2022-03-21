import datetime
from habit.habit_model import Habit, HabitHistory


class mock_datetime(object):
    """
    Monkey-patch datetime for predictable results
    """

    def __init__(self, year, month, day, hour, minute, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __enter__(self):
        class MockDate(datetime.datetime):
            @classmethod
            def today(cls):
                return cls(self.year, self.month, self.day)

            @classmethod
            def now(cls):
                return cls(
                    self.year,
                    self.month,
                    self.day,
                    self.hour,
                    self.minute,
                    self.second,
                )

        self.original_datetime = datetime.datetime
        datetime.datetime = MockDate

        return MockDate(
            self.year, self.month, self.day, self.hour, self.minute, self.second
        )

    def __exit__(self, *args, **kwargs):
        datetime.datetime = self.original_datetime


def test_complete(datasett):
    with mock_datetime(2022, 3, 23, 8, 0, 0):
        session = datasett
        habitid = 1
        q = session.query(Habit)
        h = q.get(habitid)
        h.complete()
        if h.overdue:
            h.check_if_broken_and_update()  # works only if overdue is True
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            session.add(hist)
            session.commit()
            session.close()
        h.complete()  # works only if can_complete is True
        if h.can_complete:
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            session.add(hist)
            session.commit()
            session.close()
    assert max(session.query(HabitHistory.streak).filter(HabitHistory.habitid == 1).all()) == (0,)
    assert len(session.query(HabitHistory).all()) == 1
    assert max(session.query(HabitHistory.broken_count).filter(HabitHistory.habitid == 1).all()) == (1,)