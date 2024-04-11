import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UEPME.settings')
django.setup()

from django.contrib.auth.models import User
from UEPME import db
db.create_all()