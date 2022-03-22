from habit.habit_model import Habit, HabitHistory, HabitNotCreated
from habit.habit_model import HabitNotDueForCompletion


def complete(habitid, session):
    """
        Mark a habit with the given habitid as completed and record the
        completion in the database. This method checks if the next_run date
        is less than or equal to datetime.now before committing the completion
        data to the Habit history table.

        Because the schedule method is called with the complete method and the
        :check_if_broken_method:. If a user fails to complete a habit with in a
        period of one day after the scheduled date. calling this method would
        increment broken count by one and reschedule the next_run date, Thus when
        the h.complete is called in the try block `habit not due for completion
        exception` is raised.
        """
    q = session.query(Habit)
    h = q.get(habitid)
    try:
        if h.overdue:
            h.check_if_broken_and_update()  # works only if overdue is True
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            hist_id = session.add(hist)
            session.commit()
            session.close()
        h.complete()  # works only if can_complete is True
        if h.can_complete:
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            hist_id = session.add(hist)
            session.commit()
            session.close()
        else:
            raise HabitNotDueForCompletion
    except AttributeError:
        raise HabitNotCreated
    return hist_id