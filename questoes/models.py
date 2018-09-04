from django.db import models

class Disciplina(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

class Ano(models.Model):
    descricao = models.CharField(max_length = 4, unique = True)

class Banca(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

class Nivel(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

class Orgao(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)


class Pergunta(models.Model):
    texto = models.TextField()
    respondida = models.BooleanField(default = False)
    correta = models.BooleanField(default = False)
    disciplina = models.ForeignKey('Disciplina', on_delete = models.CASCADE, related_name = 'pergunta')
    ano = models.ForeignKey('Ano', on_delete = models.CASCADE, related_name = 'pergunta')
    orgao = models.ForeignKey('Orgao', on_delete = models.CASCADE, related_name = 'pergunta')
    nivel = models.ForeignKey('Nivel', on_delete = models.CASCADE, related_name = 'pergunta')
    banca = models.ForeignKey('Banca', on_delete = models.CASCADE, related_name = 'pergunta')

class Alternativa(models.Model):
    correta = models.BooleanField(default = False)
    selecionada = models.BooleanField(default = False)
    pergunta = models.ForeignKey('Pergunta', on_delete = models.CASCADE, related_name = 'alternativa')