"""
  Django command to wait for the database to be available.
"""
import time

from pymysql import OperationalError as MysqlError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  """Django command to wait for database."""
  
  def handle(self, *args, **options):
    """Entrypoint for command."""
    self.stdout.write('waiting for database...')
    db_up = False
    while db_up is False:
      try:
        self.check(databases=['default'])
        db_up = True
      except (MysqlError, OperationalError):
        self.stdout.write(self.style.WARNING('Database unavailable, waiting 1 second...'))
        time.sleep(1)
    
    self.stdout.write(self.style.SUCCESS('Database available!'))