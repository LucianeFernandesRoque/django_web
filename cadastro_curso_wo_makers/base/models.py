from django.db import models

# Create your models here.
# Uma abstração de classe python representa uma tabela no banco de dados
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.data}'

    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contato'
        ordering = ['-data']
