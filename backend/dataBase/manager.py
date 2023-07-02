from backend.dataBase import db


class bankDate:
    
    
    def send(parameters):
        dados = {
            "payment_method_id": parameters['payment_method_id'],
            "pendingDays": parameters['pendingDays']
        }

        db.collection('pending').document(parameters["id"]).set(dados)
        
        
    def toReceive():
        pedingPaymentDatabase = db.collection('peding').get()
        pedingPayment = dict()
        for doc in pedingPaymentDatabase:
            pedingPayment[doc.id] = doc.to_dict()
            
        return pedingPayment
    
    def updateField(parameters):
        db.collection(f'pending').document(parameters["id"]).update({'pedingDays': parameters["pedingDays"]})
        
            
    
    