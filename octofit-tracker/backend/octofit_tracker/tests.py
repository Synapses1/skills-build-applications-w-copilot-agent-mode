from django.test import TestCase
from .models import Team, User, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)

    def test_team(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 50)
    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')
