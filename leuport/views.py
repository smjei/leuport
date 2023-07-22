from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy



# Create your views here.



class ContactView(FormView):
    template_name = 'leuport/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
    

class ContactSuccessView(TemplateView):
    template_name = 'leuport/success.html'

# Create your views here.



def index(request):
   return render(request, 'leuport/index.html')

def about(request):
   return render(request, 'leuport/about.html')

def contact(request):
   return render(request, 'leuport/contact.html')

def works(request):
   return render(request, 'leuport/works.html')

def services(request):
   return render(request, 'leuport/services.html')

def blog(request):
   return render(request, 'leuport/blog.html')

def blogs(request):
   return render(request, 'leuport/blogs.html')





