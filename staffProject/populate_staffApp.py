import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'staffProject.settings')
django.setup()

from staffApp.models import *
from faker import Faker

fake = Faker()


def populate(i=5):
    for entry in range(i):
        fake_name = fake.name()
        fake_nickname = fake.user_name()
        fake_url = fake.url()
        fake_date = fake.date()

        players = Human.objects.get_or_create(name=fake_name)[0]
        socials = Social.objects.get_or_create(human=players, social_name=fake_nickname, url=fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=socials, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating completed!")
