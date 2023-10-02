from django.shortcuts import render
from .models import RegistrationModel

# Create your views here.

def registration(request):
    if request.POST:
        model = RegistrationModel()
        model.first_name = request.POST.get('first_name', '')
        model.last_name = request.POST.get('last_name', '')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
    return render(request, 'index.html')
