from flask import Blueprint, jsonify, request, render_template
from backend.Payment.obterPagamen import pesquisar_pagamento
from backend.Payment.processPayment import process_payment 
from backend.bootEmail.sendEmail import enviar_email
from backend.credentials import public_key
import json


auth_route = Blueprint('auth', __name__)


@auth_route.route('/')
def home():
   return render_template('index.html', public_key=public_key)

@auth_route.route('/product', methods=['POST'])
def sendProduct():
    idPayment = request.json.get("idPayment")
    response = pesquisar_pagamento(idPayment)
    return jsonify({'Message': response[1]}), response[0]

@auth_route.route('/process_payment', methods=['POST'])
def add_income():
    request_values = request.get_json()
    payment = process_payment(request_values)
    response = pesquisar_pagamento(payment["id"])
    return jsonify(payment), response[0]