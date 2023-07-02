# Endpoint Checker
This simple program/container is used to check the status of a docker container, whether it is up or down, and send a notification/alert to slack if the checked endpoint is down.
## Usage
---
To use this, simply run `./dStart.sh` where it is basically build and run the container.
### CheckEP.py
---
In this piece of code, you can se on the `sendAlert` function, you need to input your slack's token as well as the channel id.
```
payload= {
        'token': 'xoxb-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxx', # your slack app token
        'channel': 'C0xxxxx', # your slack channel id
        'text': text
    }
```
