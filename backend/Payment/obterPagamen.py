import requests
from backend.credentials import token
from backend.bootEmail.sendEmail import enviar_email

def pesquisar_pagamento(id_pagamento):
    url = f"https://api.mercadopago.com/v1/payments/{id_pagamento}?access_token={token}"
    
    response = requests.get(url).json()
    
    if 'message' in response and 'cause' in response:
        return [response['status'], response['message']]
    elif 'approved' == response['status']:
        enviar_email(response["payer"]["email"], None)
        return [200, response["payer"]["email"]]
    elif 'pending' == response['status']:
        
        if response['payment_method_id'] == 'bolbradesco':
            enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
            return [202, {'status':response['status'], 'barcode': response['barcode']['content'], "url": response['transaction_details']['external_resource_url']}]
          
        elif response['payment_method_id'] == 'pec':
            enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
            return [202, {'status':response['status'], "url": response['transaction_details']['external_resource_url']}]
            
        elif response['payment_method_id'] == 'pix':
            
            enviar_email(dest=response['description'], parametros={"id":id_pagamento, "url": response['point_of_interaction']['transaction_data']['ticket_url']})
            return [202, {'status':response['status'], 'url': response['point_of_interaction']['transaction_data']['ticket_url']}]

    


