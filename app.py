from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


def carregar_dados_csv(arquivo):
    planilha = pd.read_csv(arquivo, sep=',')
    return planilha.to_dict(orient='records')


phone_data = carregar_dados_csv('dados.csv')

@app.route('/')
def index():
    return render_template('index.html', phone_data=phone_data)

if __name__ == '__main__':
    app.run(host='192.168.100.2', port=5000, debug=True)
    


