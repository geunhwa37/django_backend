from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()


class Patient(models.Model):
    # M:N 관계 (Dotor와 Patient의 관계) Reservation 모델을 통해 관리
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserver_at = models.DateTimeField(auto_now_add=True)