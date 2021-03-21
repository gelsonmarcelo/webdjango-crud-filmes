from django.db import models

#modelar a classe filme

class Filme(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    genero = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    
    classind = models.IntegerField(
        null=False,
        blank=False
    )
    
    sinapse = models.CharField(
        max_length=1000,
    )
    
    ano = models.IntegerField(
        null=False,
        blank=False
    )
    
    tempo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    
    qualidade = models.CharField(
        max_length=50
    )
    
    valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
    
objetos = models.Manager()
    
    