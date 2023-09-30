from flask import Blueprint, request
from backend.credentials import token
from backend.bootEmail.sendEmail import enviar_email
import stripe
import json


stripe.api_key = token

auth_route = Blueprint('auth', __name__)


@auth_route.route("/webhook", methods=['POST'])
def webhook():
    payload = request.get_json()
    if payload['type'] == 'payment_intent.succeeded':
        try:
                
                charge = stripe.Charge.retrieve(payload['data']['object']['latest_charge'])
                enviar_email(charge["billing_details"]["email"])
                
                

        except stripe.error.StripeError as e:
                print("Erro ao consultar a cobrança:", str(e))
            

    return "OK", 200