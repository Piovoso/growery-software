import json as js, os
from datetime import datetime as time


timestamp = time.timestamp(time.now())
plants = ["Strawberry Banana Seeds"]
groweryCount = 1

class Growery:
    def __init__(entryType:str = '%N'):
        if entryType == '%N':
            Growery.Main()
        elif entryType == '%S':
            Growery.AddSeed()

    def Main():
        prefix = {
            "entry": {
                "created": {
                    "timestamp": int(timestamp),
                    "gmt": str(time.fromtimestamp(timestamp))
                },
                "plants": {}
            },
            "data": {}
        }

        with open(f'dumps/{time.now().strftime("%u")}-{time.now().strftime("%V")}-{time.now().strftime("%G")}.json', 'w') as initialFile:
            js.dump(prefix, initialFile, indent=4)
    
    def DataEntry(PH:float, PPM:float, EC:float, water:float,
                   N:float, P:float, K:float, Ca:float, Mg:float,
                   temperature:float, light:float, humitity:float,
                   ventilation:float, co2:float):
        """Enter data to main database"""
        data = {
            timestamp: {
                "soil": {
                    "PH": PH,
                    "PPM": PPM,
                    "EC": EC,
                    "water": water,
                    "nitrogen": N,
                    "phosphorus": P,
                    "potassium": K,
                    "calcium": Ca,
                    "magnesium": Mg
                },
                "Climate": {
                    "temperature": temperature,
                    "light": light,
                    "humitity": humitity,
                    "ventilation": ventilation,
                    "co2": co2
                }
            }
        }
    
    def AddSeed(seed:str, indica:float, sativa:float, THC:float, CBD:float, indoor:float, outdoor:float):
        """adding seed to vault database"""
        plantData = {
            "seed": seed,
            "type": {
                "indica": indica,
                "sativa": sativa,
            },
            "Cannabis":{
                "THC": THC,
                "CBD": CBD
            },
            "Yield": {
                "indoor": indoor,
                "outdoor": outdoor
            }
        }

Growery()