# GmapFinder

## Installation  
``` pip install gmapFinder ```

## How to use it?
Here are the functions which will provide some results...  
```import gmapFinder```

#### To get current location  
``` gmapFinder.getCurrentLocation() ```  
This will provide you a dictionary, in which you will get details like,  
IP, City, Region, Country, Location, Org, Postal, Timezone  

#### To get direction details  
``` gmapFinder.getDirection("Lucknow, Uttar Pradesh", "Tokyo, Japan") ```  
It requires 2 arguments,  
StartingPoint (you don't have to put complete address, it will automatically calculate if not given complete) and DestinationPoint.  
It will then return a dictionary having the  
url of Google Map link,  
total distance in (km, miles),  
starting point and destination point address and location.  
If you write "current" in address then, it will find the directions from your current location.  

### Thank You !!!
