# Blog do Brasil.IO

Esse repositório contém o código e as publicações do [Blog do
Brasil.IO](https://blog.brasil.io/).

## Contribuindo

Caso você não tenha conhecimentos de git, GitHub e markdown mas tenha interesse
em publicar algum texto no blog envie um email através [da página de
contato](https://brasil.io/contato) falando sobre o texto que gostaria de
publicar e conversamos. :) Caso você se sinta confortável utilizando essas
tecnologias, leia mais:

O blog é um [site estático usando o
pelican](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/); crie
um pull request com o conteúdo do texto em um arquivo na pasta `content/` - o
arquivo pode estar em markdown ou no formato do [Jupyter
Notebook](https://jupyter.org/) (ipynb). Por padrão o arquivo deve conter o
formato: `content/YYYY-MM-DD-titulo-do-text.md`; no caso da utilização do
Jupyter Notebook, use a extensão `.ipynb` e crie também um arquivo
`content/YYYY-MM-DD-titulo-do-text.nbdata` com o seguinte formato:

```
Title: Escreva aqui o título do arquivo
Slug: slug (utilize o mesmo do nome do arquivo, sem extensão)
Date: YYYY-MM-DD HH:MM
Category: categoria1, categoria2
Tags: tag1, tag2
Author: username_no_github
Summary: Primeiro parágrafo do texto ou resumo
```

### Adicionar novo Autor(a)

Para que o autor apareça com imagem e descrição ao final de cada postagem é preciso
adicionar os arquivos ao blog seguindo os passos descritos a seguir

1. Adicione a sua imagem na pasta `content/images/authors/` a imagem deve conter o mesmo nome de seu usuário no github e conter a extensão `.jpg`.

2. Crie um novo arquivo na pasta `content/authors/`, o arquivo deve ter extensão .json e precisa ter os seguintes campos preenchidos:

```
{
    "name": "Seu nome",
    "image": "/images/authors/username_no_github.jpg",
    "description":"breve descrição",
    "social": {
        "github": "https://github.com/username_no_github",
        "twitter": "https://twitter.com/username_no_twitter",
        "linkedin": "https://br.linkedin.com/in/username_no_linkedin"
    }
}
```

### Rodando Localmente

Necessita de Python 3.7+. Instale as dependências:

```bash
pip install -r requirements.txt
```

Gere o site executando:

```bash
pelican content/
```

Para rodar um servidor Web, execute:

```bash
cd output && python -m pelican.server
```

Então basta acessar [localhost:8000](http://localhost:8000) em seu navegador.

### Publicando

```bash
make github  # Irá gerar novamente o site e subir para o branch gh-pages
```

### Outras Maneiras de Contribuir

Se você curte o projeto e quer contribuir de outras formas também, [veja
como](https://brasil.io/colabore).

## Licença

Todas as publicações estão disponíveis sob a licença [Creative Commons
Attribution-ShareAlike (CC
BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/).
