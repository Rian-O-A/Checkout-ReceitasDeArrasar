import requests
from backend.credentials import token
from backend.bootEmail.sendEmail import enviar_email

def pesquisar_pagamento(id_pagamento):
    url = f"https://api.mercadopago.com/v1/payments/{id_pagamento}?access_token={token}"
    
    response = requests.get(url).json()
    
    if 'message' in response and 'cause' in response:
        return [response['status'], response['message']]
    elif 'approved' == response['status']:
        return [200, response["payer"]["email"]]
    elif 'pending' == response['status']:
        enviar_email(dest=None, parametros={"id":id_pagamento, "url": response['point_of_interaction']['transaction_data']['ticket_url']})
        return [202, {'status':response['status'], 'url': response['point_of_interaction']['transaction_data']['ticket_url']}]




