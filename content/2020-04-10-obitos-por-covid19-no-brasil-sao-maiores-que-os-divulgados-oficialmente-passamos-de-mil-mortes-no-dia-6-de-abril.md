Title: Óbitos por covid19 no Brasil são maiores que os divulgados oficialmente (passamos de mil mortes no dia 6 de abril)
Slug: obitos-por-covid19-no-brasil-sao-maiores-que-os-divulgados-oficialmente-passamos-de-mil-mortes-no-dia-6-de-abril
Date: 2020-04-10 20:30
Category: datasets
Tags: covid19, opendata, ddj, colaboração
Author: turicas
Summary: Os dados sobre óbitos em decorrência da covid19 divulgados pelas Secretarias Estaduais de Saúde e pelo Ministério da Saúde estão sempre defasados: cartórios registram muito mais rapidamente óbitos por suspeita ou confirmação de covid19. Adicionamos esses dados ao Brasil.IO - confira as diferenças!

Desde que [lançamos o dataset
covid19](https://blog.brasil.io/2020/03/23/dados-coronavirus-por-municipio-mais-atualizados/),
todos os dias **dezenas de voluntários** coletam os dados das Secretarias
Estaduais de Saúde, checam, entram em contato para resolver inconsistências e
preparam os dados para serem atualizados. Desde então, melhoramos o processo de
atualização (que em parte é manual), automatizamos diversas tarefas,
aprimoramos nossa metodologia e, com isso, **atualizamos nossos dados diversas
vezes por dia**, que estão sendo acessados por milhares de pessoas todos os
dias. Para gerar um maior impacto com nosso trabalho, decidimos buscar outras
fontes que possam validar os dados que já coletamos, gerar estimativas de
subnotificação e nos permitir fazer análises mais complexas. Por isso,
resolvemos coletar, limpar e divulgar no [Brasil.IO](https://brasil.io/) os
dados de **óbitos por suspeita ou confirmação de covid19 registrados em
cartório**.

O [Portal da Transparência do Registro
Civil](https://transparencia.registrocivil.org.br/especial-covid) criou uma
página especial onde é possível ver a quantidade de óbitos por suspeita ou
confirmação de covid19 por dia:

![Foto da página covid19 no Portal da Transparência do Registro
Civil](/images/2020-04-10-registro-civil-covid19.png)

> Nota: o baixo número de casos para os 6 últimos dias **não quer dizer que o
> número de óbitos diminuiu** - eles apenas não entraram no sistema e serão
> atualizados nos próximos dias.

Os dados são atualizados a cada hora e para coletá-los por dia por estado criei
[um programa de
coleta](https://github.com/turicas/covid19-br/blob/master/obitos_spider.py) em
[Python](https://python.org/) usando o _framework_ de Web _scraping_
[scrapy](https://scrapy.org). Você pode acessar os dados no [Brasil.IO](https://brasil.io/) de três formas:

- [Pela interface](https://brasil.io/dataset/covid19/obito_cartorio)
- [Pela API](https://brasil.io/api/dataset/covid19/obito_cartorio/data)
- [Fazendo o download do dataset
  completo](https://data.brasil.io/dataset/covid19/_meta/list.html)

Independente de como preferir acessá-los, confira:

- [A documentação de nossa
  API](https://github.com/turicas/covid19-br/blob/master/api.md)
- [As perguntas (e respostas) mais frequentemente perguntadas sobre nossos
  dados](https://github.com/turicas/covid19-br/blob/master/faq.md)

Depois de uma simples análise, uma péssima notícia: **ultrapassmos os 1.000
óbitos no dia 6 de abril** (e não hoje), ou seja, **os dados divulgados pelas
SES e pelo Ministério da Saúde estão atrasados em 4 dias**. Veja:

![Gráfico mostrando diferença de óbitos das Secretarias Estaduais de Saúde e
Registro Civil](/images/2020-04-10-diferenca-obitos.png)

Além de óbitos em decorrência de suspeita ou confirmação de covid19,
adicionamos também os **óbitos em decorrência de pneumonia e insuficiência
respiratória** para 2020 e 2019; esses dados poderão nos ajudar a **estimar a
subnotificação por falta de testes**, principalmente se comparados aos mesmos
períodos de anos anteriores. Além desses dados, adicionamos no repositório uma
[planilha com as semanas
epidemiológicas](https://github.com/turicas/covid19-br/blob/master/data/epidemiological-week.csv)
e [consultas em SQL que facilitam
análises](https://github.com/turicas/covid19-br#analisando-os-dados).

Todo o trabalho desenvolvido no [Brasil.IO](https://brasil.io/) é feito de
maneira voluntária e colaborativa é mantido através de doações; [**ajude-nos
doando** para nossa campanha de financiamento
coletivo](https://apoia.se/brasilio) e se puder, fique em casa: [o isolamento
social é a única forma de diminuirmos a quantidade de
mortes](https://twitter.com/turicas/status/1248464099660279808)!
