from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.views import generic
from templates.models import models
from .forms import CommentForm


def about_me(request):
    return render(request, 'main_page/about_me.html')


def current_tima(request):
    return HttpResponse(datetime.datetime.now())


class Younger_isteView(generic.ListView):
    template_name = 'tags__name= for Olds'



    context_object_name = 'books'
    model = models.Book


def context_data(self, **kwargs):
    context = super().get_context_data(kwargs)
    context['form'] = CommentForm()
    return context


def post(self, request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.book = self.abject
        comment.save()
        return redirect('book-detail', pk=self.object.pk)
    return self.get(request, *argo, **kwargs)

class AllListView(generic.ListView):
    template_name = 'tag/all html'
    context_object_name = 'alls'
    model = Cloth

    def get_queryset(self):
        return  Cloth.objects.all()
