# GmapFinder

## Installation  
``` pip install gmapFinder ```

## How to use it?
Here are the functions which will provide some results...  
```import gmapFinder```

#### To get current location  
``` gmapFinder.getCurrentLocation() ```  

This will provide a dictionary, in which you will get details like,  
IP, City, Region, Country, Location, Org, Postal, Timezone  

#### To get direction details  
``` gmapFinder.getDirection("Lucknow, Uttar Pradesh", "Tokyo, Japan") ```  

It requires 2 arguments,  
StartingPoint (you don't have to put complete address, it will automatically calculate if not given complete) and DestinationPoint.  

It will then return a dictionary:

```
result = {
		"url": GOOGLE_MAPS_URL,
		"total_distance(km)": TOTAL_DIST_IN_KM,
		"total_distance(miles)": TOTAL_DIST_IN_MILES,
		"Starting address": STARTING_ADDR,
		"Starting Co-ordinates": START_ADDR_COORDINATES,
		"Destination Address": DESTINATION_ADDR,
		"Destination Co-ordinates": DESTINATION_ADDR_COORDINATES
	}
```

If you write "current" in address then, it will find the directions from your current location.  

### Thank You !!!
