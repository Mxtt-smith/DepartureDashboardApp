from nredarwin.webservice import DarwinLdbSession
from departureFactory import getDepartures
import json
darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")



x = getDepartures()
t = x.query("YRK")
board = darwin_sesh.get_station_board('YRK')
print(board.location_name)

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
stationDict = {}

count = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            code = alphabet[i] + alphabet[j] + alphabet[k]
            try:
                board = darwin_sesh.get_station_board(code)
            except:
                continue
            stationDict.update({code: str(board.location_name.upper())})
            count = count + 1
            print(count)
with open('stationConversions.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(stationDict))
print(len(stationDict))
