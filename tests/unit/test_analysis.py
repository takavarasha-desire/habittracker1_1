from habit.habit_model import Habit
from habit.analysis import (
    get_habit,
    get_history,
    list_all_habits,
    get_habits_by_periodicity,
    get_history_for_a_habit,
    longest_streak_of_a_habit,
    get_longest_streak_of_all_habits,
    get_largest_broken_count_for_all_habits
)


def test_get_history(dataset):
    session = dataset
    result = get_history(session)
    assert len(result) == 37


def test_get_history_for_a_habit(dataset):
    session = dataset
    result = get_history_for_a_habit(session, 1)
    assert len(result) == 31


def test_longest_streak_for_a_habit(dataset):
    session = dataset
    result = longest_streak_of_a_habit(session, 2)
    assert result == (2,)


def test_get_habit(dataset):
    session = dataset
    result = get_habit(session, 3)
    assert isinstance(result, Habit)


def test_list_all_habits(dataset):
    session = dataset
    result = list_all_habits(session)
    assert len(result) == 4


def test_get_habits_by_periodicity(dataset):
    session = dataset
    result = get_habits_by_periodicity(session, "Daily")
    assert len(result) == 1


def test_get_longest_streak_of_all_habits(dataset):
    session = dataset
    result = get_longest_streak_of_all_habits(session)
    assert result == (20,)


def test_get_largest_broken_count_for_all_habit(dataset):
    session = dataset
    result = get_largest_broken_count_for_all_habits(session)
    assert result == (2,)
