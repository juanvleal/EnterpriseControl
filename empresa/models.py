from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    carga_horaria_semanal = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    horas_necessarias = models.IntegerField()
    prazo_estimado = models.DateField()
    horas_realizadas = models.IntegerField(default=0)
    ultimo_calculo_horas = models.DateField()
    supervisor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class ProjetoFuncionario(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    horas_trabalhadas = models.IntegerField()
    horas_supervisao = models.IntegerField()