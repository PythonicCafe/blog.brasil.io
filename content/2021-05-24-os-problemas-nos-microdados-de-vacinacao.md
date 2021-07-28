Title: Os problemas nos microdados de vacinação
Slug: os-problemas-nos-microdados-de-vacinacao
Date: 2021-05-24 18:00:00
Category: meta
Tags: datasets
Authors: turicas
Summary: Desde fevereiro disponibilizamos nossa versão dos microdados de vacinação com diversas melhorias, mas o dataset possui inúmeras inconsistências que devem ser levadas em consideração antes de qualquer análise. Criamos um pedido de acesso à informação para que o Ministério da Saúde esclareça esses problemas.

Desde que identificamos que o [OpenDataSUS passou a disponibilizar os
microdados de vacinação][opendatasus-vacinacao] ganhei uma tarefa diária de
baixar, analisar e melhorar esses dados (que crescem todos os dias). Logo no
começo identifiquei diversos problemas no dataset e depois de bastante trabalho
convertendo e limpando os dados, no dia 14 de fevereiro [anunciamos a nossa
versão dos microdados de vacinação para que qualquer um possa
baixar][tweet-microdados]. **A nossa versão tem maior qualidade** que a
original (facilitando análises), mas é preciso ressaltar que **a base original
possui inconsistências** importantes que devem ser levadas em consideração
quando analisa-se essa base. Na semana passada criei um pedido de acesso à
informação, solicitando ao Ministério da Saúde que esclareça essas
inconsistências (ainda não respondido) e abaixo esclareço as melhorias que
implementei e as inconsistências encontradas.


## Melhorias e correções

O [programa que criei para converter os microdados][programa-vacinacao] é
software livre e qualquer um pode checar todas as melhorias implementadas;
ele identifica diversos problemas e limpa a base de dados, **tornando o
trabalho de quem vai analisar muito mais fácil**, pois os dados são convertidos
para um formato mais consistente e organizado. Por conta de todas as melhorias,
**nossa base de dados é bem menor que a do Ministério** (de 24GB para 18GB,
para os dados capturados na semana passada) e, para agilizar ainda mais o
processo, disponibilizamos nosso CSV já compactado (de 18GB para 5,5GB), que
faz com que nossos usuários economizem tempo de download.

As principais melhorias são:

Melhorias gerais:

- As colunas são renomeadas para que tenham **nomes mais intuitivos e
  padronizados**, facilitando o entendimento de quem vê a base pela primeira
  vez (alguns exemplos: `paciente_racaCor_valor` vira `paciente_etnia`,
  `estabelecimento_valor` vira `estabelecimento_codigo_cnes` e
  `vacina_categoria_nome` vira `paciente_grupo`);
- Todos os **valores que sejam equivalentes a nulo** (como "SEM INFORMACAO")
  são removidos e ficam em branco, poupando espaço e facilitando os filtros por
  estarem mais uniformes;
- **Espaços em branco desnecessários** (em dobro, ou sobrando no começo ou no
  fim das células) são retirados de todas as colunas;
- **Valores impossíveis** (como datas no futuro, datas de vacinação antes de
  2020 e UF "XX") são trocados para nulo (em branco);
- Os campos de data/hora contém sempre os mesmos valores para
  hora/minuto/segundo e, por isso, são transformados **apenas em datas** (dessa
  forma economizamos espaço);
- A coluna `numero_dose`, que originalmente contém valores como "   1ª Dose", é
  **convertida para o tipo inteiro** e contém os seguintes valores: (nulo), "1"
  ou "2";
- Os valores para a coluna `sistema_origem` são normalizados, **removendo as
  repetições** por diferenças na grafia;
- Os **nomes das vacinas são normalizados** (existem diferenças na grafia para
  uma mesma vacina) e ficam bem menores.


Melhorias nos dados de municípios:

- Os códigos IBGE (do paciente e do estabelecimento de saúde) são substituídos
  pelo código de 7 dígitos em vez do código de 6 dígitos original para
  facilitar o cruzamento com outras bases de dados;
- A grafia dos municípios é melhorada e fica mais apresentável ("SAO PAULO"
  vira "São Paulo", por exemplo), pois usamos como base os nomes oficiais do
  IBGE (nomes com acentos e apenas as primeiras letras maiúsculas);
- Diversos nomes, UFs e códigos IBGE de municípios são corrigidos: alguns
  municípios possuem o código errado (dado o nome/UF), já outros possuem nomes
  errados (exemplo: vários municípios de Goiás que foram transferidos para o
  Tocantins possuem "GO" como UF e o nome seguido de "(TRANSF. P/TO)");


Melhorias nos dados de pacientes:

- Os valores possíveis para a coluna `paciente_racaCor_valor` são colocados em
  um formato mais apresentável ("INDIGENA" vira "Indígena", por exemplo);
- A idade de alguns pacientes estava incorreta e, por isso, é recalculada
  a partir da data de nascimento;
- Nós **não publicamos a data de nascimento** dos pacientes: em vez
  disso, adicionamos uma coluna de faixa etária, que facilita análises e ao
  mesmo tempo não expõe um dado sensível da população brasileira;
- As colunas `paciente_id` e `documento_id` são transformadas em
  [UUID][uuid-wp]s, utilizando [uma metodologia que desenvolvi para criação de
  identificadores universais em bases de dados diferentes][metodologia-uuid].
  Como UUID é suportado por diversas bases de dados nativamente, é muito mais
  fácil e rápido importar, filtrar e agrupar por essas colunas, além de
  adicionar mais um nível de indireção nos dados (preservando ainda mais dados
  possivelmente sensíveis).


## Os problemas e o pedido de acesso à informação

Nossa base não possui as inconsistências apontadas na seção anterior, pois o
programa que criei faz as correções automaticamente, mas essa base **possui
outros problemas (mais graves)** que precisamos levar em consideração ao
analisá-la:

- Calculei a **média de atraso de importação** dos dados a partir da diferença
  entre as colunas `data_importacao_rnds` e `data_aplicacao`. Existe um atraso
  de importação médio nacional de 5.23 dias. A nível estadual, DF, RR, RJ e MS
  possuem as maiores médias (mais de 10 dias);
- Existem 467.985 `paciente_id` únicos que **possuem 3 ou mais registros de
  aplicação** (totalizando 1.492.626 registros), o que não deveria ocorrer pois
  as vacinas são administradas no máximo em duas doses - pode ser indício de
  fraude;
- Para todo o Brasil, existem 659.878 `paciente_id` que **possuem apenas a
  segunda dose registrada** (no total, são 671.417 registros) e para o estado
  de MG existem 174 registros com o valor para `vacina_descricao_dose` como "3ª
  Dose" ou apenas "Dose";
- As colunas `vacina_codigo`, `vacina_nome`, `vacina_fabricante_nome` e
  `vacina_fabricante_referencia` **possuem valores conflitantes**, como códigos
  diferentes para a mesma vacina e nomenclatura diferente para mesmos
  fabricantes. No total, essas 4 colunas geram uma combinação de 199 valores
  distintos, enquanto o esperado seria bem menos (no máximo, o total de vacinas
  vezes o total de fabricantes);
- Existem 170.129 registros de doses aplicadas em indivíduos classificados como
  grupo prioritário "Faixa Etária" na coluna `vacina_categoria_nome`, mas que
  referem-se a **pessoas com menos de 60 anos** (pela coluna `paciente_idade`)
  e que, portanto, não fariam parte do citado grupo prioritário (idosos) -
  também pode ser um indício de fraude.


Veja na íntegra [o pedido de acesso à informação que fiz][pedido-lai] e os
[arquivos SQL][analise-sql] utilizados para fazer as consultas e chegar nos
números citados acima. O pedido ainda não foi respondido, o prazo para resposta
é de até 07/06/2021.

> Atualização (08/06/2021): ontem, 07/06, o Ministério da Saúde pediu
> prorrogação da resposta ao pedido de acesso à informação. O novo prazo de
> atendimento é 17/06/2021.

> Atualização (15/07/2021): recebemos a resposta do pedido de acesso à
> informação e publicamos aqui nosso blog: [Resposta do Ministério da Saúde aos
> problemas nos microdados de vacinação][post-resposta-minsaude].


## Próximos passos

- Publicar mais rapidamente e com maior frequência: já tive bastante trabalho
  durante as últimas semanas para chegar até a forma mais eficiente de baixar e
  converter esses dados, mas ainda podemos agilizar algumas etapas;
- Adicionar base à plataforma: apesar de [disponibilizarmos o CSV para
  download][download-csv], essa base de dados ainda não está disponível para
  acesso/filtragem na plataforma Web/API. Decidi ainda não disponibilizá-la até
  ter uma resposta oficial do Ministério. Antes de adicionar um dataset no
  Brasil.IO passamos muito tempo verificando e analisando a base para ter
  certeza da consistência dos dados na fonte original (esse é um trabalho
  praticamente invisível que fazemos);
- Painel com análises: estamos trabalhando em um painel que mostrará os dados
  dos vacinados de maneira mais rápida para quem só precisar acompanhar valores
  mais gerais.

Para finalizar, gostaria de agradecer especialmente à [Fabiana
Cambricoli][twitter-cambricoli] na definição de quais análises podem ser feitas
na base para identificar inconsistências e ao [Fabrizio de
Mello][twitter-fabrizio] pelas otimizações em nosso banco PostgreSQL.


[analise-sql]: https://github.com/turicas/covid19-br/tree/master/analises/microdados-vacinacao
[metodologia-uuid]: https://github.com/turicas/brasil.io/issues/182
[opendatasus-vacinacao]: https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao
[pedido-lai]: https://github.com/turicas/covid19-br/blob/master/analises/microdados-vacinacao/README.md#pedido-de-acesso-%C3%A0-informa%C3%A7%C3%A3o
[programa-vacinacao]: https://github.com/turicas/covid19-br/blob/master/covid19br/vacinacao.py
[tweet-microdados]: https://twitter.com/brasil_io/status/1361080270791864321
[twitter-cambricoli]: https://twitter.com/Cambricoli
[twitter-fabrizio]: https://twitter.com/fabriziomello
[uuid-wp]: https://en.wikipedia.org/wiki/Universally_unique_identifier
[post-resposta-minsaude]: https://blog.brasil.io/2021/05/24/os-problemas-nos-microdados-de-vacinacao/
