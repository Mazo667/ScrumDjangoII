from django.urls import path
from . import views

app_name = "scrum"

urlpatterns = [
   path("tareas/",views.TareaListView.as_view(), name="tareas-lista")

    
]