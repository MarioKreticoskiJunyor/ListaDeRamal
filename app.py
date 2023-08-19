from flask import Flask, render_template, request
import pandas as pd
import unidecode  

app = Flask(__name__)

def carregar_dados_csv(arquivo):
    planilha = pd.read_csv(arquivo, sep=',')
    return planilha.to_dict(orient='records')

phone_data = carregar_dados_csv('dados.csv')

@app.route('/')
def index():
    return render_template('index.html', phone_data=phone_data)

@app.route('/buscar', methods=['POST'])
def buscar_contatos():
    query = unidecode.unidecode(request.form.get('searchInput').lower())  # Remova acentos da query
    
    filtered_data = []
    for entry in phone_data:
        if (
            unidecode.unidecode(entry['nome'].lower()).find(query) != -1 or
            str(entry['ramal']).lower() == query or  # Converta para string antes de aplicar lower()
            unidecode.unidecode(entry['setor'].lower()).find(query) != -1
        ):
            filtered_data.append(entry)
    
    return render_template('index.html', phone_data=filtered_data)

if __name__ == '__main__':
    app.run(host='192.168.100.2', port=5000, debug=True)