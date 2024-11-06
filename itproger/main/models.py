from symtable import Class

from django.db import models,connection
from django.db.models import QuerySet
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your models here.
# ВАЖНО!!!: я не могу пользоваться расширением objects, поэтому пользуюсь query
class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Quests(models.Model):
  author = models.CharField(max_length=50)
  quest_data = models.TextField()
  nums_of_answers = models.IntegerField(default=0)
  tags = models.JSONField(default=list) # Используем JSONField для хранения массива
  #answers = models.ForeignKey(Answer, on_delete=models.CASCADE)

  @classmethod
  def get_all_quests_id(cls, id1):
      with connection.cursor() as cursor:
          cursor.execute("SELECT * FROM main_quests WHERE id = %s", [id1])
          row = cursor.fetchone()
          qu = Quests(
              id=row[0],
              author=row[1],
              quest_data=row[2],
              nums_of_answers=row[3],
              tags=cls.get_all_tags(row[0])
          )
          return qu

  @classmethod
  def get_all_tags(cls, id1):
    with connection.cursor() as cursor:
      cursor.execute("SELECT name FROM main_tags1 WHERE id=%s", [id1])
      rows = cursor.fetchall()
      return [row[0] for row in rows]

  @classmethod
  def get_all_quests(cls):
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM main_quests")
      rows = cursor.fetchall()
      quests = []
      for row in rows:
        quest = Quests(
          id=row[0],
          author=row[1],
          quest_data=row[2],
          nums_of_answers=row[3],
          tags=cls.get_all_tags(row[0]) # Заполняем поле tags
        )
        quests.append(quest)
      return quests

  @classmethod
  def get_answers_by_quest_id(cls, quest_id):
      with connection.cursor() as cursor:
          cursor.execute(
              "SELECT * FROM main_answer WHERE quest_id = %s", [quest_id]
          )
          rows = cursor.fetchall()
          answers = []
          for row in rows:
              answer = Answer(
                  id=row[0],
                  username=row[1],
                  data=row[2],
              )
              answers.append(answer)
          return answers


class Tag(models.Model):
    name = models.CharField(max_length=50)
    quest=models.IntegerField()
    #questmany = models.ManyToManyField(Quests, related_name='quest')
    @classmethod
    def get_all_tags_id(cls, id1):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_tags1 WHERE id = %s", [id1])
            row = cursor.fetchone()
            qu = Tag(
                id=row[0],
                name=row[1]
            )
            return qu


class Tags1(models.Model):
    name = models.CharField(max_length=50)
    quest=models.ForeignKey(Quests, on_delete=models.CASCADE)
    #jjh=models.CharField(default='fbjsb')
    questmany = models.ManyToManyField(Quests,related_name='quest')
    @classmethod
    def get_all_tags_id(cls, id1):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_tags1 WHERE quest_id = %s", [id1])
            rows = cursor.fetchall()
            bests = []
            for row in rows:
                best = Tags1(
                id=row[0],
                name=row[1],
                quest=Quests.get_all_quests_id(row[2])
            )
                bests.append(best)
            return bests

    @classmethod
    def get_all_tags_by_quest_id(cls, id1):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_tags1_questmany WHERE quests_id = %s", [id1])
            rows = cursor.fetchall()
            bests = []
            for row in rows:
                bests.append(row[1])
            return bests

    @classmethod
    def get_all_quest_by_tag_id(cls, id1):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_tags1_questmany WHERE tag_id = %s", [id1])
            rows = cursor.fetchall()
            bests = []
            for row in rows:
                bests.append(row[2])
            return bests


class Answer(models.Model):
    username = models.CharField(max_length=50)
    data = models.TextField(default="def")
    quest = models.ForeignKey(Quests, on_delete=models.CASCADE, related_name='answers')  # Связь с Quests

    @classmethod
    def get_all_ans_id(cls, id1):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_answer WHERE id = %s", [id1])
            row = cursor.fetchone()
            qu = Answer(
                id=row[0],
                username=row[1],
                data=row[2],
                quest=Quests.get_all_quests_id(row[3])
            )
            return qu


class Bestquests(models.Model):
    place=models.IntegerField(default=0)
    quest=models.ForeignKey(Quests,on_delete=models.CASCADE)

    @classmethod
    def get_all_quests(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_bestquests")
            rows = cursor.fetchall()
            bests = []
            for row in rows:
                best = Bestquests(
                    id=row[0],
                    place=row[1],
                    quest=Quests.get_all_quests_id(row[2])#row[2]
                )
                bests.append(best)
            return bests


class Newquests(models.Model):
    place=models.IntegerField(default=0)
    quest=models.ForeignKey(Quests,on_delete=models.CASCADE)

    @classmethod
    def get_all_quests(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_newquests")
            rows = cursor.fetchall()
            news = []
            for row in rows:
                new = Newquests(
                    id=row[0],
                    place=row[1],
                    quest=Quests.get_all_quests_id(row[2])#row[2]
                )
                news.append(new)
            return news


class QuestionLike(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('user', 'question') # Ограничение на уровне базы данных


class AnswerLike(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('user', 'answer') # Ограничение на уровне базы данных


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(null=True,blank=True)