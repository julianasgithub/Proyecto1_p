from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto
# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            mensaje=request.POST.get('mensaje')
            
            email=EmailMessage('Mensaje desde App Django', 
                               'El usuario: {} con dirección: {} escribe:\n\n {} '.format(nombre, email, mensaje), '', ['2julianascotto@gmail.com'], reply_to=[email] )
          
            email.send()


            return redirect('/contacto/?valido')

   
   
   
    return render (request,"contacto/contacto.html", {'miFormulario': formulario_contacto})
    