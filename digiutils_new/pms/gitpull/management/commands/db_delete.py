from django.core.management.base import BaseCommand, CommandError
from gitpull.models import SSHauth 
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects'

    def handle(self, *args, **options):
        SSHauth.objects.all().delete()
