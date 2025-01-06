import flask
import requests
import os
import json


from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

app = flask.Flask(__name__)
app.config["DEBUG"] = False

ONOS_IP = os.getenv("ONOS_IP", "172.17.0.2")
ONOS_PORT = int(os.getenv("ONOS_PORT", 8181))
PORT_STATS_URL = "http://" + ONOS_IP + ":" + str(ONOS_PORT) +"/onos/v1/statistics/ports"
USERNAME = "karaf"
PASSWORD = "karaf"

DEVICE_PORTS_DICT = {"of:0000000000000001": [1,5],
                    "of:0000000000000005": [1,4],
                    "of:0000000000000003": [5,4]}

def get_port_stats(device_id=None):
    req_ses = requests.Session()
    req_ses.auth = (USERNAME,PASSWORD)

    res_ses = req_ses.get(PORT_STATS_URL)
    if device_id is not None:
        res_ses = req_ses.get(PORT_STATS_URL + "/" + device_id)

    if res_ses.status_code != 200:
        print("FAILED")
    else:
        return res_ses.json()

@app.route('/', methods=['GET'])
def home():
    return get_port_stats()

class prometheusCollector():

    def collect(self):

        self.metric = {
        'packetsReceived': GaugeMetricFamily('onos_device_packets_received','packets received per seconds', labels=["node","port"]),
        'packetsSent': GaugeMetricFamily('onos_device_packets_sent','packets sent per seconds', labels=["node","port"]),
        'bytesReceived': GaugeMetricFamily('onos_device_bytes_received','bytes received per seconds', labels=["node","port"]),
        'bytesSent': GaugeMetricFamily('onos_device_bytes_sent','bytes sends per seconds', labels=["node","port"]),
        }
        
        for device_iter, ports_list_iter in DEVICE_PORTS_DICT.items():
            port_stats_data = get_port_stats(device_id=device_iter)["statistics"][0]
            for port_number_iter in ports_list_iter:
                self.metric['packetsReceived'].add_metric([device_iter,str(port_number_iter)], port_stats_data["ports"][port_number_iter-1]["packetsReceived"])
                self.metric['packetsSent'].add_metric([device_iter,str(port_number_iter)], port_stats_data["ports"][port_number_iter-1]["packetsSent"])
                self.metric['bytesReceived'].add_metric([device_iter,str(port_number_iter)], port_stats_data["ports"][port_number_iter-1]["bytesReceived"])
                self.metric['bytesSent'].add_metric([device_iter,str(port_number_iter)], port_stats_data["ports"][port_number_iter-1]["bytesSent"])

        for metric in self.metric.values():
            yield metric

if __name__ == "__main__":
    REGISTRY.register(prometheusCollector())
    start_http_server(5001)
    app.run(host='0.0.0.0')

