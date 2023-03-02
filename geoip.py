import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord(ip) -> object:
    rec = gi.record_by_name(ip)
    city = rec['city_name']
    country = rec['country']
    longitude = rec['longitude']
    lat = rec['latitude']
    print('[+] Address: ' + ip + ' Geo-located ')
    print('[+] ' + str(city) + ', ' + str(country))
    print('[+] Latitude: ' + str(lat) + ', Longitude: ' + str(longitude))

ip = input('Enter IP:')
printRecord(ip)