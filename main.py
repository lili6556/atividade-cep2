from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    print(request.form)
    payload = request.form
    print(payload.get('cep'))
    
    # Fazendo uma requisição POST para o serviço
    res = req.post('http://127.0.0.1:8000', json={'cep': payload.get('cep')})
    print(res.text)
    
    # Fazendo uma requisição GET para o serviço
    res2 = req.get('http://127.0.0.1:8000')
    print(res2.text)    
    
    return render_template('index.html', res=res.text, res2=res2.text)

app.run(debug=True, port=7000)
