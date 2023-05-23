from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien', 
        
    },
    
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling', 
        
    },
    
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Ábitos Atômicos', 
        
    },
]

# Consultar(todos)

@app.route('/livros')

def obter_livros():
    return jsonify(livros)
    
    
# Consultar(id)    
# Editar    
# Excluir

app.run(port=5000,host='localhost',debug=True)
