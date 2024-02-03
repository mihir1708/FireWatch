from Questions import questions
import Location as loc
from Distance import distance as dist
from RiskFactor import risk_factor
from tkinter import *

def func(responses):
    city = loc.location()
    coordinates = loc.coordinates()
    distance = dist(coordinates,responses[0])

    risk = risk_factor(distance,responses)

    return risk
