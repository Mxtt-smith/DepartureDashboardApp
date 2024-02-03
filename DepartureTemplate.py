class departure:
    def __init__(self,info="",stations=[]):

        destination = ""
        platform = None
        expectedArrival = ""
        scheduledArrival = ""
        stations = []

        if info == "":
            destination,platform,expectedArrival,scheduledArrival = "---"
        else:
            destination,platform,expectedArrival,scheduledArrival = info.split(',')
            stations
        if platform == None:
            platform = 'Na'

    def getEta(self):
        if self.expectedArrival <= self.scheduledArrival:
            return "On time"
        return "Exp " + self.expectedArrival
    
    def getDestination(self):
        return self.destination
    
    def getPlatform(self):
        return self.platform
    
    def getCallingAt(self):
        callingAt= "Calling at:"

        if not self.stations:
            callingAt = callingAt + self.getDestination() + " only"
            return callingAt
        for i in range(len(self.stations)-1):
            callingAt = callingAt + self.stations[i] + ","
        return callingAt

    

    
