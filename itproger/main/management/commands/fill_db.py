import time

from django.core.management.base import BaseCommand
from django.db import connection
from faker import Faker
from random import randint, choice, sample, random


class Command(BaseCommand):
  help = 'Заполняет базу данных тестовыми данными.'

  def add_arguments(self, parser):
    parser.add_argument('ratio', type=int, help='Коэффициент заполнения сущностей.')

  def handle(self, *args, **options):
    ratio = options['ratio']
    fake = Faker()

    with connection.cursor() as cursor:
      """for _ in range(ratio):
        cursor.execute(
          "INSERT INTO main_profile (avatar,user_id) VALUES (%s,%s)",
          (fake.text(max_nb_chars=20),1)#TODO: add normal key for users with registration
        )"""
      for i in range(ratio*10):
        author = fake.name()
        quest_data = fake.text(max_nb_chars=500)
        n_o_a=randint(0,50)
        cursor.execute(
          "INSERT INTO main_quests (author, quest_data, nums_of_answers,tags) VALUES (%s, %s, %s,%s)",
          (author, quest_data, randint(0, 50),[])
        )
        if n_o_a%5==0:
          cursor.execute(
            "INSERT INTO main_bestquests (place, quest_id) VALUES (%s,%s)",
            (randint(0, 50),i+1)
          )
        if n_o_a%10==0:
          cursor.execute(
            "INSERT INTO main_newquests (place, quest_id) VALUES (%s,%s)",
            (randint(0, 50),i+1)
          )
        for _ in range(10):
          cursor.execute(
            "INSERT INTO main_answer (username, data,quest_id) VALUES (%s,%s,%s)",
            (author,fake.text(max_nb_chars=50) ,i+1)
          )
        for _ in range(20):
          cursor.execute(
            "INSERT INTO main_tags1 (name,quest_id) VALUES (%s,%s)",
            ('nekvh', i + 1)
          )

    # Создаем Bestquests

    self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными.'))

