from twilio.rest import Client 
 
account_sid = 'AC89b1eb91583825e6b13959af0a5a9e38' 
auth_token = '059c694b3515bcb3c588fee9005c7b99' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='test message',      
                              to='whatsapp:+919168533104'#6005747938' 
                          )
