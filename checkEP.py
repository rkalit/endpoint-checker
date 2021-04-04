import requests
import datetime

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# ------- Function list ------- #
def sendAlert(text):
    api = 'https://slack.com/api/chat.postMessage'
    payload= {
        'token': 'xoxb-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxx', # your slack app token
        'channel': 'C0xxxxx', # your slack channel id
        'text': text
    }
    requests.post(api, data=payload)


def checkEndpoint():
    today = datetime.datetime.now()
    timeLog = today.strftime("%c")
    endpoint = 'http://your-endpoint.com/' # put your endpoint in here 
    status = requests.get(endpoint)
    if (status.status_code == 200):
        print(f"[{timeLog}] - {endpoint} is {bcolors.OKGREEN}UP{bcolors.ENDC}, status code is {status.status_code}")
    else:
        print(f"[{timeLog}] - {endpoint} is {bcolors.FAIL}DOWN{bcolors.ENDC}, status code is {status.status_code}")
        message = '*Mayday <!channel>, the endpoint {} is returning status code {}*'.format(endpoint, status.status_code)
        sendAlert(message)


# ------ End of Function list ------ #
