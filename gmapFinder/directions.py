from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import requests

total_distance = None

def getDistance(scale='km'):
	try:
		if scale.lower()=="km":
			return total_distance.km
		if scale.lower()=="mile":
			return total_distance.miles
		return "Choose between (km / mile) only"
	except:
		print("First execute the getDirection() function")

def getCurrentLocation():
	res = requests.get("https://ipinfo.io/")
	data = res.json()
	return data

def getDirection(startingPoint, destinationPoint):
	global total_distance

	geolocator = Nominatim(user_agent='gmap')
	if 'current' in startingPoint:
		startinglocation = geolocator.reverse(getCurrentLocation()['loc'])
	else:
		startinglocation = geolocator.geocode(startingPoint)

	destinationlocation = geolocator.geocode(destinationPoint)
	startingPoint = startinglocation.address.replace(' ', '+')
	destinationPoint = destinationlocation.address.replace(' ', '+')

	URL = 'https://www.google.co.in/maps/dir/'+startingPoint+'/'+destinationPoint+'/'

	startinglocationCoordinate = (startinglocation.latitude, startinglocation.longitude)
	destinationlocationCoordinate = (destinationlocation.latitude, destinationlocation.longitude)
	total_distance = great_circle(startinglocationCoordinate, destinationlocationCoordinate)
	
	return URL
