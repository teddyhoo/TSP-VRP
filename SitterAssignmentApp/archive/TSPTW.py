from gurobipy import *
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
##        print tt
        depot = 0
        nodes = range(len(names))
        no_depot_set = nodes[1:len(nodes)-1]
        auxilary_node = len(nodes)+1

        a = []
        b = []
        M = 0
        for window in tw:
            a.append(window[0])
            b.append(window[1])
            M += window[1]

        model = Model('TSPTW')

        x = {}
        set_of_arcs = []
        routes = {}
        for i in nodes:
            for j in nodes:
                if i != j:
                    x[i,j] = model.addVar(vtype=GRB.BINARY,name="routes")
                    set_of_arcs.append((i,j))

        u = {}
        s = {}
        for i in nodes:
            u[i] = model.addVar(vtype=GRB.INTEGER)
            s[i] = model.addVar(vtype=GRB.CONTINUOUS)

        
        model.update()

        model.setObjective(quicksum(tt[i][j]*x[i,j] for i in nodes for j in nodes if i != j),GRB.MINIMIZE)
        
        for j in nodes:
            model.addConstr(quicksum( x[i,j] for i in nodes if i != j) == 1)
            
        for i in nodes:
            model.addConstr(quicksum( x[i,j] for j in nodes if i != j) == 1)

        n = len(nodes)-1
        for i in nodes:
            for j in nodes:
                if i != 0:
                    if i != j:
                        model.addConstr(u[i]-u[j]+len(nodes)*x[i,j] <= len(nodes)-1)
    
        for i in nodes:
            model.addConstr(a[i] <= s[i] <= b[i])
            
        for i in nodes:
            for j in nodes:
                if i != 0:
                    if i != j:                    
                        model.addConstr(s[i]-s[j]+(b[i]+tt[i][j]-a[j])*x[i,j] <= b[i] - a[j])
                    
                
        model.setParam('OutputFlag',False)
        model.optimize()
##        model.write("solution.sol")
        # Print Solution
        counter = 0
        indexer = 0
        val = 0
        if model.status == GRB.Status.OPTIMAL:
            solution = model.getAttr('x')
            arcsol = []
            for i in range(0,len(solution),1):
                if i < len(set_of_arcs)-1:
                    if solution[i] == 1:
                        indexer+=1
##                        print str(indexer)+" "+str(set_of_arcs[i]) , " : ", solution[i]
                        arcsol.append(set_of_arcs[i])


        #COUNT NUMBER OF ROUTES
        counter = 0
        counter_list = []
        for arc in arcsol:
            if arc[0] == 0:
                counter_list.append(counter)
                counter += 1

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
            
        return Named_Route

if __name__ == "__main__":
    siteNames = ["Depot","Loc 1","Loc 2","Loc 3","Loc 4",
                 "Loc 5","Loc 6","Loc 7"]

    #print "THE DEMAND SUM IS: " + str(demandsum)
    travel_time = [[0, 1, 9, 9, 9, 9, 9, 9],
                   [9, 0, 9, 1, 9, 9, 9, 9],
                   [9, 9, 0, 9, 9, 9, 9, 1],
                   [9, 9, 1, 0, 9, 9, 9, 9],
                   [9, 9, 9, 9, 0, 1, 9, 9],
                   [9, 9, 9, 9, 9, 0, 1, 9],
                   [1, 9, 9, 9, 9, 9, 0, 9],
                   [9, 9, 9, 9, 1, 9, 9, 0]]

    time_windows = [(0,7),(0,4),(0,5),(0,6),(0,7),(0,7),(0,6),(0,5)]
    
    #execute the function
    problem = RouteFinder()
    problem.capture_data(travel_time,time_windows,siteNames)
    result = problem.solve()
    
##    coords = [(38.8311, -77.0599), (38.8298, -77.063), (38.811, -77.0592), (38.8109, -77.0546), (38.8268, -77.0796), (38.83, -77.0635), (38.8236, -77.0651), (38.8279, -77.062), (38.8256, -77.0581), (38.8232, -77.0726)]
##    time_windows = [(0, 48), (10.0, 12.0), (11.0, 13.0), (13.0, 15.0), (12.0, 14.0), (10.0, 11.0), (10.5, 11.5), (11.5, 12.5), (16.0, 18.0), (12.0, 14.0)]
##    problem = RouteFinder()
##    problem.parse_sitter_data(coords,time_windows)
##    problem.solve()
