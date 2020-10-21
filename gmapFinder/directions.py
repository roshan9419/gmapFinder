from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import requests

def getCurrentLocation():
	res = requests.get("https://ipinfo.io/")
	data = res.json()
	return data

def getDirection(startingPoint, destinationPoint):

	geolocator = Nominatim(user_agent='gmap')
	try:
		if 'current' in startingPoint:
			startinglocation = geolocator.reverse(getCurrentLocation()['loc'])
		else:
			startinglocation = geolocator.geocode(startingPoint)

		destinationlocation = geolocator.geocode(destinationPoint)
		startingPoint = startinglocation.address.replace(' ', '+')
		destinationPoint = destinationlocation.address.replace(' ', '+')
	except:
		return "Try Something different Address"

	URL = 'https://www.google.co.in/maps/dir/'+startingPoint+'/'+destinationPoint+'/'

	startinglocationCoordinate = (startinglocation.latitude, startinglocation.longitude)
	destinationlocationCoordinate = (destinationlocation.latitude, destinationlocation.longitude)
	total_distance = great_circle(startinglocationCoordinate, destinationlocationCoordinate)
	
	result = {
		"url": URL,
		"total_distance(km)": total_distance.km,
		"total_distance(miles)": total_distance.miles,
		"Starting address": startingPoint,
		"Starting Co-ordinates": startinglocationCoordinate,
		"Destination Address": destinationPoint,
		"Destination Co-ordinates": destinationlocationCoordinate
	}

	return result
