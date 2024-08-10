from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    numero_telefonico = models.CharField(max_length=15, blank=True, null=True)
    redes_sociales = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre