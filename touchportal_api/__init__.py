import array
import json

from pyee import BaseEventEmitter
from simple_socket.tcp_client import SimpleTCPClient


class Client(BaseEventEmitter):
    def __init__(self, pluginId: str):
        """
        Initilize Touch Portal Client
        :type pluginId: str
        :rtype: None
        """
        super().__init__()
        self.pluginId = pluginId
        self.client = None
        self.customStates = {}

    def sendArray(self, dataArray: array) -> None:
        """
        Sends array of
        :param dataArray:  
        :return: None
        """
        dataString = ""
        if len(dataArray) <= 0:
            raise Exception("sendArray: dataArray has no length")
        for element in dataArray:
            dataString += json.dumps(element) + "\n"
        if dataString is None:
            return
        self.client.Send(dataString.encode())

    def send(self, data: object = None) -> None:
        self.client.Send((json.dumps(data) + "\n").encode())

    def pair(self):
        self.send({"type": "pair", "id": self.pluginId})

    def createState(self, stateId, desc, defaultValue):
        if self.customStates[stateId]:
            raise Exception("createState: Custom state {} already exists".format(stateId))
        self.send({"type": "createState", "id": stateId, "desc": desc, "defaultValue": defaultValue})

    def choicesUpdate(self, choiceId, value):
        if len(value) <= 0:
            raise Exception("choiceUpdate: value is an empty array")
        self.send({"type": "choiceUpdate", "id": choiceId, "value": value})

    def choiceUpdateSpecific(self, choiceId, value, instanceId):
        if len(value) <= 0:
            raise Exception("choiceUpdateSpecific: value is an empty array")
        if instanceId is None or instanceId == "":
            raise Exception("choiceUpdateSpecific: instanceId is not set")
        self.send({"type": "choiceUpdate", "id": choiceId, "instanceId": instanceId, "value": value})

    def stateUpdate(self, stateId, value):
        self.send({"type": "stateUpdate", "id": stateId, "value": value})

    def stateUpdateMany(self, states):
        stateArray = []
        if len(states) <= 0:
            raise Exception("stateUpdateMany: states contains no data")
        for state in states:
            stateArray.append({"type": "stateUpdate", "id": state.id, "value": state.value})
        self.sendArray(stateArray)

    def connect(self):
        self.client = SimpleTCPClient("127.0.0.1", 12136)
        self.client.onReceive = self.onReceive
        self.client.onConnected = self.onConnect
        self.client.onDisconnected = self.onDisconnect
        self.pair()

    def close(self):
        self.client.Disconnect()

    def onReceive(self, client, rawData: bytes):
        data = json.loads(rawData.decode())
        self.emit(data["type"], client, data)

    def onConnect(self, client, rawData: bytes):
        self.emit("connect", client, rawData)

    def onDisconnect(self, client, rawData):
        self.emit("connect", client, rawData)
