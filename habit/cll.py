import sys
import click
import habit.analysis as analysis
from habit.habit_model import Habit, HabitHistory, Session

session = Session()


class HabitTrackerError(Exception):
    pass


class HabitNotCreated(HabitTrackerError):
    pass


class HabitNotDueForCompletion(HabitTrackerError):
    pass


# The main entry point for the habit tracker app
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1')
def startt():
    """Entry point for The Habit Tracker app"""
    pass


@startt.command(help='exit habit tracker')
def exit():
    """Exit the habit tracking app"""
    sys.exit()


@startt.command(help='create habit')
@click.argument('activity')
@click.argument('periodicity')
@click.option('--periodicity',
              type=click.Choice(
                  ['Daily',
                   'Weekly',
                   'Monthly',
                   'Annually']))
def create(activity, periodicity):
    """create a habit"""
    habit = Habit(activity, periodicity)
    session.add(habit)
    session.commit()
    session.close()


@startt.command(help='delete habit')
@click.argument('habitid', type=int)
def delete(habitid):
    """delete a habit from the database with the given id"""
    session.query(Habit).filter(Habit.habitid == habitid).delete()
    session.commit()
    return click.echo(f'Habit {habitid} deleted!')


@startt.command(help='complete habit')
@click.argument('habitid')
def complete(habitid):
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
            session.add(hist)
            session.commit()
            session.close()
        h.complete()     # works only if can_complete is True
        if h.can_complete:
            hist = HabitHistory(habitid, h.activity, h.periodicity,
                                h.creation_date, h.completed, h.completed_at,
                                h.streak, h.date_broken, h.broken_count,
                                h.next_run)
            session.add(hist)
            session.commit()
            session.close()
        else:
            raise HabitNotDueForCompletion
    except AttributeError:
        raise HabitNotCreated


@startt.group(help='analyse habits')
def analyse() -> None:
    """Habits analysis entry point"""
    return


@analyse.command(help="Get all habits")
def show():
    """List all the habits in the database"""
    rows = analysis.list_all_habits(session)
    for row in rows:
        click.echo(row)


@analyse.command(help="Get a habit")
@click.argument("habitid", required=True)
def get(habitid):
    """Get a habit from the database"""
    h = analysis.get_habit(session, habitid)
    click.echo(h)


@analyse.command(help="Get habits by periodicity")
@click.argument("periodicity", required=True)
def p(periodicity):
    """Select habits with the given periodicity"""
    rows = analysis.get_habits_by_periodicity(session, periodicity)
    for row in rows:
        click.echo(row)


@analyse.command('lh', help="Get largest streak for a habit")
@click.argument("habitid", required=True)
def ls(habitid):
    """Find the largest streak of the habit with the given id"""
    streak = analysis.longest_streak_of_a_habit(session, habitid)
    click.echo(streak)


@analyse.command(help="Get largest broken count")
def ms():
    """Returns the habit with the largest broken count"""
    largest_broken_count = \
        analysis.get_largest_broken_count_for_all_habits(session)
    click.echo(largest_broken_count)


@analyse.command(help="Get longest streak for all habits")
def ls():
    """Returns the habit that has the largest streak in the
    database."""
    longest_streak = analysis.get_longest_streak_of_all_habits(session)
    click.echo(longest_streak)


@analyse.command(help="get history for all habits")
def ghist():
    rows = analysis.get_history(session)
    for row in rows:
        click.echo(row)


@analyse.command(help="get history for a particular habit")
@click.argument("habitid", required=True)
def ghisth(habitid):
    rows = analysis.get_history_for_a_habit(session, habitid)
    for row in rows:
        click.echo(row)


startt.add_command(analyse)
