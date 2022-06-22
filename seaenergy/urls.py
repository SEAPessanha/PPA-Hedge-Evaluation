from django.contrib import admin
from django.urls import path
from . import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vw.ppa_page, name='home'),
]
