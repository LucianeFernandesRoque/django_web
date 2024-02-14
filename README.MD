### DJANGO PYTHON

- Framework é como se fosse uma caixa de ferramentas
- MVT
- Model - representa a camada de dados
- View - Logica e processamento
- Template - Definir como os dados vão são renderizados.

![MVT](/mvt.png)

### Diferença entre MVT e MVC
- MVT - É orientada a template
- MVC - É orientada a controller

### Framework Django
- Rápido, completo, escalonável, seguro, versátil e popular
  - Montar páginas(templates)
  - Interagir com diversos banco de dados (ORM);
  - Validar input dos usuários (Forms);
  - Controlar acesso (Authorization);
  - Gerenciar a aplicação (Admin)
1- Instalação do ambiente virtual
2- Criação do ambiente virtual
3- Ativação

### Instalando o Django
Instalar o Django `pip install django`
Criar o projeto `django-admin-startproject nome_do_projeto .`
rodar o projeto `python3 manage.py runserver`
rodar novo aplicativo `python3 manage.py startapp base` Todas as partes de funcionalidades, por exemplo cadastro de curso e etc. fica na pasta app/base

settings.py => Arquiva todas as configurações principais do nosso sistema, cadastrar nossos apps, configuração do nosso banco de dados e sobre urls. 
projeto => vai ficar as configurações gerais do nosso sistema/
app => Vai implementar as funcionalidades especificas.

sempre que criar um novo aplicativo temos que falar para projeto em settings.py e setar que ele foi instalado


- Como criar uma view em urls.py
```python
    def inicio(request):
    return HttpResponse('Olá, mundo!')
```
- Como setar a url
```python
from base.views import inicio
    urlpatterns = [
    path('', inicio)]
```

Instalar o Bootstrap
`pip install django-bootstrap-v5`

### Formulários em Django
É composto por 3 classes principais
- A classe do formulário que é uma classe que vai representar todo o formulário que vai ser processado 
e nela que vamos definir quais campos, que nós temos que validar.
- Field que é um campo específico do formulário, que tipo, quais validações ele terá,
exemplo de campos: nome, senha ou email.
- WIDGET