class departure:
    def __init__(self,info="",stns=[]):

        self.destination = ""
        self.platform = None
        self.expectedArrival = ""
        self.scheduledArrival = ""
        self.stations = []

        if info == "":
            self.destination,self.platform,self.expectedArrival,self.scheduledDeparture = "---"
        else:
            self.destination,self.platform,self.expectedArrival,self.scheduledDeparture = info.split(',')
            self.stations = stns
        if self.platform == None:
            self.platform = 'Na'

    def getEta(self):
        if self.expectedArrival == 'On time':
            return self.expectedArrival
        if self.expectedArrival == 'None':
            return " --- "
        return "Exp " + self.expectedArrival
    def getDestination(self):
        return self.destination
    
    def getPlatform(self):
        return self.platform
    
    def getCallingAt(self):
        callingAt= "Calling at: "

        if not self.stations:
            callingAt = callingAt + self.getDestination() + " only"
            return callingAt
        for i in range(len(self.stations)-1):
            callingAt = callingAt + self.stations[i].location_name + ","
        return callingAt

    def getShedDeparture(self):
        return self.scheduledDeparture
    

    