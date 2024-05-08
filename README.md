# Book-Guardian:
O BookGuardian é um projeto que visa auxiliar os amantes da leitura a gerenciar suas bibliotecas pessoais de maneira eficiente e organizada.

# Sobre o Projeto:
O BookGuardian foi desenvolvido com o objetivo de proporcionar uma experiência completa para os usuários que desejam manter um registro de seus livros favoritos, acompanhar sua leitura atual e descobrir novos títulos para adicionar à sua coleção.

# Funcionalidades Principais:
- **Gerenciamento de Biblioteca**: Mantenha um registro detalhado de todos os livros que você possui, incluindo título, autor, gênero e status de leitura.

- **Acompanhamento de Leitura**: Marque os livros que você está atualmente lendo, já leu ou pretende ler em breve.

- **Pesquisa e Descoberta**: Explore novos títulos com base em suas preferências de gênero e descubra recomendações personalizadas.

  **Organizando por Gênero:** Utilize filtros no painel de administração ou crie vistas personalizadas para organizar seus livros por gênero, facilitando a localização de títulos específicos.
**Pesquisando Livros:** Utilize a funcionalidade de pesquisa do painel de administração ou implemente buscas personalizadas nas vistas para encontrar rapidamente os livros desejados.


  # Instalação e Uso:

**Configurações para acessar o BookGuardian no vs code:**

Pré-requisitos: Certifique-se de ter o Django instalado e configurado em seu ambiente de desenvolvimento.

Criação do Projeto: Inicie criando um novo projeto Django usando o comando django-admin startproject bookguardian.

Aplicativo de Biblioteca: Crie um aplicativo para gerenciar os livros da biblioteca, utilizando o comando *python manage.py startapp library*.

Modelos: Defina os modelos para representar os livros da biblioteca no arquivo models.py do aplicativo library. Inclua campos como título, autor, ISBN, gênero, data de leitura e status (lido, lendo, para ler).

Migrações: Gere as migrações para sincronizar o banco de dados com os novos modelos usando o comando python manage.py makemigrations e, em seguida, aplique-as com python manage.py migrate.
Admin Interface: Registre os modelos no painel de administração para fácil gerenciamento dos livros, acessível em http://localhost:8000/admin/.


  **Instruções de uso**:

 1.Faça login na sua conta do BookGuardian.

 2.Explore a interface para se familiarizar com as diferentes seções e funcionalidades disponíveis, como "Minha Biblioteca", "Leitura Atual" e "Descobrir Novos Livros".

**Adicionando Livros à Sua Biblioteca**
1.Vá para a seção "Minha Biblioteca".

2.Procure pelo botão ou link de "Adicionar Livro" e clique nele.

3.Insira o título do livro que você deseja adicionar e selecione a opção correta da lista de resultados.

4.Você pode adicionar informações adicionais, como autor, data de publicação e gênero, se desejar.

5.Repita esse processo para cada livro que você deseja adicionar à sua biblioteca pessoal.

 **Requisitos de sistema**:Processador de 1,8 GHz ou mais rápido,2 GB de RAM; 8 GB de RAM, são recomendados (mínimo de 2,5 GB, se executado em uma máquina virtual).Espaço em disco rígido: mínimo de 800 MB e até 210 GB de espaço disponível.

 # Como acessar o site e fazer o login:

**Usando o editor de codigo**

  Pré-requisitos: Certifique-se de ter o Django instalado e configurado em seu ambiente de desenvolvimento.

  Criação do Projeto: Inicie criando um novo projeto Django usando o comando django-admin startproject bookguardian.

  Abra o editor: Inicie o Visual Studio Code ou seu editor de codigo fonte de sua preferencia em seu computador.

  Usando seu editor de codigo abra-oAbra um *terminal integrado*, vá para o menu superior e selecione "Terminal" > "Novo Terminal" para abrir um terminal integrado.

  Use o terminal integrado para navegar até o diretório do projeto e é por onde vamos acessar o site do BookGuardian.

  Use o comando cd seguido do caminho para o diretório. Assim use o comando *source venv/Scripts/activate*, para ativar o seu anbiente virtual.

  Apos ativar o anbiente virtual use o comando *python manage.py runserver*, assim ira gerar o link do site.

  # Como Acessar pelo link:

1.Acesse o site oficial do BookGuardian que sera disponibilizado aqui.

2.Procure pelo botão ou link de "Cadastro ou Registro" e clique nele.

3.Preencha o formulário de registro com suas informações pessoais, como nome, endereço de e-mail e senha.

4.Confirme seu e-mail, se necessário, seguindo as instruções enviadas para a sua caixa de entrada.

5.Agora que consegui entra se divirta e tenha uma otima experiemcia.

