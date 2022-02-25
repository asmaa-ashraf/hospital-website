from django import forms
from django.utils import timezone
import datetime
from .models import *


class ReserveForm(forms.Form):
    patient_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    CH = ['7:00', '7:30', '8:00']

    def available_times(pk, date=datetime.date.today):
        doctor = Doctor.objects.get(pk=pk)
        schedules = doctor.schedule_set.all()
        time = doctor.available_from
        times = []
        for schedule in schedules:
            if schedule.date == date and schedule.reserved == 1:
                times.append(schedule.time)
        availables = ()
        while time < doctor.available_to:
            if time not in times:
                availables.append((time, time))
            time = time + datetime.timedelta(minutes=30)
        return availables

    date = forms.DateField(widget=forms.SelectDateWidget())
    time = forms.TimeField(widget=forms.Select(choices=available_times(pk=1)))


class CommentForm(forms.Form):
    commenter = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": ''
        })
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

