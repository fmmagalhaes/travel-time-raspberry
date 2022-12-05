# Travel Time Raspberry

This repository aims at providing periodic information about the duration of a car trip to given destinations, taking live traffic into account. This was achieved by using a mini LCD connected to a Raspberry PI.

<img src="https://user-images.githubusercontent.com/8866496/205746551-2663904d-3372-4017-b12f-5ee0e1048828.png" width="500">



The communication with the LCD was done through the interfacing made available by [The Raspberry Pi Guy](https://github.com/the-raspberry-pi-guy/lcd).

The travel information comes from [TomTom Routing API](https://developer.tomtom.com/routing-api/api-explorer)

## Setup

### Install dependencies
```pip install requests```  
```pip install schedule```  


### Run in the console
To run this in the console, simply run  
```python console_random_country.py```

### Run on Raspberry Pi
1. Follow this installation guide to setup the drivers for the LCD communication  
https://github.com/the-raspberry-pi-guy/lcd#Installation

2. Register in [TomTom for developers](https://developer.tomtom.com/) and get your API key, to replace the one in `apikey` file.

3. Change the coordinates in `coordinates.json`

4. Run ```python lcd_travel_time.py```

Updated travel times will now be shown in your lcd every 10 minutes. Make the necessary adjustments to edit the periodicity at your own will.

### Run on command line
Run ```python travel_time.py```, which does not rely on the lcd.
