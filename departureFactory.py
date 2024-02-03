from departureTemplate import departure
from nredarwin.webservice import DarwinLdbSession
#This file as one function: To return a list of departure objects reflecting the current services


class getDepartures:
    def __init__(self):
        darwin = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")
        station = ""
        #Add code to convert to station code if required

    def query(self,stn=""):
        self.station = stn
        if self.station == "":
            return [departure("ErrorStationNotFound,--,--,--",[])]
        board = self.darwin.get_station_board(self.station)

        for i in range(len(board.train_services)-1):
            service_id = board.train_services[i].service_id
            service = self.darwin.get_service_details(service_id)

            info = ""
            info += service.destination_text + ","
            info += service.platform + ","
            info += service.expectedArrival
    def getStation(self):
        return self.station
