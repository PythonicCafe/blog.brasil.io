Title: Como acessar os dados do Brasil.IO
Slug: como-acessar-os-dados-do-brasil-io
Date: 2020-10-10 20:30:00
Category: meta
Tags: api, infraestrutura
Author: turicas
Summary: Existem diversas maneiras de acessar os dados disponibilizados pelo Brasil.IO, cada uma com características específicas (algumas mais rápidas que outras, por exemplo). Veja todas as possibilidades, com exemplos de código!

Existem diversas maneiras de acessar os dados disponíveis no [Brasil.IO][brasil-io].
Dentre elas, pedimos que dê preferência ao [download de dados
completos](#dados-completos).

> Nota 1: ainda estamos trabalhando nessa documentação e, em breve, teremos
> passos mais detalhados e claros. Fique à vontade para contribuir com exemplos
> de código em outras linguagens.

> Nota 2: para acessar o dicionário de dados de uma tabela, acesse a aba
> "Metadados" dentro da página da tabela, que segue o seguinte padrão:
> `https://brasil.io/dataset/<dataset-slug>/<table-name>/`, exemplo: [tabela
> caso do dataset covid-19][covid19-caso].

## Dados completos

Essa é a melhor maneira de acessar os dados do [Brasil.IO][brasil-io] e você
deve preferí-la sobre as outras quando possível, pois onera menos nossos
servidores (lembre-se: nosso projeto é desenvolvido por voltunários e [depende
de doações](https://apoia.se/brasilio) para pagar os custos).

Siga os seguintes passos:

- Acesse a página da tabela dentro do dataset desejado, exemplo: [tabela caso
  do dataset covid-19][covid19-caso]
- Clique no link [baixar dados
  completos][covid19-files]
- Na página com os arquivos, clique na tabela desejada (o nome será algo como
  `tabela.csv.gz`)
- Descompacte o arquivo e abra o CSV da forma como preferir

Veja um exemplo de como fazer o download de forma automatizada, utilizando a
linguagem Python: [`brasil_io.py`][brasil-io-python] (em breve essa biblioteca
estará disponível no [Python Package Index][pypi]).

> Nota 1: caso o CSV abra com erros de acentuação ou de formatação das colunas
> no Microsoft Excel, [veja esse
> vídeo](https://www.youtube.com/watch?v=nl8gxzCOdCw) para aprender a maneira
> correta de abrir arquivos CSV no Excel.

> Nota 2: muitas vezes os arquivos CSVs são grandes e não abrirão facilmente
> num programa de planilhas eletrônicas como LibreOffice Calc, Microsoft Excel
> ou Google Spreadsheets. Nesse caso, é recomendável que você execute um dos
> seguintes passos:
> 2.1) Filtrar o dataset antes de baixá-lo (veja mais em [Interface Web](#interface-web)).
> 2.2) Utilizar algum software mais robusto de banco de dados que consiga lidar
> com essa quantidade de dados, como SQLite, PostgreSQL, MySQL etc. Aprenda
> mais sobre como trabalhar com grandes bases de dados [nesse curso gratuito de
> introdução ao jornalismo de dados (no módulo 5,
> especificamente)](https://github.com/turicas/braindump/blob/loading/mooc-ddj.md).
> 2.3) Caso você saiba programar e prefira acessar aos dados criando um
> programa específico para esse fim, evite carregar todo o arquivo em memória,
> prefira formas "preguiçosas" de extrair a informação que deseja (leia
> registro a registro, compute o que precisar e depois delete-o da memória).

## API

**ATENÇÃO**: essa opção **não é recomendada** caso você precise automatizar
tarefas de download/atualização de dados, pois ela onera muito mais nossos
servidores que a opção apresentada anteriormente, além de possuir limite de
requisições (em caso de abuso, seu IP/usuário/token será bloqueado).

Veja um exemplo de como acessar a API utilizando a linguagem Python:
[`brasil_io.py`][brasil-io-python] (em breve essa biblioteca
estará disponível no [Python Package Index][pypi]).

- [Cadastre-se no site](https://brasil.io/auth/entrar/) e confirme seu email
- [Autentique-se no site](https://brasil.io/auth/login/)
- Acesse a página [de criação de token](https://brasil.io/auth/tokens-api/),
  crie um token e guarde-o
- Acesse a página da tabela dentro do dataset desejado, exemplo: [tabela caso
  do dataset covid-19][covid19-caso]
- Clique no link "utilizar nossa API"
- Navegue pela interface, verificando a resposta em JSON
- Crie programas que acessem a API de maneira autenticada, passando o cabeçalho
  HTTP `Authentication` com o valor `Token <seu-token>`. Veja um exemplo em
  Python: [`brasil_io.py`][brasil-io-python] (em breve essa biblioteca estará
  disponível no [Python Package Index][pypi])

Ainda não temos uma documentação completa sobre a API, com exceção de alguns
datasets, como [a documentação das tabelas do dataset
covid19](https://github.com/turicas/covid19-br/blob/master/api.md). Criar uma
documentação mais abrangente está em nossa lista de tarefas, mas enquanto isso,
fique com as seguintes dicas:

- O padrão de URL para a API hoje é:
  `http://brasil.io/api/dataset/<dataset-slug>/<table-name>/data/` (nota: no
  futuro esse padrão mudará para
  `https://api.brasil.io/v1/dataset/<dataset-slug>/<table-name>/data`).
- Todos os filtros que podem ser feitos na [interface Web](#interface-web) (que
  são passados via _query string_) também funcionam na API (use
  `search=palavra` para _full-text-search_)
- A paginação na API funciona passando `page=N` via _query string_ e o número
  de itens como `page_size=N` (máximo de 10.000). Exemplo:
  [`https://brasil.io/api/dataset/covid19/caso/data/?page=3&page_size=10000`](https://brasil.io/api/dataset/covid19/caso/data/?page=3&page_size=10000`)

## Interface Web

**ATENÇÃO**: essa opção **não é recomendada** caso você precise automatizar
tarefas de download dos dados, pois ela possui um limite de 50.000 registros
por CSV (esse valor pode mudar no futuro) e onera muito mais nossos servidores
que as opções apresentadas anteriormente. Somente utilize-a caso você esteja
navegando nos dados, senão você poderá ser bloqueado pela quantidade de
requisições ao site.

Siga os seguintes passos:

- Acesse a página da tabela dentro do dataset desejado, exemplo: [tabela caso
  do dataset covid-19][covid19-caso]
- Faça os filtros que quiser através do formulário e clique em "Filtrar"
- Após o carregamento da página com os dados filtrados, clique em "Baixar dados
  em CSV"

> Nota 1: o botão de download dos dados em CSV não aparecerá caso o limite de
> registros tenha se excedido (nesse caso, faça mais filtros ou veja outro
> método de download).

> Nota 2: essa forma de download não baixa todas as colunas que a tabela
> possui, apenas as que são exibidas na interface Web. Caso necessite de todos
> os dados, considere [baixar os dados completos](#dados-completos).

> Nota 3: caso o CSV abra com erros de acentuação ou de formatação das colunas
> no Microsoft Excel, [veja esse
> vídeo](https://www.youtube.com/watch?v=nl8gxzCOdCw) para aprender a maneira
> correta de abrir arquivos CSV no Excel.

## Executando os scripts de captura de dados

Cada dataset da plataforma possui seus dados gerados através de programas que
capturam os dados nas fontes originais, convertem, limpam e consolidam tudo no
formato que a plataforma precisa para importá-los (em geral, são arquivos CSV
compactados). Todos esses programas são também software livre e seus
repositórios de código estão disponíveis.

Para executar por conta própria os scripts, siga os seguintes passos:

- Acesse a página da tabela dentro do dataset desejado, exemplo: [tabela caso
  do dataset covid-19][covid19-caso]
- Clique no link referente ao **código-fonte**
- Siga as instruções no README do repositório de código

[brasil-io-python]: https://gist.github.com/turicas/3e3621d61415e3453cd03a1997f7473f#file-brasil_io-py
[brasil-io]: https://brasil.io/
[covid19-caso]: https://brasil.io/dataset/covid19/caso/
[covid19-files]: https://brasil.io/dataset/covid19/files/
[pypi]: https://pypi.org/
