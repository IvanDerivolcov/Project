from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return ("Главная страница чайта Районный Савет")

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
# Create your views here.

def index(request):
    num_document = Document.objects.all().count()
    num_novosti = Novosti.objects.all().filter(status__exact=2).count()

    return render(request,"index.html",context={
    'num_document':num_document,
    'num_novosti':num_novosti,
    }
                 )

class BookListView(generic.ListView):
    model = Document
    paginate_by = 5

class BookDetailView(generic.detailViews):
    model = Document 