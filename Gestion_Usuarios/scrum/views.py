from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = "scrum/tareas_lista.html"
    context_object_name = "tareas"


class TareaDetailView(DetailView):
    model = Tarea
    context_object_name = "tarea"

class TareaCreateView(CreateView):
    model = Tarea
    template_name = "scrum/tarea_detalle.html"
    fields = ["prioridad","titulo","descripcion","estado",
              "criterios_aceptacion","esfuerzo_estimado",
              "responsable","sprint_asignado","fecha_de_creacion",
              "fecha_de_actualizacion","fecha_de_finalizacion",
              "dependencias","bloqueadores"]
    def creacion_con_exito_url(self):
        return reverse_lazy("scrum:tarea-detalle",kwargs={"pk":self.object.id})
    

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tarea_confirm_delete.html"
    success_url = reverse_lazy("scrum:tareas-lista")