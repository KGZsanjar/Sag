from django.shortcuts import render
from models import Tag, Cloth
from django.views import generic


class Younger_ListView(generic.ListView):
    template_name = 'tags/older.html'
    context_object_name = 'older'
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='For Older')

    class Younger_ListView(generic.ListView):
        template_name = 'tags/yaunger.html'
        context_object_name = 'older'
        model = Cloth

        def get_queryset(self):
            return Cloth.objects.filter(tags__name='For Yaung')

        class kidsListView(generic.ListView):
            template_name = 'tags/kids.html'
            context_object_name = 'older'
            model = Cloth

            def get_queryset(self):
                return Cloth.objects.filter(tags__name='For Kids')
