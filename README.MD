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

### Models e ModelForm
 Uma abstração de classe python representa uma tabela no banco de dados
 Se quisermos alterar o banco de dados, temos que ir em projetos e setar em settings, por default vem o sqlLite.
 Sempre que houver alterações no banco de dados temos que fazer dois comandos migrações.
 `python3 manage.py makemigrations` gera o arquivo informando o que precisa ser enviado para o banco.
 `python3 manage.py migrate` envia de fato para o banco

- Salvando dados na view
- sempre que o form for validado, uma propriedade chamada forms.cleaned_data que verifica como se fosse um dicionario
se o campo em questão é valido se o form é is_valid cria um registro automaticamente no nosso banco

- DjangoForms tem uma classe especial de formulários que são baseadas em models que se chama o model Form
- Essa classe evita duplicidade de informações

### Django Admin
`python3 manage.py createsuperuser`

sistema de grupos
sistema de usuários.

Em admin.py quando queremos registrar o modelo em admim @admin.registrar(Cadastro)

### Trabalhando com o cache REDIS
- Redis é um armazenamento de estrutura de dados em memória, usado como um banco de dados em memória distribuído de chave-valor, cache e agente de mensagens, com durabilidade opcional.Armazena diretamente na memória ram, consequentemente o torna mais rapido.

### Rest transferência do estado representacional
Quando estamos trabalhando nós construímos model model view sett, que basicamente é um conjunto de operações que podemos estar adicionando em uma view.
model view set(get,post,put,path,delete,head) como acessando as models dos nossos aplicativos.

### Serializers
converter os nossos dados ou objetos em json
queryset => vai ser executado para conseguir rodar os objetos do nosso recurso, os objetos que estão cadastrados na nossa model de curso.
Serializer => converte os nossos dados em instancias de model, para um formato que nós conseguimos entender.