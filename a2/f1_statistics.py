#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
created on Sat Jun 04 14:45:33 2022
=======
Created on Sat Jun 04 14:45:33 2022
>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
@author: Gabriel Maryshev

This is a file processor that allows to generate relevant statistics from F1 data.
"""
from copyreg import constructor
from struct import unpack
import sys
import csv
import functools
import operator
from collections import Iterable
from functools import reduce
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
<<<<<<< HEAD

plt.style.use('fivethirtyeight')

def get_question(qstr : str) -> str:
    argarr1 = qstr.split("=")
    question = argarr1[1]
    return question

def get_files(filestr :str) -> list:
    argarr2 = []
    files = []
    argarr2 = filestr.split("=")
    files = argarr2[1].split(",")
    return files


def makelist(file :str) -> list:
    list = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list.append(line)
    return list


def firstqsolver(drivers :list, results :list) -> None:
    """ solves respective question, same thing for other question solving function

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    driverWins = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    forename = drivers[d]["forename"]
                    surname = drivers[d]["surname"]
                    fullname = f'{forename} {surname}'
                    driverWins[fullname] = i

    sdrivers = dict(sorted(driverWins.items(), key=lambda x: x[0] ))#youtube                       
    sdrivers = dict(sorted(sdrivers.items(), key=lambda x: x[1], reverse=True))#youtube
    sdrivers = dict(list(sdrivers.items())[:20])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sdrivers.items(): 
            f.write(f"{key},{value}\n")
        
def secondqsolver(drivers :list, results :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    countryWins :dict = {}#same thing for other functions 
    driverWins :dict = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    id = drivers[d]['driverId']
                    id = f'{id}'
                    nat = drivers[d]['nationality']
                    nat = f'{nat}'
                    driverWins[id] = [i, drivers[d]['nationality']]

    d_list = [[k, v] for k, v in driverWins.items()] 
    flat_list = functools.reduce(operator.concat, d_list)#from djangocentral
    del flat_list[::2]
    for item in flat_list:
        key = item[1]
        if key not in countryWins:
            countryWins[key] = item[0]
        else:
            countryWins[key] += item[0]         
    sCountries = dict(sorted(countryWins.items(), key=lambda x: x[0] ))#youtube                       
    sCountries = dict(sorted(sCountries.items(), key=lambda x: x[1], reverse=True))#youtube
    sCountries = dict(list(sCountries.items())[:10])
    with open("output.csv", 'w') as f:  
        f.write("subject,statistic\n")
        for key, value in sCountries.items(): 
            f.write(f"{key},{value}\n")

def thirdqsolver(constructors :list, results :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    constructorWins = {}
    for c in range(len(constructors)):
        i = 0   
        for r in range(len(results)):
            if(constructors[c].get("constructorId") == results[r].get("constructorId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    conR = constructors[c]["name"]
                    conR = f"{conR}"
                    constructorWins[conR] = i

    sconstructors = dict(sorted(constructorWins.items(), key=lambda x: x[0] ))#youtube                       
    sconstructors = dict(sorted(sconstructors.items(), key=lambda x: x[1], reverse=True))#youtube
    sconstructors = dict(list(sconstructors.items())[:10])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sconstructors.items(): 
            f.write(f"{key},{value}\n")

def fourthqsolver(circuits :list, races :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

=======

plt.style.use('fivethirtyeight')

def get_question(qstr : str) -> str:
    argarr1 = qstr.split("=")
    question = argarr1[1]
    return question

def get_files(filestr :str) -> list:
    argarr2 = []
    files = []
    argarr2 = filestr.split("=")
    files = argarr2[1].split(",")
    return files


def makelist(file :str) -> list:
    list = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list.append(line)
    return list


def firstqsolver(drivers :list, results :list) -> None:
    """ solves respective question, same thing for other question solving function

        Paramters
        ---------
        two csv files

>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
        Returns 
        -------
        None 
    """
<<<<<<< HEAD
=======
    driverWins = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    forename = drivers[d]["forename"]
                    surname = drivers[d]["surname"]
                    fullname = f'{forename} {surname}'
                    driverWins[fullname] = i

    sdrivers = dict(sorted(driverWins.items(), key=lambda x: x[0] ))#youtube                       
    sdrivers = dict(sorted(sdrivers.items(), key=lambda x: x[1], reverse=True))#youtube
    sdrivers = dict(list(sdrivers.items())[:20])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sdrivers.items(): 
            f.write(f"{key},{value}\n")
        
def secondqsolver(drivers :list, results :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    countryWins :dict = {}#same thing for other functions 
    driverWins :dict = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    id = drivers[d]['driverId']
                    id = f'{id}'
                    nat = drivers[d]['nationality']
                    nat = f'{nat}'
                    driverWins[id] = [i, drivers[d]['nationality']]

    d_list = [[k, v] for k, v in driverWins.items()] 
    flat_list = functools.reduce(operator.concat, d_list)#from djangocentral
    del flat_list[::2]
    for item in flat_list:
        key = item[1]
        if key not in countryWins:
            countryWins[key] = item[0]
        else:
            countryWins[key] += item[0]         
    sCountries = dict(sorted(countryWins.items(), key=lambda x: x[0] ))#youtube                       
    sCountries = dict(sorted(sCountries.items(), key=lambda x: x[1], reverse=True))#youtube
    sCountries = dict(list(sCountries.items())[:10])
    with open("output.csv", 'w') as f:  
        f.write("subject,statistic\n")
        for key, value in sCountries.items(): 
            f.write(f"{key},{value}\n")

def thirdqsolver(constructors :list, results :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    constructorWins = {}
    for c in range(len(constructors)):
        i = 0   
        for r in range(len(results)):
            if(constructors[c].get("constructorId") == results[r].get("constructorId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    conR = constructors[c]["name"]
                    conR = f"{conR}"
                    constructorWins[conR] = i

    sconstructors = dict(sorted(constructorWins.items(), key=lambda x: x[0] ))#youtube                       
    sconstructors = dict(sorted(sconstructors.items(), key=lambda x: x[1], reverse=True))#youtube
    sconstructors = dict(list(sconstructors.items())[:10])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sconstructors.items(): 
            f.write(f"{key},{value}\n")

def fourthqsolver(circuits :list, races :list) -> None:
    """ solves respective question

        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
    circountries = {}
    cirdict = {}
    for c in range(len(circuits)):
        i = 0 
        for r in range(len(races)):
            if(circuits[c].get("circuitId") == races[r].get("circuitId")):
                i +=1
                country = circuits[c]['country']
                country = f'{country}'
                id = circuits[c]['circuitId']
                id = f'{id}'
                cirdict[id] = [i, country]
<<<<<<< HEAD

    c_list = [[k, v] for k, v in cirdict.items()] 
    flat_list = functools.reduce(operator.concat, c_list)
    del flat_list[::2]
    for item in flat_list:
        key = item[1]
        if key not in circountries:
            circountries[key] = item[0]
        else:
            circountries[key] += item[0]     
    scircountries = dict(sorted(circountries.items(), key=lambda x: x[0] ))#youtube                       
    scircountries = dict(sorted(scircountries.items(), key=lambda x: x[1], reverse=True))#youtube
    scircountries = dict(list(scircountries.items())[:20])

    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in scircountries.items(): 
            f.write(f"{key},{value}\n")

def fifthqsolver(drivers :list, results :list) -> None:
    """ solves respective question

=======

    c_list = [[k, v] for k, v in cirdict.items()] 
    flat_list = functools.reduce(operator.concat, c_list)
    del flat_list[::2]
    for item in flat_list:
        key = item[1]
        if key not in circountries:
            circountries[key] = item[0]
        else:
            circountries[key] += item[0]     
    scircountries = dict(sorted(circountries.items(), key=lambda x: x[0] ))#youtube                       
    scircountries = dict(sorted(scircountries.items(), key=lambda x: x[1], reverse=True))#youtube
    scircountries = dict(list(scircountries.items())[:20])

    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in scircountries.items(): 
            f.write(f"{key},{value}\n")

def fifthqsolver(drivers :list, results :list) -> None:
    """ solves respective question

>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
        Paramters
        ---------
        two csv files

        Returns 
        -------
        None 
    """
    driverWins = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    if(results[r].get("grid") != "1"):
                        i +=1
                        forename = drivers[d]["forename"]
                        surname = drivers[d]["surname"]
                        fullname = f'{forename} {surname}'
                        driverWins[fullname] = i
    sdrivers = dict(sorted(driverWins.items(), key=lambda x: x[0] ))#youtube                       
    sdrivers = dict(sorted(sdrivers.items(), key=lambda x: x[1], reverse=True))#youtube
    sdrivers = dict(list(sdrivers.items())[:5])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sdrivers.items(): 
            f.write(f"{key},{value}\n")

def plotfirstq() -> None:
    """
        plots pi chart for respective question
    """
    data = pd.read_csv('output.csv')
    drivers = data['subject']
    wins = data['statistic']

    plt.pie(wins, labels = drivers, textprops={'fontsize': 5})
    plt.title("q1")
    plt.show()
    plt.savefig("output_graph_q1.jpeg")

def plotsecondq() -> None:
    data = pd.read_csv('output.csv')
    countries = data['subject']
    wins = data['statistic']


    plt.pie(wins, labels = countries, textprops={'fontsize': 8})
    plt.title("q2")
    plt.show()
    plt.savefig("output_graph_q2.jpeg") 

def plotthirdq() -> None:
    data = pd.read_csv('output.csv')
    constructors = data['subject']
    wins = data['statistic']

    plt.pie(wins, labels = constructors, textprops={'fontsize': 8})
    plt.title("q3")
    plt.show()
    plt.savefig("output_graph_q3.jpeg")       

def plotfourthq() -> None:
    data = pd.read_csv('output.csv')
    countries = data['subject']
    races = data['statistic']

    plt.pie(races, labels = countries, textprops={'fontsize': 8})
    plt.title("q4")
    plt.show()
    plt.savefig("output_graph_q4.jpeg")          

def plotfifthq() -> None:
    data = pd.read_csv('output.csv')
    drivers = data['subject']
    wins = data['statistic']

    dataFrame = pd.DataFrame(data.head(), columns=["subject","statistic"])
    # plotting the dataframe
    dataFrame.plot(x="subject", y="statistic", kind="bar", rot = "70", figsize=(10, 9))
    plt.title("q5")
    plt.xlabel("Drivers")
    plt.ylabel("wins not on post")
    plt.show()
    plt.savefig("output_graph_q5.jpeg", bbox_inches='tight')     

def main(): 
    """The main entry of the program.
    """
    #get arguments from terminal
    files = []
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    question = get_question(arg1)
    files = get_files(arg2)
    file1 = files[0]
    file2 = files[1]

    #get list from files
    list1 = makelist(file1)
    list2 = makelist(file2)
<<<<<<< HEAD

    #solve and plot depending on question
    if(question == "1"):
        firstqsolver(list1, list2)
        plotfirstq() 

    elif(question == "2"):
        secondqsolver(list1, list2)
        plotsecondq()

    elif(question == "3"):
        thirdqsolver(list1, list2)  
        plotthirdq()     

    elif(question == "4"):
        fourthqsolver(list1, list2) 
        plotfourthq()

=======

    #solve and plot depending on question
    if(question == "1"):
        firstqsolver(list1, list2)
        plotfirstq() 

    elif(question == "2"):
        secondqsolver(list1, list2)
        plotsecondq()

    elif(question == "3"):
        thirdqsolver(list1, list2)  
        plotthirdq()     

    elif(question == "4"):
        fourthqsolver(list1, list2) 
        plotfourthq()

>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
    elif(question == "5"):
        fifthqsolver(list1, list2)
        plotfifthq()           
    
    
<<<<<<< HEAD
if __name__ == '__main__':
    main()

"""
Created on Sat Jun 04 14:45:33 2022
@author: Gabriel Maryshev

This is a file processor that allows to generate relevant statistics from F1 data.
"""
import sys
import csv
import collections
import functools
import operator
import matplotlib
import numpy as np
from collections import OrderedDict
from collections import Iterable
from functools import reduce
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

def get_question(qstr):
    argarr1 = qstr.split("=")
    question = argarr1[1]
    return question

def get_files(filestr):
    argarr2 = []
    files = []
    argarr2 = filestr.split("=")
    files = argarr2[1].split(",")
    return files


def makelist(file):
    list = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list.append(line)
    return list
#straigt from stack overflow
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def firstqsolver(drivers, results):
    driverWins = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    forename = drivers[d]["forename"]
                    surname = drivers[d]["surname"]
                    fullname = f'{forename} {surname}'
                    driverWins[fullname] = i
    sdrivers = dict(sorted(driverWins.items(), key=lambda x: x[0] ))#youtube                       
    sdrivers = dict(sorted(sdrivers.items(), key=lambda x: x[1], reverse=True))#youtube
    sdrivers = dict(list(sdrivers.items())[:20])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sdrivers.items(): 
            f.write(f"{key},{value}\n")
        
def secondqsolver(drivers, results):
    countryWins = {}
    driverWins = {}
    
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    id = drivers[d]['driverId']
                    id = f'{id}'
                    nat = drivers[d]['nationality']
                    nat = f'{nat}'
                    driverWins[id] = [i, drivers[d]['nationality']]

    d_list = [[k, v] for k, v in driverWins.items()] 
    flat_list = functools.reduce(operator.concat, d_list)#from djangocentral
    del flat_list[::2]

    for item in flat_list:
        key = item[1]
        if key not in countryWins:
            countryWins[key] = item[0]
        else:
            countryWins[key] += item[0]       
          
    sCountries = dict(sorted(countryWins.items(), key=lambda x: x[0] ))#youtube                       
    sCountries = dict(sorted(sCountries.items(), key=lambda x: x[1], reverse=True))#youtube
    sCountries = dict(list(sCountries.items())[:10])
    with open("output.csv", 'w') as f:  
        f.write("subject,statistic\n")
        for key, value in sCountries.items(): 
            f.write(f"{key},{value}\n")

def thirdqsolver(constructors, results):
    constructorWins = {}
    for c in range(len(constructors)):
        i = 0   
        for r in range(len(results)):
            if(constructors[c].get("constructorId") == results[r].get("constructorId")):
                if(results[r].get("position") == "1"):
                    i +=1
                    conR = constructors[c]["name"]
                    conR = f"{conR}"
                    constructorWins[conR] = i
    sconstructors = dict(sorted(constructorWins.items(), key=lambda x: x[0] ))#youtube                       
    sconstructors = dict(sorted(sconstructors.items(), key=lambda x: x[1], reverse=True))#youtube
    sconstructors = dict(list(sconstructors.items())[:10])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sconstructors.items(): 
            f.write(f"{key},{value}\n")

def fourthqsolver(circuits, races):
    circountries = {}
    cirdict = {}
    for c in range(len(circuits)):
        i = 0 
        for r in range(len(races)):
            if(circuits[c].get("circuitId") == races[r].get("circuitId")):
                i +=1
                country = circuits[c]['country']
                country = f'{country}'
                id = circuits[c]['circuitId']
                id = f'{id}'
                cirdict[id] = [i, country]
    c_list = [[k, v] for k, v in cirdict.items()] 
    flat_list = functools.reduce(operator.concat, c_list)
    del flat_list[::2]

    for item in flat_list:
        key = item[1]
        if key not in circountries:
            circountries[key] = item[0]
        else:
            circountries[key] += item[0]     



    scircountries = dict(sorted(circountries.items(), key=lambda x: x[0] ))#youtube                       
    scircountries = dict(sorted(scircountries.items(), key=lambda x: x[1], reverse=True))#youtube
    scircountries = dict(list(scircountries.items())[:20])

    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in scircountries.items(): 
            f.write(f"{key},{value}\n")

def fifthqsolver(drivers, results):
    driverWins = {}
    for d in range(len(drivers)):
        i = 0   
        for r in range(len(results)):
            if(drivers[d].get("driverId") == results[r].get("driverId")):
                if(results[r].get("position") == "1"):
                    if(results[r].get("grid") != "1"):
                        i +=1
                        forename = drivers[d]["forename"]
                        surname = drivers[d]["surname"]
                        fullname = f'{forename} {surname}'
                        driverWins[fullname] = i
    sdrivers = dict(sorted(driverWins.items(), key=lambda x: x[0] ))#youtube                       
    sdrivers = dict(sorted(sdrivers.items(), key=lambda x: x[1], reverse=True))#youtube
    sdrivers = dict(list(sdrivers.items())[:5])#stackoverflow
    with open("output.csv", 'w') as f: 
        f.write("subject,statistic\n")
        for key, value in sdrivers.items(): 
            f.write(f"{key},{value}\n")

def plotfirstq():
    return             

def main(): 
    """The main entry of the program.
    """
    files = []
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    question = get_question(arg1)
    files = get_files(arg2)
    file1 = files[0]
    file2 = files[1]

    list1 = makelist(file1)
    list2 = makelist(file2)
    if(question == "1"):
        firstqsolver(list1, list2)

    elif(question == "2"):
        secondqsolver(list1, list2)

    elif(question == "3"):
        thirdqsolver(list1, list2)       

    elif(question == "4"):
        fourthqsolver(list1, list2) 

    elif(question == "5"):
        fifthqsolver(list1, list2)           
    
    
=======
>>>>>>> 3536fccbbe202b63f56421c0383fdab24fbad901
if __name__ == '__main__':
    main()

