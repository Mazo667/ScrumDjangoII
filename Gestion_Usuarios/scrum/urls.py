from django.urls import path
from . import views

app_name = "scrum"

urlpatterns = [
   path("pagina_principal/",views.pagina_principal, name="pagina_principal")

    
]