from departureTemplate import departure
from nredarwin.webservice import DarwinLdbSession
#This file as one function: To return a list of departure objects reflecting the current services


class getDepartures:
    def __init__(self):
        darwin = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")

    def query(self,stn=""):
        self.station = stn #Will be changed so user can use the actual name of the station
        if self.station == "":
            return [departure("ErrorStationNotFound,--,--,--",[])]
        board = self.darwin.get_station_board(self.station)

        departures = []
        for i in range(len(board.train_services)-1):

            service_id = board.train_services[i].service_id
            service = self.darwin.get_service_details(service_id)

            info = ""
            info += service.destination_text + ","
            info += service.platform + ","
            info += service.expectedArrival + ","
            info += service.scheduledArrival
            callingPoints = service.subsequent_calling_points

            departures.append(departure(info,callingPoints))
        
        return departures
    def getStation(self):
        return self.station #No use for this yet
    
    def _convertStation(self,stn):
        #Code to convert station codes to station names and codes
        pass
