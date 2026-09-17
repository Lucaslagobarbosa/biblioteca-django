from django.db import models

class Livro(models.Model):

    TIPO_ACERVO_CHOICES = [
        ('digital', 'Digital'),
        ('fisico', 'Físico'),
    ]

    CATEGORIA_CHOICES = [
        ('000', '000 - Generalidades e Informacao'),
        ('100', '100 - Filosofia e Psicologia'),
        ('200', '200 - Religiao e Teologia'),
        ('300', '300 - Ciencias Sociais e Direito'),
        ('400', '400 - Linguistica e Idiomas'),
        ('500', '500 - Ciencias Puras (Exatas e Naturais)'),
        ('600', '600 - Ciencias Aplicadas (Tecnologia)'),
        ('700', '700 - Artes e Recreacao'),
        ('800', '800 - Literatura'),
        ('900', '900 - Historia e Geografia'),
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
    categoria = models.CharField(
        max_length=3,
        choices=CATEGORIA_CHOICES,
        default='000'
    )

    def __str__(self):
        return self.titulo
