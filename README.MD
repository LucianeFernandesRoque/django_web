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