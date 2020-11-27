from django.urls import path

from . import views

app_name = 'fun'

urlpatterns = [
    path('', views.Submission.as_view(), name='submission'),
    path('results/', views.Results.as_view(), name='results'),
]
