# Análise de empresas por análise de sentimentos
Trabalho para a disciplina de Inteligência Artificial

## ToDo

- [x] Criar rotas
- [x] Configurar scraper para twitter ([snscrape](https://github.com/JustAnotherArchivist/snscrape))
- [x] Analisar informações sobre empresa buscada 
- [x] Mostrar ao usuário em formas gráficas

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

É necessário fazer alterações na biblioteca google_trans_new para que funcione corretamente. Para isso, no arquivo google_trans_new/google_trans_new.py, na linha 151 e 233, troque 
```bash
response = (decoded_line + ']')
```
para
```bash
response = (decoded_line)
```

Para inicializar o projeto com o debug ligado, para desenvolvimento, utilize o comando abaixo ou execute o arquivo run.py.
```bash
flask --app company_analysis run --debug
```