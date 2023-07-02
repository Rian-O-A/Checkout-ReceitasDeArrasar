from backend.Payment import sdk
import json

def process_payment(request_values):
    json.dump(request_values, open('teste.json', 'w', encoding="UTF-8"), indent=6, ensure_ascii=False)
    if request_values["formData"]["payment_method_id"] == 'pix':
        payment_data = {
            "transaction_amount": request_values["formData"]["transaction_amount"],
            "description": "Receitas para arrasar",
            "payment_method_id": "pix",
            "payer": {
                "email": request_values["formData"]["payer"]["email"]
                }
            }
    else:
        payment_data = {
                "transaction_amount": float(request_values["formData"]["transaction_amount"]),
                "token": request_values["formData"]["token"],
                "installments": int(request_values["formData"]["installments"]),
                "payment_method_id": request_values["formData"]["payment_method_id"],
                "issuer_id": request_values["formData"]["issuer_id"],
                "payer": {
                    "email": request_values["formData"]["payer"]["email"],
                    "identification": {
                        "type": request_values["formData"]["payer"]["identification"]["type"], 
                        "number": request_values["formData"]["payer"]["identification"]["number"]
                    }
                }
            }
    

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    # print("status =>", payment["status"])
    # print("status_detail =>", payment["status_detail"])
    # print("id=>", payment["id"])

    return payment