from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Tony Stark', team='marvel')
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Peter Parker', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Bruce Wayne', team='dc')
        superman = User.objects.create(email='superman@dc.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=ironman.email, type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=spiderman.email, type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=batman.email, type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user=superman.email, type='run', duration=50, date='2024-01-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=110)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 10 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
