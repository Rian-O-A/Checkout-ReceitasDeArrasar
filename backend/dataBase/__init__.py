import firebase_admin
from firebase_admin import credentials, firestore
from backend.credentials import credDataBase

firebase_admin.initialize_app(credentials.Certificate(credDataBase))

db = firestore.client()

