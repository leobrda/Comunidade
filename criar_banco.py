from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario

with app.app_context():
    database.drop_all()
    database.create_all()
