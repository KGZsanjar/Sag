from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library_blog/', include('library_blog.urls')),
]
urlpatterns = [
    path('about_me/', views.about_me, name='https://btk.kg/media/Specialty/programmirovanie-v-kompjuternyh-sistemah.webp'),
    path('about_pets/', views.about_pets, name='https://www.purina.ru/sites/default/files/styles/ttt_image_510/public/2021-02/CAT%20BREED%20Hero%20Mobile_0042_Asian_OG.jpg?itok=tTaqbW-R'),
    path('system_time/', views.system_time, name='system_time'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
