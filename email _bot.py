from email import message
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener=sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()




def get_info():
    try:
         with sr.Microphone() as source:
          print("listening...")
         voice=listener.listen(source)
         info = listener.recognize_google(voice)
         print(info)
         return info.lower()
    except:
          pass

def send_email(receiver,subject):

   server =smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login('akritimenon123@gmail.com','Akriti@1111')
   email=EmailMessage()
   email['from']='akritimenon123@gmail.com'
   email['to']=receiver
   email['subject'] = subject
   email.set_content(message)
   server.send_message(email)

#    server.sendmail('akritimenon123@gmail.com','snehakumars2000@gmail.com','hi')

email_list = {
       'dude':'snehakumars2000@gmail.com'
   }

def get_email_info():
    talk('to whom u want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("subject of ur wmail")
    subject = get_info()
    talk('tell me the text')
    message = get_info()


    send_email(receiver,subject)
    

    get_email_info()
