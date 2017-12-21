from twilio.rest import Client

def send_msg(to_person, from_person, msg_body):
    # Your Account SID from twilio.com/console
    account_sid = "AC842e47b850f8b630c1ca262a016bb00a"
    # Your Auth Token from twilio.com/console
    auth_token = "0774b918cb629ea7282d4473d6eddd7a"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to_person,
        from_=from_person,
        body=msg_body)

    return message.sid

MSG_BODY = '''Hey, Bobby See this cool sms python module.
             It's Marvin you asshole. BTW Don't Reply except you want spend N20 for an sms'''

send_msg("+2348138538619", "+14843948124", MSG_BODY)
