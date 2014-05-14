from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
account_sid = "AC120f7d09bcdc0353956393d2d1904c2e"
auth_token = "81382ffade7eda8b73e94a7cc5e5ee39"

client = TwilioRestClient(account_sid, auth_token)
call = client.calls.create(
from_="+12392045487",
to="+919036291587",
url='http://twimlets.com/echo?Twiml=%3CResponse%3E%3CSay%3EHouse+on+fire+House+on+fire%3C%2FSay%3E%3C%2FResponse%3E')
print call.sid
