import __init__ as touchportal_api

if __name__ == "__main__":
    tpClient = touchportal_api.Client(pluginId="EDTPP")


    @tpClient.on("info")
    def onInfo(_, data):
        print(data)


    @tpClient.on("action")
    def onAction(_, data):
        print(data)


    tpClient.connect()

    tpClient.stateUpdate("test-id", "value")
