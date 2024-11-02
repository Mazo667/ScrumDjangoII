from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs): #Instanciamos UserCreationForm
        super().__init__(*args, **kwargs)  #Llamamos al constructor
        self.fields['username'].widget.attrs.update({'class': 'username','placeholder':"Ingrese un nombre de usuario"})
        self.fields['password1'].widget.attrs.update({'class': 'password','placeholder':"Ingrese una contraseña"})
        self.fields['password2'].widget.attrs.update({'class': 'password','placeholder':"Repita la contraseña"})