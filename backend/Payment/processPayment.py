from backend.Payment import sdk
import json

def process_payment(request_values):
    payment_data = request_values['formData']
    payment_response = sdk.payment().create(payment_data)
 

   
    return payment_response["response"]