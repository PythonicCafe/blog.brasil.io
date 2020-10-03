Title: Relatório mensal: setembro de 2020
Slug: relatorio-mensal-setembro-de-2020
Date: 2020-10-01 16:25:00
Category: meta
Tags: relatório, desenvolvimento, infraestrutura
Author: Álvaro Justen
Summary: Com o objetivo de aumentar a transparência do que estamos fazendo e nos aproximarmos dos apoiadores e usuários do projeto, estamos reestruturando nossa comunicação e os relatórios mensais são parte desse processo.


Apesar de estarmos bastante atarefados por aqui, muitas das coisas que estamos
fazendo no [Brasil.IO](https://brasil.io/) não são tão facilmente visíveis a
todos, por isso resolvi criar relatórios mensais, que são parte de uma
estratégia de comunicação mais estruturada, para tornar nosso processo mais
transparente e nos aproximarmos de quem apoia e utiliza o projeto.

Escrevo na primeira pessoa do plural pois do lado de cá temos muitas pessoas
envolvidas no projeto: além das [pessoas voluntárias no projeto
COVID-19](https://brasil.io/covid19/voluntarios/), eu (Álvaro Justen), Bernardo
Fontes e Marcel Marques estamos trabalhando no desenvolvimento e infraestrutura
(existem vários outros contribuidores de código também, em vários repositórios,
mas nós 3 estamos no dia-a-dia trabalhando na plataforma).


## O que fizemos

Vamos então ao que fizemos em setembro de 2020:


### Projeto COVID-19

Trabalhamos **diariamente** na atualização dos [dados da
COVID-19](https://brasil.io/covid19/) desde 20 de março de 2020. A partir de 6
de junho, [quando houve o apagão de dados do Ministério da
Saúde](https://www.bbc.com/portuguese/brasil-52974181), começamos a publicar um
boletim próprio, com base nos dados que coletamos - já publicamos mais de 100!

Além do trabalho diário, nesse mês fizemos diversas melhorias e correções em
ferramentas internas que utilizamos para checar os dados, atualizar o dataset
etc.

Nossos dados já foram utilizados por diversos veículos nacionais e
internacionais, além de instituições renomadas como FioCruz e IBGE. [Confira
nosso
*clipping*](https://github.com/turicas/covid19-br/blob/master/clipping.md).


### Combate aos ataques

Sim, fomos atacados (virtualmente), mas não foi um ataque estilo "invasão": nas
últimas semanas recebemos uma quantidade muito grande de requisições
coordenadas. Foram tantas que nossos servidores não aguentaram muito bem (o
site ficou bastante lento em alguns momentos, inclusive atrasando a atualização
de dados da COVID-19). Talvez a intenção não tenha sido fazer com que a
plataforma caísse, mas não podemos aceitar que o site fique lento por conta de
usuários abusivos e, por isso, precisamos implementar limitações de acesso à
API.

O processo foi relativamente longo (para mais detalhes [veja as *issues* no
GitHub](https://github.com/turicas/brasil.io/issues?q=is%3Aissue+cloudflare)),
mas já conseguimos resolver boa parte do problema e o site está responsivo
novamente. Ainda temos algumas questões a serem endereçadas, mas já traçamos um
plano.


### Atualizações na página inicial

No caminho de aumentar a visibilidade do que estamos fazendo, adicionamos uma
coluna de últimas atualizações na página inicial; lá ficarão todos os datasets
que foram atualizados recentemente. Em breve adicionaremos mais detalhes a esse
coluna e outras funcionalidades, como a opção de assinar as atualizações por
RSS (e eventualmente até a opção de "seguir" um dataset).


### Melhoria na importação de dados e Página de download de arquivos

Atualizar os dados da COVID-19 ainda nos toma muito tempo e, por isso, estamos
sempre melhorando o processo de importação de dados, para que seja cada vez
mais automático. Uma das melhorias que fizemos nesse mês tem a ver com a forma
como os arquivos completos dos datasets são listados e hospedados: agora estão
mais integrados com a plataforma e cada dataset possui um link mais amigável -
o da COVID-19, por exemplo, ficou como
[brasil.io/dataset/covid19/files/](https://brasil.io/dataset/covid19/files/).

Apesar de pouco impacto para os usuários, essa alteração nos ajudou a ser mais
produtivos na atualização dos datasets e a reestruturação no código abriu
caminho para outras melhorias que virão.


### Correção da página de empresas

A página que contém informações consolidadas de empresas (como [essa, da
Odebrecht](https://brasil.io/especiais/documento/15102288000182/)) estava com
um pequeno bug, que não permitia visualizar algumas das empresas disponíveis no
[dataset socios-brasil](https://brasil.io/dataset/socios-brasil/). Já foi
corrigido e agora todas estão acessíveis!


## Próximos passos

Para outubro, pretendemos:

- Implementar autenticação na API (e por segurança precisaremos deixar o
  cadastro mais rigoroso);
- Atualizar os seguintes datasets:
    - [Eleições](https://brasil.io/dataset/eleicoes-brasil/) (atualizar e
      melhorar código do programa que converte os dados e atualizar dados na
      plataforma);
    - [Empresas e sócios](https://brasil.io/dataset/socios-brasil/) (atualizar
      dados na plataforma);
    - Criar dataset de candidatos em 2020 que possuem empresas;
    - [Auxílio emergencial](https://brasil.io/dataset/govbr/auxilio_emergencial/)
      (atualizar dataset na plataforma, com novas parcelas);
- Criar páginas exclusivas para acessar dados das eleições, facilitando o
  acesso de usuários leigos;
- Atualizar dados da população dos municípios (usados no [Painel
  COVID-19](https://brasil.io/covid19/) e no portal das eleições que será
  criado);
- Melhorar a documentação da API;
- Continuar atualizando diariamente os dados da COVID-19.


## Feedback sobre a comunicação

Ainda estamos experimentando as melhores formas de comunicar novidades do
projeto. Algumas ideias são:

- Publicar o relatório mensal em [nossa campanha de financiamento
  coletivo](https://apoia.se/brasilio) e aqui no blog;
- Utilizar o [canal no Telegram](https://t.me/brasil_io) para enviar de forma
  imediata as principais atualizações;
- Reativar a [conta @brasil_io no TWitter](https://twitter.com/brasil_io) para
  publicar os boletins diários da COVID-19 e atualizações em datasets;
- Repensar o conteúdo e a periodicidade da newsletter.

E aí, o que achou?
Abração!
