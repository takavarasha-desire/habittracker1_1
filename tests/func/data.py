def test_complete(datasett):
    session = datasett
    habitid = 1
    q = session.query(Habit)
    h = q.get(habitid)
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
        assert max(session.query(HabitHistory.broken_count).filter(HabitHistory.habitid == 1).all()) == (1,)
        assert max(session.query(HabitHistory.streak).filter(HabitHistory.habitid == 1).all()) == (0,)
        assert len(session.query(HabitHistory).all()) == 1
