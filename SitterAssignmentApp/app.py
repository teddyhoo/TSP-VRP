from flask import Flask, render_template, request
import json
from VisitAnalyzer import VisitAssigner
from TSPTW_GLPK import RouteFinder

visit_assigner = VisitAssigner('2018-05-27','doggywalkeri2', 'doggywalkeri2_password8649')
#visit_assigner.get_static_data()

sitter_info,optimal_assignment,recommendation_matrix,unassigned_list = visit_assigner.executeAssignment()

##print(sitter_info)
sitter_schedule = []


for sitter_id in sitter_info:
    avail_list = sitter_info[sitter_id]['sitter_avail']
    update = []
    for i in avail_list:
        if i == 1:
            update.append(0)
        else:
            update.append(10)
    avail_list = update
    sitter_name = sitter_info[sitter_id]['sitter_name'] 
    ##.encode("ascii")
    ##sitter_name.decode('utf-8')
    ##sitter_name = sitter_name.decode('ascii')

    sitter_schedule.append({
    'label': sitter_name,
    'data': avail_list
    })

All_Routes = []
sitter_addresses = {}

counter = 0
for sitter_id in sitter_info:
    counter += 1
    if counter <= 50:
    ##    addresses = []
        sitter_home = sitter_info[sitter_id]['sitter_home']['latlon']
        lat = float(sitter_home[0].encode("utf-8"))
        lon = float(sitter_home[1].encode("utf-8"))
        sitter_home = (lat,lon)

        #no time restriction on sitters home
        time_windows = [(0,48)]
        #initiate sitter home as first coord
        coordinates = [sitter_home]        
        sitter_home_addr = sitter_info[sitter_id]['sitter_home']['address']

        addresses = [sitter_home_addr]
        location_info = sitter_info[sitter_id]
        for location in location_info:
            if location != 'sitter_avail':
                if location != 'sitter_home':
                    if location != 'sitter_name':
                        addresses.append(sitter_info[sitter_id][location]['full_addr'])
                        coordinates.append(sitter_info[sitter_id][location]['coord'])
                        time_windows.append(sitter_info[sitter_id][location]['time_window'])

        coordinates.append(sitter_home)
        addresses.append(sitter_home_addr)
        time_windows.append((0,48))
        #avg walking speed is 1 km per 10 minutes
        #there fore travel time is 10*km
        #this is 2 times walking speed
        travel_multiplier = 1
        #service time is 15 minutes a pet
        service_time = 0
        print("=====================")
        print(sitter_id)
        print("=====================")

        sitter_addresses[sitter_info[sitter_id]['sitter_name']] = addresses
##        try:
        Route = RouteFinder()
        Route.parse_sitter_data(coordinates,time_windows,travel_multiplier,service_time)
        result = Route.solve()
        All_Routes.append(result)
##            print sitter_id,result
##        except Exception as e:
##            "couldn't find route"

#NEW GOAL
# unassigned visit locations
#        u1,u2,u3 -> don't use real unassigned addresses for presentation
#{'data':[p1,p2,p3]'label':SITTERNAME: []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/schedule')
def my_view():
    return render_template('view_schedule.html',sitter_data=sitter_schedule,recommend_data=recommendation_matrix,unassigned_labels=unassigned_list)

@app.route('/routes')
def route_view():
    return render_template('view_routes.html',route_data=All_Routes,sitter_routes=sitter_addresses)

if __name__ == "__main__":
    app.run()
