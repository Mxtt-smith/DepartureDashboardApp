class departure:

    def __init__(self,info="",stns=[]):

        self.destination = ""
        self.platform = None
        self.expectedArrival = ""
        self.scheduledArrival = ""
        self.stations = []
        self.colour = "pink"

        if info == "":
            self.destination,self.platform,self.expectedArrival,self.scheduledDeparture = "---"
        else:
            self.destination,self.platform,self.expectedArrival,self.scheduledDeparture = info.split('|')
            self.stations = stns
        if self.platform == None:
            self.platform = 'Na'

    def getEta(self):
        if self.expectedArrival == 'On time':
            self.colour = "green"
            return self.expectedArrival
        if self.expectedArrival == 'None':
            self.colour = "yellow"
            return " --- "
        self.colour = "red"
        if self.expectedArrival == 'Cancelled':
            return "Cancelled"
        return "Exp " + self.expectedArrival
    def getDestination(self):
        return self.destination
    
    def getPlatform(self):
        return self.platform
    
    def getCallingAt(self):
        callingAt=""

        if len(self.stations) == 1:
            callingAt = callingAt + self.getDestination() + " only"
            return callingAt
        for i in range(len(self.stations)-1):
            callingAt = callingAt + self.stations[i].location_name + ","
        return callingAt + self.getDestination() + "      "

    def getShedDeparture(self):
        return self.scheduledDeparture
    def getColour(self):
        Useless = self.getEta()
        return self.colour

    
