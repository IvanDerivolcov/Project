from django.db import models
from django import forms
from django.urls import reverse


class Novosti(models.Model):
     Persona = models.CharField(max_length=60,
                            help_text="Введите атвора публикаций ",
                            verbose_name="Автор Публикаций")

     Data = models.DateField(max_length=30,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")

     def __str__(self):
         return self.Persona

class Opisanie(models.Model):
     title = models.CharField(max_length=10000,
                             help_text="Описание Новостей",
                             verbose_name="Описание")
     summary = models.TextField(max_length=75,
                             help_text="Введите заголовок Новостей", verbose_name="Заголовок Новостей ")

class Dobavlenie(models.Model):
     Sekretari = models.ForeignKey('opisanie', on_delete=models.CASCADE,
                             help_text = "Секретарь может добавить свой собственное описание",
                             verbose_name = "Добавление описание Секретаря", null = True)

     name = models.CharField(max_length=100,
                             help_text = "Введите имя Секретаря",
                             verbose_name = "Имя Секретаря")
     release_date = models.DateField(max_length=30,
                             help_text="Введите дату публицакий ",
                             verbose_name="Дата публикация")

     def __str__(self):
        return self.name

class Document(models.Model):
    Data = models.DateField(max_length=30,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50,
                            help_text="Введите атвора публикаций",
                            verbose_name="Автор Публикаций")




    def __str__(self):
        return '%s %s %s' % (self.data, self.persona, self.title)

