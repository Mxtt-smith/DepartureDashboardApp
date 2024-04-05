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
            return self.expectedArrival
        if self.expectedArrival == 'None':
            return "On time"
        self.colour = "red"
        if self.expectedArrival == 'Cancelled':
            return "Cancelled"
        return "Exp " + self.expectedArrival
    def getDestination(self):
        return self.destination
    
    def getPlatform(self):
        if self.platform == 'None':
            return "-"
        return self.platform
    
    def getCallingAt(self):
        callingAt=""

        if len(self.stations) == 1:
            callingAt = callingAt + self.getDestination() + "{" + self.stations[i].st + "}" + " only" 
            return callingAt
        for i in range(len(self.stations)-1):
            callingAt = callingAt + self.stations[i].location_name + "{" + self.stations[i].st + "}" + "," #switch this to an F string matt you idiot
        return callingAt + self.getDestination() + "{" + self.stations[-1].st + "}      "

    def getShedDeparture(self):
        return self.scheduledDeparture
    
