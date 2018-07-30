from pymprog import *
from math import sin, cos, sqrt, atan2, radians

class RouteFinder():
    def __init__(self):
        self
        
    def capture_data(self,travel_time,time_windows,siteNames):
        self.travel_time = travel_time
        self.time_windows = time_windows
        self.siteNames = siteNames

    def parse_sitter_data(self,coordinates,time_windows,travel_multiplier,service_time):

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

        def dist_to_time(dist,travel_multiplier,service_time):
            #avg walking speed is 1 km per 10 minutes
            #there fore travel time is 10*km
            travel_time = dist*travel_multiplier

            #time to service the pup at very least is 15min
            total_time = travel_time + service_time

            #convert total time into hours to match windows
            return total_time/60
        
        travel_time = []
        counter = 0
        for first_coord in coordinates:
            travel_time.append([])
            for second_coord in coordinates:
                if first_coord == second_coord:
                    time = 0
                else:
                    lat1 = first_coord[0]
                    lon1 = first_coord[1]
                    lat2 = second_coord[0]
                    lon2 = second_coord[1]
                    dist = calculate_distance(lat1, lon1, lat2, lon2)
                    time = dist_to_time(dist,travel_multiplier,service_time)
                    #convert to time                    
                travel_time[counter].append(time)
            counter +=1
        
        self.travel_time = travel_time
        self.time_windows = time_windows
        self.siteNames = coordinates
        
    def solve(self):
        tt = self.travel_time
        tw = self.time_windows
        names = self.siteNames
        depot = 0
        nodes = range(len(names))
        no_depot_set = nodes[1:len(nodes)-1]
        auxilary_node = len(nodes)+1

        #time window variables
        a = []
        b = []
        M = 0
        for window in tw:
            a.append(window[0])
            b.append(window[1])
            M += window[1]

        begin('assign')
        
        #build variables
        arcs = []
        for i in nodes:
            for j in nodes:
                if i != j:
                    arcs.append((i,j))
        
        #decision variable x
        x=var('x',arcs,kind=bool)

        #subtour elimination u
        u=var('u',nodes,kind=int)
        s=var('s',nodes,kind=float)

        #constraint 2.1 (objective)
        minimize(sum(tt[i][j]*x[i,j] for i in nodes for j in nodes if i != j))

        #constraint 2.2
        for i in nodes:
            sum(x[i,j] for j in nodes if i != j) == 1

        for j in nodes:
            sum(x[i,j] for i in nodes if i != j) == 1

        

        n = len(nodes)-1
        for i in nodes:
            for j in nodes:
                if i != 0:
                    if i != j:
                        u[i]-u[j]+len(nodes)*x[i,j] <= len(nodes)-1

        for i in nodes:
            a[i] <= s[i] <= b[i]
            
        for i in nodes:
            for j in nodes:
                if i != 0:
                    if i != j:                    
                        s[i]-s[j]+(b[i]+tt[i][j]-a[j])*x[i,j] <= b[i] - a[j]



        solver(int)#,presolve=glpk.GLP_ON,pp_tech=glpk.GLP_PP_ALL,cov_cuts=glpk.GLP_ON,presolve=glpk.GLP_ON
        solve()#,out_frq=1,it_lim=1,tm_lim=1000


        arcsol = []
        assign = [(i,j) for i in nodes for j in nodes]
        for i,j in arcs:
            if x[i,j].primal >0:
                arcsol.append((i,j))

        result_set = None

        #ROUTE FINDER
        Single_Route = []
        counter = 0
        for arc in arcsol:
            if arc[0] == 0:
                counter += 1
                if arc[0] not in Single_Route:
                    Single_Route.append(arc[0])
                    Single_Route.append(arc[1])
            if len(Single_Route) > 0:
                next_one = Single_Route[len(Single_Route)-1]
                for arc in arcsol:
                    if next_one == 0:
                        break
                    if arc[0] == next_one:
                        Single_Route.append(arc[1])
        Named_Route = []
        for i in Single_Route:
            Named_Route.append(str(names[i]))
##        solver(int,br_tech=glpk.GLP_BR_PCH)
##        solver(br_tech=glpk.GLP_BR_PCH)
##        solver(br_tech=glpk.BR_DTH)
#options
#https://github.com/langit/pymprog/blob/master/pymprog.py
#https://github.com/heisencoder/route-finder/blob/master/third_party/lib/python/pymprog.py
#http://www.cnd.mcgill.ca/~ivan/it_ineq_script/python%20LP%20solvers/pympl.4.2/html/solvopt.html      
##        glpk.GLP_MSG_OFF 
        #simplex presolve option
##        solver(float,msg_lev=glpk.GLP_OFF)
##        solve(lm_tim=1)
##        solve(tm_lim=1,out_frq=1,it_lim=1)
##        solver(float,msg_lev=glpk.GLP_MSG_OFF,gmi_cuts=glpk.GLP_ON,pp_tech=glpk.GLP_PP_ALL,mir_cuts=glpk.GLP_ON,cov_cuts=glpk.GLP_ON,clq_cuts=glpk.GLP_ON,msg_lev=glpk.GLP_ON,presolve=glpk.GLP_ON,tm_lim=1,out_frq=1,it_lim=1)
#        save(sol='10.sol')
#        model.setParam('OutputFlag',True)
#        model.optimize()
#        # Print Solution
#        if model.status == GRB.Status.OPTIMAL:
#            solution = model.getAttr('x')
#            arcsol = []
#            for i in range(0,len(solution),1):
#                if solution[i] == 1:
#                    if i <= len(vehicle_arcs):
#                        print vehicle_arcs[i] , " : ", solution[i]
#                        arcsol.append(arcs[i])
        return Named_Route

if __name__ == "__main__":

    #node list data
    #the directed set, goes back to the depot at the end
    siteNames = ["Depot","Loc 1","Loc 2","Loc 3","Loc 4",
                 "Loc 5","Loc 6","Depot"]

    sites = range(len(siteNames))
    clients = sites[1:]
    #print "THE LENGTH OF CLIENTS: " + str(len(clients))

    #demand data
    demand = [ 0,1000, 1200, 1600, 1400, 1200, 1000, 0]
    demandsum = 0
    for i in demand:
        demandsum += i
    #print "THE DEMAND SUM IS: " + str(demandsum)

    #distance data
    dist = [[0, 59.3, 31.6, 47.8, 34.2, 47.1, 36.1, 31.9],
            [62.2, 0, 27.9, 21.0, 77.5, 30.0, 27.1, 44.7],
            [32.2, 27.7, 0, 16.2, 50.0, 39.4, 24.9, 42.6],
            [50.7, 21.0, 16.4, 0, 66.1, 49.7, 35.2, 52.9],
            [34.4, 77.4, 49.6, 65.9, 0, 80.8, 67.1, 65.5],
            [46.9, 30.1, 39.6, 49.7, 80.5, 0, 14.4, 15.0],
            [36.9, 27.1, 25.2, 35.2, 67.1, 14.4, 0, 17.6],
            [31.9, 44.7, 62.8, 52.8, 65.6, 15.0, 17.6, 0]]

    

    #capacity of bus data
    capacity = 50000
    vehicleTW = {1:[[1,24]],2:[[1,24]]}
    dist = [[0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0]]
    travel_time = dist
    time_windows = [[1,19],[1,3],[1,4],[1,5],[1,7],[1,15],[1,24],[11,25]]


    #execute the function
    problem = RouteFinder()
    problem.capture_data(travel_time,time_windows,siteNames)
    result = problem.solve()

