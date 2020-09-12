
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Details
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/covid-register'
}

initialize_db(app)


@app.route('/details')
def get_details():
    details = Details.objects().to_json()
    return Response(details, mimetype="application/json", status=200)


@app.route('/details', methods=['POST'])
def add_detail():
    body = request.get_json()
    detail = Details(**body).save()
    id = detail.id
    return {'id': str(id)}, 200


@app.route('/details/<id>', methods=['PUT'])
def update_detail(id):
    body = request.get_json()
    Details.objects.get(id=id).update(**body)
    return '', 200


@app.route('/details/<id>', methods=['DELETE'])
def delete_detail(id):
    detail = Details.objects.get(id=id).delete()
    return '', 200


@app.route('/details/<id>')
def get_detail(id):
    details = Details.objects.get(id=id).to_json()
    return Response(details, mimetype="application/json", status=200)


app.run()
