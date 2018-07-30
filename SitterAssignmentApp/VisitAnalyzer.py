
import argparse 
import urllib3
import json
import certifi

class HTTPClient:  
    def __init__(self, host): 
        self.host = host
        self.http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED', ca_certs=certifi.where()) 

        self.USERNAME = 'doggywalkeri2'
        self.PASSWORD = 'doggywalkeri2_password8649'
        self.start_date = '2018-06-06'
        self.end_date = '2018-06-06'

        self.VISIT_DATA = self.host + 'routing-endpoint.php?visits=1&unassigned=1&username=' + self.USERNAME + '&password=' + self.PASSWORD + '&start='+self.start_date+'&end=' + self.end_date
        self.SITTER_DATA =  self.host + 'routing-endpoint.php?sitters=1&all=1&username=' + self.USERNAME + '&password=' + self.PASSWORD + '&start='+self.start_date+'&end=' + self.end_date
        self.TIME_OFF_DATA = self.host + 'routing-endpoint.php?timeoff=1&bysitter=1&username=' + self.USERNAME + '&password=' + self.PASSWORD + '&start='+ self.start_date+'&end=' + self.end_date

         
    def fetch_visit_data(self): 
        response = self.http.request('GET',self.VISIT_DATA) 
        visit_data = json.loads(response.data.decode('utf-8'))
        ##print (str(visit_data))
        return visit_data 

    def fetch_sitter_data(self):
        response = self.http.request('GET',self.SITTER_DATA)
        sitter_data = json.loads(response.data.decode('utf=8'))
        ##print(str(sitter_data))
        return sitter_data

    def fetch_time_off_data(self):
        response = self.http.request('GET',self.TIME_OFF_DATA)
        print (response.data.decode('utf-8'))
        time_off_data = json.loads(response.data.decode('utf-8'))
        return time_off_data

        parser = argparse.ArgumentParser(description='HTTP Client Example') 
        parser.add_argument('--host', action="store",dest="host",  default=self.REMOTE_SERVER_HOST) 
     
        given_args = parser.parse_args()  
        host = given_args.host 
        client = HTTPClient(host) 
        visit_data = client.fetch_visit_data()
        sitter_data = client.fetch_sitter_data()
        time_off_data = client.fetch_time_off_data()

        return visit_data,sitter_data,time_off_data

class VisitAssigner():
    def __init__(self,visits_for_date,username,password):


        REMOTE_SERVER_HOST = 'https://leashtime.com/'

        client = HTTPClient(REMOTE_SERVER_HOST) 
        self.visit_data = client.fetch_visit_data()
        self.sitter_data = client.fetch_sitter_data()
        self.time_off = client.fetch_time_off_data()

        list_visits = self.visit_data['visits']
        for visit in list_visits:
            if visit['sitterid'] == '0':
                print (visit['appointmentid'] + ' --> ' + visit['timeofday'])

    


    def get_static_data(self):

        

        return self.sitter_data,self.visit_data,self.time_off

    def executeAssignment(self):
        time_off = self.time_off
        visit_data = self.visit_data
        sitter_data = self.sitter_data
        
        from math import sin, cos, sqrt, atan2, radians

        ###################
        #parse time off data
        ###################

        sitters_time_off = []
        for time_off_set in time_off:
            if time_off_set != 'timeoff':
                for timeoff in time_off_set:
                    for sitter_id in time_off_set[timeoff]:
                        if 'allday' or 'allday' in time_off_set[timeoff][sitter_id]["2018-04-19"]:
                            sitters_time_off.append(sitter_id)

        ##################
        #parse sitter data
        ##################

        all_sitter_info = {}
        for sitter in sitter_data['sitters']:
            #ignore all inactive sitters
            if sitter['active'] == '1':
                #ignore sitters with all day off
                if sitter['sitterid'] not in sitters_time_off:
                    all_sitter_info[sitter['sitterid']] = {'latlon':(sitter['lat'],sitter['lon']),'address': sitter['street1']+','+sitter['city']+','+sitter['state']+sitter['zip'],'name':sitter['sitter']}

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

        def reformat_window(time_window):
            a = time_window.split("-")[0]
            b = time_window.split("-")[1]
            
            atime = float(a.split(' ')[0].replace(":","."))    
            if ".3" in str(atime):
                atime +=.2
            if ".15" in str(atime):
                atime +=.1
                
            if a.split(" ")[1] == 'pm':
                if atime <12:        
                    atime += 12

            btime = float(b.split(' ')[0].replace(":","."))
            if ".3" in str(btime):
                btime +=.2
            if ".15" in str(btime):
                btime +=.1

            if b.split(" ")[1] == 'pm':
                if btime < 12:
                    btime += 12
                    
            if 'pm' in a:
                if 'am' in b:
                    btime = 24.0

            return (atime,btime)

        sitter_id_list = []
        addresses = []
        unassigned_window_list = []
        unassigned_lat_lons = []
        sitter_lat_lons = {}

        #master dictionaries
        unassigned_info = {}
        sitter_info = {}

        unassigned = '0'
        address_index = 0
                
        for visit in visit_data['visits']:

            #parse visit data
            sitter = visit['sitter']
            sitter_id = visit['sitterid']
            visit['status']
            full_address = visit['street1'] + "," + visit['city'] + "," + visit['state'] + visit['zip']
            lat = float(visit['lat'])
            lon = float(visit['lon'])
            coord = (lat,lon)
            times = visit['timeofday']
            TW = reformat_window(times)

            #build address list
            if full_address not in addresses:
                address_index += 1
                addresses.append(full_address)

                #GET UNASSIGNED DATA
                if sitter_id == unassigned:

                    #unassigned info
                    unassigned_info[address_index] = {'coord':coord,'time_window':TW,'full_addr':full_address}
                    #build unassigned list
                    unassigned_lat_lons.append(coord)
                    #build the time windows
                    unassigned_window_list.append(TW)

                    print (unassigned_info[address_index])

                if sitter_id != unassigned:
                    #GET ASSIGNED DATA
                    if sitter_id not in sitter_info:
                        sitter_info[sitter_id] = {address_index:{'coord':coord,'time_window':TW,'full_addr':full_address}}
                    else:
                        sitter_info[sitter_id][address_index] = {'coord':coord,'time_window':TW,'full_addr':full_address}
                        
                    if sitter_id not in sitter_lat_lons:
                        sitter_id_list.append(sitter_id)
                        sitter_lat_lons[sitter_id] = [coord]
                    else:
                        sitter_lat_lons[sitter_id].append(coord)

##        print '========================='
        #what we have so far
        sitter_lat_lons
        unassigned_lat_lons
        sitter_id_list
        all_sitter_info


        #A FULL 24 HOUR TIME WINDOW
        num_half_hours = 24*2

        #initiate sitter avail
        sitter_avail = []
        for time in range(1,num_half_hours+1,1):
            sitter_avail.append(0)

        #Build the sitter time window list
        for sitter_id in sitter_info:
            #wipe out sitter avail
            for i in range(0,len(sitter_avail),1):
                sitter_avail[i] = 0

            #get the data
            data = sitter_info[sitter_id]
            for loc in data:
                TW = data[loc]['time_window']
                if sitter_avail[int(TW[0]*2)-1] == 1:
                    c = 1
                    checker = True
                    while checker == True:
                        if sitter_avail[int(TW[0]*2)-1+c] != 1:
                            sitter_avail[int(TW[0]*2)-1+c] = 1
                            checker = False
                        c+=1
                else:
                    sitter_avail[int(TW[0]*2)-1] = 1

            availability = []
            for i in sitter_avail:
                availability.append(i)

            sitter_info[sitter_id]['sitter_avail'] = availability



        ##for sitter_id in sitter_info:
        ##    print all_sitter_info[sitter_id]['name'],sitter_info[sitter_id]['sitter_avail']

        #FEASIBILITY CHECKER
##        counter = -1
##        for loc in unassigned_info:
##            counter +=1
##            if counter ==1:
##                loc_info = unassigned_info[loc]
##                TW = loc_info['time_window']
##                for sitter_id in sitter_info:
##                    sitter_av = sitter_info[sitter_id]['sitter_avail']
##                    TW_start = int(TW[0]*2)-1
##                    TW_end = int(TW[1]*2)-1
##                    list_length = TW_end - TW_start
##        ##            print sitter_id, sitter_av[TW_start:TW_end], [1 for i in range(0,list_length,1)]
##                    if sitter_av[TW_start:TW_end] == [1 for i in range(0,TW_end - TW_start,1)]:
##                        print sitter_id, "INFEAS",sitter_av[TW_start:TW_end]
##                    else:
##                        print sitter_id, "FEAS",sitter_av[TW_start:TW_end]


        #before
        ##before_sitter_info = sitter_info['189']
        ##print before_sitter_info
        ##print '======================'
        penalty_columns = []
        optimal_assignment = {}
        recommendation_matrix = {}
        #old
        ##for unassigned in unassigned_lat_lons:
        ##    print unassigned


        ##################################
        #IF NO VISITS THIS WILL BREAK!!!!!!
        ################################# 
        for loc_id in unassigned_info:
            loc_info = unassigned_info[loc_id]
    
            TW = loc_info['time_window']    

            lat1 = loc_info['coord'][0]
            lon1 = loc_info['coord'][1]

            sitter_penalty_lookup = {}
            penalty_column = []
            sitter_list_for_pc = []
            for sitter_id in sitter_info:
                #initiate distance calc
                distance_aggregate_calc = 0

                #get the locations of the sitters
                sitter_coords = sitter_lat_lons[sitter_id]

                #get sitter availability
                sitter_av = sitter_info[sitter_id]['sitter_avail']
                TW_start = int(TW[0]*2-1)
                TW_end = int(TW[1]*2-1)

                #check for feasibility
                #no penalty as the visit is feasible
                visit_feas = 0
                if sitter_av[TW_start:TW_end] == [1 for i in range(0,TW_end - TW_start,1)]:
                    #large penalty as the visit is infeasible
                    visit_feas = 100000
         
                for coord in sitter_coords:
                    lat2 = coord[0]
                    lon2 = coord[1]
                    #sum all the distances together
                    distance_aggregate_calc += calculate_distance(lat1,lon1,lat2,lon2)
                    
                #get average distance to unassigned
                avg_dist = distance_aggregate_calc/len(sitter_coords)
                                        #avg distace  #penalty for the number pre-assigned
                sitter_penalty_score = avg_dist + len(sitter_coords)*0.5 + visit_feas

                sitter_penalty_lookup[sitter_id] = sitter_penalty_score
                sitter_list_for_pc.append(sitter_id)
                penalty_column.append(sitter_penalty_score)            

            ###################################
            # BUILD THE RECOMMENDATION OUTPUT #
            ###################################

            for sitter_id in sitter_penalty_lookup:
                sitter_name = all_sitter_info[sitter_id]['name']
                pen = sitter_penalty_lookup[sitter_id]
                if sitter_name not in recommendation_matrix:
                    pen = sitter_penalty_lookup[sitter_id]
                    recommendation_matrix[sitter_name] = [pen]
                else:
                    recommendation_matrix[sitter_name].append(pen)
            #############################################
            

            penalty_columns.append(penalty_column)

            #optimal assignment calculations
            min_sitter_id = min(sitter_penalty_lookup,key=sitter_penalty_lookup.get)
            sitter_lat_lons[min_sitter_id].append(loc_info['coord'])

            #Add all new information to the sitter info
            current_avail = sitter_info[min_sitter_id]['sitter_avail']
            
            if current_avail[TW_start] == 1:
                c = 1
                checker = True
                while checker == True:
                    if sitter_avail[int(TW[0]*2)-1+c] != 1:
                        sitter_avail[int(TW[0]*2)-1+c] = 1
                        checker = False
                    c+=1
            else:
                current_avail[int(TW[0]*2)-1] = 1

            availability = []
            for i in current_avail:
                availability.append(i)

            sitter_info[min_sitter_id]['sitter_avail'] = availability
            sitter_info[min_sitter_id][loc_id] = loc_info
                
            if min_sitter_id not in optimal_assignment:
                optimal_assignment[min_sitter_id] = [loc_info['coord']]
            else:
                optimal_assignment[min_sitter_id].append(loc_info['coord'])

##all_sitter_info[sitter['sitterid']] = {'latlon':(sitter['lat'],sitter['lon']),'address': sitter['street1']+','+sitter['city']+','+sitter['state']+sitter['zip'],'name':sitter['sitter']}
            for sitter_id in sitter_info:

                sitter_info[sitter_id]['sitter_name'] = all_sitter_info[sitter_id]['name']
                sitter_info[sitter_id]['sitter_home'] = {'latlon':all_sitter_info[sitter_id]['latlon'],'address':all_sitter_info[sitter_id]['address']}

##        print "=================="
##        print "OPTIMAL ASSIGNMENT"
##        print "=================="
##        for i in optimal_assignment:
##            print i, optimal_assignment[i]    
##        
##        
##        print "===================================================================="
##        print "================ PENALTY MATRIX ===================================="
##        print "===================================================================="
##        c = 0
##        for sitter_id in sitter_id_list:
##            print sitter_id,
##            for penalty_column in penalty_columns:
##                print penalty_column[c],
##            print " "
##            c += 1
##        for sitter_id in sitter_info:
##            print sitter_info[sitter_id]['sitter_avail']

        #recommendation matrix print out
        #goal -> {{'label':sitter_name},
        reformat = []
        for sitter_name in recommendation_matrix:
            data = recommendation_matrix[sitter_name]
            best_value = min(data)
            update = []
            for i in data:
                if i > 100:
                    u = 20
                else:
                    u = i
                if i == best_value:
                    u = 0
                update.append(u)
            data = update
            reformat.append({'label':sitter_name.encode('ascii'),'data':data})
        recommendation_matrix = reformat
    
        unassigned_location_list = []
        for loc_id in unassigned_info:
            unassigned_location_list.append(str(loc_id))

        return sitter_info, optimal_assignment,recommendation_matrix,unassigned_location_list


if __name__ == '__main__':
    visit_assigner = VisitAssigner()
    visit_assigner.get_static_data()
    sitter_info,optimal_assignment,penalty_matrix,unassigned_info = visit_assigner.executeAssignment()
    
