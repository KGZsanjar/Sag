from django .urls import path, include
from . import views


urlpatterns = [
    path('older/', views.OlderLisView.as_view name='older'),
    path('younger/', views.YounterLisView.as_view, name='younter'),
    path('kids/', views.KidsLisView.as_view, name='kids'),
    path('all/', views.AllLisView.as_view, name='all'),
]