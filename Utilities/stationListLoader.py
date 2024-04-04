from nredarwin.webservice import DarwinLdbSession
from departureFactory import getDepartures
import json
darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")

# x = getDepartures()
# t = x.query("YRK")
# board = darwin_sesh.get_station_board('YRK')
# print(board.location_name)

def stationListLoaderScript():
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    stationDict = {}
    codeList=[]
    count = 0
    for i in range(26):
        for j in range(26):
            for k in range(26):
                code = alphabet[i] + alphabet[j] + alphabet[k]
                codeList.append(code)
                count = count + 1
                print(count)
    count = 0
    for c in codeList[14701:]:
        count = count + 1
        print(count)
        try:
            board = darwin_sesh.get_station_board(c)
        except:
            continue
        stationDict.update({c: str(board.location_name.upper())})

    with open('stationConversions14701-end.txt', 'w') as convert_file: 
        convert_file.write(json.dumps(stationDict))
    print(len(stationDict))

def stationListMerge():
    f = open('stationConversions1-4900.txt')
    f2 = open('stationConversions4901-9800.txt')
    f3 = open('stationConversions9801-14700.txt')
    f4 = open('stationConversions14701-end.txt')
    s1 = json.load(f)
    s2 = json.load(f2)
    s3 = json.load(f3)
    s4 = json.load(f4)
    s1.update(s2)
    s1.update(s3)
    s1.update(s4)
    print(len(s1))
    with open('stationConversionsAPR24.txt', 'w') as convert_file: 
        convert_file.write(json.dumps(s1))
    print(len(s1))
    f.close()
    f2.close()
    f3.close()
    f4.close()

stationListMerge()
