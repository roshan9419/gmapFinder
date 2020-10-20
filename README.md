# GmapDirection

## Installation  
``` pip install gmapdirection ```

## How to use it?
Here are the functions which will provide some results...  
```import gmapdirection```

#### To get current location  
``` gmapdirection.getCurrentLocation() ```  
This will provide you a dictionary, in which you will get details like,  
IP, City, Region, Country, Location, Org, Postal, Timezone  

#### To get direction link  
``` gmapdirection.getDirection("Lucknow, Uttar Pradesh", "Tokyo, Japan") ```  
It require 2 arguments, first StartingPoint (you don't have to put complete address, it will automatically calculate if not given complete) and DestinationPoint.  
It will then return a google map link, showing the direction from starting point to destination point.  
If you write "current" in address then, it will find the directions from your current location.  

#### To get total distance  
``` gmapdirection.getDistance(type) ```  
Replace type with "km" or "mile", by default it will return total distance from start to destination in "km". You must first execute the getDirection() function to store total_distance  

### Thank You !!!