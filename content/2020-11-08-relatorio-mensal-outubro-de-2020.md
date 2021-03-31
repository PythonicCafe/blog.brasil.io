Title: Relatório mensal: outubro de 2020
Slug: relatorio-mensal-outubro-de-2020
Date: 2020-11-08 12:00:00
Category: meta
Tags: relatório, desenvolvimento, infraestrutura
Author: turicas
Summary: Além da atualização de diversos datasets (COVID-19, empresas/sócios e auxílio emergencial), fizemos diversas melhorias no backend e trabalhamos nos dados das eleições.

Pretendia publicar esse relatório no primeiro dia do mês, mas por conta de
[meu keynote na Python Brasil 2020][keynote-pybr2020] acabei atrasando. Como
saiu atrasado, então aproveitei para listar o que fizemos em outubro e nessa
primeira semana de novembro. Vamos lá:

- [O que Fizemos](#o-que-fizemos)
- [Próximos Passos](#proximos-passos)
- [Como Você Pode Ajudar](#como-voce-pode-ajudar)

## O que Fizemos

### Atualização dos dados da COVID-19

Essa seção vai aparecer nos relatórios dos próximos meses sempre, pois
continuamos trabalhando **diariamente** na atualização dos [dados da
COVID-19][brasil-io-covid19] **desde 20 de março de 2020**. A partir de 6 de
junho, [quando houve o apagão de dados do Ministério da
Saúde][apagao-minsaude], começamos a publicar um boletim próprio, com base nos
dados que coletamos - **já publicamos mais de 150 boletins diários**! Esse
dataset só é possível devido à colaboração de [dezenas de pessoas
voluntárias][brasil-io-covid19-voluntarios], que coletam e checam os dados
diretamente das Secretarias Estaduais de Saúde. Nossos dados já foram utilizados por diversos veículos nacionais e
internacionais, além de instituições renomadas como FioCruz e IBGE. [Confira
nosso
_clipping_](https://github.com/turicas/covid19-br/blob/master/clipping.md).

Em 15 de outubro reativamos o perfil do [@brasil_io no
Twitter][twitter-brasil-io] e passamos a publicar nosso boletim diário por lá
também (antes era publicado em [meu perfil pessoal][twitter-turicas]).

### Atualização da população dos municípios

Atualizamos a população (estimada para 2020) dos municípios brasileiros, dado
relevante para calcular as taxas de confirmação de casos da COVID-19 em nosso
[Painel COVID-19][brasil-io-covid19]. Como a forma de escrever os nomes de
alguns municípios mudou, precisamos também fazer algumas correções no código da
plataforma. Ainda não publicamos um dataset específico para esses dados (é
usado apenas internamente), mas você pode acessar [o código de captura dos
dados do censo do IBGE][censo-ibge] e [os arquivos CSV com estimativas da
população][censo-ibge-dados].

### Implementação da autenticação na API

Deixamos nosso cadastro mais robusto (agora, existe um captcha e é necessário
confirmar o email) e implementamos autenticação obrigatória na API, passos
importantes para a nossa defesa contra novos ataques. O código já foi revisado
e devidamente testado, mas a autenticação obrigatória ainda não está habilitada
para que os usuários tenham tempo hábil para migração de suas bases de código.

Aproveitando essas alterações, também migramos o _hostname_ de acesso à API
(agora será: `https://api.brasil.io/v1/`) e configuramos redirecionamentos nas
URLs antigas. Essa alteração, além de facilitar a criação de futuras versões,
nos ajudará a executar o backend da API independente do backend do site em si
(no futuro).

Habilitaremos a **autenticação obrigatória na API amanhã, 9 de novembro**. Se
você utiliza a API, [entenda como proceder][blog-api-autenticada].

### Dataset atualizado: auxílio emergencial

Adicionamos dados de mais parcelas do auxílio emergencial: agora temos, no
total, informações sobre o pagamento de 5 parcelas (abril a agosto),
totalizando mais de **257 milhões de registros** em uma única tabela.

Com esses dados é possível entender quantas parcelas cada pessoa recebeu,
quanto foi direcionado a cada município/unidade federativa e, inclusive, cruzar
os beneficiários com outras bases de dados para detectar possíveis
irregularidades no recebimento.

- [Baixe os dados completos](https://brasil.io/dataset/govbr/files/) (4,7GB)
- [Navegue e filtre os
  dados](https://brasil.io/dataset/govbr/auxilio_emergencial/) (257M+
  registros)
- [Baixe os dados originais](https://data.brasil.io/mirror/govbr/_meta/list.html)
- [Veja o código de captura, conversão e limpeza dos
  dados](https://github.com/turicas/transparencia-gov-br)

### Dataset atualizado: empresas, sócios e atividades empresariais (CNAE)

Esse dataset é um dos mais relevantes que publicamos e é utilizado por
jornalistas, pesquisadores e empresas. Com ele é possível entender relações de
interesse entre políticos, mapear o empreendedorismo local e até fazer
pesquisas de mercado. Antes de ser libertado em 2018, já quiseram [nos cobrar
R$ 506.000,00 por esses dados][tweet-socios-brasil] (públicos!). Felizmente,
vários recursos e meses depois conseguimos ganhar o pedido de acesso à
informação ([confira a história completa][historia-socios-brasil]).

A Receita Federal atualizou esses dados no fim de setembro e nós publicamos uma
cópia em nosso servidor (para download mais rápido), porém por conta das
alterações que estávamos fazendo na API para conter os ataques, ainda não
tínhamos publicado os dados na plataforma.

- [Baixe os dados completos](https://brasil.io/dataset/socios-brasil/files/)
- [Navegue e filtre os dados](https://brasil.io/dataset/socios-brasil/empresas/)
- [Baixe os dados originais](https://data.brasil.io/mirror/socios-brasil/_meta/list.html)
- [Veja o código de captura, conversão e limpeza dos
  dados](https://github.com/turicas/socios-brasil)

> **Nota**: por questões históricas, os dados apresentados em nossa plataforma
> ainda não contemplam todas as colunas disponíveis nesse dataset (apesar de
> estarem atualizados). Estamos trabalhando na migração desses dados e, em
> breve, teremos mais novidades.

### Últimas Atualizações na Página Inicial

Com o intuito de dar mais visibilidade ao que estamos fazendo, adicionamos uma
pequena seção na [página principal da plataforma][brasil-io-home] com as
últimas atualizações em datasets e publicações aqui no blog:

![Últimas Atualizações na Página Inicial](/images/2020-11-08-ultimas-atualizacoes.png)

Estamos planejando a melhoria dessas atualizações, com notificações
personalizadas, mas essa etapa ainda deve demorar um pouco por conta de outras
prioridades.

### Melhorias no Código do Backend

Apesar de não ficarem visíveis para quem acessa o site e os dados, fizemos
melhorias importantes no código do _backend_, que nos ajudarão a evoluir mais
rapidamente no futuro (e, possivelmente, destacar parte do código em outras
bibliotecas, para que outras pessoas possam também utilizá-las - isso diminuirá
a complexidade do código da plataforma e o tornará ainda mais fácil de manter).
Caso queira saber mais, veja os _pull requests_ [#455][pr-455] e [466][pr-466].

### O que não conseguimos finalizar

Apesar de termos iniciado tudo que prometi fazer em outubro (e diversas outras
coisas), não conseguimos finalizar todas as tarefas (algumas já estão quase
finalizadas). São elas:

- **Atualizar dataset eleições brasil com dados de 2020**: não conseguimos
  concluir a atualização porque:
  - Precisaremos migrar o schema dos dados (e para isso precisaremos
    implementar alguns redirecionamentos, para não quebrar links antigos),
  - O trabalho de normalizar os nomes de colunas foi maior do que
    esperávamos e ainda estamos concluindo.
- **Criar tabela com candidatos em 2020 que possuem empresas**: para a correta
  extração desses dados dependemos da finalização da tarefa acima.
- **Melhorar a documentação da API**: iniciamos, mas não finalizamos por conta
  de outras demandas que acabaram se tornando mais importantes (como as
  melhorias no backend, que facilitarão a implementação dos redirecionamentos).
- **Criar páginas exclusivas para acessar dados das eleições**, facilitando o
  acesso de usuários leigos: iniciamos um esboço das telas, mas como essa
  página depende totalmente dos dados das eleições, preferimos pausar o
  desenvolvimento até que o dataset seja atualizado.

## Próximos passos

Para o restante do mês de novembro, pretendemos:

- Organizar o sprint na [Python Brasil 2020][pybr2020] (**hoje**, 8 de
  novembro), para facilitar a colaboração por novas pessoas.
- Habilitar a autenticação na API (amanhã, 9 de novembro).
- Começar a implementação da LGPD na plataforma, com a colaboração do [Juliano
  Madalena][juliano-madalena], advogado especializado em direito digital e
  fundador do fórum [direitodigital.io][direito-digital]. A
  primeira etapa será levantar todos os dados pessoais que temos em datasets já
  publicados.
- Implementar redirecionamentos nos datasets, para que seja possível migrarmos
  o schema (nomes de colunas e das tabelas) e, ainda assim, manter os links
  antigos funcionais
- [Dataset de eleições brasileiras][brasil-io-eleicoes]:
  - Checar e finalizar normalizações de nomes de colunas das tabelas de
    receitas e despesas de partidos, comitês/diretórios e candidaturas
    (trabalho já iniciado, com ajuda de [Rhenan Bartels][rhenan-bartels]).
  - Implementar os redirecionamentos do schema antigo para o novo.
  - Atualizar dados na plataforma.
- Continuar **atualizando diariamente** os dados da COVID-19 e publicando
  boletins.

## Como Você Pode Ajudar

Se você quiser nos ajudar nessa jornada de **tornar acessíveis os dados
públicos brasileiros**, considere:

- [Doar para nossa campanha de financiamento coletivo][brasil-io-apoiase]
- Unir-se às [pessoas voluntárias do projeto
  COVID-19][brasil-io-covid19-voluntarios] através do [nosso
  chat][brasil-io-chat]
- [Colaborar programando][brasil-io-colabore]

Aproveite também para **acompanhar nosso trabalho**:

- Siga o [RSS desse blog][blog-rss]
- Entre para nosso [canal no Telegram][brasil-io-telegram], onde enviamos de
  forma imediata as principais atualizações
- Siga o [@brasil_io no TWitter][brasil-io-twitter]

Até a próxima! :)

[apagao-minsaude]: https://www.bbc.com/portuguese/brasil-52974181
[blog-api-autenticada]: https://blog.brasil.io/2020/10/31/nossa-api-sera-obrigatoriamente-autenticada/
[blog-rss]: https://blog.brasil.io/feed.rss
[brasil-io-apoiase]: https://apoia.se/brasilio
[brasil-io-chat]: https://chat.brasil.io/
[brasil-io-covid19-voluntarios]: https://brasil.io/covid19/voluntarios/
[brasil-io-covid19]: https://brasil.io/covid19/
[brasil-io-colabore]: https://brasil.io/colabore/
[brasil-io-eleicoes]: https://brasil.io/dataset/eleicoes-brasil/
[brasil-io-home]: https://brasil.io/
[brasil-io-telegram]: https://t.me/brasil_io
[brasil-io-twitter]: https://twitter.com/brasil_io
[censo-ibge-dados]: https://github.com/turicas/censo-ibge/tree/main/data/output
[censo-ibge]: https://github.com/turicas/censo-ibge
[direito-digital]: https://direitodigital.io/
[historia-socios-brasil]: https://github.com/turicas/socios-brasil/blob/master/historia-do-dataset.md
[juliano-madalena]: https://www.julianomadalena.com.br
[keynote-pybr2020]: https://www.youtube.com/watch?v=cUYFIga_JXU
[pr-455]: https://github.com/turicas/brasil.io/pull/455
[pr-466]: https://github.com/turicas/brasil.io/pull/466
[pybr2020]: https://2020.pythonbrasil.org.br/grade/
[rhenan-bartels]: https://github.com/rhenanbartels/
[tweet-socios-brasil]: https://twitter.com/turicas/status/1019272233095745537
[twitter-brasil-io]: https://twitter.com/brasil_io
[twitter-turicas]: https://twitter.com/turicas
