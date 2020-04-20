from django.db import models

# Create your models here.
class Pembayaranform(models.Model):
    namalengkap=models.CharField(max_length=20, null=True)
    nis=models.CharField(max_length=10, null=True)
    jenjangsekolah=models.Choices('SD','SMP'),('SMA','SMK')
    kelas=models.CharField(max_length=10, null=True)
    jenispembayaran=models.Choices('Uang Pangkal','SPP')