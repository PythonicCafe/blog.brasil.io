Title: Dissecando os custos (e a infraestrutura) do projeto
Slug: dissecando-os-custos-e-a-infraestrutura-do-projeto
Date: 2019-04-17 17:30
Category: meta
Tags: infra, hosting, crowdfunding, história, django, postgresql, neo4j
Author: turicas
Summary: Quando visitamos um site geralmente não temos noção de todo o trabalho e infraestrutura envolvidos para mantê-lo online; nesse artigo detalho os custos do Brasil.IO e falo um pouco da infraestrutura. _Spoiler_: **o projeto ainda está deficitário**.

Quando visitamos um site geralmente não temos noção de todo o trabalho e
infraestrutura envolvidos para mantê-lo online; por trás dos dados apresentados
no [Brasil.IO](https://brasil.io/) existem diversos programas que fazem
raspagem de sites (_Web scraping_), limpeza de dados, além de outros que
armazenam e servem as centenas de gigabytes de dados que temos atualmente;
esses programas rodam em servidores que nos custam em torno de **R$1.100,00**
mensais.

Desde o início do projeto a infraestrutura foi bancada por mim, até que abri
uma [campanha de financiamento coletivo](https://brasil.io/doe) e algumas
pessoas começaram a doar (porém a quantidade de doações que recebemos ainda não
é suficiente e eu ainda pago metade desse valor). Os custos de infraestrutura
que temos hoje estão listados [nessa
planilha](https://docs.google.com/spreadsheets/d/1ZElv9dWuEmhi-X_K674vQ_8YlmLeMo_m6swIqsSfdF0/view)
e segue abaixo um detalhamento de cada item:

## Domínio "brasil.io" (namecheap.com)

Domínio do projeto, registrado em 28 de novembro de 2013 (apesar da ideia ser
antiga, a plataforma começou a ser desenvolvida como é hoje em 2018).

Custo: 35,00 USD / ano.

## Servidor na DigitalOcean EUA (+ extra storage)

Servidor principal (VPS), onde é hospedada a plataforma. Características:
Intel(R) Xeon(R) CPU E5-2650L v3 @ 1.80GHz (dual core), 2GB RAM, 60GB SSD + 1TB
extra de SSD. Está no datacenter de San Francisco.

Nesse servidor rodam a aplicação feita em Django (frontend e API) e os bancos
de dados PostgreSQL (utilizado para [hospedar os
dados](https://brasil.io/datasets) e os índices de busca) e Neo4J (utilizado
para [traçar caminhos entre pessoas e empresas](https://brasil.io/especiais)).

Para o _deployment_ utilizamos o [dokku](https://github.com/dokku/dokku) (um
_platform-as-a-service_ livre) e, com isso, conseguimos subir alterações com um
simples `git push` (como no Heroku, porém mais barato).

Custo: 120 USD / mês.

## DigitalOcean Spaces (arquivos estáticos)

[Digital Ocean Spaces](https://m.do.co/c/5b17037059e9) é um serviço de
hospedagem de arquivos estáticos, similar ao AWS S3. Está sendo utilizado em
caráter de testes para hospedar os arquivos estáticos (para quem quer baixar um
dataset completo) e para os futuros _mirrors_ que teremos. Atualmente o meu
Google Drive pessoal está sendo utilizado para disponibilizar os arquivos
completos, mas ele possui limitações e em breve migraremos totalmente.

Custo: 5 USD / mês.

## Servidor na OVH (+ extra storage)

Servidor secundário (dedicado), onde rodamos os programas que coletam, limpam e
convertem os dados, hospedamos backups e fazemos outros testes.
Características: Intel(R) Xeon(R) CPU D-1520 @ 2.20GHz (8 cores), 32GB de RAM,
60GB HD + extra de 760GB. Está num datacenter no Canadá.

Como o custo é bem menor, está em nossos planos migrar a hospedagem da
plataforma para esse servidor dedicado e rodar os scripts coletores em uma VPS
mais barata (porém essa migração requer algum trabalho).

Custo: 89,90 USD / mês.

## Hospedagem rocketchat - chat.brasil.io (Heroku)

Instância do [Rocket.Chat](https://rocket.chat/) que está por trás do
[chat.brasil.io](https://chat.brasil.io/), onde os colaboradores podem se
comunicar mais facilmente, com divisão por assunto. Roda em um dyno simples (o
mais barato).

Custo: 7,00 USD / mês.

## Horas de trabalho

Trabalho de desenvolvimento de novos scripts de coleta de dados,
desenvolvimento de novas funcionalidades na plataforma, manutenção da
plataforma (verificação de erros, atualização de datasets etc.) e divulgação do
projeto (eventos, palestras, entrevistas, blog etc.).

Todas as horas de trabalho na plataforma (por enquanto) são voluntárias e não
estão sendo pagas porque o projeto atualmente não tem verba disponível (uma de
nossas metas desse ano é justamente conseguir tornar a plataforma sustentável
economicamente. Atualmente trabalho em torno de 60 horas mensais (além do
trabalho de [diversos outros voluntários](https://brasil.io/contribuidores)).

> Nota: os valores descritos são os cobrados pelos provedores de serviços,
> porém como todos os pagamentos são feitos via cartão de crédito em Dólar o
> valor final pago é de 110,38% do que está descrito (4% de spread + 6,38% de
> IOF).
