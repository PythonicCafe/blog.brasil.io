Title: Nossa API será obrigatoriamente autenticada
Slug: nossa-api-sera-obrigatoriamente-autenticada
Date: 2020-10-31 16:30:00
Category: meta
Tags: api, infraestrutura
Author: Álvaro Justen
Summary: A partir do dia 9 de novembro de 2020 nossa API só aceitará requisições autenticadas. Entenda como acessá-la a partir dessa data e porque precisamos fazer essa alteração.

A partir do dia **9 de novembro de 2020** nossa API aceitará **somente
requisições autenticadas**. Entenda como acessá-la a partir dessa data e porque
precisamos fazer essa alteração:

- [Como acessar a API autenticada](#como-acessar-a-api-autenticada)
- [Entendendo o Problema](#entendendo-o-problema)
- [Lições Aprendidas](#licoes-aprendidas)
- [Como Você Pode Ajudar](#como-voce-pode-ajudar)


## Como acessar a API autenticada

Em resumo: você precisará criar cadastro na plataforma, criar um *token* e
enviá-lo no cabeçalho HTTP `Authorization`. Vamos ao passo-a-passo:

- Caso você não possua um cadastro na plataforma,
  **[cadastre-se](https://brasil.io/auth/entrar/) e confirme seu email**;
- [**Autentique-se** na plataforma](https://brasil.io/auth/login/);
- Acesse a página [de **criação de *API
  tokens***](https://brasil.io/auth/tokens-api/), crie um e guarde-o em local
  seguro;
- Ao criar programas que acessem a API do Brasil.IO, utilize apenas o *host*
  `api.brasil.io` (em vez do antigo `brasil.io/api`) e envie o **cabeçalho HTTP
  `Authentication` com o valor `Token <seu-token>`**. Veja um exemplo em
  Python: [`brasil_io.py`][brasil-io-python] (em breve essa biblioteca estará
  disponível no [Python Package Index][pypi]).

Você já pode alterar seus programas **agora** e testá-los na API e, caso as
requisições sejam feitas com sucesso utilizando a autenticação, você não
precisará fazer alterações em seus programas no dia 9 de novembro. Caso tenha
problemas, [entre em contato conosco][brasil-io-contato].

> **IMPORTANTE**: caso você precise acessar uma quantidade muito grande de
> dados, é provável que seja mais eficiente baixar os datasets completos. Para
> entender como fazer isso e detalhes de como acessar os dados através da API,
> veja nosso artigo [Como acessar os dados do
> Brasil.IO][brasil-io-como-acessar-dados].


## Entendendo o Problema

Apesar de existir como é hoje desde 2018, o [Brasil.IO][brasil-io] ganhou muita
visibilidade após lançarmos o [dataset COVID-19][brasil-io-covid19] em março de
2020, o que mostra a **carência por dados abertos acessíveis sobre a pandemia**
e a **importância de nosso trabalho**. Desde março, além de diversas demandas
para sanar dúvidas sobre os dados e entrevistas sobre os apagões de dados,
precisamos fazer (e fizemos) várias otimizações no código do nosso *backend*
para que a API funcionasse mais rapidamente e conseguisse atender a todos;
essas alterações (como implementação de um sistema de cache mais robusto) nos
tomaram tempo, mas foram necessárias devido ao novo tamanho e às novas
responsabilidades que o projeto assumiu.

Apesar de pequenas lentidões pontuais, conseguimos contornar o problema da
quantidade de acessos, até que durante dias recebemos uma **quantidade enorme
de requisições complexas** (com muitos filtros, custosas aos nossos servidores)
aos [dados do auxílio emergencial][brasil-io-auxemerg], desproporcional com o
tamanho da plataforma (mesmo depois do recente crescimento). Essas requisições
impactaram negativamente a experiência de quem acessa o site, deixando-o mais
lento que o normal e impossibilitou, inclusive, que diversas [pessoas
voluntárias][brasil-io-covid19-voluntarias] pudessem subir os dados da
COVID-19, que são atualizados várias vezes por dia e utilizados por diversas
instituições no acompanhamento da pandemia no Brasil.

Sempre acreditei que **a API do Brasil.IO deveria ser aberta** (sem
autenticação), para facilitar o uso dos dados, por exemplo na criação de
aplicações Web *front-end* que não necessitem de um *backend* próprio. Isso
potencializa o controle social, como mostrei [em uma palestra em 2014 durante o
Fórum Internacional de Software Livre][palestra-fisl], antes mesmo do
[Brasil.IO][brasil-io] existir como é hoje.

Porém, a partir do momento em que essas requisições impedem que outros usuários
acessem o site e que consigamos fazer a atualização devida, precisamos tomar
alguma atitude. Emergencialmente, implementamos limites à quantidade de acessos
por IP por minuto e bloqueios para os IPs que excederem várias vezes os limites
(bloqueando diretamente na [CloudFlare][cloudflare], a [rede de distribuição de
conteúdo][cdn] que utilizamos, e baixando a pressão sobre nossos servidores).
Também precisei entrar em contato diretamente com alguns provedores, reportando
o abuso vindo de alguns IPs (nem todos responderam).

Com os limites e bloqueios a plataforma se estabilizou, mas sabemos que essa
não é a melhor alternativa a longo prazo. Queremos aumentar os limites e
gostaríamos de ter contato mais próximo com quem usa a API (pelo fato de não
conseguirmos identificar as pessoas que fizeram essas requisições, tivemos
dificuldade não somente em comunicar melhores práticas de acesso aos dados,
como também de bloquear mais facilmente esses usos abusivos). Por isso,
decidmos que todo acesso à API será autenticado e, para isso, melhoramos nosso
cadastro, adicionando *captcha* e confirmação por e-mail. A partir do cadastro
mais robusto conseguiremos não somente controlar os acessos (e bloqueá-los, se
necessário), mas também contatar os responsáveis por eventuais abusos.

Se você quiser saber mais detalhes técnicos por trás dessa decisão, acesse as
*issues* [392][issue-392], [426][issue-426], [427][issue-427], [438][issue-438]
e [474][issue-474]. Também estamos trabalhando na melhoria da API na [*issue*
488][issue-488].


### Ataques ou uso massivo?

É possível (apesar de eu achar improvável) que a(s) pessoa(s) que fez(fizeram)
todas essas requisições nocivas não tenham feito com o intuito de atacar a
plataforma, mas de fato o resultado foi prejudicial a todos os usuários. Seria
muito mais fácil e eficiente tecnicamente se a pessoa simplesmente baixasse o
*dataset* completo.

As características do ataque me levam a crer que tenha sido um DDoS
(*distributed denial of service*), pelo fato de serem muitas requisições de IPs
completamente diferentes e mirando apenas um *dataset*, com filtros muito
parecidos. Além disso, na mesma época em que sofremos esses ataques, o [Portal
da Transparência do Governo Federal][transparencia-gov-br] também recebeu
muitas requisições (tornando seu uso bastante lento) para o mesmo *dataset* e
cheguei a receber um email de alguém supostamente da Polícia Federal, exigindo
que eu retirasse do ar esses dados pois estavam sendo usados por criminosos (o
que não faz sentido, dado que os dados são públicos e temos total respeito com
a privacidade das pessoas descritas nesse *dataset*, não informando dados
sensíveis como CPF, mesmo que a fonte oficial divulgue essas informações).

Se você não sabe o que é um ataque DDoS, imagine uma pizzaria que recebe 50
pedidos por dia em média e, num determinado dia, passa a receber ligações de
diversas pessoas a partir de telefones que nunca antes ligaram, fazendo um
total de 500 pedidos, passando endereços falsos. Imagine o caos na cozinha
dessa pizzaria nesse dia e a quantidade de clientes fiés que não terão suas
pizzas em casa no tempo previso. Em outras palavras, num ataque de negação de
serviço o atacante estressa o sistema com requisições inválidas, para que o
sistema não consiga atender aos clientes reais. Vale notar que no caso do
Brasil.IO os "clientes" **não pagam** pelo serviço e os "cozinheiros" são
voluntários que doam seu tempo com o objetivo de disponibilizar dados
brasileiros mais acessíveis.


## Lições Aprendidas

- **Não podemos contar com o bom senso das pessoas para questões que podem
  impactar negativamente o projeto**: infelizmente, muitas vezes pessoas agem
  sem empatia e foi exatamente o que aconteceu nesse caso. Algumas
  (possivelmente poucas) pessoas abusaram da API e fizeram com que muitas
  outras pessoas fossem prejudicadas (nesse caso, desabilitamos a API para esse
  *dataset* e não prosseguimos com a atualização de dados que estava
  programada). Em casos como esses precisamos assumir uma **postura
  defensiva**.
- **Precisamos investir mais tempo em educar usuários**: tempo não investido em
  mostrar aos usuários da plataforma como utilizá-la da melhor forma é
  revertido em tempo gasto na mitigação dos problemas causados por isso e, com
  isso, teremos menos para evoluir a plataforma, adicionando funcionalidades e
  *datasets*. Nesse ponto, precisamos melhorar a documentação de uso e
  contribuição com a plataforma (esse caminho já está sendo trilhado).
- **Precisamos nos aproximar mais dos usuários**: fica evidente a necessidade
  de estarmos em contato mais próximo com quem utiliza nossos dados e a
  plataforma (esse foi um dos motivos de obrigatoriedade da API: assim
  conseguimos identificar cada um e, caso necessário, entrar em contato). Para
  ajudar a resolver isso, criamos um [canal no Telegram][brasil-io-telegram],
  reativamos nossa [conta no Twitter][brasil-io-twitter] e me comprometo a
  publicar relatórios mensais ([como o de setembro de
  2020][brasil-io-relatorio-set2020]).


## Como Você Pode Ajudar

Ainda temos muito trabalho a fazer e, se você quiser nos ajudar nesse jornada
de **tornar acessíveis os dados públicos brasileiros**, considere [doar em
nossa campanha de financiamento coletivo][brasil-io-apoiase] ou se unir às
[pessoas voluntárias do projeto COVID-19][brasil-io-covid19-voluntarios]
através do [nosso chat][brasil-io-chat].

[brasil-io-relatorio-set2020]: /2020/10/01/relatorio-mensal-setembro-de-2020/
[brasil-io-chat]: https://chat.brasil.io/
[brasil-io-covid19-voluntarios]: https://brasil.io/covid19/voluntarios/
[brasil-io-apoiase]: https://apoia.se/brasilio
[brasil-io-auxemerg]: https://brasil.io/dataset/govbr/auxilio_emergencial/
[brasil-io-como-acessar-dados]: /2020/10/10/como-acessar-os-dados-do-brasil-io/
[brasil-io-contato]: https://brasil.io/contato/
[brasil-io-covid19-voluntarias]: https://brasil.io/covid19/voluntarios/
[brasil-io-covid19]: https://brasil.io/dataset/covid19/
[brasil-io-python]: https://gist.github.com/turicas/3e3621d61415e3453cd03a1997f7473f#file-brasil_io-py
[brasil-io-telegram]: https://t.me/brasil_io
[brasil-io-twitter]: https://twitter.com/brasil_io
[brasil-io]: https://brasil.io/
[cdn]: https://pt.wikipedia.org/wiki/Rede_de_fornecimento_de_conte%C3%BAdo
[cloudflare]: https://www.cloudflare.com/
[issue-392]: https://github.com/turicas/brasil.io/issues/392
[issue-426]: https://github.com/turicas/brasil.io/issues/426
[issue-427]: https://github.com/turicas/brasil.io/issues/427
[issue-438]: https://github.com/turicas/brasil.io/issues/438
[issue-474]: https://github.com/turicas/brasil.io/issues/474
[issue-488]: https://github.com/turicas/brasil.io/issues/488
[palestra-fisl]: https://www.youtube.com/watch?v=EbbSx41BGRw
[pypi]: https://pypi.org/
[transparencia-gov-br]: http://transparencia.gov.br/
