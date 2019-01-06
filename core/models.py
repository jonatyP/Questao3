from django.db import models
from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"

class Tema(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valorAluguel = models.DecimalField('Valor do aluguel', max_digits=8, decimal_places=2, default=0)
    corToalha = models.CharField('Cor da toalha', max_length=100)

    class Meta:
        verbose_name_plural = 'Temas'
        verbose_name = 'Tema'

class ItemTema(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name_plural = 'Itens de Temas'
        verbose_name = 'Tema'

class Aluguel(models.Model):
    dataFesta = models.DateField('Data da festa')
    horaInicio = models.TimeField('Hora de inicio')
    horaTermino = models.TimeField('Hora termino')
    valorCobrado = models.DecimalField('Valor cobrado',  max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Alugueis'
        verbose_name = 'aluguel'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.dataFesta
        )
class Endereco(models.Model):
    logradouro = models.CharField('Endereço', max_length=150)
    numero = models.CharField('N', max_length=50)
    complemento = models.CharField('Complemento', max_length=150)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=30)
    uf = models.CharField('UF', max_length=2)
    cep = models.CharField('CEP', max_length=20)

    class Meta:
        verbose_name_plural = 'Endereços'
        verbose_name = 'Endereço'

class Cliente(models.Model):
    nome = models.DateField()
    telefone = models.TimeField()

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'