from DepartureTemplate import departure
from nredarwin.webservice import DarwinLdbSession
#This file as one function: To return a list of departure objects reflecting the current services


class getDepartures
    def __init__(self,stn=""):
        darwin = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")

