Title: Painel COVID-19 e 2 anos de Brasil.IO
Slug: painel-covid19-e-2-anos-de-brasilio
Date: 2020-04-18 19:45
Category: datasets
Tags: covid19, opendata, ddj, colaboração
Author: turicas
Summary: No dia em que o Brasil.IO faz dois anos, lançamos nossa primeira visualização de dados: um mapa com os dados da COVID-19 no Brasil, com diversas informações por município.

O Brasil.IO [está fazendo dois anos
hoje](https://blog.brasil.io/2019/04/18/1-ano-de-dados-acessiveis/) e lançamos
nossa primeira visualização de dados! O foco do projeto continua sendo coletar
e disponibilizar dados públicos em formatos acessíveis, mas por ser um lugar
central de dados abertos no país, podemos gerar maior impacto com os dados que
publicamos se também tivermos visualizações: assim a informação fica mais fácil
de ser consumida e fica acessível a mais pessoas.

No [Painel COVID-19](https://brasil.io/covid19/) é possível ver números gerais
sobre a propagação da doença, bem como informações detalhadas sobre municípios
em uma mapa e uma tabela.

![Mapa com dados da covid19 por município brasileiro](/images/2020-04-18-covid19-mapa.png)

No mapa, é possível selecionar 4 variáveis diferentes: total de casos
confirmados, confirmados por 100.000 habitantes, total de óbitos e taxa de
letalidade. Também é possível dar zoom em cada estado e, ao passar o mouse
sobre o município, informações detalhadas são exibidas no canto inferior
direito. Usei uma escala logarítmica (log2) para determinar as cores de cada
município.

Apesar de parecer simples, exibir polígonos de municípios a nível nacional em
um mapa que carregue rapidamente não é tarefa simples: o Brasil possui 5.570
municípios e os polígonos disponibilizados pelo IBGE (_shapefiles_) somam quase
500MB quando convertidos para o formato GeoJSON (usado em visualizações na
Web). Para que o tempo de carregamento seja viável, é necessário simplificar
os polígonos e, em alguns casos, filtrar para que nem todos os polígonos sejam
baixados. Em breve publicaremos um dataset com esses _shapefiles_ de municípios
brasileiros em formato GeoJSON, para facilitar a vida de quem precisa de
visualizações desse tipo.

![Tabela com dados da covid19 por município brasileiro](/images/2020-04-18-covid19-tabela.png)

Na tabela é possível buscar facilmente as informações mais recentes sobre cada
município e baixar os dados em formato CSV.

Espero que gostem. ;)

O [Brasil.IO](https://brasil.io/) surgiu como ideia em 2013, mas só entrou em
operação como é hoje em 2018. Hoje faz 2 anos que estamos online, servindo
dados acessíveis aos brasileiros gratuitamente. :) [Contribua com o
projeto](https://apoia.se/brasilio).
