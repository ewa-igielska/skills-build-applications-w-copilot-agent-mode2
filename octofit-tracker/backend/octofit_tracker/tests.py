# Basic tests for all endpoints
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class SmokeTest(TestCase):
    def test_user_model(self):
        User.objects.create(email='test@example.com', name='Test', team='marvel')
        self.assertEqual(User.objects.count(), 1)
    def test_team_model(self):
        Team.objects.create(name='marvel', description='Marvel Team')
        self.assertEqual(Team.objects.count(), 1)
    def test_activity_model(self):
        Activity.objects.create(user='test@example.com', type='run', duration=30, date='2024-01-01')
        self.assertEqual(Activity.objects.count(), 1)
    def test_leaderboard_model(self):
        Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(Leaderboard.objects.count(), 1)
    def test_workout_model(self):
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        self.assertEqual(Workout.objects.count(), 1)
