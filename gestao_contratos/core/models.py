from django.db import models

from gestao_contratos.core.validators import name_validator, cpf_validator


class Athlete(models.Model):
    name = models.CharField(verbose_name='nome', max_length=40, validators=[name_validator])
    email = models.EmailField(verbose_name='e-mail')
    cpf = models.CharField(verbose_name='cpf', max_length=14, unique=True, validators=[cpf_validator])
    rg = models.CharField(verbose_name='rg', max_length=14)

    class Meta:
        verbose_name = 'atleta'
        verbose_name_plural = 'atletas'

    def __str__(self):
        return self.name


class Address(models.Model):
    cep = models.CharField(max_length=30)
    country = models.CharField(verbose_name='país', max_length=30)
    state = models.CharField(verbose_name='estado',  max_length=30)
    city = models.CharField(verbose_name='cidade', max_length=30)
    street = models.CharField(verbose_name='logradouro', max_length=30)
    number = models.CharField(verbose_name='número', max_length=10)
    complement = models.CharField(verbose_name='complemento', max_length=10, blank=True)
    athlete = models.ForeignKey('Athlete', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'endereço'
        verbose_name_plural = 'endereços'

    def __str__(self):
        return self.cep
