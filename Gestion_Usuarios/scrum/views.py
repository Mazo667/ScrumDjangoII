from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.utils.decorators import method_decorator #Otra alternativa es method_decorator para proteger nuestras vistas
from .models import Tarea, Sprint
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


@login_required
def tareas_por_usuario(request):
    tareas = Tarea.objects.filter(responsable=request.user.id)
    return render(request,'scrum/tareas_lista.html', {'tareas':tareas})

@permission_required('scrum.puede_completar_tarea')
def completar_tarea(request,tarea_id):
    tarea = get_object_or_404(Tarea,id=tarea_id)
    if request.method == 'POST':
        tarea.estado = 'COMPLETADA'
        tarea.save()
        messages.success(request, 'Tarea completada con exito')
        return redirect('scrum:tareas-lista')
    return render(request,'scrum/confirmar_completar_tarea.html', {'tarea':tarea})

#@method_decorator(login_required, name='dispatch') #se utiliza para aplicar el decorador login_required a vistas basadas en clases
class TareaListView(LoginRequiredMixin,ListView):
    model = Tarea
    template_name = "scrum/tareas_lista.html"
    context_object_name = "tareas"

class SprintListView(LoginRequiredMixin,ListView):
    model = Sprint
    template_name = "scrum/sprints_lista.html"
    context_object_name = "sprints"    

class SprintDetailView(LoginRequiredMixin,DetailView):
    model = Sprint
    context_object_name = "sprint"

class TareaDetailView(LoginRequiredMixin,DetailView):
    model = Tarea
    context_object_name = "tarea"


class TareaCreateView(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = "scrum/tarea_detalle.html"
    fields = ["prioridad","titulo","descripcion","estado",
              "criterios_aceptacion","esfuerzo_estimado",
              "responsable","sprint_asignado","fecha_de_creacion",
              "fecha_de_actualizacion","fecha_de_finalizacion",
              "dependencias","bloqueadores"]
    def creacion_con_exito_url(self):
        return reverse_lazy("scrum:tarea-detalle",kwargs={"pk":self.object.id})
    

class TareaDeleteView(LoginRequiredMixin,DeleteView):
    model = Tarea
    template_name = "tarea_confirm_delete.html"
    success_url = reverse_lazy("scrum:tareas-lista")