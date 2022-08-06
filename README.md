<h1>Como rodar este projeto</h1>
<div>
<p> Primeiramente isntale a biblioteca virtual env para serparar a isntalação do python da instalação do seu computador<p>
<code> pip3 install virtualenv </code>

<p>depois de instalar realize a criação de um ambiente virtual</p>
<code> virtualenv -p python3 venv </code>
<br>
<p> uma pasta com o ambiente será criada </p>
<img src='https://user-images.githubusercontent.com/57547119/181656890-d3938266-7d8b-4019-a7d6-d031c9f16dbe.png'>

<p> para habilitar o ambiente virual siga os seguintes passos</p>
no linux
<code>. venv/bin/activate</code>
<br>
no Windows
<code>.venv/scripts/activate</code>
<p></p>
<p>Após isto basta realizar a isntalação das bibliotecas com o comando</p>
<code>pip3 install -r caminho do arquivo requirements.txt</code>
<p></p>

<p> 
<h3>Adicionndo as tabelas do banco de dados</h3>
Para adicionar o banco de dados, primeiramente precisamos possuir o mesmo em nossa maquina com o nome <b>flask</b>, após isto devemos rodas os seguintes comandos no terminal, dentro da pasta onde se encontra o arquivo <b> run.py </b>
<code> flask db stamp head </code>
<code> flask db migrate</code>
<code> flask db upgrade</code>
Se tudo der certo, as tabelas serão criadas corretamente
</p>
<p></p>
<p> Após estes passos podemos rodar nosso código usando o seguinte comando</p>
<code> python run.py </code>
