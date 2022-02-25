
from django.shortcuts import render
from .models import *
from .forms import *

from django.views import generic



def index(request):
    departments = Department.objects.all()
    context = {
        'departments' : departments
    }
    return render(request, 'reservation/index.html', context)
    
def detail(request, pk):
    department = Department.objects.get(pk=pk)
    context = {
        'department' : department
    }
    return render(request, 'reservation/department_detail.html', context)
    
    
def doctor_detail(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    form = CommentForm()
    form1 = ReserveForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        form1 = ReserveForm(request.POST)
        if form1.is_valid():
            appointment=Schedule(doctor=doctor,
                                 reserved=1,
                                 date=form1.cleaned_data["date"],
                                 )
            appointment.save()
            patient= Patient(
                        patient_name=form1.cleaned_data["patient_name"],
                        patient_phone=form1.cleaned_data["phone"],
                        appointment=appointment
                    )
            patient.save()
        if form.is_valid():
            
            comment=Review(doctor=doctor,commenter=form.cleaned_data['commenter'],
            comment=form.cleaned_data['comment'],
            )
            comment.save()
            

   
	           
     
    context = {  'doctor' : doctor,  'form': form,'form1':form1}
    return render(request, 'reservation/doctor_detail.html', context)
	
