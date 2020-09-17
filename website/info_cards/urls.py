from django.urls import path

from . import views

app_name = 'info_cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:basicinfocard_id>/', views.detail, name='detail')
]