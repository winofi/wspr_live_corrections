"""
Script names starting with _ are ignored. This file contains an example on how to define a fast check for spot validation.
"""
class WsprSpotCheck:
    def getName(self):
        return "Dummy Check"

    def getDescription(self):
        return "Dummy Wspr Spot check to show how things might work"

    """
    Runs static validation against a wspr spot. 
    :param spot: The wspr spot to check, looks as follows:
    {
			"id": 7126367466,
			"time": "2001-02-16 09:14:00",
			"band": 7,
			"rx_sign": "JE1JDL",
			"rx_lat": 36.479,
			"rx_lon": 138.958,
			"rx_loc": "PM96",
			"tx_sign": "K6MCS",
			"tx_lat": 38.688,
			"tx_lon": -121.375,
			"tx_loc": "CM98hq",
			"distance": 8291,
			"azimuth": 305,
			"rx_azimuth": 52,
			"frequency": 7040060,
			"power": 37,
			"snr": -20,
			"drift": 0,
			"version": "1.9.1",
			"code": 1
		}
    :return: Expected to return a negative result for bad spots, a positive one for spots passing the validation and 0 if this validation does not apply to the specified spot. 
    """
    def checkSpot(self, spot:dict[str, any]) -> int:
        return 0
