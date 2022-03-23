from habit.complete_habit import complete


def test_overdue_habit(datasett):
    session = datasett
    complete(1, session)


def test_a_habit_due_for_completion():
    pass
