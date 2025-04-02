from django.urls import path
from.import views
from django.contrib import admin


urlpatterns = [
    # Основные страницы
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Добавил слеш в конце
    path('postypauchim/', views.postypauchim, name='postypauchim'),
    path('roditeli/', views.roditeli, name='roditeli'),

    # Аутентификация
    path('registr/', views.registr, name='registr'),  # Регистрация
    path('vxod/', views.vxod, name='vxod'),  # Вход
    path('akkaynt/', views.akkaynt, name='akkaynt'),
    # path('logout/', views.logout_view, name='logout'),  # Добавил выход

    # Другие страницы
    path('ychiteluam/', views.ychiteluam, name='ychiteluam'),
    path('contakt/', views.contakt, name='contakt'),
    path('pravila/', views.pravila, name='pravila'),
    
    # Админка
    path('admin/', admin.site.urls),

    # Добавьте это в конце для обработки 404
    path('<path:not_found>/', views.handler404, name='404')
  
]

handler404 = 'main.views.handler404'





