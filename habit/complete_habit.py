from habit.habit_model import Habit, HabitHistory, HabitNotCreated
import click


def complete(habitid, session):
    """
     When this method is called by the user through the command line interface
     it first checks if the habit is overdue. If it is, broken_habit_update
     method is called which calls the schedule() thus ensuring h.next_run is
     changed before h.can_complete is checked.
     This ensurer a user does not mark overdue habits as completed instead of
     broken.
     It should be noted that this method only works if the user tries to comp-
     lete the habit. that is to say broken fields will on be updated on the
     next attempt to complete a habit.
     """
    try:
        q = session.query(Habit)
        h = q.get(habitid)
        if h.overdue:
            h.broken_habit_update()  # works only if overdue is True
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            hist_id = session.add(hist)
            click.echo(f"too late to complete Habit {h.habitid}, habit broken"
                       f" fields have been updated instead.")
            session.commit()
            session.close()
            return hist_id

        elif h.can_complete:
            h.complete()  # works only if can_complete is True

            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            hist_id = session.add(hist)
            click.echo(f"Habit {h.habitid} successfully completed!")
            session.commit()
            session.close()
            return hist_id
        else:
            click.echo(f"Habit {h.habitid} is not due for completion yet")

    except AttributeError:
        raise HabitNotCreated
