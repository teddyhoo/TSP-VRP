import numpy as np
import scipy.spatial as ssp
import numpy.random as nprnd
import matplotlib.pyplot as plt
from matplotlib import animation
import argparse 
import urllib3
import json
import certifi
import re
from math import sin, cos, sqrt, atan2, radians
from selenium import webdriver


## git commit number one

numLow = 1
numHigh = 1000
m = 10
ims = []
unassigned_visits = []
visits_by_sitter = {}
depots_sitter = {}
total_distance_all = 0

class HTTPClient: 
 
    def __init__(self, host): 
        self.host = host
        self.http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED', ca_certs=certifi.where()) 
 
    def fetch_visit_data(self): 
        response = self.http.request('GET',VISIT_DATA) 
        visit_data = json.loads(response.data.decode('utf-8'))
        return visit_data 

    def fetch_sitter_data(self):
        response = self.http.request('GET',SITTER_DATA)
        sitter_data = json.loads(response.data.decode('utf=8'))
        return sitter_data

    def fetch_time_off_data(self):
        response = self.http.request('GET',TIME_OFF_DATA)
        time_off_data = json.loads(response.data.decode('utf-8'))
        return time_off_data
 
USERNAME = 'doggywalkeri2'
PASSWORD = 'doggywalkeri2_password8649'
start_date = '2018-07-24'
end_date = '2018-07-24'

REMOTE_SERVER_HOST = 'https://leashtime.com/'
VISIT_DATA = REMOTE_SERVER_HOST + 'routing-endpoint.php?visits=1&unassigned=1&username=' + USERNAME + '&password=' + PASSWORD + '&start='+start_date+'&end=' + end_date
SITTER_DATA = REMOTE_SERVER_HOST + 'routing-endpoint.php?sitters=1&all=1&username=' + USERNAME + '&password=' + PASSWORD + '&start='+start_date+'&end=' + end_date
TIME_OFF_DATA = REMOTE_SERVER_HOST + 'routing-endpoint.php?timeoff=1&bysitter=1&username=' + USERNAME + '&password=' + PASSWORD + '&start='+start_date+'&end=' + end_date



def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    latitude_start = radians(lat1)
    longitude_start = radians(lon1)
    latitude_end = radians(lat2)
    longitude_end = radians(lon2)
    dlon = longitude_end - longitude_start
    dlat = latitude_end - latitude_start
    a = sin(dlat / 2)**2 + cos(latitude_end) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance

def plotcities(opttour,xys):
    #Plots the cities on a square
    #Input: list of 2 lists with x,y coordinates on each list
    xy1 = xys[0][:]
    xy2 = xys[1][:]
    #Sort according to latest tour optimization
    xy1 = [xy1[i] for i in opttour]
    xy2 = [xy2[i] for i in opttour]
    #Make it a cycle
    xy1.append(xy1[0])
    xy2.append(xy2[0])
    ims.append(plt.plot(xy1, xy2, linestyle = '-', marker ='o', color = 'b', markerfacecolor = 'red'))
    plt.ylabel('original path')

def genDistanceMat(x,y):
    X=np.array([x,y])
    distMat=ssp.distance.pdist(X.T)
    sqdist=ssp.distance.squareform(distMat)
    return sqdist

def calcTourLength(Dist, hamPath):
    tourLength=sum(Dist[hamPath[0:-1], hamPath[1:len(hamPath)]])
    tourLength+=Dist[hamPath[-1],hamPath[0]]
    return tourLength

def calculateTotalDistance(numCities, optlist, visit_list):
    
    total_all = 0
    for i in range(numCities):
        opt_index = optlist[i]
        ##print ('['+str(i)+'] Opt index val: ' + str(opt_index))       
        visit_dic = visit_list[opt_index]
        lat = float(visit_dic['lat'])
        lon = float(visit_dic['lon'])

        if i > 0 and i < numCities:
            opt_index_2 = optlist[i-1]
            ##print ('['+str(i)+'] Opt 2 index val: ' + str(opt_index_2))       
            visit_dic_2 = visit_list[opt_index_2]
            lat2 = float(visit_dic_2['lat'])
            lon2 = float(visit_dic_2['lon'])
            d = calculate_distance(lat,lon,lat2,lon2)
            ##print("Distance:  " + str(d))                
            total_all = total_all + d

    ##print ('Total Distance: ' + str(total_all))

def runAlgo(numCities, xcities, ycities,visit_array):

    beginTourLen = 0

    if numCities > 3:
        Dist=np.zeros((numCities,numCities))
        Dist = genDistanceMat(xcities, ycities)
        optlist = list(range(0, numCities))
        improvement=1
        fig1 = plt.figure()
        beginTourLen = calcTourLength(Dist,optlist) * 100
        print ('Tour distance: ' + str(beginTourLen))
        print ('Pre Optimize DISTANCE: ')
        calculateTotalDistance(numCities,optlist,visit_array)

        while (improvement > 0):    #Check for every pair of cities that are neighbors in the tour whether improvement can be found
            bestTourLength = calcTourLength(Dist, optlist)
            bestListSoFar = optlist
            improvement = -1
            total_improvement = 0

            print ('Best tour length: ' + str(bestTourLength) + ', bestListSoFar: ' + str(bestListSoFar))
            plotcities(optlist, [xcities,ycities])
            for i in range(0, len(optlist)):
                for j in range(2, len(optlist)-1):

                    tempOptList = optlist[0:j]+optlist[:j-1:-1]

                    tempTourLength = calcTourLength(Dist, tempOptList)

                    if(tempTourLength + 10e-12 < bestTourLength):

                        improvement = bestTourLength - tempTourLength
                        total_improvement = total_improvement + improvement
                        bestListSoFar = tempOptList
                        bestTourLength = tempTourLength
                        plotcities(optlist, [xcities,ycities])

                        ##calculateTotalDistance(numCities,optlist,visit_array)

                    if(bestTourLength+10e-12 < calcTourLength(Dist, optlist)):

                        optlist = bestListSoFar
                        calculateTotalDistance(numCities,optlist,visit_array)
                        for visit_dic in visit_array:
                            if visit_dic['appointmentid'] != 'DEPOT':
                                print (visit_dic['timeofday'] + '--> ' + ', client: ' + visit_dic['client'])
                        break

                    optlist = [optlist[-1]] + optlist[0:-1]

        
        print('End tour: '  + str(optlist)) 
        calculateTotalDistance(numCities,optlist,visit_array)
        end_tour = calcTourLength(Dist,optlist) * 100
        print ('End tour length: ' + str(end_tour))
        savings = beginTourLen - end_tour
        print ('SAVINGS: ' + str(savings))
        print ('\n\n------------************-----------\n')
        plotcities(optlist, [xcities,ycities])
        im_ani = animation.ArtistAnimation(fig1, ims, interval=1200, repeat_delay=1200, blit=True)
        plt.show()

def optimizeSitter(visits_by_sitter):

    sitter_visits_keys = visits_by_sitter.keys()

    
    for key in sitter_visits_keys:
            visit_array = visits_by_sitter[key]

            print ('------------------------------')
            print ('Sitter id: ' + key)
            print ('------------------------------')
            xcities = []
            ycities = []
            count = 0

            total_service_time = 0
            for visit_dic in visit_array:
                if 'lat' in visit_dic and 'lon' in visit_dic:
                    if visit_dic['appointmentid'] == 'DEPOT' and visit_dic['lat'] != None and visit_dic['lon'] != None:
                        print('DEPOT: ' + visit_dic['lat'] + ', ' + visit_dic['lon'])
                    elif visit_dic['lat'] == None or visit_dic['lon'] == None:
                        print ('----------------->' + visit_dic['client'])
                    else:
                        ##print('['+ str(count) + ']' + 'time window: ' + visit_dic['timeofday'] + ' at: ' + visit_dic['lat'] + ', ' + visit_dic['lon'] + ', client: ' + visit_dic['client'] + ', sitter: ' + visit_dic['sitter'] )
                        
                        latitude = float(visit_dic['lat'])
                        longitude = float(visit_dic['lon'])
                        service_time = str(visit_dic['hours'])

                        sitter_visit_times = calcTimeWindows(visit_dic['timeofday'], visit_dic['appointmentid'])
                        total_service_time = total_service_time + int(sitter_visit_times['service_time'])

                        xcities.append(latitude)
                        ycities.append(longitude)
                        count = count + 1

            print ('total service time: ' + str(total_service_time))
            numCities = len(xcities) 
            runAlgo(numCities,xcities,ycities,visit_array)

def calcTimeWindows(time_data, appointmentid):
    time_window_regex = re.compile(r'([0-9]+)\:([0-9]+)\s([A-Za-z]+)\-([0-9]+):([0-9]+)\s([A-Za-z]+)')
    results = time_window_regex.match(time_data)
    if results != None:
        match_groups = results.group()
        time_begin = int(results.group(1))
        time_begin_min = int(results.group(2))
        am_pm_begin = results.group(3)
        time_end = int(results.group(4))
        time_end_min = int(results.group(5))
        am_pm_end = results.group(6)

        if am_pm_begin == 'pm':
            if time_begin != 12:
                time_begin = time_begin + 12
            else:
                time_begin = int('12')

        if am_pm_end == 'pm':
            if time_end != '12':
                time_end = time_end + 12
            else:
                time_end = '12'

        time_diff = (time_end - time_begin) * 60

        visit_time_var = {}
        visit_time_var[appointmentid] = appointmentid
        visit_time_var['begin'] = str(time_begin)
        visit_time_var['end'] = str(time_end)
        visit_time_var['travel_time'] = str(time_diff)
        visit_time_var['service_time'] = '30'

        if time_begin_min == time_end_min:
            print ('TIME WINDOW MINS: ' + str(time_diff))
        elif time_begin_min != time_end_min:
            print ('DIFF HALF HOUR: ')


        return visit_time_var

def assignVisitsSitters(visit_data):
    visits_by_sitter = {}
    visit_keys = visit_data.keys()

    for visit_keys_sitter in visit_keys:
        if visit_keys_sitter == 'visits':
            visit_j = visit_data[visit_keys_sitter]
            for visit_dic in visit_j:
                dic_keys = visit_dic.keys()

                apointment_id = ''
                sitter_profile = {}

                for key in dic_keys:
                    if visit_dic[key] != None:
                        if key == 'appointmentid':
                            appointment_id = visit_dic[key]
                        elif key == 'sitterid':
                            sitterid = str(visit_dic[key])
                            if sitterid in depots_sitter:
                                sitter_profile = depots_sitter[sitterid]

                if sitterid == '0':
                    unassigned_visits.append(visit_dic)

                if sitterid in visits_by_sitter:
                    visits_for_sitter = []
                    visits_for_sitter = visits_by_sitter[sitterid]
                    visits_for_sitter.append(visit_dic)
                    visits_by_sitter[sitterid]= visits_for_sitter
                else:
                    visits_for_sitter = []
                    depot = {}
                    if 'lat' in sitter_profile and 'lon' in sitter_profile:
                        if sitter_profile['lat'] != None and sitter_profile['lon'] != None:
                            depot['appointmentid'] = 'DEPOT'
                            depot['lat'] = str(sitter_profile['lat'])
                            depot['lon'] = str(sitter_profile['lon'])
                            depot['timeofday'] = 'BEGIN'
                            depot['hours'] = 'NONE'
                            visits_for_sitter.append(depot)
                        visits_for_sitter.append(visit_dic)
                        visits_by_sitter[sitterid] = visits_for_sitter

    optimizeSitter(visits_by_sitter)

def createVisitsBySitter(visit_data, sitter_data):
    visit_keys = visit_data.keys()   
    sitter_array_of_dict = sitter_data['sitters']

    for sitter_dict in sitter_array_of_dict:
        active = str(sitter_dict['active'])
        if active == '1':
            if 'lat' in sitter_dict and 'lon' in sitter_dict:
                if sitter_dict['lat'] != None and sitter_dict['lon'] != None:
                    id_sitter = str(sitter_dict['sitterid'])
                    depots_sitter[id_sitter] = sitter_dict
    assignVisitsSitters(visit_data)


parser = argparse.ArgumentParser(description='HTTP Client Example') 
parser.add_argument('--host', action="store",dest="host",  default=REMOTE_SERVER_HOST) 
given_args = parser.parse_args()  
host = given_args.host 
client = HTTPClient(host) 
visit_data = client.fetch_visit_data()
sitter_data = client.fetch_sitter_data()

createVisitsBySitter(visit_data, sitter_data)





            





