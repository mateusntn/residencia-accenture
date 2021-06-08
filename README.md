<h1> Manual de utilização - Alokar </h1>

<div class="indice">
        <h3> Índice </h3>
        <ul>
            <li>Itens para instalar
                <ul>
                    <li>FrontEnd</li>
                    <li>BackEnd</li>
                    <li>Banco de dados</li>
                </ul>
            </li>
            <li>Visão Geral</li>
            <li>Tela de projetos </li>
            <li>Adicionar projeto</li>
            <li>Alocação</li>
            <li>Detalhes do projeto</li>
        </ul>
</div>

<div class="instalar-frontend">
    <h3> Itens para instalar - FrontEnd </h3>
        <p> Para nosso projeto, utilizamos o <a href="https://code.visualstudio.com/"> Visual Studio Code </a> e o <a href="https://dev.mysql.com/downloads/workbench/"> MySQL Workbench </a>. Todo o tutorial é baseado nesses programas.</p>

<ol>
        <li> Para executar as ações, é necessário primeiro instalar o Node no <a href="https://nodejs.org/pt-br/"> site oficial</a></li>
        <li> Clique no botão <img src="/img/versao-node.png" alt="Node versão 14.17.0 LTS" height="40px"> para fazer o download do Node</li>
        <li> Após o download e instalação, para conferir se a operação ocorreu com sucesso, no prompt de comando, execute o comando "node -v" (Sem as aspas), o resultado deverá ser a versão do node que foi instalada. Neste caso, "v14.17.0"</li>
        <li> Depois de abrir a pasta do projeto no VsCode, clique no menu "Terminal" e depois em "New terminal" <img src="/img/menus-vscode.png" alt="Menu terminal" height="30px"> <div><img src="/img/new-terminal.png" alt="New terminal" height="300px"></div></li>
        <li> No terminal que foi aberto, execute o comando "npm install -g npm" (sem as aspas) para instalar as dependências do node</li>
        <li> Instalar o Angular com o comando "npm install -g @angular/cli" (sem as aspas)</li>
        <li> Rodar o servidor com o comando "ng serve --open" (sem as aspas)</li>
</ol>
</div>

<div class="instalar-backend">
    <h3> Itens para instalar - BackEnd </h3>
        
<ol>
        <li> Instalar o python no <a href="https://www.python.org/downloads/">site oficial</a> clicando em donwload</li>
        <img src="/img/python.png" alt="instalação do python" height="250px">
        <li> Abrir outro terminal (repetindo o processo anterior, item 4) para criar o virtual environment (venv):
                py -m venv nomedapasta(geralmente venv). Ex: "py -m venv env".
        </li>
        <li> Ativar o ambiente virtual (env): "env\Scripts\activate" (sem as aspas)</li>
                Você saberá que o ambiente está ativado se estiver como na imagem <img src="/img/env.png" alt="print de env ativado" height="30px">        
        <li> Instalar o arquivo de requerimento "requirement.txt", que está no repositório, com o comando "pip install -r requirements.txt" (sem as aspas)</li>
        <li> Rodar o servidor com o comando "py app.py" (sem as aspas)</li>
</ol>
</div>

<div class="bancodedados">
    <h3> Itens para instalar - Banco de dados </h3>
    <ol>
        <li> Faça a importação do banco de dados. Para isso, na barra de tarefas, vá em "Server" e depois em "Data import" como na imagem.</li>
        <img src="/img/banco-de-dados1.png" alt="imagem do data import" height="250px">
        <li> Após isso, selecione a opção "Import from Self-Contained File" e escolha o diretório em que o arquivo ficará e clicar em "Import".</li>
        <img src="/img/banco-de-dados2.png" alt="imagem do data import" height="250px">
        <li> Na próxima tela, clicar em "Start import" </li>
        <img src="/img/banco-de-dados3.png" alt="imagem do data import" height="250px">
        <li> No app.py, linha 18, adicionar a configuração do seu banco como na imagem </li>
        <img src="/img/linha-banco.png" alt="linha 18">
    </ol>
</div>

<div class="visao-geral">
    <h3> Visão geral </h3>
    <img src="/img/dashboards.png" alt="Imagem da tela" height="300px">
        <p>Ao abrir a aplicação, a primeira tela será a de "Visão geral", onde encontram-se os dashboards.
        Atualmente o conteúdo está estático, pois é uma das funcionalidades que pretendemos adicionar no futuro. 
        </p>

<h4> Menu lateral </h4>            
    <img src="/img/menu.jpg" alt="Imagem do menu lateral" height="150px">
        <p> No canto superior esquerdo encontra-se o menu lateral, que pode ser acessado através de qualquer tela.
            Com esse recurso visual é possível acessar os principais serviços do software, bem como informar ao usuário sobre em qual ambiente ele está e para quais outros ele poderá se dirigir dentro da aplicação.
        </p>

</div>

<div class="tela-projetos">
        <h3> Tela de projetos </h3>
        <p>A tela "Projetos" lista todos os projetos cadastrados no sistema.
            Também é possível visualizar as principais informações de cada projeto, como duração, custo e área de atuação.
        </p>
        <div class="img-projetos"> 
            <img src="/img/tela-projetos1.png" alt="Imagem da tela" height="250px">
            <img src="/img/tela-projetos2.jpg" alt="Imagem da tela" height="250px">
        </div>        
</div>

<div class="tela-add-projeto">
        <h3> Adicionar projeto </h3>
            <p> Clicando no botão <img src="/img/btn-add-projeto.jpg" alt="botão adicionar projeto" height="35px">
                da tela inicial,você será direcionado para a tela "Adicionar projeto", onde terá um formulário
                sobre detalhes como nome e descrição do projeto, skills que serão necessárias para
                o desenvolvimento, custos previstos, e as funções que serão requeridas de acordo com o projeto.
                Clique em <img src="/img/btn-concluir.jpg" alt="botão concluir" height="35px"> para ir para tela de alocação.
            </p>
            <div class="adicionar-projeto">
                <img src="/img/adicionar-projeto.jpg" alt="foto da tela adicionar projeto" height="250px">
                <img src="/img/adicionar-projeto2.jpg" alt="foto da tela adicionar projeto" height="250px">
            </div>
</div>

<div class="tela-alocacao">
        <h3> Tela de alocação </h3>
            <p> Nesta tela são listados os funcionários disponíveis para serem alocados juntamente com as skills que possui.
            Neste processo de alocação, o usuário poderá otimizar a sua busca usando os filtros situados no canto esquerdo.
                <img src="/img/filtros.png" alt="imagem dos filtros" height="100px">
            Nele é possível priorizar os resultados, levando em conta as skills ou as funções.
            Para usá-lo basta marcar o checkbox da opção desejada.
            Para alocar o funcionário no projeto basta selecioná-lo clicando no checkbox, ao montar o time desejado,
            clique no botão <img src="/img/btn-alokar.png" alt="imagem do botão alokar" height="40px"> para finalizar a operação. </p>
                <img src="/img/tela-alocacao.png" alt="imagem da tela de alocação" height="300px">
</div>

<div class="tela-detalhes">
        <h3> Tela de detalhes do projeto </h3>
            <p> Em “detalhes do projeto” o usuário poderá acessar as informações mais específicas de um determinado projeto,
                por exemplo, a descrição completa do projeto, as skills que foram cadastradas e as pessoas já foram alocadas.
                Além disso, nesta tela encontra-se a opção de editar as informações ou alterar o conjunto de pessoas participantes.
            </p>
            <div class="detalhes-projeto-img">
                <img src="/img/detalhes-projeto1.png" alt="imagem da tela de detalhes do projeto" height="250px">
                <img src="/img/detalhes-projeto2.png" alt="imagem da tela de detalhes do projeto" height="250px">
            </div>               
</div>