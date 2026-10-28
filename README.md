# Lista de Ramais

Aplicação web para consultar ramais telefônicos de uma organização por nome,
setor ou número do ramal.

Os contatos de `dados.csv` são **fictícios**.

## Funcionalidades

- Lista todos os contatos do arquivo CSV na página inicial
- Busca por nome ou setor, sem diferenciar maiúsculas, minúsculas e acentos
- Busca pelo número exato do ramal

## Tecnologias

- Python
- Flask
- pandas (leitura do CSV)
- unidecode (busca sem acentos)
- HTML e CSS

## Estrutura

```text
app.py              # aplicação Flask: carrega o CSV e define as rotas
dados.csv           # contatos (nome, ramal, setor)
templates/index.html
static/             # styles.css e logo.png
```

## Como executar

```bash
python -m venv venv
venv\Scripts\activate          # Windows  ·  Linux/macOS: source venv/bin/activate
pip install flask pandas unidecode
flask --app app run
```

Acesse `http://127.0.0.1:5000/`.

> Executar com `python app.py` usa o endereço de rede fixado no código, que só
> existe na máquina onde o projeto foi criado. Por isso a forma recomendada é
> `flask --app app run`. Execute o comando dentro da pasta do projeto, porque o
> `dados.csv` é lido por caminho relativo.

## Testes

O projeto não possui testes automatizados.

## Estado atual

Funcional para consulta. Os dados são carregados uma vez, quando a aplicação inicia.

## Melhorias planejadas

*Ainda não implementadas:*

- Adicionar `requirements.txt`
- Ler host, porta e modo debug de variáveis de ambiente
- Cadastrar e editar contatos pela interface
- Testes das rotas de busca
