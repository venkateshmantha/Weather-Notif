import requests,json
from twilio.rest import Client

## Wunderground credentials
zipcode = "<Enter you zipcode here>"
key = "<Your Wunderground key>"
url = "http://api.wunderground.com/api/" + key + "/conditions/q/" + zipcode + ".json"

## Twilio credentials
account = "<Your Twilio account credentials>"
token = "<Your token number>"

result = requests.get(url)
parsed_json = json.loads(result.text)
location = parsed_json['current_observation']['display_location']['city']
temp_f = parsed_json['current_observation']['temp_f']
weather = parsed_json['current_observation']['weather']
msg = "Current temperature in " + location + " is " + str(temp_f) + " and the weather is " + weather + "."

## Create twilio client object
client = Client(account, token)
message = client.messages.create(to="<To>", from_="<From>",
                                 body=msg)

result.close()
