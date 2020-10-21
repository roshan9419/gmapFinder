"""This piece of software was last updated on 21-October-2020 at 09:00 IST"""
"""
Function getCurrentLocation()
	-Gives the current location of your device, with some details
	IP, City, Region, Country, Location, Org, Postal, Timezone

Function getDirection(startingAddress, destinationAddress)
	-returns a dictionary having:
		url of Google Map link,
		total distance in (km, miles),
		starting point and destination point address and location.

Example::
	import gmapFinder as gp

	gp.getCurrentLocation()
	gp.getDirection("Lucknow, UttarPradesh", "Tokyo, Japan")
"""

from gmapFinder.directions import getDirection, getCurrentLocation
