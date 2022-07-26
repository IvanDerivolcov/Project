from django.db import models
from django import forms
from django.urls import reverse

class Novosti(models.Model):
    name=models.CharField(max_length=200,help_text="Введите тему новостей", verbose_name="Тема новостей")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык на котором вы хотите посмотреть новости", verbose_name="Язык новостей")

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введите тип документа",
                             verbose_name="Тип документа")
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text="Выберите язык для просмотра документа",
                                 verbose_name="Язык докумета", null=True)
    summary = models.TextField(max_length=1000,
                               help_text="Введите краткое описание документа",
                               verbose_name="Аннотация документа")

    def __str__(self):
        return '%s %s %s' % (self.inv_doc, self.nov, self.lang)
