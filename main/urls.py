from django.urls import path
from .views import home,seminar,training,job

urlpatterns = [
    path("",home,name="home"),
    path("seminar/",seminar,name="seminar"),
    path("training/",training,name="training"),
    path("job/",job,name="job")
]