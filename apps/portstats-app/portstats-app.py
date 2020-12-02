import flask
import requests
import os
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#ONOS_IP = os.getenv("ONOS_IP", "127.0.0.1")
ONOS_IP = os.getenv("ONOS_IP", "172.17.0.5")
ONOS_PORT = int(os.getenv("ONOS_PORT", 8181))
PORT_STATS_URL = "http://" + ONOS_IP + ":" + str(ONOS_PORT) +"/onos/v1/statistics/ports"


@app.route('/', methods=['GET'])
def home():

    username = "karaf"
    password = "karaf"
    req_ses = requests.Session()
    req_ses.auth = (username,password)

    res_ses = req_ses.get(PORT_STATS_URL)


    if res_ses.status_code != 200:
        print("FAILED")
    else: 
        return res_ses.json()


app.run(host='0.0.0.0')
