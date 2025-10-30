from django.urls import path
from .import views
urlpatterns = [
    path('api/', view=views.greet),
    path('wishes/', view=views.greeting),
    path('api1/', view=views.greets),
    path('api2/', view=views.grts),
]
