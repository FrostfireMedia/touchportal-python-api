# Touch Portal API for Python
Build a Touch Portal plugin using Python and this module. This module handles all the socket connections and formatting, you just handle the data.

- [Touch Portal API for Python](#touch-portal-api-for-python)
    - [Changelog](#changelog)
    - [Usage](#usage)
        - [Installing](#installing)
        - [Basic Usage](#basic-usage)
        - [Full Documentation](#full-documentation)
    - [Contribute](#contribute)

## Changelog
```
v1.0.0 Initial release
```

## Usage
### Installing
This module is available through PyPI, or through the releases page.
```shell
pip install touchportal-api
```
### Basic Usage
Touch Portal communicates through UTF-8 encoded strings containing JSON data. This module handles the reading, and conversion and returns a simple Python dictionary.
```python
import touchportal_api

# Initialize a Client using the plugin ID that is in your entry.tp
TPClient = touchportal_api.Client(pluginId="YOUR_PLUGIN_ID")

# Set up a callback when info is received
@TPClient.on("info")
def onInfo(client, data):
    # client is the Client that called this function.
    # data is a Python dictionary containing the data from Touch Portal
    print("This is called when the connection is successful.")

# Set up a callback when an action is received 
@TPClient.on("action")
def onAction(client, data):
    print("Neat. I just got called from an action.")

# Tell the Client to connect to Touch Portal.
# Call this after you've set up your callbacks. 
TPClient.connect()

# Tell Touch Portal to update a state.
TPClient.stateUpdate("STATE_ID", "VALUE")

# Tell Touch Portal to update many states.
states = [
    {
        "id": "state1",
        "value": "value1"
    },
    {
        "id": "state2",
        "value": "value2"
    }
]
TPClient.stateUpdateMany(states)

# Call this when your program is closing to clean up sockets.
TPClient.close()
```

### Full Documentation
The documentation of this module can be found here: [Touch Portal API for Python](https://github.com/FrostfireMedia/touchportal-python-api/wiki) 

The documentation of Touch Portal's interface can be found here: [Touch Portal Interface API](https://www.touch-portal.com/api/)

## Contribute
Feel free to report bugs, suggest enhancements, fork, or create a pull request. I am always open to enhancements and bug fixes.