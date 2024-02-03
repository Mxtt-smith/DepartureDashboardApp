from nredarwin.webservice import DarwinLdbSession
darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="89ca18ad-9591-4384-a634-472c772763b2")

board = darwin_sesh.get_station_board('YRK')
#print(board.train_services[2])
# print(board.location_name)
# print(board.train_services[0].destination_text)
#print([s.destination_text for s in board.train_services])
service_id = board.train_services[0].service_id
service = darwin_sesh.get_service_details(service_id)
print(service.operator_name)
#print(service.platform)
#print([cp.location_name for cp in service.subsequent_calling_points])
