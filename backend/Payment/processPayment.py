from backend.Payment import sdk
import json

def process_payment(request_values):
    request_values["formData"]['transaction_amount'] = 1
    request_values["formData"]['description'] = request_values['formData']['payer']["email"]
    payment_data = request_values['formData']
    
    payment_response = sdk.payment().create(payment_data)
 
    # json.dump(payment_response, open('payment.json', 'w', encoding="UTF-8"), indent=6, ensure_ascii=False)
   
    return payment_response["response"]