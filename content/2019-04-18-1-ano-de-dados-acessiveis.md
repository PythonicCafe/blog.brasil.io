Title: 1 Ano de Dados Acessíveis
Slug: 1-ano-de-dados-acessiveis
Date: 2019-04-18 23:05
Category: meta
Tags: história, opendata, crowdfunding
Author: turicas
Summary: A ideia do Brasil.IO surgiu em 2013, mas o projeto como é conhecido hoje está no ar há mais ou menos 1 ano. Veja algumas conquistas passadas e desafios fututos.

Tive a [ideia de criar o Brasil.IO há muitos anos, em
2013](http://whois.domaintools.com/brasil.io), porém por diversos motivos
(incluindo mudanças na ideia inicial) o desenvolvimento da plataforma como
existe hoje foi iniciado somente em 2018 - o pontapé inicial aconteceu após
[uma palestra que
apresentei](https://speakerfight.com/events/python-sudeste-2018-tutoriais/#libertando-bases-de-dados-publicas)
na [Python Sudeste 2018](https://2018.pythonsudeste.org/), em São Paulo:
algumas das pessoas que assistiram ficaram comovidas com a ideia e se
voluntariaram a ajudar, daí no evento mesmo já estruturamos algumas coisas.

O site foi ao ar alguns dias depois do evento e diversas alterações foram sendo
feitas, então eu tive que escolher um desses dias para considerar o início do
projeto; escolhi o dia em que [adicionei o código de configuração de
infraestrutura do
PostgreSQL](https://github.com/turicas/brasil.io/commit/9968c8c80bc13c1a5f13557158518d57871a6a5b).
[PostgreSQL](https://www.postgresql.org/) é um dos mais avançados sistemas de
gerenciamento de banco de dados, é software livre e peça fundamental no
[Brasil.IO](https://brasil.io/): os metadados, os dados e os índices de busca
de todos os _datasets_ da plataforma são servidos por ele e, por conta disso,
resolvi fazer essa homenagem.

Nesses últimos 12 meses tivemos algumas conquistas e ainda temos alguns
desafios pela frente:

## Interface Acessível

Apesar de razoavelmente simples, **nossa interface facilita muito o trabalho de
diversas pessoas** (que possivelmente não teriam tempo/conhecimento
técnico/dinheiro suficientes para fazer todo o trabalho de coleta, limpeza,
conversão e hospedagem dos dados), pois apresenta _datasets_ com milhões de
registros de uma maneira rápida, possibilitando filtros, paginação e exportação
dos resultados (seja baixando como CSV ou através de [nossa
API](https://brasil.io/api/datasets)). Além das páginas de _datasets_, as
[páginas especiais](http://brasil.io/especiais) facilitam o cruzamento entre
datasets e análises mais profundas, com poucos cliques.

Como ponto a melhorar temos a experiência do usuário e usabilidade das páginas.

## Datasets Relevantes

Dois _datasets_ da plataforma são de extrema relevância tanto para jornalistas
investigativos, cientistas políticos, advogados, ativistas, dentre outros:
[socios-brasil](https://brasil.io/dataset/socios-brasil/socios) (contém a lista
de CNPJs das empresas brasileiras e seus sócios) e
[eleicoes-brasil](https://brasil.io/dataset/eleicoes-brasil/candidatos) (contém
dados de candidaturas, votação, declaração de bens e filiação partidária das
eleições, desde 1996).

Por conta de termos esses dados acessíveis possibilitamos diversas matérias
serem publicadas, como:

- [Indício de candidaturas laranjas em nomes de
  mulheres](http://www.generonumero.media/candidatura-semvoto-eleicoes2018/)
- [Redução da abertura de novas igrejas no
  país](https://oglobo.globo.com/sociedade/crise-reduz-abertura-de-novas-igrejas-no-pais-23385508)
- [Operações do Exército no Rio geraram milhões para empresa da "Farra do
  Guardanapo"](https://theintercept.com/2018/04/03/exercito-rio-empresa-investigada/)

Contribuímos também com o desenvolvimento de aplicativos que ajudaram no
processo eleitoral:

- [Políticos do Brasil (Poder360)](https://eleicoes.poder360.com.br/)
- [Perfil Político (Open Knowledge Foundation Brasil)](https://perfilpolitico.serenata.ai/)

Como ponto a melhorar, precisamos adicionar mais _datasets_ à plataforma:
apesar de eu ter criado divesos outros programas de coleta de dados (como
recentemente um em que extraí os [beneficiados da Lei da
Anistia](https://twitter.com/turicas/status/1112491956314259457)), parte deles
não está disponível porque precisamos melhorar o processo de criação e
atualização de _datasets_, que tem parte manual.

## Luta por Dados Abertos

Infelizmente, **nem sempre os dados que precisamos estão disponíveis** - e
quando isso acontece tenho duas tarefas: alertar sobre o problema e utilizar a
[Lei de Acesso à
Informação](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm)
para resolver a questão.

Um caso bastante famoso que teve diversas repercussões foi quando [a Receita
Federal quis nos cobrar meio milhão de Reais por dados
públicos](https://medium.com/serenata/o-dia-que-a-receita-nos-mandou-pagar-r-500-mil-para-ter-dados-p%C3%BAblicos-8e18438f3076),
porém diversos outros casos aconteceram (e os processos ainda estão rolando),
como:

- [Diários Oficiais do Rio de Janeiro não possuem licença de dados abertos (e
  outras questões)](https://twitter.com/turicas/status/1091767340134514690),
- [Diários Oficiais de Rondônia não são acessíveis de fora do
  Brasil](https://twitter.com/turicas/status/1094069287206248450),
- [ALERJ libera "dados abertos" em PDF, dificultando o
  acesso](https://twitter.com/turicas/status/1117488008805146625).

Acredito que esse ativismo seja importante não só para resolver as questões
pontualmente, mas também para **mudar a cultura do setor público com relação às
políticas de transparência e dados abertos**. Utilizo bastante [minha conta no
Twitter](https://twitter.com/turicas) e [minhas
palestras](https://github.com/turicas/slides/tree/gh-pages/brasil.io) para
divulgar esses casos (em breve talvez eu faça uma sessão de vídeos contando em
mais detalhes!).

## Comunicação

Por muitas vezes a comunicação da plataforma foi falha, deixando dúvidas sobre
seu funcionamento, processo de desenvolvimento, atualizações etc. Para suprir
essa necessidade criamos uma _newsletter_ e, recentemente, [nosso
blog](https://blog.brasil.io/2019/04/01/ola-brasil/) (que em breve terá mais
publicações técnicas). Aos poucos estamos mudando as páginas da plataforma para
comunicarem melhor o que gostaríamos (que inclusive irá diminuir o fluxo que
recebo de emails com dúvidas).

## Financiamento

Durante os 12 últimos meses foquei bastante na questão técnica (criar novos
programas coletores de dados, melhorar o código da plataforma) e divulgação
(palestras) e acabei deixando de lado a questão financeira. Hoje **o projeto é
deficitário**: ainda não arrecadamos o suficiente em doações para pagar a
infraestrutura ([veja sobre os custos do
projeto](https://blog.brasil.io/2019/04/17/dissecando-os-custos-e-a-infraestrutura-do-projeto/))
e, por isso, mantenho boa parte dos custos.
Precisamos de em torno de **R$ 1.100,00 mensais** (varia conforme a cotação do
dólar - valores em abril de 2019) apenas para manter a plataforma online (esse
valor não contempla horas de trabalho) e por enquanto [nossa campanha de
financiamento coletivo](https://apoia.se/brasilio) recebe metade desse valor.

Estou buscando instituições que acreditem nos valores do projeto e queiram
apoiá-lo (seja em forma de apoios voluntários ou _grants_/editais com algum
entregável) e também clientes de projetos de _Web scraping_ de dados públicos
que paguem o tempo de desenvolvimento de novos coletores ou a melhoria dos já
existentes. Se você puder ajudar ou conhece alguém que possa, por favor [entre
em contato](https://brasil.io/contato).

## Conclusão

Os últimos 12 meses foram maravilhosos, a plataforma se mostrou madura e
geramos diversos impactos positivos, porém ainda temos muito o que melhorar
principalmente no que diz respeito à sustentabilidade financeira do projeto.
Para os próximos 12 meses estamos abertos a
[colaborações](https://brasil.io/colabore) para criar um ecossistema de dados
abertos acessíveis que facilite o surgimento de diversas iniciativas que tem
como objetivo exercer [controle
social](https://pt.wikipedia.org/wiki/Controlo_social). **Vida longa ao
Brasil.IO!**
