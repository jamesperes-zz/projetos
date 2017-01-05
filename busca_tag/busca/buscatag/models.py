from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    mail = models.EmailField()
    projeto = models.CharField(max_length=50)


class Tag(models.Model):
    nometag = models.CharField(max_length=50)

class PessoaTag (models.Model):
    id_pessoa = models.ForeignKey(Pessoa)
    id_tag = models.ForeignKey(Tag)
    rating = models.IntegerField()
    obs = models.CharField(max_length=200)
