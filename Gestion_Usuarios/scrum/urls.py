from django.urls import path
from . import views

app_name = "scrum"

urlpatterns = [
   path("tareas/",views.tareas_por_usuario, name="tareas-lista"),
   path("tarea/<int:pk>/",views.TareaDetailView.as_view(),name="tarea-detalle"),
   path("sprints/",views.SprintListView.as_view(),name="sprints-lista"),
   path("sprint/<int:pk>/",views.SprintDetailView.as_view(),name="sprint-detalle"),
    
]