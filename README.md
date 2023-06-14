# Análise de empresas por análise de sentimentos
Trabalho para a disciplina de Inteligência Artificial

## ToDo

- [ ] Criar rotas
- [ ] Configurar scraper para twitter ([snscrape](https://github.com/JustAnotherArchivist/snscrape))
- [ ] Buscar informações sobre empresa buscada 
- [ ] Mostrar ao usuário em formas gráficas

## Instalação

Versão do Python: 3.10

Clone o repositório:
```bash
git clone https://github.com/pabloghid/company_analysis.git
```

Crie um ambiente virtual. Ex:
```bash
python -m venv venv
```
Ative o ambiente virtual.
No Windows:
```bash
venv\Scripts\activate
```
No Linux/macOS:
```bash
source venv/bin/activate
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Para inicializar o projeto com o debug ligado, para desenvolvimento, utilize o comando abaixo ou execute o arquivo run.py.
```bash
flask --app company_analysis run --debug
```