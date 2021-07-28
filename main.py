import json

from phpTravels_tc1 import phpTravels_tc1
from phpTravels_tc2 import phpTravels_tc2
from phpTravels_tc3 import phpTravels_tc3
from phpTravels_tc4 import phpTravels_tc4



if __name__=="__main__":
    # Web Driver Config Path stored in JSON
    _configFilePath = "config.json"
    _browser = "chrome"

    json_file = open(_configFilePath)
    config = json.load(json_file)
    path = config['webdriverFilepath']


    testObject = phpTravels_tc1()
    testObject.automationRunner(_browser, path)
    testObject = phpTravels_tc2()
    testObject.automationRunner(_browser, path)
    testObject = phpTravels_tc3()
    testObject.automationRunner(_browser, path)
    testObject = phpTravels_tc4()
    testObject.automationRunner(_browser, path)

