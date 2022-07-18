# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

def gender_cleaning(string):  
    ## This function returns Man or Woman depending of what it founds in the string

  
    string = str(string).lower().strip()
    if "m" in string:
        return "Man"
    elif "f" in string:
        return "Woman"
    else:
        return np.nan


def age_cleaning(string):  ## function to clean the Age variable and get rid of values which cant be int.
    try:
        string = int(string)
    except:
        return np.nan
    return int(string)

def autoconvert_format(value):  # here i convert DataFrame column type from string to datetime with a exception of format
    try:
        value = pd.to_datetime(value)
        return value
    except:
        pass
    return value

def activites_cleaning(string): ## function to apply to clean the activity base, if i return nan i can get 8 major values
    string = str(string).lower().strip()
    if string != string:
        return np.nan
    elif "swimming" in string or "bathing" in string or "floating" in string or "splashing" in string or "jumped into the water" in string or "playing" in string:
        return "Swimming"
    elif "diving" in string or "snorkel" in string:
        return "Diving"
    elif "fishing" in string:
        return "Fishing"
    elif "surf" in string or "body boarding" in string or "body-boarding" in string or "boogie boarding" in string or "paddleskiing" in string:
        return "Surf"
    elif "standing" in string:
        return "Standing"
    elif "kayaking" in string or "ship" in string or "sail" in string or "boat" in string or "canoeing" in string or "board" in string or "rowing" in string or "fell into the water" in string:
        return "Boating"
    elif "disaster" in string:
        return "Sea catastrophe"
    elif "wading" in string or "walking" in string or "treading water" in string:
        return "Walking near the water"
    elif "Flying" in string or "sky" in string or "fly" in string:
        return "SHARKNADO??"
    else:
        return np.nan
    
    
def type_cleaning(string): ## i do the same with the type of attack column
    string = str(string).lower().strip()
    if "unprovoked" in string:
        return "Probably no"
    elif "provoked" in string:
        return "They had it coming"
    else:
        return np.nan
    
    
def fatality_clean(string):
    string = str(string).lower().strip()
    if "yes" in string or "y" in string or "s" in string:
        return "Fatal attack"
    elif "no" in string or "Neg" in string or "n" in string:
        return "Barely alive"
    else:
        return np.nan
    

def shark_species(string):
    string = str(string).lower().strip()
    if "white" in string or "blanco" in string or "great" in string:
        return "Great white shark"
    elif "invalid" in string or "not confirmed" in string or "questionable" in string or "unconfirmed" in string or "unidentified" in string:
        return np.nan
    elif "tiger" in string:
        return "Tiger shark"
    elif "bronze" in string:
        return "Bronze whaler shark"
    elif "bull" in string:
        return "Bull shark"
    elif "wobbegong" in string:
        return "Wobbegong shark"
    elif "blacktip" in string:
        return "Blacktip shark"
    elif "raggedtooth" in string:
        return "Raggedtooth shark"
    elif "blue" in string:
        return "Blue shark"
    elif "mako" in string:
        return "Mako shark"
    elif "grey" in string:
        return "Grey shark"
    elif "zambesi" in string:
        return "Zambesi shark"
    
    
def country_cleaning(string):
    string = str(string).lower().strip()
    if "usa" in string or "united states" in string or "the states" in string or "u.s.a" in string or "u.s" in string:
        return "United States of America"
    elif "australia" in string or "aus" in string:
        return "Australia"
    elif "south africa" in string:
        return "South Africa"
    elif "brazil" in string or "brasil" in string:
        return "Brazil"
    elif "zealand" in string:
        return "New Zealand"
    elif "papua new guinea" in string or "papua" in string or "guinea" in string:
        return "Papua New Guinea"
    elif "mexico" in string:
        return "Mexico"
    elif "reunion" in string:
        return "Reunion (France)"
    elif "philippines" in string or "filipin" in string:
        return "Philippines"
    elif "italy" in string or "italia" in string:
        return "Italy"
    elif "mozambique" in string:
        return "Mozambique"
    elif "caledonia" in string:
        return "New Caledonia"
    elif "japan" in string or "nihon" in string:
        return "Japan"
    elif "spain" in string:
        return "Spain"
    else:
        return np.nan