from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from flask_cors import CORS
import re
from execptions import InvalidEmail, Missingfield

app = Flask(__name__)
CORS(app)

username = 'postgres'
password = quote_plus('lilY@')
host = 'localhost'
port = '5432'
database = 'leadsdb'


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    proposta = db.Column(db.String(200), nullable=False)

    def to_json(self):
        return {'id': self.id, 'nome':self.nome, 'email':self.email, 'proposta':self.proposta}

with app.app_context():
    db.create_all()


# POST
@app.route('/api', methods=['POST'])
def add_person():

    try:
        data = request.get_json()

        if not data.get('nome') or not data.get('email') or not data.get('proposta'):
            raise Missingfield('Todos os campos precisam ser preenchidos')

        if not is_valid_email(data['email']):
            raise InvalidEmail("Endereço de email invalido")

        new_person = Person(nome=data['nome'], email=data['email'], proposta=data['proposta'])
        db.session.add(new_person)
        db.session.commit()
        return jsonify(new_person.to_json()), 201

    except Missingfield as e:
        return jsonify({'error': str(e)}), 400

    except InvalidEmail as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500


# GET
@app.route('/api', methods=['GET'])
def read_all():
    people = Person.query.all()
    return jsonify([pessoa.to_json() for pessoa in people])


@app.route('/api/<int:id>', methods = ['GET'])
def read_by_id(id):
    person = Person.query.get(id)
    if person:
        return jsonify(person.to_json())
    return jsonify({'error': 'Não encontrado no banco de dados'}), 404

# DELETE
@app.route('/api/<int:id>', methods= ['DELETE'])
def delete(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'error': 'Não encontrado no banco de dados'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Exclusao realizada com sucesso'})

@app.route('/home')
def hello():
    return 'Hello World'

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=True)