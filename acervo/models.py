from django.db import models

class Livro(models.Model):

    TIPO_ACERVO_CHOICES = [
        ('digital', 'Digital'),
        ('fisico', 'Físico'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo_acervo = models.CharField(
        max_length=10,
        choices=TIPO_ACERVO_CHOICES,
        default='fisico'
    )

    def __str__(self):
        return self.titulo
