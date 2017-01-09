from django.db import models
from PIL import Image

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    mail = models.EmailField()
    projeto = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nome

class PessoaTag (models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tag = models.ForeignKey(Tag)
    rating = models.IntegerField()
    obs = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.pessoa.nome, self.tag.nome)
