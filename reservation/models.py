from django.db import models
from django.utils import timezone
import datetime


class Department(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    picture = models.CharField(max_length=100, default='reservation/images/baby.jpg')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50, default='doctor')
    picture = models.CharField(max_length=100, default='reservation/images/baby.jpg')
    available_from = models.TimeField(default="7:00 ")
    available_to = models.TimeField(default="16:00 ")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=0)

    def a(self):

        schedules = self.schedule_set.all()
        time = self.available_from
        times = []
        for schedule in schedules:
            if schedule.date == datetime.date.today and schedule.reserved == 1:
                times.append(schedule.time)
        availables = ["6:00"]
        while time < self.available_to:
            availables.append("7:00")
            if time not in times:
                availables.append("t")
                availables.append(time)
            date = date(100,1,1,time.serialize ) + datetime.timedelta(minutes=30)
        availables.append("toz")
        return availables
    def __str__(self):
        return self.doctor_name


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reserved = models.IntegerField(default=0)
    date = models.DateField('reservation date')
    time = models.TimeField(default=timezone.now)


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_phone = models.IntegerField()
    appointment = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Review(models.Model):
    commenter = models.CharField(max_length=100)
    comment = models.TextField()
    review = models.IntegerField(default=3)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
