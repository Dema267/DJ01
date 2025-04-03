from django.contrib import admin
from django.urls import path, include  # Добавляем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Подключаем URL-адреса приложения
]