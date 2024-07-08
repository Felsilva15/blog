# blog/management/commands/init_db.py
from django.core.management.base import BaseCommand
import os
import shutil

class Command(BaseCommand):
    help = 'Initializes the database'

    def handle(self, *args, **kwargs):
        db_path = '/tmp/db.sqlite3'
        if not os.path.exists(db_path):
            # Copy the initial database from the project directory to /tmp
            shutil.copy('path/to/your/db.sqlite3', db_path)
            self.stdout.write(self.style.SUCCESS('Database initialized successfully'))
        else:
            self.stdout.write(self.style.WARNING('Database already exists'))
