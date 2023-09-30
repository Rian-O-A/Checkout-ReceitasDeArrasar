from flask import Blueprint, request
from backend.credentials import token
import stripe
import json



stripe.api_key = token
# Consultar a cobrança na Stripe
charge = stripe.Charge.retrieve("ch_3NvqZ6FiGNH9KgND1r9vFEXx")

# Acessar o endereço de e-mail do cliente

print("Endereço de e-mail do cliente:", charge)
