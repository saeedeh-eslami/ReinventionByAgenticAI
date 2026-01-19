from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')

        # Activities
        Activity.objects.create(user=users[0], workout=pushups, date=timezone.now(), duration_minutes=30, notes='Good effort!')
        Activity.objects.create(user=users[1], workout=running, date=timezone.now(), duration_minutes=45, notes='Great run!')
        Activity.objects.create(user=users[2], workout=pushups, date=timezone.now(), duration_minutes=20, notes='Strong!')
        Activity.objects.create(user=users[3], workout=running, date=timezone.now(), duration_minutes=60, notes='Fast!')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=130)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
