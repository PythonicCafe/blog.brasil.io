Title: Resposta do Ministério da Saúde aos problemas nos microdados de vacinação
Slug: resposta-do-ministerio-da-saude-aos-problemas-nos-microdados-de-vacinacao
Date: 2021-07-15 15:30:00
Category: meta
Tags: datasets
Authors: turicas
Summary: Após diversos atrasos, o Ministério da Saúde respondeu ao nosso pedido de acesso à informação, na qual questionamos os problemas e inconsistências que encontramos nos microdados de vacinação. Veja resposta completa.

Após **perder o prazo de resposta** ao pedido de acesso à informação,
requisitar adiamento e perder o prazo do adiamento, o Ministério da Saúde
finalmente respondeu à nossa requisição, na qual questionamos os problemas dos
[microdados de vacinação disponíveis no OpenDataSUS][opendatasus-vacinacao].

Desde fevereiro acompanhamos essa base de dados, quando então iniciamos a
**publicação de uma versão "corrigida"** dela (com diversas limpezas e
modificações que facilitam a análise). Porém, ao fazer análises exploratórias
nos deparamos com **diversos problemas** (relatados no artigo [Os Problemas nos
Microdados de Vacinação][post-problemas]) e [criamos um **pedido de acesso à
informação** ao Ministério da Saúde][pedido-lai], questionando e solicitando
correções.

O pedido foi criado no dia **17 de maio de 2021** na plataforma
[FalaBr][falabr], mantida pela Controladoria Geral da União e só foi
**respondido no dia 12 de julho, quase 2 meses depois**, após a criação de um
recurso por conta do atraso. Apesar da utilização do FalaBr, o pedido
tramitou internamente pelo sistema OuvidorSUS, que mostra que apenas no dia 30
de junho (depois de já vencido o prazo do adiamento) o pedido foi encaminhado
ao departamento responsável (DATASUS):

![Tabela com as tramitações do pedido no sistema
OuvidorSUS](/images/2021-07-15-tramitacao-ouvidorsus.png)

*(por algum motivo estranho, TUDO NO OUVIDORSUS É ESCRITO EM MAIÚSCULAS)*

Confira as perguntas e respostas na íntegra:

**AJ: 1- Qual algoritmo de hashing foi utilizado para gerar a coluna `paciente_id`?**

> MS: POR QUESTÕES DE SEGURANÇA E SIGILO, VISANDO A PRIVACIDADE DOS DADOS DOS
> USUÁRIOS E CONSIDERANDO O QUE DISPÕE A LEI Nº 13.709, NÃO PODEMOS INFORMAR.

**AJ: 2- A coluna `paciente_id` é gerada pelos municípios, pelos Estados ou
pelo próprio Ministério?**

>> MS: É GERADA PELO MINISTÉRIO.

**AJ: 3- Quais dados do paciente são utilizados (como CPF, CNS etc.) para
compor o valor final de `paciente_id`?**

> MS: POR QUESTÕES DE SEGURANÇA E SIGILO, VISANDO A PRIVACIDADE DOS DADOS DOS
> USUÁRIOS E CONSIDERANDO O QUE DISPÕE A LEI Nº 13.709, NÃO PODEMOS INFORMAR.

**AJ: 4- Calculei a média de atraso de importação dos dados a partir da
diferença entre as colunas `data_importacao_rnds` e `data_aplicacao`. Existe um
atraso de importação médio nacional de 5.23 dias. A nível estadual, DF, RR, RJ
e MS possuem as maiores médias (mais de 10 dias). Quais são os prazos que os
municípios/Estados têm após a aplicação da dose para registrá-la no sistema
federal e para que o Ministério publique os dados após receber o registro
desses entes federativos?**

> MS: DE ACORDO COM O ART.2° § 1º E 2° DA PORTARIA GM/MS Nº 69, DE 14 DE
> JANEIRO DE 2021, QUE INSTITUI A OBRIGATORIEDADE DE REGISTRO DE APLICAÇÃO DE
> VACINAS CONTRA A COVID-19 NOS SISTEMAS DE INFORMAÇÃO DO MINISTÉRIO DA SAÚDE,
> O PRAZO DE REGISTRO É DE 48 HORAS APÓS A APLICAÇÃO DAS VACINAS.
>
> § 1º OS REGISTROS E A NOTIFICAÇÃO NOS SISTEMAS DO MINISTÉRIO DA SAÚDE DE QUE
> TRATAM OS INCISOS I, III, V E VI DO CAPUT DEVERÃO SER REALIZADOS DIARIAMENTE
> E DE FORMA INDIVIDUALIZADA, NOS TERMOS DO ART. 15 DA MEDIDA PROVISÓRIA Nº
> 1.026, DE 6 DE JANEIRO DE 2021.
>
> § 2º NA HIPÓTESE DE ALIMENTAÇÃO OFF-LINE, SERÁ RESPEITADO O PRAZO DE QUARENTA
> E OITO HORAS PARA REGISTRO E NOTIFICAÇÃO NOS SISTEMAS DO MINISTÉRIO DA SAÚDE.


**AJ: 5- Existem 467.985 `paciente_id` únicos que possuem 3 ou mais registros
(totalizando 1.492.626 registros), o que não deveria ocorrer pois as vacinas
são administradas no máximo em duas doses. O que explica esse erro? Pode ser
indício de fraude? O que o Ministério está fazendo para investigar o problema e
corrigi-lo?**

> MS: O DATASUS TEM INVESTIGADO OS CASOS E TEM ADOTADO AS SEGUINTES AÇÕES:
>
> - IMPLEMENTAÇÃO DE REGRAS PARA EVITAR ENTRADA DE REGISTROS DUPLICADOS NO
>   SI-PNI (IMPLEMENTAÇÃO REALIZADA EM 14/03/2021);
> - IMPLEMENTAÇÃO DE REGRAS PARA EVITAR ENTRADA DE REGISTROS DUPLICADOS POR
>   DIFERENTES SISTEMAS NA RNDS (IMPLEMENTAÇÃO REALIZADA EM 06/05/2021);
> - ESTRATÉGIA DE DEDUPLICAÇÃO NO DATALAKE DA RNDS (PACTUAÇÃO GT DE INFORMAÇÃO
>   E INFORMÁTICA DA CIT EM 02/07/2021 E PREVISÃO DE ENTRADA EM PRODUÇÃO EM
>   12/07/2021).
> - INVESTIGAÇÃO DE CASOS ANÔMALOS E NOTIFICAÇÃO DOS INTEGRADORES DA RNDS PARA
>   REALIZAR OPERAÇÃO DE EXCLUSÃO OU ALTERAÇÃO DE REGISTRO (PREVISÃO ATÉ
>   16/07/2021).
> - DISCUSSÃO DE NOVAS REGRAS DE ENTRADA DE REGISTROS, CONSIDERANDO DIFERENTES
>   ESQUEMAS DE VACINAÇÃO, ENTRE CGPNI E DATASUS.

**AJ: 6- Para todo o Brasil, existem 659.878 `paciente_id` que possuem apenas a
segunda dose registrada (no total, são 671.417 registros) e para o estado de MG
existem 174 registros com o valor para `vacina_descricao_dose` como "3ª Dose"
ou apenas "Dose". O que explica isso e quando será resolvido?**

> MS:
> - REGISTROS SOMENTE DE SEGUNDA DOSE SE REFEREM A AUSÊNCIA DE REGISTROS DA
>   PRIMEIRA DOSE, QUE PROVAVELMENTE OCORRE DEVIDO AO INADEQUADO PROCESSO DE
>   DIGITAÇÃO DOS COMPROVANTES DE PAPEL NOS SISTEMAS.
>
> - REGISTROS COM VACINA_DESCRICAO_DOSE COMO "3ª DOSE" SÃO INTERPRETADOS COMO
>   ERRO E DEVEM SER CORRIGIDOS PELOS SISTEMAS DE ORIGEM.
>
> - REGISTROS COM VACINA_DESCRICAO_DOSE COMO "DOSE" SÃO INTERPRETADOS COMO
>   CORRETO, POIS SE REFEREM A DESCRIÇÃO DA APLICAÇÃO DA VACINA CÓDIGO 88 -
>   VACINA COVID-19 - AD26.COV2.S - JANSSEN-CILAG.
>
> - O DATASUS ESTÁ AGUARDANDO ORIENTAÇÃO DA CGPNI PARA A UTILIZAÇÃO DO CÓDIGO
>   CORRETO (CÓDIGOS 8 - DESCRIÇÃO DOSE, PARA VACINA JANSSEN) E CORREÇÃO DOS
>   OUTROS CAMPOS, COM PREVISÃO DE PUBLICAÇÃO EM 09/07/2021.

**AJ: 7- As colunas `vacina_codigo`, `vacina_nome`, `vacina_fabricante_nome` e
`vacina_fabricante_referencia` possuem valores conflitantes, como códigos
diferentes para a mesma vacina e nomenclatura diferente para mesmos
fabricantes. No total, essas 4 colunas geram uma combinação de 199 valores
distintos, enquanto o esperado seria bem menos (no máximo, o total de vacinas
vezes o total de fabricantes). O que justifica essa inconsistência? Qual é o
prazo previsto para normalização desses valores?**

> MS: A NOMENCLATURA DE VACINAS DEVE SEGUIR O DOMÍNIO OU CODE SYSTEM (CS)
> DISPONÍVEL EM:  HTTP://WWW.SAUDE.GOV.BR/FHIR/R4/CODESYSTEM/BRIMUNOBIOLOGICO.
>
> A NOMENCLATURA VARIANTE PARA FABRICANTES SE DEVE AO FATO DO CAMPO ESTAR EM
> TEXTO FORMATO LIVRE. A IMPLEMENTAÇÃO DO DOMÍNIO É DE FABRICANTES ESTÁ
> PREVISTA PARA PRÓXIMA VERSÃO DO MODELO DE INFORMAÇÃO RIA-C - REGISTRO DE
> IMUNOBIOLÓGICO ADMINISTRADO.
>
> APÓS IMPLEMENTAÇÃO DO DOMÍNIO DE FABRICANTES E PUBLICAÇÃO DA NOVA VERSÃO DO
> MODELO, OS INTEGRADORES TERÃO UM PRAZO DE 60 DIAS PARA ADEQUAÇÃO DE SEUS
> SISTEMAS.
>
> INCONSISTÊNCIA RELACIONADA À IDADE E AO GRUPO PRIORITÁRIO DEVE-SE A ERRO DE
> DIGITAÇÃO E DEVE SER RETIFICADO PELO SISTEMA DE ORIGEM.

**AJ: 8- Existem 170.129 registros de doses aplicadas em indivíduos
classificados como grupo prioritário "Faixa Etária" na coluna
`vacina_categoria_nome`, mas que referem-se a pessoas com menos de 60 anos
(pela coluna `paciente_idade`) e que, portanto, não fariam parte do citado
grupo prioritário (idosos). Como o Ministério garante que não há desvio de
doses para indivíduos que não são do grupo prioritário?**

> MS: TODOS OS REGISTROS DE VACINAÇÃO CONTRA COVID-19 SÃO IDENTIFICADOS PELO
> CPF/CNS DO CIDADÃO E APRESENTADOS NAS BASES DE DISSEMINAÇÃO DE FORMA
> DESIDENTIFICADA E NO APLICATIVO CONECTE SUS, O QUE PERMITE O CONTROLE SOCIAL
> EFETIVO. O PLANO NACIONAL DE OPERACIONALIZAÇÃO DA VACINAÇÃO CONTRA A COVID-19
> ORIENTA A VACINAÇÃO EM GRUPOS ESPECÍFICOS, ENTRETANTO OS ESTADOS E MUNICÍPIOS
> SÃO AUTÔNOMOS PARA DEFINIREM A ORDEM E GRUPOS DE ATENDIMENTOS DE ACORDO COM A
> SITUAÇÃO EPIDEMIOLÓGICA LOCAL.
>
> ACESSO CONCEDIDO COM RESTRIÇÕES DE SIGILO.


[analise-sql]: https://github.com/turicas/covid19-br/tree/master/analises/microdados-vacinacao
[opendatasus-vacinacao]: https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao
[pedido-lai]: https://github.com/turicas/covid19-br/blob/master/analises/microdados-vacinacao/README.md#pedido-de-acesso-%C3%A0-informa%C3%A7%C3%A3o
[post-problemas]: /2021/05/24/os-problemas-nos-microdados-de-vacinacao/
[falabr]: https://falabr.cgu.gov.br/
