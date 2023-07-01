from backend.Payment import sdk

def process_payment(request_values):
    payment_data = {
            "transaction_amount": float(request_values["transaction_amount"]),
            "token": request_values["token"],
            "installments": int(request_values["installments"]),
            "payment_method_id": request_values["payment_method_id"],
            "issuer_id": request_values["issuer_id"],
            "payer": {
                "email": request_values["payer"]["email"],
                "identification": {
                    "type": request_values["payer"]["identification"]["type"], 
                    "number": request_values["payer"]["identification"]["number"]
                }
            }
        }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    # print("status =>", payment["status"])
    # print("status_detail =>", payment["status_detail"])
    # print("id=>", payment["id"])

    return payment