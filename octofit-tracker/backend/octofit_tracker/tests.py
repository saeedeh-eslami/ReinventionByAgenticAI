from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, date=timezone.now(), duration_minutes=30)
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_workout(self):
        self.assertEqual(self.activity.workout.name, 'Pushups')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.total_points, 100)
