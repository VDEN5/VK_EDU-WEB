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
      # Заполнение таблицы Quests с помощью bulk-вставки
      quests_data = [
        (fake.name(), fake.text(max_nb_chars=500), randint(0, 50), [])
        for _ in range(ratio * 10)
      ]
      cursor.executemany(
        "INSERT INTO main_quests (author, quest_data, nums_of_answers, tags) VALUES (%s, %s, %s, %s)",
        quests_data
      )

      # Получение ID последнего вопроса (PostgreSQL)
      cursor.execute("SELECT currval('main_quests_id_seq')")
      last_quest_id = cursor.fetchone()[0]

      # Заполнение таблиц Bestquests и Newquests
      for i in range(ratio * 10):
        if (i+1) % 5 == 0:
          cursor.execute(
            "INSERT INTO main_bestquests (place, quest_id) VALUES (%s,%s)",
            (randint(0, 50), i + 1)
          )
        if (i+1) % 10 == 0:
          cursor.execute(
            "INSERT INTO main_newquests (place, quest_id) VALUES (%s,%s)",
            (randint(0, 50), i + 1)
          )

      # Заполнение таблицы Answer с помощью bulk-вставки
      answers_data = [
        (fake.name(), fake.text(max_nb_chars=50), i + 1)
        for i in range(ratio * 10)
        for _ in range(10)
      ]
      cursor.executemany(
        "INSERT INTO main_answer (username, data, quest_id) VALUES (%s, %s, %s)",
        answers_data
      )

      # Заполнение таблицы Tags1 с помощью bulk-вставки
      tags_data = [
        ('nekvh', i + 1)
        for i in range(ratio * 10)
        for _ in range(20)
      ]
      cursor.executemany(
        "INSERT INTO main_tags1 (name, quest_id) VALUES (%s, %s)",
        tags_data
      )
      for i in range(ratio*10):
        cursor.execute(
          "INSERT INTO main_tags1_questmany (quests_id, tags1_id) VALUES (%s,%s)",
          (i+1, 1+i%5)
        )

    # Вывод сообщения об успешном завершении
    self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными.'))
