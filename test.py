'''        else:
            give_output("dont know this one should i search on internet?")
            ans = take_input()
            if "yes" in ans:
                answer = check_on_wikipedia(quest)
                if answer!="":
                    return answer    
            elif "no" == ans:
                answer='okay'
                return answer
            else:        
                give_output('i dont know this one, can you tell me what it mean')
                ans = take_input()
                if "it means" in ans:
                    ans = ans.replace("it means","")
                    ans.strip()

                    value = database.get_answers_from_memory(ans)
                    if value=="":
                        return("can't help with this one")
                    else:
                        database.insert_question_and_answer(quest,value)
                        return "thanks i will remember it for the next time"
                else:
                    return ("can't help with this")

                return('nothing to return')


said = 'my name is bravo'.replace('name',"")

site = said[0:said.index(" ")].strip()
query = said[said.index(" ")+1:].strip()
print(site)
print(query)'''

# importing the module 
import pywhatkit 
import wikipedia
import os
from datetime import datetime,date
os.system('cls')

'''
now = datetime.now()

hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
print (hour)

print (minute+1)
rec = '6268 811 789'
cont="automatically generated msg h bro chill kr"
# using Exception Handling to avoid 
# unprecedented errors 
try: 
	
    # sending message to reciever 
    # using pywhatkit 
    pywhatkit.sendwhatmsg(f"+91{rec}", f"{cont}", hour, minute+1) 
    print("Successfully Sent!") 

except: 
	
    # handling exception 
    # and printing error message 
    print("An Unexpected Error!")'''
'''
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("friday959822@gmail.com", "9598221049") 
  
# message to be sent 
message = "automatically generated msg from B.R.A.V.OY"
  
# sending the mail 
s.sendmail("friday959822@gmail.com", "kp959822@gmail.com", message) 
  
# terminating the session 
s.quit() 
'''
import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('friday959822@gmail.com', '9822104900')
    server.sendmail('friday959822@gmail.com', to, content)
    server.close()


content = "automatic mail generated by B.R.A.V.O"
to = "kp959822@gmail.com"    
sendEmail(to, content)
print("Email has been sent!")







