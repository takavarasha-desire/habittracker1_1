from habit.habit_model import HabitHistory
from habit.complete_habit import complete


def test_overdue_habit(datasett):
    session = datasett
    complete(1, session)
    result = session.query(HabitHistory.broken_count).filter(HabitHistory.habitid == 1).all()
    assert result == [(1,)]


def test_a_habit_due_for_completion():
    pass
