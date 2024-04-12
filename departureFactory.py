from departureTemplate import departure
from nredarwin.webservice import DarwinLdbSession
import os
from dotenv import find_dotenv, load_dotenv
import json
import random

envPath = find_dotenv()
load_dotenv(envPath)
#This file has one function: To return a list of departure objects reflecting the current services

class getDepartures:
    
    def __init__(self):
        self.darwin = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key=os.getenv("API_KEY"))
        self.stnConversions = {}
        self.station = ""
        f = open('Utilities\stationConversionsAPR24.txt')
        self.stnConversions = json.load(f)
        f.close()

    def query(self,stn=""):
        self.station = self.convertStation(stn)
        if self.station == "":
            return [departure("That station is not found|404|Now|--",[])]
    
        board = self.darwin.get_station_board(self.station)
    
        if len(board.train_services) == 0:
            return [departure('---|---|---|---',[])]
        
        departures = []
        for i in range(len(board.train_services)-1):

            service_id = board.train_services[i].service_id
            service = self.darwin.get_service_details(service_id)

            info = f'{str(board.train_services[i].destination_text)}|{str(service.platform)}|{str(service.eta)}|{str(service.std)}'
            callingPoints = service.subsequent_calling_points
            departures.append(departure(info,callingPoints))
        
        return departures
    def getStation(self):
        return self.station
    
    def convertStation(self,stn):
        if stn in self.stnConversions.keys():
            return stn
        if stn in self.stnConversions.values():
            return list(self.stnConversions.keys())[list(self.stnConversions.values()).index(stn)]
        return ""
    def getRandomDepartures(self):
        key, val = random.choice(list(self.stnConversions.items()))
        print(key)
        return self.query(key)
