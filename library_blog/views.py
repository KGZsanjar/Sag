
from django.shortcuts import render, HttpResponse
import datetime
from django.views import generic
from templates.models import models


def about_me(request):
    return render(request, 'main_page/about_me.html')



def about_my_pet(request):
    return HttpResponse(f"Its my cat - Murrr")



def current_tima(request):
    return HttpResponse(datetime.datetime.now())


class BooklistView(generic.ListView):
    template_name = 'main_page/book.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'main_page/book_detail.html'
    context_object_name = 'book'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.all()


