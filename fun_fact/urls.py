from django.urls import path

from . import views

app_name = 'fun'

urlpatterns = [
    path('', views.submission, name='submission'),
    path('results/', views.results, name='results'),
]
