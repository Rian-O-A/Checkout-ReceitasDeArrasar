import requests
from backend.credentials import token
from backend.bootEmail.sendEmail import enviar_email

def statusPayment(id_pagamento, action):
    url = f"https://api.mercadopago.com/v1/payments/{id_pagamento}?access_token={token}"
    
    response = requests.get(url).json()
    
    if action != 'payment.created':
        if 'approved' == response['status']:
            if response["payment_method_id"] == "pix":
                enviar_email(response["description"], None)
            else:   
                enviar_email(response["payer"]["email"], None)
          
        
        elif 'pending' == response['status']:
            
                if response['payment_method_id'] == 'bolbradesco':
                    enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
                    
                    
            
                elif response['payment_method_id'] == 'pec':
                    enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
                    
                    
                elif response['payment_method_id'] == 'pix':
                    enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['point_of_interaction']['transaction_data']['ticket_url']})
                    
            

    
            
            

