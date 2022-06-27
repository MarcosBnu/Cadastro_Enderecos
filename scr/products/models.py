from django.db import models

class Pessoa(models.Model):
    cep= models.CharField(max_length=150)
    ende= models.CharField(max_length=500)
    numero= models.CharField(max_length=150)
    complemento= models.CharField(max_length=150)
    bairro= models.CharField(max_length=150)
    cidade= models.CharField(max_length=150)
    uf= models.CharField(max_length=2)
    descricao= models.CharField(max_length=150)
    
    def __str__(self):
        return self.cep
        
# Create your models here.
#cep, endereço, numero, complemento, bairro, cidade, uf e descrição. 