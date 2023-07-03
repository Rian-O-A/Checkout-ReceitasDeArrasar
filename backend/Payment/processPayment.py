from backend.Payment import sdk

def process_payment(request_values):
    
    if request_values["formData"]["payment_method_id"] == 'pix':
        request_values["formData"]['description'] = request_values['formData']['payer']["email"]
    
    
    payment_data = request_values['formData']    
    payment_response = sdk.payment().create(payment_data)
    return payment_response["response"]