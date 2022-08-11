from django.db import models
from django import forms
from django.urls import reverse


class Novosti(models.Model):
     Persona = models.CharField(max_length=30,
                            help_text="Введите атвора публикаций ",
                            verbose_name="Автор Публикаций")

     Data = models.CharField(max_length=20,
                        help_text="Введите дату публицакий ",
                        verbose_name="Дата публикация")

     def __str__(self):
         return self.name

class Opisanie(models.Model):
     title = models.CharField(max_length=200,
                             help_text="Описание Новостей",
                             verbose_name="Описание")
     summary = models.TextField(max_length=1000,
                               help_text="Введите заголовок Новостей", verbose_name="Заголовок Новостей ")


    def __str__(self):
        return self.name

class Document(models.Model):
    Data = models.CharField(max_length=20,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")
    Persona = models.CharField(max_length=30,
                               help_text="Введите атвора публикаций ",
                               verbose_name="Автор Публикаций")


    def __str__(self):
        return '%s %s %s' % (self.data, self.persona, self.title)

