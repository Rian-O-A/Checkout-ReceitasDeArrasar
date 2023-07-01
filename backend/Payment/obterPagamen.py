import requests
from backend.credentials import token

def pesquisar_pagamento(id_pagamento):
    url = f"https://api.mercadopago.com/v1/payments/{id_pagamento}?access_token={token}"
    
    response = requests.get(url).json()
    
    if 'message' in response and 'cause' in response:
        return [response['status'], response['message']]
    elif 'approved' == response['status']:
        return [200, response["payer"]["email"]]




