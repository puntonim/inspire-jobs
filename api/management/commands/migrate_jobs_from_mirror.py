from django.core.management.base import BaseCommand, CommandError

from api.models.inspirehep import LegacyRecordsMirror


class Command(BaseCommand):
    help = 'Migrate jobs from mirror'

    def handle(self, *args, **options):
        count = LegacyRecordsMirror.objects.count()
        self.stdout.write('{} objects'.format(count))
        self.stdout.write(self.style.SUCCESS('Successfully migrated'))
