<h2>🔥 Teste prático – Projeto em Django</h2>
<p>Faça um sistema onde terá um cadastro de endereços, utilizando a linguagem de programação Python, e o framework Django.</p>

<h2>🖥️ Tecnologias Utilizadas</h2>


+ <h4>📌 Front-end:</h4>  HTML, JavaScript, CSS, bootstrap.
+ <h4>📌 Back-end:</h4>   Python 3.8.10
+ <h4>📌 Bibliotecas do Python:</h4> django 4.0.5
+ <h4>📌 IDE:</h4>  Visual Studio Code

<h2>Implementações</h2>

<table border="1">
    <tr>
        <td>1. Tela de listagem de endereços cadastrados;</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>1.1. Mostrará uma tabela contendo os endereços cadastrados no banco de dados;</td>
        <td>✔️</td>
    </tr>
    <tr>
      <td>1.2. Terá um botão chamado “cadastrar”, onde será redirecionado para a página do
cadastro de endereços;</td>
      <td>✔️</td>
  </tr>
    <tr>
      <td>1.3. Será a tela inicial do sistema;</td>
      <td>✔️</td>
  </tr>
  <tr>
      <td>2. Tela de cadastro de endereços;</td>
      <td>✔️</td>
  </tr>
  <tr>
      <td>2.1. Terá um formulário com os campos: cep, endereço, número, complemento,
bairro, cidade, uf e descrição;</td>
      <td>✔️</td>
  </tr>
  <tr>
      <td>2.2. Os campos cep, endereço, número, bairro, cidade e uf são obrigatórios;</td>
      <td>✔️</td>
  </tr>
    <tr>
        <td>2.3. Quando digitar um cep, buscar os dados do endereço utilizando a api Viacep</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>2.5. Ao obter os dados do cep, preencher os campos do formulário
automaticamente;</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>2.7. Terá um botão “cadastrar”, onde serão gravados os dados do endereço no
banco de dados. Caso a gravação seja feita com sucesso, redirecionar para a
página de listagem de endereços;</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>2.8. Ao gravar, caso o cep já exista no banco de dados, deve-se atualizar os demais
campos de endereço;</td>
        <td>✔️</td>
    </tr>
</table>

<h2>Execução do sistema</h2>

<ol>
  <li>pip install -r requirements.TXT</li>
  <li>cd scr</li>
  <li>python manage.py makemigrations</li>
  <li>python manage.py migrate</li>
  <li>python manage.py runserver</li>
</ol>

