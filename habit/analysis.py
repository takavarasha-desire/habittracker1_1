from habit.habit_model import Habit, HabitHistory


class HabitAnalysisError(Exception):
    pass


class NoHabitsInHistoryTableYet(HabitAnalysisError):
    pass


def get_habit(session, habitid):
    """
    :param habitid: given from the cll module when the get_habit is called.
    :param session: from the cll module
    :return: habit from database
    """
    h = session.query(Habit).get(habitid)
    return h


def list_all_habits(session):
    """
    :return: returns all the rows in the habits table
    """
    rows = session.query(Habit).all()
    return rows


def get_history(session):
    """
    :return: return all the rows in the habits_history table.
    """
    rows = session.query(HabitHistory).all()
    return rows


def get_history_for_a_habit(session, habitid):
    """
    :returns: habits_history rows with the specified habitid
    """
    rows = session.query(HabitHistory).\
        filter(HabitHistory.habitid == habitid).all()
    return rows


def get_habits_by_periodicity(session, periodicity):
    """
    :param periodicity: specified from the commandline module cll
    :param session:
    :return: all the rows with the specified periodicity for the habits table.
    """
    rows = session.query(Habit).filter(Habit.periodicity == periodicity).all()
    return rows


def longest_streak_of_a_habit(session, habitid):
    """
    :param habitid: take the habit id parameter from the Habits table.
    :param session: takes the session parameter from the module cll
    :return: the largest streak value of the habit with the given habitid
    """
    try:
        longest_streak_for_habit = (max(session.query(HabitHistory.streak).
                                    filter(HabitHistory.habitid == habitid)
                                    .all()))
    except ValueError:
        raise NoHabitsInHistoryTableYet

    return longest_streak_for_habit


def get_largest_broken_count_for_all_habits(session):
    """
    :return: the largest value in the broken count column.
    """
    try:
        largest_broken_count = (max(session.query(HabitHistory.broken_count)
                                .all()))
    except ValueError:
        raise NoHabitsInHistoryTableYet
    return largest_broken_count


def get_longest_streak_of_all_habits(session):
    """
    :return: the value of the largest value in the streak column.
    """
    try:
        longest_streak_for_all_habits = (max(session.query(HabitHistory.streak)
                                         .all()))
    except ValueError:
        raise NoHabitsInHistoryTableYet
    return longest_streak_for_all_habits
