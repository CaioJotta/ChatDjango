from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    
    class Meta:
        app_label = 'core'
