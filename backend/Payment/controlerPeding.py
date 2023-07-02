import requests
from backend.credentials import token
from backend.bootEmail.sendEmail import enviar_email
from backend.dataBase.manager import bankDate

approvedPayment = list()

def statusPayment(id_pagamento):
    url = f"https://api.mercadopago.com/v1/payments/{id_pagamento}?access_token={token}"
    
    response = requests.get(url).json()
    
    
    if 'approved' == response['status']:
        enviar_email(response["payer"]["email"], None)
        return response['status']
    
    elif 'pending' == response['status']:
        
            if response['payment_method_id'] == 'bolbradesco':
                enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
                
                
          
            elif response['payment_method_id'] == 'pec':
                enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['transaction_details']['external_resource_url']})
                
                
            elif response['payment_method_id'] == 'pix':
                
                enviar_email(dest=response['payer']['email'], parametros={"id":id_pagamento, "url": response['point_of_interaction']['transaction_data']['ticket_url']})
                
                
            return response['status']

    
def managerPayments():
    paymentsPendings = bankDate.toReceive()
    print(paymentsPendings)
    for payment in paymentsPendings:
        print(type(payment))
        status = statusPayment(int(payment))
        if status == 'pending':
            bankDate.updateField({"id": payment, "pedingDays": paymentsPendings[payment]["pedingDays"]+1})
            
            

