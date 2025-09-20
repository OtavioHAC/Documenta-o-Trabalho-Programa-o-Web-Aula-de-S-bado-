from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

vagas = [
    {"id": 1, "titulo": "Estágio em TI", "empresa": "Bradesco", "cidade": "São Paulo", "salario": 1500, "descrição": "Suporte e Desenvolvimento."},
    {"id": 2, "titulo": "Estágio em Marketing", "empresa": "Agência Sense", "cidade": "Rio de Janeiro", "salario": 1200, "descrição": "Gestão de redes sociais."},
    {"id": 3, "titulo": "Estágio em Administrção", "empresa": "Unilever Brasil", "cidade": "São Paulo", "salario": 1350, "descrição": "Estágio na área administrativa."},
]

candidaturas = []

@app.route('/')
def home():
    return render_template('index.html', vagas=vagas)

@app.route('/vaga/<int:id>')
def vaga_detalhe(id):
    vaga = next((v for v in vagas if v["id"] == id), None)
    return render_template('vaga.html', vaga=vaga)

@app.route('/candidatar/<int:id>', methods=['POST'])
def candidatar(id):
    nome = request.form.get('nome')
    email = request.form.get('email')
    candidaturas.append({"vaga_id": id, "nome": nome, "email": email})
    return redirect(url_for('home'))

def index_html():
    return '''
    <html>
    <head><title>Portal de Vagas</title></head>
    <body>
        <h1>Vagas de Estágio</h1>
        <ul>
        {% for vaga in vagas %}
            <li>
                <a href="/vaga/{{ vaga.id }}">{{ vaga.titulo }}</a> - {{ vaga.cidade }} - R$ {{ vaga.salario }}
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''

def vaga_html():
    return '''
    <html>
    <head><title>{{ vaga.titulo }}</title></head>
    <body>
        <h1>{{ vaga.titulo }}</h1>
        <p><b>Empresa:</b> {{ vaga.empresa }}</p>
        <p><b>Cidade:</b> {{ vaga.cidade }}</p>
        <p><b>Salário:</b> R$ {{ vaga.salario }}</p>
        <p>{{ vaga.descricao }}</p>
        <form action="/candidatar/{{ vaga.id }}" method="post">
            <input type="text" name="nome" placeholder="Seu nome" required><br>
            <input type="email" name="email" placeholder="Seu email" required><br>
            <button type="submit">Candidatar-se</button>
        </form>
        <br><a href="/">Voltar</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
