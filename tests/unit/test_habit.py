import unittest
import datetime
from datetime import timedelta
from habit.habit_model import Habit


class TestHabitAcceptance(unittest.TestCase):
    def test_create_daily_habit(self):
        daily_habit = Habit("running", "Daily")
        assert daily_habit.periodicity == "Daily"

    def test_create_weekly_habit(self):
        weekly_habit = Habit("jogging", "Weekly")
        assert weekly_habit.periodicity == "Weekly"

    def test_create_monthly_habit(self):
        monthly_habit = Habit("cleaning the garage", "Monthly")
        assert monthly_habit.periodicity == "Monthly"

    def test_create_annual_habit(self):
        annual_habit = Habit("visiting the dentist", "Annually")
        assert annual_habit.periodicity == "Annually"

    def test_complete_a_habit_within_given_period(self):
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now()
        habit.complete()
        assert habit.completed is True

    def test_completion_date_and_time(self):  # need to freeze
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now()
        habit.complete()
        assert habit.completed_at is not None

    def test_streak_counter(self):  # my own. # fails # have to mock schedule
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now()
        habit.complete()
        assert habit.streak == 1

    def test_habit_overdue(self):  # my own.
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now() - timedelta(days=1)
        assert habit.overdue is True

    def test_habit_can_complete(self):
        habit = Habit("visiting the dentist", "Annually")
        habit.next_run = datetime.datetime.now()
        assert habit.can_complete is True

    def test_date_broken(self):
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now() - timedelta(days=1)
        habit.check_if_broken_and_update()
        assert habit.date_broken is not None

    def test_broken_counter(self):  # my own
        habit = Habit("dancing", "Daily")
        habit.next_run = datetime.datetime.now() - timedelta(days=1)
        habit.check_if_broken_and_update()
        assert habit.broken_count == 1

    def test_creation_date(self):
        habit = Habit("dancing", "Daily")
        assert habit.creation_date == datetime.datetime.today()

    def test__schedule_next_run_for_daily_habit(self):
        habit = Habit("dancing", "Daily")
        assert habit.next_run == datetime.datetime.now() + timedelta(days=1)

    def test__schedule_next_run_for_weekly_habit(self):
        habit = Habit("jogging", "Weekly")
        assert habit.next_run == datetime.datetime.now() + timedelta(days=7)

    def test__schedule_next_run_for_monthly_habit(self):
        habit = Habit("cleaning the garage", "Monthly")
        assert habit.next_run == datetime.datetime.now() + timedelta(days=30)

    def test__schedule_next_run_for_annual_habit(self):
        habit = Habit("visiting the dentist", "Annually")
        assert habit.next_run == datetime.datetime.now() + timedelta(days=365)

    def test_habit_reschedule_after_completion(self):
        habit = Habit("jogging", "Weekly")
        habit.next_run = datetime.datetime.now()
        habit.complete()
        assert habit.next_run == datetime.datetime.now() + timedelta(days=7)

    def test_habit_reschedule_after_broken(self):
        habit = Habit("cleaning the garage", "Monthly")
        habit.next_run = datetime.datetime.now() - timedelta(days=1)
        habit.check_if_broken_and_update()
        assert habit.next_run == datetime.datetime.now() + timedelta(days=30)
