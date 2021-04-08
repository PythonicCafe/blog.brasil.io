Title: Um ano de coleta diária de dados da COVID-19: Um balanço sobre o projeto e sua importância
Slug: um-ano-de-coleta-diaria-covid19
Date: 2021-04-07 21:00:00
Category: meta
Tags: datasets
Authors: bru-menani, turicas
Summary: Após um ano de coleta de dados sobre a COVID-19, contamos um pouco sobre esse projeto, as pessoas envolvidas e fazemos um paralelo com notícias atuais, demonstrando a importância de dados abertos estarem disponíveis a todos.

20 de março de 2020 foi o início de um projeto marcante aqui no Brasil.IO: a
coleta de [dados diários a nível municipal sobre a COVID-19][painel-covid],
doença que havia acabado de ser [declarada como Pandemia pela Organização
Mundial da Saúde][oms-pandemia].

Naquele momento, como o governo já dava sinais de que os dados da pandemia
poderiam não ser disponibilizados de forma estruturada e acessível, o que,
inclusive, [se comprovou mais tarde][reducao-boletim], a ideia era tentar
ajudar a comunidade a tomar decisões certeiras no combate à pandemia. A partir
de uma primeira análise das diversas formas e meios pelos quais as informações
estavam sendo fornecidas pelas autoridades locais, foram convocados
[voluntários][voluntarios] a ajudar no projeto.

<center>
<blockquote class="twitter-tweet"><p lang="pt" dir="ltr">DADOS: CASOS DE <a href="https://twitter.com/hashtag/COVID19?src=hash&amp;ref_src=twsrc%5Etfw">#COVID19</a> POR MUNICÍPIO POR DIA!<br><br>A população precisa saber o quanto antes a quantidade de casos em seu município, bem como sua evolução *diária*, só assim teremos agilidade e efetividade nas ações de combate à propagação do vírus. Quer os dados? Segue o fio:</p>&mdash; Álvaro Justen #UsePFF2 #VacinaJá (@turicas) <a href="https://twitter.com/turicas/status/1241068121202536448?ref_src=twsrc%5Etfw">March 20, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

Desde então, pessoas de diversos lugares do mundo (tem brasileiro até da
Inglaterra coletando dados) dispõem de alguns minutos do seu dia para traduzir
um monte de dados esparsos em informação limpa, organizada e estruturada.
Algumas precisaram sair da equipe por questões pessoais, outras entraram
depois, mas sem elas não seria possível publicarmos atualizações diárias.
Definimos uma metodologia para a coleta e checagem, automatizamos diversos
processos e finalmente passamos a ter dados confiáveis sobre a pandemia no
Brasil (houve dias em que até os dados oficiais do Governo Federal foram
publicados com erros, mas os nossos estavam corretos). Com a disponibilização
dessa informação, jornais (nacionais e internacionais, pequenos e grandes, na
Web e em manchetes no impresso) e órgãos como a FioCruz e o IBGE começaram a
utilizá-la. Mais info no [clipping].

Em junho do ano passado, devido ao [apagão proposital de dados do Ministério da
Saúde][apagao_MS], reunimos mais uma força-tarefa para criar um boletim diário
com os totais informados pelos estados em seus boletins. Enquanto os
voluntários de cada Estado coletavam a base completa com os dados dos
Municípios, essa outra equipe começou a coletar o total de casos
confirmados/óbitos por Estado. Desde então, todos os dias, sem exceção,
divulgamos nosso [boletim].

<center>
<a href="https://brasil.io/covid19/boletins/">
  <img
    alt="Boletim Brasil.IO COVID-19 de 7 de abril de 2021"
    src="https://data.brasil.io/dataset/covid19/boletim/2021-04-07.png"
    width="80%">
</a>
</center>

Com os meses se passando, outros dados relevantes foram incorporados, como os
óbitos registrados em [cartórios][cartorios], [beneficiários do auxílio
emergencial][aux_emergencial] e os microdados de [vacinação][vacinacao]. Também
criamos nosso próprio [painel][painel-covid], no qual é possível ver mapas e
gráficos.

Não podemos deixar de ressaltar como essa iniciativa de coleta de dados diária
**demonstra sua importância todos os dias**. Um exemplo disso foi quando [o
Governo Federal alterou os parâmetros para inserção de dados no Sivep-Gripe
(Sistema de Informação de Vigilância da Gripe)][parametros_MS], cujo
preenchimento é obrigatório desde 2009 para casos gripais e também está sendo
utilizado para monitorar a COVID-19. Dentre as alterações, que não foram
combinadas com estados e municípios, passou-se a ser obrigatória a informação
de pelo menos um de dois números: o CPF e, na ausência deste, o do  cartão SUS.
Isso ocasionou diversos problemas, que impactaram a notificação de óbitos pela
doença, levando a uma diminuição irreal nesses números enquanto a mudança ficou
vigente.

Apesar do Ministério da Saúde ter [voltado atrás na alteração da
ferramenta][parametros_MS_desfaz], isso é bem mais grave do que parece. Há
estados em que os números são preenchidos diretamente no Sivep, enquanto outros
possuem seus próprios registros e, com isso, o atraso de preenchimento do Sivep
resultaria em dados completamente diferentes sendo divulgados por órgãos
oficiais (estados e Governo Federal), o que poderia dificultar ainda mais o
acesso à informação de qualidade, resultando em mais desinformação.

A falta de dados atuais, confiáveis e padronizados, como seria esperado que o
Ministério da Saúde fizesse, dificultam o controle da pandemia, causando mortes
que poderiam ser evitadas. Na história do Brasil infelizmente temos um outro
exemplo disso: [durante a ditadura militar, na década de 70, o país sofreu uma
epidemia de meningite][meningite_ditadura] e, naquela época, os profissionais
de saúde e comunicação foram proibidos de se manifestar sobre o que estava
acontecendo, conduta que gerou prejuízos irreparáveis, já que nem os médicos
tinham informações sobre qual doença estava atingindo gravemente tantas
pessoas.

Apesar de saber que essa crise poderia ser muito pior caso não houvesse
iniciativas como esta, nós, colaboradores do projeto, nunca esquecemos que cada
número preenchido na planilha significa uma cadeira vazia na mesa das famílias
durante as refeições. E como a gente gostaria de não ter que contabilizar isso!
Esperamos que a velocidade com que esses números vêm aumentando seja freada em
breve, mas, até que a maioria da população seja vacinada e essa fase dolorosa
não passe, conte com nosso trabalho para acompanhar os dados sobre a pandemia
e, se você puder e quiser, colabore com nosso projeto divulgando-o,
[programando][contribuidores] ou mesmo [doando para nossa campanha de
financiamento coletivo][apoiase].

[painel-covid]: https://brasil.io/covid19/
[oms-pandemia]: https://twitter.com/WHO/status/1237774421307228160
[reducao-boletim]: https://g1.globo.com/politica/noticia/2020/06/06/apos-reduzir-boletim-governo-bolsonaro-retira-dados-acumulados-da-covid-19-de-site-oficial.ghtml
[voluntarios]: https://brasil.io/covid19/voluntarios/
[clipping]: https://github.com/turicas/covid19-br/blob/master/clipping.md
[boletim]: https://brasil.io/covid19/boletins/
[apagao_MS]: https://noticias.uol.com.br/ultimas-noticias/ansa/2020/06/06/ministerio-da-saude-tira-portal-com-dados-sobre-covid-do-ar.htm
[cartorios]: https://brasil.io/dataset/covid19/obito_cartorio
[aux_emergencial]: https://brasil.io/dataset/govbr/auxilio_emergencial
[vacinacao]: https://twitter.com/brasil_io/status/1376682456028438530
[parametros_MS]: https://g1.globo.com/bemestar/coronavirus/noticia/2021/03/24/apos-recorde-de-mortes-por-covid-19-ministerio-da-saude-altera-criterios-de-confirmacao-dos-obitos.ghtml
[parametros_MS_desfaz]: https://www.gov.br/saude/pt-br/assuntos/noticias/nota-a-imprensa-sivep-gripe
[meningite_ditadura]: https://blogs.oglobo.globo.com/blog-do-acervo/post/epidemia-de-meningite-que-ditadura-militar-no-brasil-tentou-esconder-da-populacao.html
[contribuidores]:https://brasil.io/contribuidores
[apoiase]: http://apoia.se/brasilio
