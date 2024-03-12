from departureTemplate import departure
from nredarwin.webservice import DarwinLdbSession
#This file has one function: To return a list of departure objects reflecting the current services

class getDepartures:
    def __init__(self):
        self.darwin = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")

    def query(self,stn=""):
        self.station = stn #Will be changed so user can use the actual name of the station
        if self.station == "":
            return [departure("ErrorStationNotFound,--,--,--",[])]
        try:
            board = self.darwin.get_station_board(self.station)
        except:
           return [departure("ErrorStationNotFound,--,--,--",[])]

        if len(board.train_services) == 0:
            return [departure(f'welcome to {self.station},---,---,---',[])]
        
        departures = []
        for i in range(len(board.train_services)-1):

            service_id = board.train_services[i].service_id
            service = self.darwin.get_service_details(service_id)

            info = ""
            info += str(board.train_services[i].destination_text) + ","
            info += str(service.platform) + ","
            info += str(service.eta) + ","
            #info += str(service.eta) + ","
            info += str(service.std)
            callingPoints = service.subsequent_calling_points

            service.std

            departures.append(departure(info,callingPoints))
        
        return departures
    def getStation(self):
        return self.station #No use for this yet
    
    def _convertStation(self,stn):
        #Code to convert station codes to station names and codes
        pass
