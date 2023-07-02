import smtplib, email. message
from backend.bootEmail.massege import corpo_email
from backend.credentials import password



def enviar_email(dest, parametros):
   
    msg_email = corpo_email(parametros)
    msg = email.message.Message()
    msg['Subject'] = msg_email[0]
    msg['From'] = 'grupoalcarroz@gmail.com'
    msg['To'] = 'superrecgt@gmail.com'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(msg_email[1])

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    
    return [200, "Email enviado com sucesso!"]
