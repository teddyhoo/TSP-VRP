
import argparse 
import urllib3
import json


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
        print (response.data.decode('utf-8'))
        time_off_data = json.loads(response.data.decode('utf-8'))
        return time_off_data

        parser = argparse.ArgumentParser(description='HTTP Client Example') 
        parser.add_argument('--host', action="store",dest="host",  default=REMOTE_SERVER_HOST) 
     
        given_args = parser.parse_args()  
        host = given_args.host 
        client = HTTPClient(host) 
        visit_data = client.fetch_visit_data()
        sitter_data = client.fetch_sitter_data()
        time_off_data = client.fetch_time_off_data()

        return visit_data,sitter_data,time_off_data

class VisitAssigner():

    def get_static_data(self):
        visit_data ={u'visitcount': 204,
                         u'visits': [{u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22304', u'appointmentid': u'848900', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Cam', u'completed': None, u'lon': u'-77.1168', u'clientid': u'9', u'hours': u'00:00', u'lat': u'38.8099', u'state': u'VA', u'client': u'@9', u'servicecode': u'19', u'street1': u'191 Somervelle St', u'sitterid': u'27', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'848901', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Cam', u'completed': None, u'lon': u'-77.0936', u'clientid': u'945', u'hours': u'00:00', u'lat': u'38.8128', u'state': u'VA', u'client': u'@945', u'servicecode': u'19', u'street1': u'134 Sylvan Court', u'sitterid': u'27', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848902', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Anna', u'completed': None, u'lon': u'-77.0845', u'clientid': u'956', u'hours': u'00:00', u'lat': u'38.8098', u'state': u'VA', u'client': u'@956', u'servicecode': u'19', u'street1': u'1100 Quaker Hill Dr', u'sitterid': u'212', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848903', u'service': u'Monthly 30 Min Visit - 3 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.062', u'clientid': u'143', u'hours': u'00:00', u'lat': u'38.8273', u'state': u'VA', u'client': u'@143', u'servicecode': u'21', u'street1': u'7 W. Caton Ave.', u'sitterid': u'222', u'timeofday': u'12:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'848904', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Karen', u'completed': None, u'lon': u'-77.0714', u'clientid': u'1311', u'hours': u'00:00', u'lat': u'38.7262', u'state': u'VA', u'client': u'@1311', u'servicecode': u'19', u'street1': u'8503 Camden St', u'sitterid': u'121', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'848905', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Karen', u'completed': None, u'lon': u'-77.1242', u'clientid': u'681', u'hours': u'00:00', u'lat': u'38.7058', u'state': u'VA', u'client': u'@681', u'servicecode': u'20', u'street1': u'5205 Burke Dr', u'sitterid': u'121', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848906', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Robbyn', u'completed': None, u'lon': u'-77.0538', u'clientid': u'1478', u'hours': u'00:00', u'lat': u'38.8232', u'state': u'VA', u'client': u'@1478', u'servicecode': u'19', u'street1': u'1813 Leslie Ave', u'sitterid': u'251', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848907', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Ron', u'completed': None, u'lon': u'-77.0479', u'clientid': u'1142', u'hours': u'00:00', u'lat': u'38.8139', u'state': u'VA', u'client': u'@1142', u'servicecode': u'20', u'street1': u'811 Parker Gray School Way', u'sitterid': u'234', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848908', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Ron', u'completed': None, u'lon': u'-77.0475', u'clientid': u'1502', u'hours': u'00:00', u'lat': u'38.8119', u'state': u'VA', u'client': u'@1502', u'servicecode': u'19', u'street1': u'625 N Alfred St', u'sitterid': u'234', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ARLINGTON', u'zip': u'22206', u'appointmentid': u'848909', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.092', u'clientid': u'358', u'hours': u'00:00', u'lat': u'38.8341', u'state': u'VA', u'client': u'@358', u'servicecode': u'19', u'street1': u'4612 S. 34th St.', u'sitterid': u'256', u'timeofday': u'1:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'848910', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Karen', u'completed': None, u'lon': u'-77.1081', u'clientid': u'1625', u'hours': u'00:00', u'lat': u'38.7235', u'state': u'VA', u'client': u'@1625', u'servicecode': u'48', u'street1': u'8637 Gateshead Road', u'sitterid': u'121', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848911', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0601', u'clientid': u'1900', u'hours': u'00:00', u'lat': u'38.812', u'state': u'VA', u'client': u'@1900', u'servicecode': u'20', u'street1': u'15 E Walnut St', u'sitterid': u'222', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848913', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.045', u'clientid': u'903', u'hours': u'00:00', u'lat': u'38.7968', u'state': u'VA', u'client': u'@903', u'servicecode': u'19', u'street1': u'728 S Royal St', u'sitterid': u'260', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848916', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0593', u'clientid': u'1835', u'hours': u'00:00', u'lat': u'38.8197', u'state': u'VA', u'client': u'@1835', u'servicecode': u'20', u'street1': u'212 E. Nelson Ave', u'sitterid': u'255', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848917', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0545', u'clientid': u'2012', u'hours': u'00:00', u'lat': u'38.8026', u'state': u'VA', u'client': u'@2012', u'servicecode': u'19', u'street1': u'305 S. Payne St.', u'sitterid': u'260', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848918', u'service': u'30 Min Flex Visit - 2 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0604', u'clientid': u'1380', u'hours': u'00:00', u'lat': u'38.8153', u'state': u'VA', u'client': u'@1380', u'servicecode': u'56', u'street1': u'23 E Braddock Rd', u'sitterid': u'222', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22315', u'appointmentid': u'848919', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1567', u'clientid': u'265', u'hours': u'00:00', u'lat': u'38.7557', u'state': u'VA', u'client': u'@265', u'servicecode': u'19', u'street1': u'6234 Walkers Croft Way', u'sitterid': u'274', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848921', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Ron', u'completed': None, u'lon': u'-77.043', u'clientid': u'874', u'hours': u'00:00', u'lat': u'38.8191', u'state': u'VA', u'client': u'@874', u'servicecode': u'113', u'street1': u'1407 E. Abingdon Dr, #6', u'sitterid': u'234', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'848922', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.0568', u'clientid': u'1106', u'hours': u'00:00', u'lat': u'38.8591', u'state': u'VA', u'client': u'@1106', u'servicecode': u'113', u'street1': u'1751-A S Hayes St', u'sitterid': u'269', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'848923', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Karen', u'completed': None, u'lon': u'-77.0601', u'clientid': u'1692', u'hours': u'00:00', u'lat': u'38.7249', u'state': u'VA', u'client': u'@1692', u'servicecode': u'114', u'street1': u'8513 Buckboard Drive', u'sitterid': u'121', u'timeofday': u'11:30 am-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848924', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Barbara', u'completed': None, u'lon': u'-77.0472', u'clientid': u'1828', u'hours': u'00:00', u'lat': u'38.8147', u'state': u'Va.', u'client': u'@1828', u'servicecode': u'113', u'street1': u'928 N. Alfred St.', u'sitterid': u'177', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848925', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0614', u'clientid': u'1984', u'hours': u'00:00', u'lat': u'38.822', u'state': u'VA', u'client': u'@1984', u'servicecode': u'114', u'street1': u'102 E Cliff St', u'sitterid': u'255', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848926', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0494', u'clientid': u'2022', u'hours': u'00:00', u'lat': u'38.8071', u'state': u'Va', u'client': u'@2022', u'servicecode': u'119', u'street1': u'913 Cameron St.', u'sitterid': u'260', u'timeofday': u'10:00 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848927', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0494', u'clientid': u'2022', u'hours': u'00:00', u'lat': u'38.8071', u'state': u'Va', u'client': u'@2022', u'servicecode': u'119', u'street1': u'913 Cameron St.', u'sitterid': u'260', u'timeofday': u'2:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22306', u'appointmentid': u'848929', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Keith', u'completed': None, u'lon': u'-77.0734', u'clientid': u'2056', u'hours': u'00:00', u'lat': u'38.7599', u'state': u'VA', u'client': u'@2056', u'servicecode': u'19', u'street1': u'7225 Ludwood Court', u'sitterid': u'276', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848930', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Anna', u'completed': None, u'lon': u'-77.0857', u'clientid': u'1', u'hours': u'00:00', u'lat': u'38.8115', u'state': u'VA', u'client': u'@1', u'servicecode': u'19', u'street1': u'1207 Dartmouth Rd', u'sitterid': u'212', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'848932', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Bella', u'completed': None, u'lon': u'-77.1165', u'clientid': u'2016', u'hours': u'00:00', u'lat': u'38.8095', u'state': u'VA', u'client': u'@2016', u'servicecode': u'113', u'street1': u'171 Somervelle St.', u'sitterid': u'266', u'timeofday': u'12:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848933', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Barbara', u'completed': None, u'lon': u'-77.0476', u'clientid': u'2065', u'hours': u'00:00', u'lat': u'38.8148', u'state': u'Virginia', u'client': u'@2065', u'servicecode': u'19', u'street1': u'911 Parker Gray School Way', u'sitterid': u'177', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'848934', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Cam', u'completed': None, u'lon': u'-77.1205', u'clientid': u'1185', u'hours': u'00:00', u'lat': u'38.8061', u'state': u'VA', u'client': u'@1185', u'servicecode': u'19', u'street1': u'5109 Knapp Place', u'sitterid': u'27', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848936', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0549', u'clientid': u'2070', u'hours': u'00:00', u'lat': u'38.7981', u'state': u'VA', u'client': u'@2070', u'servicecode': u'114', u'street1': u'726 S. Payne Street', u'sitterid': u'260', u'timeofday': u'3:00 pm-5:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'848937', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Keith', u'completed': None, u'lon': u'-77.0692', u'clientid': u'1672', u'hours': u'00:00', u'lat': u'38.7615', u'state': u'VA', u'client': u'@1672', u'servicecode': u'19', u'street1': u'7200 Beachwood Rd', u'sitterid': u'276', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848938', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0593', u'clientid': u'1789', u'hours': u'00:00', u'lat': u'38.8299', u'state': u'VA', u'client': u'@1789', u'servicecode': u'20', u'street1': u'2719 Mount Vernon Avenue', u'sitterid': u'256', u'timeofday': u'12:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'848939', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Keith', u'completed': None, u'lon': u'-77.0737', u'clientid': u'2068', u'hours': u'00:00', u'lat': u'38.7205', u'state': u'Virginia', u'client': u'@2068', u'servicecode': u'48', u'street1': u'8723 Waterford RD', u'sitterid': u'276', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848941', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0796', u'clientid': u'2036', u'hours': u'00:00', u'lat': u'38.8328', u'state': u'Virginia', u'client': u'@2036', u'servicecode': u'20', u'street1': u'3110 Valley Drive', u'sitterid': u'256', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848943', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Barbara', u'completed': None, u'lon': u'-77.0416', u'clientid': u'691', u'hours': u'00:00', u'lat': u'38.8031', u'state': u'VA', u'client': u'@691', u'servicecode': u'19', u'street1': u'126 Prince St', u'sitterid': u'177', u'timeofday': u'12:00 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22311', u'appointmentid': u'848944', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Bella', u'completed': None, u'lon': u'-77.1305', u'clientid': u'2025', u'hours': u'00:00', u'lat': u'38.8292', u'state': u'VA', u'client': u'@2025', u'servicecode': u'20', u'street1': u'5771 Harwich Court Apt 233', u'sitterid': u'266', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'848945', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0549', u'clientid': u'2078', u'hours': u'00:00', u'lat': u'38.8325', u'state': u'Va.', u'client': u'@2078', u'servicecode': u'113', u'street1': u'319 Laverne Ave.', u'sitterid': u'256', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22315', u'appointmentid': u'848946', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1623', u'clientid': u'579', u'hours': u'00:00', u'lat': u'38.7488', u'state': u'Virginia', u'client': u'@579', u'servicecode': u'19', u'street1': u'7712 Stone Wheat Ct', u'sitterid': u'274', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848947', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0701', u'clientid': u'1590', u'hours': u'00:00', u'lat': u'38.8263', u'state': u'VA', u'client': u'@1590', u'servicecode': u'19', u'street1': u'406 Jackson Place', u'sitterid': u'222', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'848948', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0506', u'clientid': u'2060', u'hours': u'00:00', u'lat': u'38.8423', u'state': u'VA', u'client': u'@2060', u'servicecode': u'113', u'street1': u'3650 South Glebe Road, Unit 256', u'sitterid': u'255', u'timeofday': u'1:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848954', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Ron', u'completed': None, u'lon': u'-77.0438', u'clientid': u'1438', u'hours': u'00:00', u'lat': u'38.8155', u'state': u'VA', u'client': u'@1438', u'servicecode': u'19', u'street1': u'635 First Street #305', u'sitterid': u'234', u'timeofday': u'12:00 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'848955', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Ron', u'completed': None, u'lon': u'-77.0416', u'clientid': u'1470', u'hours': u'00:00', u'lat': u'38.8169', u'state': u'VA', u'client': u'@1470', u'servicecode': u'48', u'street1': u'1107 N. Pitt St Apt 1A', u'sitterid': u'234', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'848956', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Cam', u'completed': None, u'lon': u'-77.1196', u'clientid': u'208', u'hours': u'00:00', u'lat': u'38.8066', u'state': u'VA', u'client': u'@208', u'servicecode': u'113', u'street1': u'5015 Murtha St', u'sitterid': u'27', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848959', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0742', u'clientid': u'1770', u'hours': u'00:00', u'lat': u'38.8335', u'state': u'VA', u'client': u'@1770', u'servicecode': u'48', u'street1': u'803 Beverley Dr', u'sitterid': u'0', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'848960', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0693', u'clientid': u'1340', u'hours': u'00:00', u'lat': u'38.8389', u'state': u'VA', u'client': u'@1340', u'servicecode': u'19', u'street1': u'512 N. Overlook Drive', u'sitterid': u'0', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'848961', u'service': u'20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0643', u'clientid': u'1838', u'hours': u'00:00', u'lat': u'38.8361', u'state': u'VA', u'client': u'@1838', u'servicecode': u'110', u'street1': u'246 Burgess Avenue', u'sitterid': u'0', u'timeofday': u'3:00 pm-5:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22206', u'appointmentid': u'848962', u'service': u'30 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.1042', u'clientid': u'1336', u'hours': u'00:00', u'lat': u'38.8427', u'state': u'VA', u'client': u'@1336', u'servicecode': u'1', u'street1': u'2542 S. Walter Reed Dr.', u'sitterid': u'291', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848963', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0796', u'clientid': u'2116', u'hours': u'00:00', u'lat': u'38.8268', u'state': u'VA', u'client': u'@2116', u'servicecode': u'20', u'street1': u'1210 Hillside Terrace', u'sitterid': u'294', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ARLINGTON', u'zip': u'22206', u'appointmentid': u'848964', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0725', u'clientid': u'462', u'hours': u'00:00', u'lat': u'38.8487', u'state': u'VA', u'client': u'@462', u'servicecode': u'19', u'street1': u'1537 28th St. South ', u'sitterid': u'256', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22311', u'appointmentid': u'848965', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1081', u'clientid': u'1986', u'hours': u'00:00', u'lat': u'38.8342', u'state': u'VA', u'client': u'@1986', u'servicecode': u'114', u'street1': u'2507 Hunton Place', u'sitterid': u'0', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848966', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.0935', u'clientid': u'1065', u'hours': u'00:00', u'lat': u'38.8309', u'state': u'VA', u'client': u'@1065', u'servicecode': u'113', u'street1': u'2514 N Dearing St.', u'sitterid': u'291', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'848967', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0633', u'clientid': u'1652', u'hours': u'00:00', u'lat': u'38.8342', u'state': u'VA', u'client': u'@1652', u'servicecode': u'19', u'street1': u'3114 Landover St', u'sitterid': u'0', u'timeofday': u'11:30 am-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'848969', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1165', u'clientid': u'1927', u'hours': u'00:00', u'lat': u'38.8277', u'state': u'VA', u'client': u'@1927', u'servicecode': u'20', u'street1': u'1411A N Van Dorn St', u'sitterid': u'0', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'848970', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.062', u'clientid': u'2120', u'hours': u'00:00', u'lat': u'38.8279', u'state': u'Va', u'client': u'@2120', u'servicecode': u'19', u'street1': u'9 West Uhler Ave', u'sitterid': u'294', u'timeofday': u'11:30 am-12:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22302', u'appointmentid': u'848975', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0764', u'clientid': u'1421', u'hours': u'00:00', u'lat': u'38.8343', u'state': u'VA', u'client': u'@1421', u'servicecode': u'113', u'street1': u'902 Crescent Drive', u'sitterid': u'0', u'timeofday': u'10:00 am-11:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22302', u'appointmentid': u'848976', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0764', u'clientid': u'1421', u'hours': u'00:00', u'lat': u'38.8343', u'state': u'VA', u'client': u'@1421', u'servicecode': u'113', u'street1': u'902 Crescent Drive', u'sitterid': u'0', u'timeofday': u'2:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22206', u'appointmentid': u'848978', u'service': u'20 Min VP - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.0798', u'clientid': u'2105', u'hours': u'00:00', u'lat': u'38.8484', u'state': u'VA', u'client': u'@2105', u'servicecode': u'116', u'street1': u'2400 24th Road South, ', u'sitterid': u'269', u'timeofday': u'11:00 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22310', u'appointmentid': u'848980', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1525', u'clientid': u'2140', u'hours': u'00:00', u'lat': u'38.7692', u'state': u'VA', u'client': u'@2140', u'servicecode': u'113', u'street1': u'6911 Victoria Dr', u'sitterid': u'274', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848981', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0726', u'clientid': u'1985', u'hours': u'00:00', u'lat': u'38.8232', u'state': u'VA', u'client': u'@1985', u'servicecode': u'19', u'street1': u'606 W Windsor AVE', u'sitterid': u'294', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848986', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Bella', u'completed': None, u'lon': u'-77.1049', u'clientid': u'2141', u'hours': u'00:00', u'lat': u'38.8338', u'state': u'VA', u'client': u'@2141', u'servicecode': u'20', u'street1': u'2801 Park Center Drive', u'sitterid': u'266', u'timeofday': u'12:00 pm-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848987', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0821', u'clientid': u'739', u'hours': u'00:00', u'lat': u'38.8361', u'state': u'VA', u'client': u'@739', u'servicecode': u'119', u'street1': u'1741 Preston Rd', u'sitterid': u'222', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'848988', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0821', u'clientid': u'739', u'hours': u'00:00', u'lat': u'38.8361', u'state': u'VA', u'client': u'@739', u'servicecode': u'119', u'street1': u'1741 Preston Rd', u'sitterid': u'222', u'timeofday': u'3:00 pm-5:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'848990', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.0642', u'clientid': u'1439', u'hours': u'00:00', u'lat': u'38.8479', u'state': u'VA', u'client': u'@1439', u'servicecode': u'19', u'street1': u'2645 S. June St.', u'sitterid': u'269', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22206', u'appointmentid': u'848992', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.104', u'clientid': u'2119', u'hours': u'00:00', u'lat': u'38.8398', u'state': u'Va', u'client': u'@2119', u'servicecode': u'19', u'street1': u'2842 S Columbus St', u'sitterid': u'291', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington ', u'zip': u'22206', u'appointmentid': u'848998', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.1008', u'clientid': u'1698', u'hours': u'00:00', u'lat': u'38.8389', u'state': u'VA', u'client': u'@1698', u'servicecode': u'113', u'street1': u'4814 29th St S', u'sitterid': u'291', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'849006', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Shawna', u'completed': None, u'lon': u'-77.0733', u'clientid': u'1466', u'hours': u'00:00', u'lat': u'38.8478', u'state': u'VA', u'client': u'@1466', u'servicecode': u'114', u'street1': u'1437 28th St S', u'sitterid': u'222', u'timeofday': u'1:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'849009', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Anna', u'completed': None, u'lon': u'-77.0762', u'clientid': u'1964', u'hours': u'00:00', u'lat': u'38.8095', u'state': u'VA', u'client': u'@1964', u'servicecode': u'113', u'street1': u'105 Skyhill Road', u'sitterid': u'212', u'timeofday': u'10:00 am-11:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'849011', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0592', u'clientid': u'1736', u'hours': u'00:00', u'lat': u'38.811', u'state': u'VA', u'client': u'@1736', u'servicecode': u'19', u'street1': u'26A East Linden Street', u'sitterid': u'294', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22306', u'appointmentid': u'849013', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.1127', u'clientid': u'2112', u'hours': u'00:00', u'lat': u'38.7639', u'state': u'VA', u'client': u'@2112', u'servicecode': u'113', u'street1': u'6918 Deer Run Dr', u'sitterid': u'304', u'timeofday': u'11:00 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'849016', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0693', u'clientid': u'1722', u'hours': u'00:00', u'lat': u'38.8254', u'state': u'VA', u'client': u'@1722', u'servicecode': u'19', u'street1': u'305 Fontaine St', u'sitterid': u'255', u'timeofday': u'11:30 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'849018', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0728', u'clientid': u'129', u'hours': u'00:00', u'lat': u'38.8235', u'state': u'VA', u'client': u'@129', u'servicecode': u'19', u'street1': u'609 W. Windsor Ave', u'sitterid': u'255', u'timeofday': u'12:00 pm-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'849020', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Bella', u'completed': None, u'lon': u'-77.1189', u'clientid': u'1682', u'hours': u'00:00', u'lat': u'38.811', u'state': u'VA', u'client': u'@1682', u'servicecode': u'19', u'street1': u'5129 Gardner Drive', u'sitterid': u'266', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'849026', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Bri', u'completed': None, u'lon': u'-77.1001', u'clientid': u'1389', u'hours': u'00:00', u'lat': u'38.8087', u'state': u'VA', u'client': u'@1389', u'servicecode': u'114', u'street1': u'53 S. Floyd St.', u'sitterid': u'301', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22305', u'appointmentid': u'849030', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0624', u'clientid': u'2145', u'hours': u'00:00', u'lat': u'38.8313', u'state': u'VA', u'client': u'@2145', u'servicecode': u'19', u'street1': u'2908 Hickory St', u'sitterid': u'0', u'timeofday': u'10:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'849032', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.058', u'clientid': u'2121', u'hours': u'00:00', u'lat': u'38.8513', u'state': u'VA', u'client': u'@2121', u'servicecode': u'113', u'street1': u'708 25th Street South', u'sitterid': u'269', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'849035', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0493', u'clientid': u'124', u'hours': u'00:00', u'lat': u'38.8034', u'state': u'VA', u'client': u'@124', u'servicecode': u'20', u'street1': u'224 South Alfred St', u'sitterid': u'306', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'849037', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0481', u'clientid': u'1671', u'hours': u'00:00', u'lat': u'38.8135', u'state': u'VA', u'client': u'@1671', u'servicecode': u'20', u'street1': u'927 Parker Gray School Way', u'sitterid': u'306', u'timeofday': u'1:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22315', u'appointmentid': u'849045', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1276', u'clientid': u'2096', u'hours': u'00:00', u'lat': u'38.7677', u'state': u'VA', u'client': u'@2096', u'servicecode': u'114', u'street1': u'5321 LaRochelle Court', u'sitterid': u'274', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'849048', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.082', u'clientid': u'2163', u'hours': u'00:00', u'lat': u'38.8333', u'state': u'VA', u'client': u'@2163', u'servicecode': u'113', u'street1': u'3203 Martha Custis Drive', u'sitterid': u'256', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22311', u'appointmentid': u'849049', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Bri', u'completed': None, u'lon': u'-77.1099', u'clientid': u'101', u'hours': u'00:00', u'lat': u'38.8326', u'state': u'VA', u'client': u'@101', u'servicecode': u'113', u'street1': u'2406 Gretter Place', u'sitterid': u'301', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22206', u'appointmentid': u'849050', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Bri', u'completed': None, u'lon': u'-77.1004', u'clientid': u'2150', u'hours': u'00:00', u'lat': u'38.8365', u'state': u'VA', u'client': u'@2150', u'servicecode': u'19', u'street1': u'4908 30th St S', u'sitterid': u'301', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'849053', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0509', u'clientid': u'2058', u'hours': u'00:00', u'lat': u'38.8034', u'state': u'VA', u'client': u'@2058', u'servicecode': u'19', u'street1': u'1001 Duke St', u'sitterid': u'260', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22305', u'appointmentid': u'849054', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0635', u'clientid': u'268', u'hours': u'00:00', u'lat': u'38.83', u'state': u'VA', u'client': u'@268', u'servicecode': u'119', u'street1': u'2716 Hemlock Ave', u'sitterid': u'294', u'timeofday': u'10:00 am-11:00 am'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22305', u'appointmentid': u'849055', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0635', u'clientid': u'268', u'hours': u'00:00', u'lat': u'38.83', u'state': u'VA', u'client': u'@268', u'servicecode': u'119', u'street1': u'2716 Hemlock Ave', u'sitterid': u'294', u'timeofday': u'12:30 pm-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'849056', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1041', u'clientid': u'1912', u'hours': u'00:00', u'lat': u'38.8198', u'state': u'VA', u'client': u'@1912', u'servicecode': u'20', u'street1': u'905 N. Howard st', u'sitterid': u'0', u'timeofday': u'9:00 am-11:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'849057', u'service': u'30 Min Flex Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1041', u'clientid': u'1912', u'hours': u'00:00', u'lat': u'38.8198', u'state': u'VA', u'client': u'@1912', u'servicecode': u'56', u'street1': u'905 N. Howard st', u'sitterid': u'0', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'849067', u'service': u'20 Min VP - 1 dog', u'sitter': u'Barbara', u'completed': None, u'lon': u'-77.0463', u'clientid': u'2093', u'hours': u'00:00', u'lat': u'38.8148', u'state': u'VA', u'client': u'@2093', u'servicecode': u'116', u'street1': u'912 N. Columbus St', u'sitterid': u'177', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22310', u'appointmentid': u'849068', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.0841', u'clientid': u'1785', u'hours': u'00:00', u'lat': u'38.7951', u'state': u'VA', u'client': u'@1785', u'servicecode': u'113', u'street1': u'5731 Heritage Hill Ct.', u'sitterid': u'274', u'timeofday': u'12:30 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'849070', u'service': u'Monthly 20 Min Puppy - 2 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0651', u'clientid': u'66', u'hours': u'00:00', u'lat': u'38.8236', u'state': u'VA', u'client': u'@66', u'servicecode': u'120', u'street1': u'105 W Howell Ave', u'sitterid': u'294', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'849071', u'service': u'Monthly 20 Min Puppy - 2 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0651', u'clientid': u'66', u'hours': u'00:00', u'lat': u'38.8236', u'state': u'VA', u'client': u'@66', u'servicecode': u'120', u'street1': u'105 W Howell Ave', u'sitterid': u'294', u'timeofday': u'2:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22311', u'appointmentid': u'849072', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1093', u'clientid': u'1353', u'hours': u'00:00', u'lat': u'38.8362', u'state': u'VA', u'client': u'@1353', u'servicecode': u'113', u'street1': u'4773 W Braddock Rd', u'sitterid': u'0', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'849073', u'service': u'Emergency Weekday', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0581', u'clientid': u'352', u'hours': u'00:00', u'lat': u'38.8256', u'state': u'Va', u'client': u'@352', u'servicecode': u'31', u'street1': u'202 E Custis Ave', u'sitterid': u'294', u'timeofday': u'4:00 pm-8:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'849086', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Keith', u'completed': None, u'lon': u'-77.0563', u'clientid': u'43', u'hours': u'00:00', u'lat': u'38.7491', u'state': u'VA', u'client': u'@43', u'servicecode': u'19', u'street1': u'7628 Essex Manor Pl', u'sitterid': u'276', u'timeofday': u'1:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'851549', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0836', u'clientid': u'1746', u'hours': u'00:00', u'lat': u'38.8389', u'state': u'VA', u'client': u'@1746', u'servicecode': u'19', u'street1': u'3201 Martha Custis Dr', u'sitterid': u'256', u'timeofday': u'4:00 pm-5:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22304', u'appointmentid': u'852832', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.1165', u'clientid': u'2000', u'hours': u'00:00', u'lat': u'38.8277', u'state': u'VIRGINIA', u'client': u'@2000', u'servicecode': u'113', u'street1': u'1609B N VAN DORN ST', u'sitterid': u'291', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'852896', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.092', u'clientid': u'2110', u'hours': u'00:00', u'lat': u'38.8091', u'state': u'Va', u'client': u'@2110', u'servicecode': u'113', u'street1': u'3520 Duke St.', u'sitterid': u'293', u'timeofday': u'9:00 am-11:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'852960', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.077', u'clientid': u'987', u'hours': u'00:00', u'lat': u'38.8101', u'state': u'VA', u'client': u'@987', u'servicecode': u'20', u'street1': u'204 Skyhill Rd. #4', u'sitterid': u'293', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22301', u'appointmentid': u'853024', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.067', u'clientid': u'860', u'hours': u'00:00', u'lat': u'38.8099', u'state': u'VA', u'client': u'@860', u'servicecode': u'20', u'street1': u'311 Park Rd', u'sitterid': u'293', u'timeofday': u'11:00 am-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'853088', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.0737', u'clientid': u'1674', u'hours': u'00:00', u'lat': u'38.8094', u'state': u'Virginia', u'client': u'@1674', u'servicecode': u'113', u'street1': u'203 E Taylor Run Pkwy', u'sitterid': u'293', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22302', u'appointmentid': u'853152', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.0853', u'clientid': u'394', u'hours': u'00:00', u'lat': u'38.8164', u'state': u'VA', u'client': u'@394', u'servicecode': u'19', u'street1': u'1215 Janneys Lane ', u'sitterid': u'293', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'853216', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kate-T', u'completed': None, u'lon': u'-77.0955', u'clientid': u'132', u'hours': u'00:00', u'lat': u'38.817', u'state': u'VA', u'client': u'@132', u'servicecode': u'19', u'street1': u'3803 Colonel Ellis Avenue', u'sitterid': u'293', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'854126', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.063', u'clientid': u'2183', u'hours': u'00:00', u'lat': u'38.8298', u'state': u'VA', u'client': u'@2183', u'servicecode': u'114', u'street1': u'2715 Hemlock Ave', u'sitterid': u'294', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'855488', u'service': u'30 Min Flex Pet Sit - 1 pet', u'sitter': u'Jessica ', u'completed': None, u'lon': u'-77.0539', u'clientid': u'2188', u'hours': u'00:00', u'lat': u'38.8375', u'state': u'VA', u'client': u'@2188', u'servicecode': u'49', u'street1': u'100 Luna Park Drive', u'sitterid': u'189', u'timeofday': u'7:30 pm-9:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'855564', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.0822', u'clientid': u'2189', u'hours': u'00:00', u'lat': u'38.8399', u'state': u'VA', u'client': u'@2189', u'servicecode': u'19', u'street1': u'3762 Gunston Road', u'sitterid': u'269', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'856493', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Katy', u'completed': None, u'lon': u'-77.0883', u'clientid': u'2192', u'hours': u'00:00', u'lat': u'38.8114', u'state': u'VA', u'client': u'@2192', u'servicecode': u'19', u'street1': u'251 N. Quaker Lane', u'sitterid': u'291', u'timeofday': u'10:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'857713', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0457', u'clientid': u'2190', u'hours': u'00:00', u'lat': u'38.8078', u'state': u'VA', u'client': u'@2190', u'servicecode': u'48', u'street1': u'358 N St Asaph ', u'sitterid': u'306', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'857785', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1224', u'clientid': u'2122', u'hours': u'00:00', u'lat': u'38.8101', u'state': u'VA', u'client': u'@2122', u'servicecode': u'19', u'street1': u'108 S Pickett St', u'sitterid': u'0', u'timeofday': u'11:15 am-1:15 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'858155', u'service': u'30 Min Pet Sit - 1 pet', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0653', u'clientid': u'172', u'hours': u'00:00', u'lat': u'38.8261', u'state': u'VA', u'client': u'@172', u'servicecode': u'22', u'street1': u'2215 Russell Rd.', u'sitterid': u'255', u'timeofday': u'5:00 pm-7:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'859455', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0496', u'clientid': u'1258', u'hours': u'00:00', u'lat': u'38.7966', u'state': u'VA', u'client': u'@1258', u'servicecode': u'113', u'street1': u'820 S Columbus St', u'sitterid': u'0', u'timeofday': u'10:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'859815', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Kate', u'completed': None, u'lon': u'-77.0634', u'clientid': u'79', u'hours': u'00:00', u'lat': u'38.8212', u'state': u'VA', u'client': u'@79', u'servicecode': u'119', u'street1': u'1 West Mason Ave. ', u'sitterid': u'255', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'859816', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Robbyn', u'completed': None, u'lon': u'-77.0634', u'clientid': u'79', u'hours': u'00:00', u'lat': u'38.8212', u'state': u'VA', u'client': u'@79', u'servicecode': u'119', u'street1': u'1 West Mason Ave. ', u'sitterid': u'251', u'timeofday': u'2:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'859993', u'service': u'20 Min VP - 2 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0419', u'clientid': u'2187', u'hours': u'00:00', u'lat': u'38.8153', u'state': u'VA', u'client': u'@2187', u'servicecode': u'117', u'street1': u'949 N Pitt Street', u'sitterid': u'260', u'timeofday': u'12:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'860269', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0473', u'clientid': u'2139', u'hours': u'00:00', u'lat': u'38.8151', u'state': u'VA', u'client': u'@2139', u'servicecode': u'48', u'street1': u'926 N. Alfred St.', u'sitterid': u'306', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'860764', u'service': u'30 Min Flex Visit - 2 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0589', u'clientid': u'2040', u'hours': u'00:00', u'lat': u'38.8166', u'state': u'VA', u'client': u'@2040', u'servicecode': u'56', u'street1': u'206 1/2 Adams Ave', u'sitterid': u'314', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22305', u'appointmentid': u'861365', u'service': u'30 Min Visit - 2 dogs', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0608', u'clientid': u'2185', u'hours': u'00:00', u'lat': u'38.8337', u'state': u'Va', u'client': u'@2185', u'servicecode': u'2', u'street1': u'3110 Mt Vernon Ave ', u'sitterid': u'316', u'timeofday': u'1:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'862569', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0574', u'clientid': u'76', u'hours': u'00:00', u'lat': u'38.8049', u'state': u'VA', u'client': u'@76', u'servicecode': u'19', u'street1': u'1600 Prince St.', u'sitterid': u'0', u'timeofday': u'3:00 pm-5:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863012', u'service': u'20 Min VP - 2 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0544', u'clientid': u'1813', u'hours': u'00:00', u'lat': u'38.8177', u'state': u'Virginia', u'client': u'@1813', u'servicecode': u'117', u'street1': u'506 E Glendale Ave', u'sitterid': u'314', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'863065', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0588', u'clientid': u'1994', u'hours': u'00:00', u'lat': u'38.8356', u'state': u'VA', u'client': u'@1994', u'servicecode': u'19', u'street1': u'20 W Glebe Rd ', u'sitterid': u'316', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863130', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0592', u'clientid': u'1938', u'hours': u'00:00', u'lat': u'38.8346', u'state': u'Virginia', u'client': u'@1938', u'servicecode': u'113', u'street1': u'31 Herbert St.', u'sitterid': u'316', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'863195', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0596', u'clientid': u'2017', u'hours': u'00:00', u'lat': u'38.8347', u'state': u'VA', u'client': u'@2017', u'servicecode': u'113', u'street1': u'39 Herbert Street', u'sitterid': u'316', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'863260', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0532', u'clientid': u'2075', u'hours': u'00:00', u'lat': u'38.8364', u'state': u'Virginia', u'client': u'@2075', u'servicecode': u'19', u'street1': u'232 Lynhaven Drive', u'sitterid': u'316', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863390', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0501', u'clientid': u'2148', u'hours': u'00:00', u'lat': u'38.8288', u'state': u'VA', u'client': u'@2148', u'servicecode': u'19', u'street1': u'615 Swann Ave', u'sitterid': u'316', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863455', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.0501', u'clientid': u'2152', u'hours': u'00:00', u'lat': u'38.8288', u'state': u'VA', u'client': u'@2152', u'servicecode': u'48', u'street1': u'615 Swann Ave', u'sitterid': u'316', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863520', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0589', u'clientid': u'141', u'hours': u'00:00', u'lat': u'38.8194', u'state': u'VA', u'client': u'@141', u'servicecode': u'19', u'street1': u'217 E Nelson Ave', u'sitterid': u'314', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22301', u'appointmentid': u'863585', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0596', u'clientid': u'1680', u'hours': u'00:00', u'lat': u'38.8192', u'state': u'VA', u'client': u'@1680', u'servicecode': u'113', u'street1': u'207 E Nelson Ave #B', u'sitterid': u'314', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863671', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0598', u'clientid': u'2176', u'hours': u'00:00', u'lat': u'38.8196', u'state': u'VA', u'client': u'@2176', u'servicecode': u'119', u'street1': u'206 E Nelson Ave', u'sitterid': u'314', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'863672', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Aaron', u'completed': None, u'lon': u'-77.0598', u'clientid': u'2176', u'hours': u'00:00', u'lat': u'38.8196', u'state': u'VA', u'client': u'@2176', u'servicecode': u'119', u'street1': u'206 E Nelson Ave', u'sitterid': u'314', u'timeofday': u'2:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'864065', u'service': u'30 Min Flex Visit - 2 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.053', u'clientid': u'2164', u'hours': u'00:00', u'lat': u'38.8272', u'state': u'VA', u'client': u'@2164', u'servicecode': u'56', u'street1': u'2310-A E Randolph Ave', u'sitterid': u'316', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'864117', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0464', u'clientid': u'1241', u'hours': u'00:00', u'lat': u'38.8173', u'state': u'VA', u'client': u'@1241', u'servicecode': u'19', u'street1': u'1117 Powhatan St', u'sitterid': u'0', u'timeofday': u'11:00 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22302', u'appointmentid': u'864392', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1023', u'clientid': u'2153', u'hours': u'00:00', u'lat': u'38.8342', u'state': u'VA', u'client': u'@2153', u'servicecode': u'113', u'street1': u'3309 Wyndham Circle', u'sitterid': u'0', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'864520', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0538', u'clientid': u'605', u'hours': u'00:00', u'lat': u'38.7757', u'state': u'VA', u'client': u'@605', u'servicecode': u'114', u'street1': u'6507 Tenth St', u'sitterid': u'46', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22306', u'appointmentid': u'864584', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0699', u'clientid': u'1180', u'hours': u'00:00', u'lat': u'38.7514', u'state': u'VA', u'client': u'@1180', u'servicecode': u'19', u'street1': u'7611 Range Road', u'sitterid': u'46', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22307', u'appointmentid': u'864648', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0711', u'clientid': u'533', u'hours': u'00:00', u'lat': u'38.7808', u'state': u'VA', u'client': u'@533', u'servicecode': u'19', u'street1': u'2220 Windsor Rd', u'sitterid': u'46', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'864712', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0549', u'clientid': u'148', u'hours': u'00:00', u'lat': u'38.7784', u'state': u'VA', u'client': u'@148', u'servicecode': u'19', u'street1': u'6407 11th St', u'sitterid': u'46', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22306', u'appointmentid': u'864956', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0633', u'clientid': u'1208', u'hours': u'00:00', u'lat': u'38.751', u'state': u'VA', u'client': u'@1208', u'servicecode': u'20', u'street1': u'1901 Whiteoaks Drive', u'sitterid': u'46', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'ALEXANDRIA', u'zip': u'22308', u'appointmentid': u'865020', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0731', u'clientid': u'292', u'hours': u'00:00', u'lat': u'38.7314', u'state': u'VA', u'client': u'@292', u'servicecode': u'19', u'street1': u'8302 Marble Dale Ct', u'sitterid': u'46', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'865086', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0477', u'clientid': u'1314', u'hours': u'00:00', u'lat': u'38.8081', u'state': u'VA', u'client': u'@1314', u'servicecode': u'20', u'street1': u'318 N. Columbus St.', u'sitterid': u'306', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'865900', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0485', u'clientid': u'1957', u'hours': u'00:00', u'lat': u'38.8313', u'state': u'Virginia (VA)', u'client': u'@1957', u'servicecode': u'113', u'street1': u'731 Seaton Ave', u'sitterid': u'0', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'866080', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0479', u'clientid': u'1448', u'hours': u'00:00', u'lat': u'38.8161', u'state': u'VA', u'client': u'@1448', u'servicecode': u'19', u'street1': u'1014 Colonial Ave', u'sitterid': u'0', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'866686', u'service': u'Monthly 20 Min Puppy - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0414', u'clientid': u'2144', u'hours': u'00:00', u'lat': u'38.806', u'state': u'VA', u'client': u'@2144', u'servicecode': u'120', u'street1': u'212 N. Lee St.', u'sitterid': u'0', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'866687', u'service': u'Monthly 20 Min Puppy - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0414', u'clientid': u'2144', u'hours': u'00:00', u'lat': u'38.806', u'state': u'VA', u'client': u'@2144', u'servicecode': u'120', u'street1': u'212 N. Lee St.', u'sitterid': u'0', u'timeofday': u'1:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'866772', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0455', u'clientid': u'685', u'hours': u'00:00', u'lat': u'38.8191', u'state': u'VA', u'client': u'@685', u'servicecode': u'20', u'street1': u'1306 Michigan Ave', u'sitterid': u'0', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'867169', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.053', u'clientid': u'1090', u'hours': u'00:00', u'lat': u'38.7385', u'state': u'VA', u'client': u'@1090', u'servicecode': u'20', u'street1': u'8108 Wellington Rd.', u'sitterid': u'304', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'867233', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1077', u'clientid': u'505', u'hours': u'00:00', u'lat': u'38.7389', u'state': u'VA', u'client': u'@505', u'servicecode': u'19', u'street1': u'4315 Lawrence St.', u'sitterid': u'274', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'867325', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0526', u'clientid': u'2099', u'hours': u'00:00', u'lat': u'38.7741', u'state': u'Va', u'client': u'@2099', u'servicecode': u'119', u'street1': u'6608 Boulevard View #A2', u'sitterid': u'46', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'867326', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0526', u'clientid': u'2099', u'hours': u'00:00', u'lat': u'38.7741', u'state': u'Va', u'client': u'@2099', u'servicecode': u'119', u'street1': u'6608 Boulevard View #A2', u'sitterid': u'46', u'timeofday': u'2:30 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22307', u'appointmentid': u'867425', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Natasha ', u'completed': None, u'lon': u'-77.0616', u'clientid': u'957', u'hours': u'00:00', u'lat': u'38.78', u'state': u'VA', u'client': u'@957', u'servicecode': u'19', u'street1': u'6320 Barrister Pl', u'sitterid': u'46', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22306', u'appointmentid': u'867574', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Keith', u'completed': None, u'lon': u'-77.0899', u'clientid': u'2062', u'hours': u'00:00', u'lat': u'38.7645', u'state': u'VA', u'client': u'@2062', u'servicecode': u'19', u'street1': u'3413 Spring Dr', u'sitterid': u'276', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'867620', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.0715', u'clientid': u'168', u'hours': u'00:00', u'lat': u'38.7322', u'state': u'VA', u'client': u'@168', u'servicecode': u'19', u'street1': u'2316 Lakeshire Dr.', u'sitterid': u'304', u'timeofday': u'10:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22308', u'appointmentid': u'867653', u'service': u'20 Min Visit - 2 dogs', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.0579', u'clientid': u'2063', u'hours': u'00:00', u'lat': u'38.7378', u'state': u'VA', u'client': u'@2063', u'servicecode': u'111', u'street1': u'8049 Fairfax Road', u'sitterid': u'304', u'timeofday': u'11:30 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'867724', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.1063', u'clientid': u'2194', u'hours': u'00:00', u'lat': u'38.7122', u'state': u'VA', u'client': u'@2194', u'servicecode': u'119', u'street1': u'9014 Nomini Lane', u'sitterid': u'304', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'867725', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Terri', u'completed': None, u'lon': u'-77.1063', u'clientid': u'2194', u'hours': u'00:00', u'lat': u'38.7122', u'state': u'VA', u'client': u'@2194', u'servicecode': u'119', u'street1': u'9014 Nomini Lane', u'sitterid': u'304', u'timeofday': u'1:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22309', u'appointmentid': u'867852', u'service': u'20 Min VP - 2 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.1136', u'clientid': u'1974', u'hours': u'00:00', u'lat': u'38.7283', u'state': u'VA', u'client': u'@1974', u'servicecode': u'117', u'street1': u'8446 Hallie Rose Street', u'sitterid': u'274', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22303', u'appointmentid': u'867896', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Kyle', u'completed': None, u'lon': u'-77.0799', u'clientid': u'1217', u'hours': u'00:00', u'lat': u'38.7868', u'state': u'VA', u'client': u'@1217', u'servicecode': u'19', u'street1': u'6016 Monticello Rd', u'sitterid': u'274', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'868282', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.05', u'clientid': u'2199', u'hours': u'00:00', u'lat': u'38.856', u'state': u'VA', u'client': u'@2199', u'servicecode': u'19', u'street1': u'220 20th St S', u'sitterid': u'269', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'868571', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0457', u'clientid': u'2057', u'hours': u'00:00', u'lat': u'38.825', u'state': u'VA', u'client': u'@2057', u'servicecode': u'19', u'street1': u'707 Fitzhugh Way', u'sitterid': u'0', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'868868', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Bella', u'completed': None, u'lon': u'-77.1051', u'clientid': u'1942', u'hours': u'00:00', u'lat': u'38.8099', u'state': u'VA', u'client': u'@1942', u'servicecode': u'113', u'street1': u'51 S Gordon St', u'sitterid': u'266', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22305', u'appointmentid': u'869524', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0723', u'clientid': u'1809', u'hours': u'00:00', u'lat': u'38.8332', u'state': u'VA', u'client': u'@1809', u'servicecode': u'114', u'street1': u'3100 Circle Hill Road', u'sitterid': u'0', u'timeofday': u'10:30 am-11:30 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria ', u'zip': u'22305', u'appointmentid': u'869525', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0723', u'clientid': u'1809', u'hours': u'00:00', u'lat': u'38.8332', u'state': u'VA', u'client': u'@1809', u'servicecode': u'20', u'street1': u'3100 Circle Hill Road', u'sitterid': u'0', u'timeofday': u'2:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'869653', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0532', u'clientid': u'1830', u'hours': u'00:00', u'lat': u'38.809', u'state': u'Virginia', u'client': u'@1830', u'servicecode': u'19', u'street1': u'326 N Payne St.', u'sitterid': u'0', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'869903', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'John M.', u'completed': None, u'lon': u'-77.0546', u'clientid': u'1405', u'hours': u'00:00', u'lat': u'38.8109', u'state': u'VA', u'client': u'@1405', u'servicecode': u'113', u'street1': u'1503 Oronoco St.', u'sitterid': u'294', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'870718', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0495', u'clientid': u'2179', u'hours': u'00:00', u'lat': u'38.8075', u'state': u'VA', u'client': u'@2179', u'servicecode': u'20', u'street1': u'918 Queen St', u'sitterid': u'306', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'871301', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0499', u'clientid': u'1653', u'hours': u'00:00', u'lat': u'38.8041', u'state': u'VA', u'client': u'@1653', u'servicecode': u'19', u'street1': u'906 Prince Street Apt. 302', u'sitterid': u'306', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'871362', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0501', u'clientid': u'1950', u'hours': u'00:00', u'lat': u'38.8142', u'state': u'VA', u'client': u'@1950', u'servicecode': u'19', u'street1': u'1111 Belle Pre Way #334', u'sitterid': u'260', u'timeofday': u'11:00 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'871415', u'service': u'30 Min Pet Sit - 1 pet', u'sitter': u'Melaina', u'completed': None, u'lon': u'-77.0894', u'clientid': u'2170', u'hours': u'00:00', u'lat': u'38.8089', u'state': u'VA', u'client': u'@2170', u'servicecode': u'22', u'street1': u'35 Arell Court', u'sitterid': u'309', u'timeofday': u'7:00 am-9:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'871423', u'service': u'30 Min Pet Sit - 1 pet', u'sitter': u'Melaina', u'completed': None, u'lon': u'-77.0894', u'clientid': u'2170', u'hours': u'00:00', u'lat': u'38.8089', u'state': u'VA', u'client': u'@2170', u'servicecode': u'22', u'street1': u'35 Arell Court', u'sitterid': u'309', u'timeofday': u'5:00 pm-7:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'871662', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.055', u'clientid': u'1415', u'hours': u'00:00', u'lat': u'38.8345', u'state': u'VA', u'client': u'@1415', u'servicecode': u'113', u'street1': u'124 E Glebe Road', u'sitterid': u'316', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'871794', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0444', u'clientid': u'1806', u'hours': u'00:00', u'lat': u'38.8256', u'state': u'VA', u'client': u'@1806', u'servicecode': u'113', u'street1': u'1810 W Abingdon Drive #202', u'sitterid': u'318', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'871907', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0449', u'clientid': u'2086', u'hours': u'00:00', u'lat': u'38.8293', u'state': u'VA', u'client': u'@2086', u'servicecode': u'19', u'street1': u'701 Rose Square', u'sitterid': u'318', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22206', u'appointmentid': u'871949', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Brianna', u'completed': None, u'lon': u'-77.0947', u'clientid': u'2169', u'hours': u'00:00', u'lat': u'38.8374', u'state': u'VA', u'client': u'@2169', u'servicecode': u'19', u'street1': u'4640 31st Street South', u'sitterid': u'256', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872045', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0402', u'clientid': u'2191', u'hours': u'00:00', u'lat': u'38.8169', u'state': u'VA', u'client': u'@2191', u'servicecode': u'20', u'street1': u'328 3rd St', u'sitterid': u'318', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22312', u'appointmentid': u'872149', u'service': u'Monthly 30 Min Visit - 3 dog', u'sitter': u'Andrea R.', u'completed': None, u'lon': u'-77.1473', u'clientid': u'2137', u'hours': u'00:00', u'lat': u'38.822', u'state': u'VA', u'client': u'@2137', u'servicecode': u'21', u'street1': u'4542 Southland Ave', u'sitterid': u'317', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22312', u'appointmentid': u'872214', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Andrea R.', u'completed': None, u'lon': u'-77.154', u'clientid': u'619', u'hours': u'00:00', u'lat': u'38.8072', u'state': u'VA', u'client': u'@619', u'servicecode': u'113', u'street1': u'5267 Broadwing Place', u'sitterid': u'317', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22312', u'appointmentid': u'872271', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Andrea R.', u'completed': None, u'lon': u'-77.1382', u'clientid': u'1636', u'hours': u'00:00', u'lat': u'38.8252', u'state': u'VA', u'client': u'@1636', u'servicecode': u'19', u'street1': u'6109 N. Morgan St.', u'sitterid': u'317', u'timeofday': u'11:30 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'872380', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Andrea R.', u'completed': None, u'lon': u'-77.1252', u'clientid': u'1941', u'hours': u'00:00', u'lat': u'38.8095', u'state': u'VA', u'client': u'@1941', u'servicecode': u'113', u'street1': u'265 S. Pickett St. ', u'sitterid': u'317', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22304', u'appointmentid': u'872444', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Andrea R.', u'completed': None, u'lon': u'-77.1162', u'clientid': u'1958', u'hours': u'00:00', u'lat': u'38.8252', u'state': u'VA', u'client': u'@1958', u'servicecode': u'113', u'street1': u'1380 N Pegram Street', u'sitterid': u'317', u'timeofday': u'12:30 pm-2:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872508', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0466', u'clientid': u'1758', u'hours': u'00:00', u'lat': u'38.7975', u'state': u'VA', u'client': u'@1758', u'servicecode': u'113', u'street1': u'713 S Pitt St', u'sitterid': u'318', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872569', u'service': u'20 Min Visit - 1 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0455', u'clientid': u'1745', u'hours': u'00:00', u'lat': u'38.8001', u'state': u'VA', u'client': u'@1745', u'servicecode': u'110', u'street1': u'500 S. Pitt St', u'sitterid': u'318', u'timeofday': u'2:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872639', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0489', u'clientid': u'1928', u'hours': u'00:00', u'lat': u'38.8106', u'state': u'Va', u'client': u'@1928', u'servicecode': u'119', u'street1': u'517 N Patrick St', u'sitterid': u'319', u'timeofday': u'11:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872640', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0489', u'clientid': u'1928', u'hours': u'00:00', u'lat': u'38.8106', u'state': u'Va', u'client': u'@1928', u'servicecode': u'119', u'street1': u'517 N Patrick St', u'sitterid': u'319', u'timeofday': u'3:00 pm-4:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872751', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0496', u'clientid': u'1689', u'hours': u'00:00', u'lat': u'38.7966', u'state': u'VA', u'client': u'@1689', u'servicecode': u'113', u'street1': u'820 S Columbus St Apt 220', u'sitterid': u'319', u'timeofday': u'11:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872815', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0604', u'clientid': u'2161', u'hours': u'00:00', u'lat': u'38.8028', u'state': u'VA', u'client': u'@2161', u'servicecode': u'19', u'street1': u'401 Holland Lane #711', u'sitterid': u'319', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'872948', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.049', u'clientid': u'1138', u'hours': u'00:00', u'lat': u'38.7987', u'state': u'VA', u'client': u'@1138', u'servicecode': u'19', u'street1': u'680 S Columbus St', u'sitterid': u'319', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'873012', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0401', u'clientid': u'68', u'hours': u'00:00', u'lat': u'38.8005', u'state': u'VA', u'client': u'@68', u'servicecode': u'20', u'street1': u'4 Wolfe St.', u'sitterid': u'319', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22303', u'appointmentid': u'873076', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.0751', u'clientid': u'2107', u'hours': u'00:00', u'lat': u'38.7894', u'state': u'VA', u'client': u'@2107', u'servicecode': u'113', u'street1': u'5965 Grand Pavilion Way', u'sitterid': u'308', u'timeofday': u'10:00 am-12:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22310', u'appointmentid': u'873134', u'service': u'Monthly 30 Min Visit - 1 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.1459', u'clientid': u'1352', u'hours': u'00:00', u'lat': u'38.7868', u'state': u'VA', u'client': u'@1352', u'servicecode': u'19', u'street1': u'6012 Larkspur Drive', u'sitterid': u'308', u'timeofday': u'11:00 am-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22303', u'appointmentid': u'873281', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.0791', u'clientid': u'1977', u'hours': u'00:00', u'lat': u'38.7835', u'state': u'VA', u'client': u'@1977', u'servicecode': u'113', u'street1': u'6200 N Kings Hwy #248', u'sitterid': u'308', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'alexandria', u'zip': u'22310', u'appointmentid': u'873345', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.0988', u'clientid': u'1244', u'hours': u'00:00', u'lat': u'38.7803', u'state': u'VA', u'client': u'@1244', u'servicecode': u'20', u'street1': u'6302 Hillview Ave', u'sitterid': u'308', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22303', u'appointmentid': u'873409', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.0631', u'clientid': u'1592', u'hours': u'00:00', u'lat': u'38.7927', u'state': u'Va', u'client': u'@1592', u'servicecode': u'113', u'street1': u'5850 Cameron Run Terrace ', u'sitterid': u'308', u'timeofday': u'1:00 pm-3:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22303', u'appointmentid': u'873473', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Sandra', u'completed': None, u'lon': u'-77.0778', u'clientid': u'1487', u'hours': u'00:00', u'lat': u'38.7881', u'state': u'VA', u'client': u'@1487', u'servicecode': u'113', u'street1': u'5937 Williamsburg Rd', u'sitterid': u'308', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'873562', u'service': u'Monthly 20 Min Visit - 2 dog', u'sitter': u'Lara G.', u'completed': None, u'lon': u'-77.0476', u'clientid': u'1887', u'hours': u'00:00', u'lat': u'38.821', u'state': u'VA', u'client': u'@1887', u'servicecode': u'114', u'street1': u'1023 Bernard St.', u'sitterid': u'318', u'timeofday': u'11:30 am-1:30 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'874420', u'service': u'30 Min Pet Sit - 2 pets', u'sitter': u'Danny', u'completed': None, u'lon': u'-77.0505', u'clientid': u'1688', u'hours': u'00:00', u'lat': u'38.8135', u'state': u'VA', u'client': u'@1688', u'servicecode': u'23', u'street1': u'1122 Madison Street', u'sitterid': u'260', u'timeofday': u'5:00 pm-7:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'874423', u'service': u'30 Min Visit - 2 dogs', u'sitter': u'', u'completed': None, u'lon': u'-77.0505', u'clientid': u'1688', u'hours': u'00:00', u'lat': u'38.8135', u'state': u'VA', u'client': u'@1688', u'servicecode': u'2', u'street1': u'1122 Madison Street', u'sitterid': u'0', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'874471', u'service': u'30 Min Pet Sit - 2 pets', u'sitter': u'', u'completed': None, u'lon': u'-77.0554', u'clientid': u'1836', u'hours': u'00:00', u'lat': u'38.8595', u'state': u'VA', u'client': u'@1836', u'servicecode': u'23', u'street1': u'590 15th Street South, #339', u'sitterid': u'0', u'timeofday': u'5:00 pm-7:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'874794', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'Alba', u'completed': None, u'lon': u'-77.0433', u'clientid': u'1467', u'hours': u'00:00', u'lat': u'38.8182', u'state': u'va', u'client': u'@1467', u'servicecode': u'113', u'street1': u'604 bashford lane #2123', u'sitterid': u'82', u'timeofday': u'12:00 pm-2:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'874853', u'service': u'30 Min Pet Sit - 1 pet', u'sitter': u'', u'completed': None, u'lon': u'-77.0522', u'clientid': u'1945', u'hours': u'00:00', u'lat': u'38.8226', u'state': u'VA', u'client': u'@1945', u'servicecode': u'22', u'street1': u'501 E Duncan Ave', u'sitterid': u'0', u'timeofday': u'7:00 am-9:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'874854', u'service': u'30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0522', u'clientid': u'1945', u'hours': u'00:00', u'lat': u'38.8226', u'state': u'VA', u'client': u'@1945', u'servicecode': u'1', u'street1': u'501 E Duncan Ave', u'sitterid': u'0', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'875123', u'service': u'Monthly 30 Min Visit - 2 dog', u'sitter': u'Andy H.', u'completed': None, u'lon': u'-77.0496', u'clientid': u'2200', u'hours': u'00:00', u'lat': u'38.8075', u'state': u'VA', u'client': u'@2200', u'servicecode': u'20', u'street1': u'920 Queen St', u'sitterid': u'319', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Arlington', u'zip': u'22202', u'appointmentid': u'875203', u'service': u'30 Min Flex Visit - 1 dog', u'sitter': u'Anya', u'completed': None, u'lon': u'-77.0605', u'clientid': u'2079', u'hours': u'00:00', u'lat': u'38.8521', u'state': u'VA', u'client': u'@2079', u'servicecode': u'48', u'street1': u'820 24th St S', u'sitterid': u'269', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'alexandria', u'zip': u'22304', u'appointmentid': u'875250', u'service': u'Monthly 20 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.1243', u'clientid': u'1270', u'hours': u'00:00', u'lat': u'38.8206', u'state': u'VA', u'client': u'@1270', u'servicecode': u'113', u'street1': u'721 N Ripley St', u'sitterid': u'0', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22305', u'appointmentid': u'875584', u'service': u'Monthly 30 Min Visit - 3 dog', u'sitter': u'Farrah', u'completed': None, u'lon': u'-77.06', u'clientid': u'1212', u'hours': u'00:00', u'lat': u'38.8322', u'state': u'VA', u'client': u'@1212', u'servicecode': u'21', u'street1': u'3024 Mt Vernon Ave', u'sitterid': u'316', u'timeofday': u'1:00 pm-3:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22301', u'appointmentid': u'875846', u'service': u'30 Min Visit - 1 dog', u'sitter': u'', u'completed': None, u'lon': u'-77.0528', u'clientid': u'2002', u'hours': u'00:00', u'lat': u'38.8238', u'state': u'VA', u'client': u'@2002', u'servicecode': u'1', u'street1': u'416 E Bellefonte Ave', u'sitterid': u'0', u'timeofday': u'11:00 am-1:00 pm'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'875881', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0496', u'clientid': u'2200', u'hours': u'00:00', u'lat': u'38.8075', u'state': u'VA', u'client': u'@2200', u'servicecode': u'119', u'street1': u'920 Queen St', u'sitterid': u'306', u'timeofday': u'9:00 am-10:00 am'}, 
        {u'status': u'incomplete', u'city': u'Alexandria', u'zip': u'22314', u'appointmentid': u'875896', u'service': u'Monthly 20 Min Puppy - 1 dog', u'sitter': u'Cheryl S.', u'completed': None, u'lon': u'-77.0496', u'clientid': u'2200', u'hours': u'00:00', u'lat': u'38.8075', u'state': u'VA', u'client': u'@2200', u'servicecode': u'119', u'street1': u'920 Queen St', u'sitterid': u'306', u'timeofday': u'2:30 pm-3:30 pm'}]}

        sitter_data = {u'sittercount': 300,
                       u'sitters': [{u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'202 E. Custis Ave', u'lon': u'-77.0581', u'sitterid': u'1', u'lat': u'38.8256', u'state': u'VA', u'sitter': u'System Admin', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'3123 Elmwood Drive', u'lon': u'-77.0861', u'sitterid': u'2', u'lat': u'38.7985', u'state': u'VA', u'sitter': u'Ben Ball', u'active': u'0'}, 
        {u'city': u'ANNANDALE', u'zip': u'22003', u'street1': u'4204 Breezewood Lane', u'lon': u'-77.169', u'sitterid': u'3', u'lat': u'38.8327', u'state': u'VA', u'sitter': u'Bill', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22303', u'street1': u'2314 Victory Dr', u'lon': u'-77.0715', u'sitterid': u'4', u'lat': u'38.7959', u'state': u'VA', u'sitter': u'Ashley', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22206', u'street1': u'2961 S. Columbus St.', u'lon': u'-77.1009', u'sitterid': u'5', u'lat': u'38.8381', u'state': u'VA', u'sitter': u'Patricia', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'1710 Commonwealth Ave', u'lon': u'-78.2011', u'sitterid': u'6', u'lat': u'38.9351', u'state': u'VA', u'sitter': u'Dena', u'active': u'1'}, 
        {u'city': u'Annandale', u'zip': u'22003', u'street1': u'4303 S. Valiant Ct', u'lon': u'-77.2312', u'sitterid': u'7', u'lat': u'38.8302', u'state': u'VA', u'sitter': u'Dean', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22310', u'street1': u'6400 Wayside Place', u'lon': u'-77.1156', u'sitterid': u'8', u'lat': u'38.7793', u'state': u'VA', u'sitter': u'Holly', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22310', u'street1': u'6400 Wayside Place', u'lon': u'-77.1156', u'sitterid': u'9', u'lat': u'38.7793', u'state': u'VA', u'sitter': u'Robin', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22312', u'street1': u'301 N Beauregard St.', u'lon': u'-77.1381', u'sitterid': u'10', u'lat': u'38.8198', u'state': u'VA', u'sitter': u'Tammy Freeman', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22307', u'street1': u'Belle View Boulevards', u'lon': u'-77.0603', u'sitterid': u'11', u'lat': u'38.775', u'state': u'VA', u'sitter': u'Jackie Goin', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22311', u'street1': u'4713 West Braddock #10', u'lon': u'-77.1089', u'sitterid': u'12', u'lat': u'38.8362', u'state': u'VA', u'sitter': u'Brian Griffith', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22311', u'street1': u'4713 West Braddock Road #10', u'lon': u'-77.1089', u'sitterid': u'13', u'lat': u'38.8362', u'state': u'VA', u'sitter': u'Melissa Hall', u'active': u'0'}, 
        {u'city': u'ANNANDALE', u'zip': u'22003', u'street1': u'4575 Airlie Way', u'lon': u'-77.175', u'sitterid': u'14', u'lat': u'38.8265', u'state': u'VA', u'sitter': u'Erica', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22305', u'street1': u'18 F Auburn Court', u'lon': u'-77.0574', u'sitterid': u'15', u'lat': u'38.8346', u'state': u'VA', u'sitter': u'David Logan', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'2703 Dewitt Ave.', u'lon': u'-77.0566', u'sitterid': u'16', u'lat': u'38.8299', u'state': u'VA', u'sitter': u'Aubrey Ludwig', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20001', u'street1': u'1548 New Jersey Ave NW', u'lon': u'-77.0172', u'sitterid': u'17', u'lat': u'38.911', u'state': u'DC', u'sitter': u'John', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22308', u'street1': u'1008 DeWolfe Dr.', u'lon': u'-77.0491', u'sitterid': u'18', u'lat': u'38.7232', u'state': u'VA', u'sitter': u'Meredith Muckerman', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'3700 Valley Drive', u'lon': u'-77.0792', u'sitterid': u'19', u'lat': u'38.8406', u'state': u'VA', u'sitter': u'Kelly', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22207', u'street1': u'1810 N. Taylor St.', u'lon': u'-77.1135', u'sitterid': u'20', u'lat': u'38.8932', u'state': u'VA', u'sitter': u'Josh', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'300 Yoakum Parkway #1426', u'lon': u'-77.1383', u'sitterid': u'21', u'lat': u'38.8103', u'state': u'VA', u'sitter': u"Amy O'Halloran", u'active': u'0'}, 
        {u'city': u'WASHINGTON', u'zip': u'20002', u'street1': u'1119 Montello Ave NE', u'lon': u'-76.9895', u'sitterid': u'22', u'lat': u'38.9032', u'state': u'DC', u'sitter': u'Beth', u'active': u'0'}, 
        {u'city': u'Fairfax', u'zip': u'22033', u'street1': u'12249 Fairfield House Drive', u'lon': u'-77.3715', u'sitterid': u'23', u'lat': u'38.8635', u'state': u'VA', u'sitter': u'Andy', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'3815 Jason Ave', u'lon': u'-77.0945', u'sitterid': u'24', u'lat': u'38.8304', u'state': u'VA', u'sitter': u'Jessica', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'232 Evans Lane', u'lon': u'-77.0531', u'sitterid': u'25', u'lat': u'38.8355', u'state': u'VA', u'sitter': u'Sue', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'6419 Haystack Rd. in Alexandria', u'lon': u'-77.1182', u'sitterid': u'26', u'lat': u'38.7759', u'state': u'VA', u'sitter': u'Sarah', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'225 Century Place', u'lon': u'-77.1275', u'sitterid': u'27', u'lat': u'38.8163', u'state': u'VA', u'sitter': u'Cam', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'503 E. Windsor Ave', u'lon': u'-77.052', u'sitterid': u'28', u'lat': u'38.825', u'state': u'VA', u'sitter': u'Kim', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'232 Evans Lane', u'lon': u'-77.0531', u'sitterid': u'29', u'lat': u'38.8355', u'state': u'VA', u'sitter': u'Cori', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22201', u'street1': u'1904 Key Bvld', u'lon': u'-77.083', u'sitterid': u'30', u'lat': u'38.8945', u'state': u'VA', u'sitter': u'Matthew  Wagner', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'116 Hume Ave', u'lon': u'-77.0579', u'sitterid': u'31', u'lat': u'38.8312', u'state': u'VA', u'sitter': u'Becky', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'814 S. Patrick St. ', u'lon': u'-77.0519', u'sitterid': u'32', u'lat': u'38.7969', u'state': u'VA', u'sitter': u'Mechelle', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'2934 Sycamore St', u'lon': u'-77.0632', u'sitterid': u'33', u'lat': u'38.8325', u'state': u'VA', u'sitter': u'Larissa Gibson', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'309 Yoakum Parkway #1802', u'lon': u'-77.1419', u'sitterid': u'34', u'lat': u'38.8091', u'state': u'Va', u'sitter': u'Natalie', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'269 S. Pickett St.  ', u'lon': u'-77.1257', u'sitterid': u'35', u'lat': u'38.8094', u'state': u'VA', u'sitter': u'Vicki', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'6008 Stoddard ct.', u'lon': u'-77.1403', u'sitterid': u'36', u'lat': u'38.7622', u'state': u'VA', u'sitter': u'Geoff ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'1726 W Abingdon Dr.', u'lon': u'-77.0447', u'sitterid': u'37', u'lat': u'38.8237', u'state': u'VA', u'sitter': u'Jess ( Mc) ', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'3433 Pipit Drive', u'lon': u'-77.0907', u'sitterid': u'38', u'lat': u'38.7472', u'state': u'VA', u'sitter': u'Courtney', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'7932 Bayberry Drive ', u'lon': u'-77.0721', u'sitterid': u'39', u'lat': u'38.7408', u'state': u'VA', u'sitter': u'Becky B ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'5300 Larochelle Court', u'lon': u'-77.1279', u'sitterid': u'40', u'lat': u'38.7682', u'state': u'VA', u'sitter': u'Michelle', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'3775 Gunston Rd', u'lon': u'-77.0827', u'sitterid': u'41', u'lat': u'38.8403', u'state': u'VA', u'sitter': u'Jackie d', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'5831 Edgehill Dr', u'lon': u'-77.0807', u'sitterid': u'42', u'lat': u'38.7922', u'state': u'VA', u'sitter': u'Brian', u'active': u'0'}, 
        {u'city': None, u'zip': None, u'street1': None, u'sitterid': u'43', u'0': False, u'state': None, u'sitter': u'Tom ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'3488 Gunston Road', u'lon': u'-77.0781', u'sitterid': u'44', u'lat': u'38.8375', u'state': u'VA', u'sitter': u'Ron ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'1023 N Royal St #111', u'lon': u'-77.041', u'sitterid': u'45', u'lat': u'38.8153', u'state': u'VA', u'sitter': u'Sara Unsal ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22307', u'street1': u'7104 Rebecca Drive ', u'lon': u'-77.0693', u'sitterid': u'46', u'lat': u'38.7626', u'state': u'VA', u'sitter': u'Natasha ', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22305', u'street1': u'4 West Glebe Road', u'lon': u'-77.0582', u'sitterid': u'47', u'lat': u'38.8354', u'state': u'VA', u'sitter': u'Nicole', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22203', u'street1': u'4400 Starr Jordan Drive', u'lon': u'-77.2557', u'sitterid': u'48', u'lat': u'38.8289', u'state': u'VA', u'sitter': u'Christine', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22305', u'street1': u'8 Kennedy St', u'lon': u'-77.0602', u'sitterid': u'49', u'lat': u'38.8326', u'state': u'VA', u'sitter': u'Abby ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22311', u'street1': u'5001 Seminary Rd #1529', u'lon': u'-77.114', u'sitterid': u'50', u'lat': u'38.8329', u'state': u'VA', u'sitter': u'Jack', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'7932 Bayberry Drive', u'lon': u'-77.072', u'sitterid': u'51', u'lat': u'38.7407', u'state': u'VA', u'sitter': u'James ', u'active': u'0'}, 
        {u'city': u'Herndon', u'zip': None, u'street1': u'13123 Curved Iron Road', u'lon': u'-77.4014', u'sitterid': u'52', u'lat': u'38.9377', u'state': u'VA 20171', u'sitter': u'Niki', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'7129 Tolliver Street', u'lon': u'-77.0984', u'sitterid': u'53', u'lat': u'38.7635', u'state': u'VA', u'sitter': u'Richard', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'208 E. Howell Ave', u'lon': u'-77.0575', u'sitterid': u'54', u'lat': u'38.8241', u'state': u'VA', u'sitter': u'Emily', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22207', u'street1': u'3315 N Glebe Road', u'lon': u'-77.1324', u'sitterid': u'55', u'lat': u'38.9106', u'state': u'VA', u'sitter': u'Jackie', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22310', u'street1': u'6419 Haystack Road', u'lon': u'-77.118', u'sitterid': u'56', u'lat': u'38.7761', u'state': u'VA', u'sitter': u'John F', u'active': u'0'}, 
        {u'city': u'Coronado', u'zip': None, u'street1': u'228 F Ave', u'lon': u'-117.177', u'sitterid': u'57', u'lat': u'32.6984', u'state': u'92118', u'sitter': u'Lee', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22309', u'street1': u'3109 Battersea Lane', u'lon': u'-77.0853', u'sitterid': u'58', u'lat': u'38.726', u'state': u'VA', u'sitter': u'Mellisa', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22308', u'street1': u'8324 Fleetwood Ct.', u'lon': u'-77.0621', u'sitterid': u'59', u'lat': u'38.7321', u'state': u'VA', u'sitter': u'Ricky', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22207', u'street1': u'1810 North Taylor Street', u'lon': u'-77.1135', u'sitterid': u'60', u'lat': u'38.8932', u'state': u'VA', u'sitter': u'Jake', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22207', u'street1': u'4608 N. 37th Street', u'lon': u'-77.133', u'sitterid': u'61', u'lat': u'38.9166', u'state': u'VA', u'sitter': u'Will', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22204', u'street1': u'706 Arlington Mill Drive S.', u'lon': u'-77.1155', u'sitterid': u'62', u'lat': u'38.8605', u'state': u'VA', u'sitter': u'Kim C', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'1205 S. Washington St. ', u'lon': u'-77.0503', u'sitterid': u'63', u'lat': u'38.7927', u'state': u'VA', u'sitter': u'Brittany', u'active': u'0'}, 
        {u'city': u'SPRINGFIELD', u'zip': u'22150', u'street1': u'7433 Hastings Street', u'lon': u'-77.2013', u'sitterid': u'64', u'lat': u'38.7794', u'state': u'VA', u'sitter': u'Mark ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22311', u'street1': u'5731 Leverett Court', u'lon': u'-77.1282', u'sitterid': u'65', u'lat': u'38.8334', u'state': u'VA', u'sitter': u'Wendy ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': None, u'street1': u'7834 Flamingo Drive', u'lon': u'-77.0922', u'sitterid': u'66', u'lat': u'38.7439', u'state': u'VA', u'sitter': u'Luis', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22306', u'street1': u'6521 Brick Hearth Court', u'lon': u'-77.0874', u'sitterid': u'67', u'lat': u'38.7764', u'state': u'VA', u'sitter': u'Shannon W', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'508 A East Windsor Ave', u'lon': u'-77.0516', u'sitterid': u'68', u'lat': u'38.8255', u'state': u'VA', u'sitter': u'Meghan', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'13 Sunset Drive', u'lon': u'-77.0611', u'sitterid': u'69', u'lat': u'38.8076', u'state': u'VA', u'sitter': u'Lauren ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22311', u'street1': u'4719 W Braddock Rd', u'lon': u'-77.109', u'sitterid': u'70', u'lat': u'38.8362', u'state': u'VA', u'sitter': u'Emily S', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20019', u'street1': u'3335 Croffut Place SE Apt B ', u'lon': u'-76.9583', u'sitterid': u'71', u'lat': u'38.8866', u'state': u'DC', u'sitter': u'Diann', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'826 N. Iverson St', u'lon': u'-77.1065', u'sitterid': u'72', u'lat': u'38.8195', u'state': u'VA', u'sitter': u'Bruce', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'708 Duke Street', u'lon': u'-77.0483', u'sitterid': u'73', u'lat': u'38.8025', u'state': u'VA', u'sitter': u'Shannon S', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': None, u'street1': u'1205 H St.', u'lon': u'-77.0531', u'sitterid': u'74', u'lat': u'38.7775', u'state': u'22307', u'sitter': u'Say', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'7756 Desiree Street', u'lon': u'-77.1714', u'sitterid': u'75', u'lat': u'38.747', u'state': u'VA', u'sitter': u'James C', u'active': u'0'}, 
        {u'city': u'FAIRFAX', u'zip': u'22031', u'street1': u'3315 Rocky Mount Road', u'lon': u'-77.2638', u'sitterid': u'76', u'lat': u'38.8573', u'state': u'VA', u'sitter': u'Brian ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'904 1/2 Pendleton St', u'lon': u'-77.0484', u'sitterid': u'77', u'lat': u'38.8109', u'state': u'VA', u'sitter': u'Cassie', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22204', u'street1': u'5310 8th Road South', u'lon': u'-77.1196', u'sitterid': u'78', u'lat': u'38.8562', u'state': u'VA', u'sitter': u'Greg', u'active': u'0'}, 
        {u'city': u'FALLS CHURCH', u'zip': u'22042', u'street1': u'3287 Blue Heron Drive', u'lon': u'-77.1834', u'sitterid': u'79', u'lat': u'38.8585', u'state': u'VA', u'sitter': u'Susan', u'active': u'0'}, 
        {u'city': u'Bethesha', u'zip': None, u'street1': u'4517 sanganmore road', u'lon': u'-77.1184', u'sitterid': u'80', u'lat': u'38.9485', u'state': u'MD', u'sitter': u'Katie', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'6044 Joust Lane', u'lon': u'-77.1429', u'sitterid': u'81', u'lat': u'38.7636', u'state': u'VA', u'sitter': u'Charity', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'4390 King Street', u'lon': u'-77.1049', u'sitterid': u'82', u'lat': u'38.838', u'state': u'VA', u'sitter': u'Alba', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'502 Canterbury Lane', u'lon': u'-77.0863', u'sitterid': u'83', u'lat': u'38.8136', u'state': u'VA', u'sitter': u'Margaret', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22310', u'street1': u'4202 Javins Drive', u'lon': u'-77.1054', u'sitterid': u'84', u'lat': u'38.789', u'state': u'VA', u'sitter': u'Stewart', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'815 Duke Street', u'lon': u'-77.0493', u'sitterid': u'85', u'lat': u'38.8032', u'state': u'VA', u'sitter': u'Heather', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'5290 Duke St.', u'lon': u'-77.1247', u'sitterid': u'86', u'lat': u'38.8122', u'state': u'VA', u'sitter': u'Lain', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'5290 Duke St.', u'lon': u'-77.1247', u'sitterid': u'87', u'lat': u'38.8122', u'state': u'VA', u'sitter': u'Laine ', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'6009 Keble Drive', u'lon': u'-77.1443', u'sitterid': u'88', u'lat': u'38.7723', u'state': u'VA', u'sitter': u'Cheryl', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22209', u'street1': u'1305 North Pierce St', u'lon': u'-77.0766', u'sitterid': u'89', u'lat': u'38.8899', u'state': u'VA', u'sitter': u'Joey', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20024', u'street1': u'1150 4th St SW ', u'lon': u'-77.0176', u'sitterid': u'90', u'lat': u'38.8764', u'state': u'DC', u'sitter': u'Joe', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': None, u'street1': None, u'lon': u'-77.0469', u'sitterid': u'91', u'lat': u'38.8048', u'state': u'VA', u'sitter': u'Bryan', u'active': u'0'}, 
        {u'city': u'SPRINGFIELD', u'zip': u'22152', u'street1': u'8384 Forrester Blvd', u'lon': u'-77.2344', u'sitterid': u'92', u'lat': u'38.7918', u'state': u'VA', u'sitter': u'Chels', u'active': u'0'}, 
        {u'city': u'SPRINGFIELD', u'zip': u'22152', u'street1': u'8384 Forrester Blvd', u'lon': u'-77.2344', u'sitterid': u'93', u'lat': u'38.7918', u'state': u'VA', u'sitter': u'Chelsea', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'501 Holland Lane Apt. 702', u'lon': u'-77.0605', u'sitterid': u'94', u'lat': u'38.8018', u'state': u'VA', u'sitter': u'Becca1', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'501 Holland Lane Apt. 702', u'lon': u'-77.0605', u'sitterid': u'95', u'lat': u'38.8018', u'state': u'VA', u'sitter': u'B', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'501 Holland Lane Apt. 702', u'lon': u'-77.0605', u'sitterid': u'96', u'lat': u'38.8018', u'state': u'VA', u'sitter': u'Becca', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22307', u'street1': u'1304 Belle View Blvd. Unit #A1', u'lon': u'-77.0563', u'sitterid': u'97', u'lat': u'38.7755', u'state': u'VA', u'sitter': u'Chris', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22303', u'street1': u'5921 Williamsburg Road', u'lon': u'-77.0773', u'sitterid': u'98', u'lat': u'38.7889', u'state': u'VA', u'sitter': u'Laura', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'1314 Martha Custis Dr', u'lon': u'-77.0814', u'sitterid': u'101', u'lat': u'38.8418', u'state': u'VA', u'sitter': u'Tom 1', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22315', u'street1': u'7147 Barry Road', u'lon': u'-77.1685', u'sitterid': u'119', u'lat': u'38.7627', u'state': u'VA', u'sitter': u'Stephen ', u'active': u'0'}, 
        {u'city': u'ARLINGTON', u'zip': u'22202', u'street1': u'550 14th Road S, Apt 434', u'lon': u'-77.0561', u'sitterid': u'120', u'lat': u'38.8604', u'state': u'VA', u'sitter': u'Casey', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22309', u'street1': u'3117 McGeorge Terr', u'lon': u'-77.0846', u'sitterid': u'121', u'lat': u'38.7269', u'state': u'VA', u'sitter': u'Karen', u'active': u'1'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22308', u'street1': u'7801 Accotink Place', u'lon': u'-77.0536', u'sitterid': u'122', u'lat': u'38.7462', u'state': u'VA', u'sitter': u'Daniel', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'714 S. Fayette St', u'lon': u'-77.0536', u'sitterid': u'123', u'lat': u'38.7982', u'state': u'VA', u'sitter': u'EmilyC', u'active': u'0'}, 
        {u'city': u'FAIRFAX', u'zip': u'22032', u'street1': u'9108 Joyce Stree', u'lon': u'-77.2601', u'sitterid': u'124', u'lat': u'38.8356', u'state': u'VA', u'sitter': u'Ashley Briggs', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22307', u'street1': u'6621 Wakefield Drive #710', u'lon': u'-77.056', u'sitterid': u'125', u'lat': u'38.7722', u'state': u'VA', u'sitter': u'Maggie', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22304', u'street1': u'3533 Malvern Court', u'lon': u'-77.0915', u'sitterid': u'126', u'lat': u'38.8145', u'state': u'VA', u'sitter': u'Wesley', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22314', u'street1': u'404 Oronoco Street', u'lon': u'-77.043', u'sitterid': u'127', u'lat': u'38.8091', u'state': u'VA', u'sitter': u'MelissaR', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22301', u'street1': u'510 North View Terrace', u'lon': u'-77.0672', u'sitterid': u'128', u'lat': u'38.8119', u'state': u'VA', u'sitter': u'Cal', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22308', u'street1': u'8109 Wellington Road', u'lon': u'-77.053', u'sitterid': u'129', u'lat': u'38.739', u'state': u'VA', u'sitter': u'Kathy', u'active': u'0'}, 
        {u'city': u'ANNANDALE', u'zip': u'22003', u'street1': u'7400 Auburn St', u'lon': u'-77.2007', u'sitterid': u'130', u'lat': u'38.8182', u'state': u'VA', u'sitter': u'Lyn', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'804 W Timber Branch Pkwy', u'lon': u'-77.0768', u'sitterid': u'131', u'lat': u'38.8222', u'state': u'VA', u'sitter': u'Deke', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22310', u'street1': u'6511 Berkshire Dr', u'lon': u'-77.0954', u'sitterid': u'132', u'lat': u'38.7757', u'state': u'VA', u'sitter': u'Amy', u'active': u'0'}, 
        {u'city': u'ALEXANDRIA', u'zip': u'22302', u'street1': u'804 Timber Branch Parkway', u'lon': u'-77.0768', u'sitterid': u'133', u'lat': u'38.8222', u'state': u'VA', u'sitter': u'Teddy', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'604 South Fairfax Street', u'lon': u'-77.0436', u'sitterid': u'134', u'lat': u'38.7986', u'state': u'VA', u'sitter': u'Lisa', u'active': u'0'}, 
        {u'city': u'Springfield', u'zip': u'22153', u'street1': u'7303 Whitson Drive', u'lon': u'-77.2452', u'sitterid': u'135', u'lat': u'38.7579', u'state': u'VA', u'sitter': u'Loren ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'1003 Croton Drive', u'lon': u'-77.0486', u'sitterid': u'136', u'lat': u'38.7246', u'state': u'VA', u'sitter': u'Jeff', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': None, u'lon': u'-77.0469', u'sitterid': u'137', u'lat': u'38.8048', u'state': u'VA', u'sitter': u'KathyB', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'224 N Patrick St ', u'lon': u'-77.0501', u'sitterid': u'138', u'lat': u'38.8074', u'state': u'VA', u'sitter': u'Sara', u'active': u'0'}, 
        {u'city': u'Fairfax', u'zip': u'22033', u'street1': u'4433 Majestic Lane', u'lon': u'-77.4076', u'sitterid': u'139', u'lat': u'38.8728', u'state': u'VA', u'sitter': u'Andrew', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22306', u'street1': u'7255 Stover Drive', u'lon': u'-77.1004', u'sitterid': u'140', u'lat': u'38.762', u'state': u'VA', u'sitter': u'Linda', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22303', u'street1': u'5612 Norton Road', u'lon': u'-77.0936', u'sitterid': u'141', u'lat': u'38.7985', u'state': u'VA', u'sitter': u'Jamie', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'1600 Cool Spring Dr', u'lon': u'-77.0596', u'sitterid': u'142', u'lat': u'38.7322', u'state': u'VA', u'sitter': u'Leisha', u'active': u'1'}, 
        {u'city': u'Fairfax', u'zip': u'22033', u'street1': u'3606 Paramount rd', u'lon': u'-77.3844', u'sitterid': u'143', u'lat': u'38.8891', u'state': u'VA', u'sitter': u'ChrisM', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'404 Oronoco Street', u'lon': u'-77.043', u'sitterid': u'144', u'lat': u'38.8091', u'state': u'VA', u'sitter': u'Emma', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22044', u'street1': u'6189 Vine Forest Court', u'lon': u'-77.149', u'sitterid': u'145', u'lat': u'38.8609', u'state': u'VA', u'sitter': u'Christen ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'3823 Courtland Circle', u'lon': u'-77.0663', u'sitterid': u'146', u'lat': u'38.8406', u'state': u'VA', u'sitter': u'Sarah B', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'2351 Eisenhower Avenue #720', u'lon': u'-77.0692', u'sitterid': u'147', u'lat': u'38.8014', u'state': u'VA', u'sitter': u'Ximena', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'5300 Holmes Run Pkwy', u'lon': u'-77.1223', u'sitterid': u'148', u'lat': u'38.8149', u'state': u'VA', u'sitter': u'David', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'2730 Monacan Street Apt. 303', u'lon': u'-77.0805', u'sitterid': u'149', u'lat': u'38.8035', u'state': u'VA', u'sitter': u'Janet', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22205', u'street1': u'1007 N George Mason Drive', u'lon': u'-77.1226', u'sitterid': u'150', u'lat': u'38.8828', u'state': u'VA', u'sitter': u'Kristin ', u'active': u'0'}, 
        {u'city': u'Vienna', u'zip': u'22182', u'street1': u'2246 Richelieu Drive', u'lon': u'-77.2404', u'sitterid': u'151', u'lat': u'38.8986', u'state': u'VA', u'sitter': u'DeanG', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'5611 Franconia Rd', u'lon': u'-77.1312', u'sitterid': u'152', u'lat': u'38.7836', u'state': u'VA', u'sitter': u'Katie k', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'1211 Hillside Terrace', u'lon': u'-77.0796', u'sitterid': u'153', u'lat': u'38.8272', u'state': u'VA', u'sitter': u'Nate', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22206', u'street1': u'2400 South Glebe Road', u'lon': u'-77.0818', u'sitterid': u'154', u'lat': u'38.8492', u'state': u'VA', u'sitter': u'Andrea', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1204 S. Alfred Street', u'lon': u'-77.0504', u'sitterid': u'155', u'lat': u'38.7916', u'state': u'VA', u'sitter': u'Liz  ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'6304 Hillview Ave', u'lon': u'-77.0991', u'sitterid': u'156', u'lat': u'38.7802', u'state': u'VA', u'sitter': u'Bridget', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22206', u'street1': u'5036 22nd Street South', u'lon': u'-77.1079', u'sitterid': u'158', u'lat': u'38.8437', u'state': u'VA', u'sitter': u'Jeannie', u'active': u'0'}, 
        {u'city': u'Annandale', u'zip': u'22003', u'street1': u'7038 Bradley Circle ', u'lon': u'-77.1898', u'sitterid': u'159', u'lat': u'38.8442', u'state': u'VA', u'sitter': u'Arielle', u'active': u'0'}, 
        {u'city': u'LATROBE', u'zip': u'15650', u'street1': u'4130 ST RT 982', u'lon': u'-79.3761', u'sitterid': u'160', u'lat': u'40.2664', u'state': u'PA', u'sitter': u'Mina', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': None, u'street1': u'5733 Heritage Hill Court ', u'lon': u'-77.0841', u'sitterid': u'161', u'lat': u'38.7951', u'state': u'22310', u'sitter': u'Leah', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'4506 Taney Ave', u'lon': u'-77.109', u'sitterid': u'162', u'lat': u'38.8156', u'state': u'VA', u'sitter': u'Rachael', u'active': u'0'}, 
        {u'city': u'Fairfax', u'zip': u'22031', u'street1': u'9010 Bowler Drive', u'lon': u'-77.2573', u'sitterid': u'163', u'lat': u'38.8693', u'state': u'VA', u'sitter': u'Gerald', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'518 N. Columbus St', u'lon': u'-77.0473', u'sitterid': u'164', u'lat': u'38.8104', u'state': u'VA', u'sitter': u'Jeanette', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22043', u'street1': u'6805 Montour Drive', u'lon': u'-77.1793', u'sitterid': u'165', u'lat': u'38.9026', u'state': u'VA', u'sitter': u'Steve', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'801 S. Pitt Street', u'lon': u'-77.0471', u'sitterid': u'166', u'lat': u'38.7962', u'state': u'VA', u'sitter': u'Jacqui', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'2500 N. Van Dorn St.', u'lon': u'-77.0997', u'sitterid': u'167', u'lat': u'38.8327', u'state': u'VA', u'sitter': u'Karen B.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'7124 Judith Ave', u'lon': u'-77.1601', u'sitterid': u'168', u'lat': u'38.763', u'state': u'VA', u'sitter': u'Laura W', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'3900 Adrienne Dr', u'lon': u'-77.099', u'sitterid': u'169', u'lat': u'38.7183', u'state': u'VA', u'sitter': u'Erik', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'6727 West Wakefield Dr,', u'lon': u'-77.0612', u'sitterid': u'170', u'lat': u'38.7738', u'state': u'VA', u'sitter': u'Diane', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'1600 Cool Spring Drive', u'lon': u'-77.0596', u'sitterid': u'171', u'lat': u'38.7322', u'state': u'VA', u'sitter': u'Peyton', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22311', u'street1': u'1464 South Greenmount Drive', u'lon': u'-77.1252', u'sitterid': u'172', u'lat': u'38.8283', u'state': u'VA', u'sitter': u'Kassandra', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22042-3315', u'street1': u'3268 Holly Berry Ct.', u'lon': u'-77.2163', u'sitterid': u'173', u'lat': u'38.8562', u'state': u'VA 22042-3315', u'sitter': u'Robert', u'active': u'0'}, 
        {u'city': u'Melbourne', u'zip': u'32935', u'street1': u'2785 Forest Run Drive', u'lon': u'-80.6683', u'sitterid': u'174', u'lat': u'28.1802', u'state': u'FL', u'sitter': u'Kellee', u'active': u'0'}, 
        {u'city': None, u'zip': None, u'street1': None, u'sitterid': u'175', u'0': False, u'state': None, u'sitter': u'Colleen', u'active': u'0'}, 
        {u'city': u'Springfield', u'zip': u'22153', u'street1': u'8043 Felecity Court', u'lon': u'-77.2147', u'sitterid': u'176', u'lat': u'38.7395', u'state': u'VA', u'sitter': u'Sharon', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'171 Sommervelle St #213', u'lon': u'-77.1164', u'sitterid': u'177', u'lat': u'38.8093', u'state': u'VA', u'sitter': u'Barbara', u'active': u'1'}, 
        {u'city': u'Deltona', u'zip': u'32725', u'street1': u'1132 Swan St', u'lon': u'-81.2432', u'sitterid': u'178', u'lat': u'28.9156', u'state': u'FL', u'sitter': u'Robbie', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'1504 Cool Spring Drive', u'lon': u'-77.0588', u'sitterid': u'179', u'lat': u'38.732', u'state': u'VA', u'sitter': u'DavidM', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'708 Pendleton St.', u'lon': u'-77.0464', u'sitterid': u'180', u'lat': u'38.8106', u'state': u'VA', u'sitter': u'Testy', u'active': u'1'}, 
        {u'city': u'EAST BURKE', u'zip': u'05832', u'street1': u'149 Marshall Newland Rd', u'lon': u'-71.9237', u'sitterid': u'181', u'lat': u'44.6191', u'state': u'VT', u'sitter': u'Haillie', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22306', u'street1': u'2412 Fairview Drive', u'lon': u'-77.0748', u'sitterid': u'182', u'lat': u'38.7782', u'state': u'VA', u'sitter': u'Dave', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'610 N. West Street', u'lon': u'-77.0537', u'sitterid': u'183', u'lat': u'38.8119', u'state': u'VA', u'sitter': u'Jess', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'4206 Duvawn Street', u'lon': u'-77.1048', u'sitterid': u'184', u'lat': u'38.7872', u'state': u'VA', u'sitter': u'Lara', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'305 S. Edgewood Street', u'lon': u'-77.0873', u'sitterid': u'185', u'lat': u'38.8702', u'state': u'VA', u'sitter': u'Jennifer', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'4604 Raleigh Avenue', u'lon': u'-77.1114', u'sitterid': u'186', u'lat': u'38.8142', u'state': u'VA', u'sitter': u'Rebecca', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'4401 Groombridge Way', u'lon': u'-77.1075', u'sitterid': u'187', u'lat': u'38.7327', u'state': u'VA', u'sitter': u'Francis', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'1509 Belle View Blvd', u'lon': u'-77.0591', u'sitterid': u'188', u'lat': u'38.7746', u'state': u'VA', u'sitter': u'Sa\xfal', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1020 Queen Street', u'lon': u'-77.0505', u'sitterid': u'189', u'lat': u'38.8077', u'state': u'VA', u'sitter': u'Jessica ', u'active': u'1'}, 
        {u'city': u'Washington', u'zip': u'20032', u'street1': None, u'lon': u'-77.0369', u'sitterid': u'190', u'lat': u'38.9072', u'state': u'DC', u'sitter': u'Brendan', u'active': u'0'}, 
        {u'city': u'Centreville', u'zip': u'20120', u'street1': u'14531 South Hills Court', u'lon': u'-77.4533', u'sitterid': u'191', u'lat': u'38.8682', u'state': u'VA', u'sitter': u'Cat', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'4922 Celtic Drive ', u'lon': u'-77.1195', u'sitterid': u'192', u'lat': u'38.7821', u'state': u'VA', u'sitter': u'Alek', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'7628 Hayfield Road', u'lon': u'-77.1371', u'sitterid': u'193', u'lat': u'38.7494', u'state': u'VA', u'sitter': u'Amanda', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22303', u'street1': u'5840 Cameron Run Terrace', u'lon': u'-77.0617', u'sitterid': u'194', u'lat': u'38.7937', u'state': u'VA', u'sitter': u'Stephanie', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22203', u'street1': u'900 North Stuart St. ', u'lon': u'-77.1122', u'sitterid': u'195', u'lat': u'38.8806', u'state': u'VA', u'sitter': u'Kelsey', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'205 E. Oxford Ave', u'lon': u'-77.0581', u'sitterid': u'196', u'lat': u'38.8267', u'state': u'VA', u'sitter': u'Olivia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'412 Hanson Lane ', u'lon': u'-77.0698', u'sitterid': u'197', u'lat': u'38.8186', u'state': u'VA', u'sitter': u'Jacque', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'5375 Duke St', u'lon': u'-77.1246', u'sitterid': u'198', u'lat': u'38.8144', u'state': u'VA', u'sitter': u'Nathan ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'3301 Valley Drive', u'lon': u'-77.0798', u'sitterid': u'199', u'lat': u'38.8353', u'state': u'VA', u'sitter': u'HeatherR', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'620 N Fayette St ', u'lon': u'-77.0516', u'sitterid': u'200', u'lat': u'38.8122', u'state': u'VA', u'sitter': u'Fabio ', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1202 Colonial Avenue ', u'lon': u'-77.0487', u'sitterid': u'201', u'lat': u'38.8179', u'state': u'VA', u'sitter': u'Brett', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'401 E. Del Ray Avenue', u'lon': u'-77.0543', u'sitterid': u'202', u'lat': u'38.8263', u'state': u'VA', u'sitter': u'Bob', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'3904 Ivanhoe Lane ', u'lon': u'-77.0991', u'sitterid': u'203', u'lat': u'38.7899', u'state': u'VA', u'sitter': u'August', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22205', u'street1': u'6110 23rd St. N', u'lon': u'-77.1489', u'sitterid': u'204', u'lat': u'38.8917', u'state': u'VA', u'sitter': u'Mollie', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22046', u'street1': u'413 Sherrow Avenue', u'lon': u'-77.1809', u'sitterid': u'205', u'lat': u'38.8829', u'state': u'VA', u'sitter': u'Frances', u'active': u'0'}, 
        {u'city': u'Burr Hill', u'zip': u'22433', u'street1': u'29228 Raccoon Ford Rd', u'lon': u'-77.8658', u'sitterid': u'206', u'lat': u'38.3495', u'state': u'VA', u'sitter': u'Laura M.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'5332 Truman Avenue', u'lon': u'-77.1227', u'sitterid': u'207', u'lat': u'38.8188', u'state': u'VA', u'sitter': u'Piero', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22041', u'street1': u'6369 Lakewood Dr.', u'lon': u'-77.1568', u'sitterid': u'208', u'lat': u'38.8396', u'state': u'VA', u'sitter': u'Sam', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'7469 Digby Green', u'lon': u'-77.1549', u'sitterid': u'209', u'lat': u'38.7569', u'state': u'VA', u'sitter': u'Christine W', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1012 Pendleton Street', u'lon': u'-77.0497', u'sitterid': u'210', u'lat': u'38.811', u'state': u'VA', u'sitter': u'Caren', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'40 S. Ingram St.', u'lon': u'-77.1064', u'sitterid': u'211', u'lat': u'38.8103', u'state': u'VA', u'sitter': u'Sarah D', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'2719 Bryan Place', u'lon': u'-77.0765', u'sitterid': u'212', u'lat': u'38.8149', u'state': u'VA', u'sitter': u'Anna', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'501 Slaters Lane', u'lon': u'-77.0412', u'sitterid': u'213', u'lat': u'38.8227', u'state': u'VA', u'sitter': u'Jess T', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'1313 South Columbus St', u'lon': u'-77.1084', u'sitterid': u'214', u'lat': u'38.8512', u'state': u'VA', u'sitter': u'Mike', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'922 S Washington Street', u'lon': u'-77.0484', u'sitterid': u'215', u'lat': u'38.7961', u'state': u'VA', u'sitter': u'Nathan V', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'2703 Mount Vernon Ave ', u'lon': u'-77.0592', u'sitterid': u'216', u'lat': u'38.8296', u'state': u'VA', u'sitter': u'Bill P', u'active': u'0'}, 
        {u'city': u'Fairfax', u'zip': u'22031', u'street1': u'3316 Highland Lane ', u'lon': u'-77.2425', u'sitterid': u'217', u'lat': u'38.8572', u'state': u'VA', u'sitter': u'Stephen B', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1111 Belle Pre Way', u'lon': u'-77.0504', u'sitterid': u'218', u'lat': u'38.8143', u'state': u'VA', u'sitter': u'Miguel', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'308 Virginia', u'lon': u'-77.0695', u'sitterid': u'219', u'lat': u'38.8269', u'state': u'VA', u'sitter': u'Randy', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'404 E Monroe Ave', u'lon': u'-77.0553', u'sitterid': u'220', u'lat': u'38.8211', u'state': u'VA', u'sitter': u'Marcia Bennett', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22202', u'street1': u'2629 S. Hayes Street', u'lon': u'-77.0588', u'sitterid': u'221', u'lat': u'38.8492', u'state': u'VA', u'sitter': u'Stephanie W', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'116 Hume Ave', u'lon': u'-77.0579', u'sitterid': u'222', u'lat': u'38.8312', u'state': u'VA', u'sitter': u'Shawna', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'3100 Commonwealth Ave #307', u'lon': u'-77.0592', u'sitterid': u'223', u'lat': u'38.833', u'state': u'VA', u'sitter': u'Jenna', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'7037 Quander Road', u'lon': u'-77.0612', u'sitterid': u'224', u'lat': u'38.7646', u'state': u'VA', u'sitter': u'Leila', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22205', u'street1': u'5507 22nd Street North', u'lon': u'-77.1381', u'sitterid': u'225', u'lat': u'38.8932', u'state': u'VA', u'sitter': u'Ayse', u'active': u'1'}, 
        {u'city': u'Burke', u'zip': u'22015', u'street1': u'5418 Tripolis Court', u'lon': u'-77.271', u'sitterid': u'226', u'lat': u'38.804', u'state': u'VA', u'sitter': u'AndrewP', u'active': u'0'}, 
        {u'city': u'Washington DC', u'zip': u'20003', u'street1': u'1810 C Street SE', u'lon': u'-76.9786', u'sitterid': u'227', u'lat': u'38.8856', u'state': u'District of Columbia', u'sitter': u'Colby', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'318 E. Windsor Ave', u'lon': u'-77.0548', u'sitterid': u'228', u'lat': u'38.8252', u'state': u'VA', u'sitter': u'Wes', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22205', u'street1': u'5507 22nd Street North', u'lon': u'-77.1381', u'sitterid': u'229', u'lat': u'38.8932', u'state': u'VA', u'sitter': u'Chris R', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'1400 South Barton Street # 418', u'lon': u'-77.0834', u'sitterid': u'230', u'lat': u'38.8598', u'state': u'VA', u'sitter': u'Christine K', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'1517 Belle View Blvd A2', u'lon': u'-77.0595', u'sitterid': u'231', u'lat': u'38.7745', u'state': u'VA', u'sitter': u'Daniel L', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'220 N. Saint Aspah St Apt. 2', u'lon': u'-77.0458', u'sitterid': u'232', u'lat': u'38.8068', u'state': u'VA', u'sitter': u'Lacey', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'525 Bashford Lane', u'lon': u'-77.043', u'sitterid': u'233', u'lat': u'38.8191', u'state': u'VA', u'sitter': u'Ruth', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20002', u'street1': u'401 13th street NE', u'lon': u'-76.988', u'sitterid': u'234', u'lat': u'38.8951', u'state': u'DC', u'sitter': u'Ron', u'active': u'1'}, 
        {u'city': u'Washington', u'zip': u'20016', u'street1': u'3218 Wisconsin Ave. NW', u'lon': u'-77.073', u'sitterid': u'235', u'lat': u'38.9326', u'state': u'DC', u'sitter': u'Margie', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'16 E. Mason Ave Apt. 24', u'lon': u'-77.0619', u'sitterid': u'236', u'lat': u'38.8212', u'state': u'VA', u'sitter': u'Alecia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'3110 Mount Vernon Apt. 1007', u'lon': u'-77.0608', u'sitterid': u'237', u'lat': u'38.8337', u'state': u'VA', u'sitter': u'Stephanie D', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22207', u'street1': u'2105 N Glebe Rd # 1316', u'lon': u'-77.1218', u'sitterid': u'238', u'lat': u'38.8964', u'state': u'VA', u'sitter': u'Kylie', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'3244 Valley Drive', u'lon': u'-77.0779', u'sitterid': u'239', u'lat': u'38.8416', u'state': u'VA', u'sitter': u'Lisa H.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'813 Prince Street', u'lon': u'-77.049', u'sitterid': u'240', u'lat': u'38.8044', u'state': u'VA', u'sitter': u'Mary', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'309 Holland Lane #323', u'lon': u'-77.0599', u'sitterid': u'241', u'lat': u'38.8038', u'state': u'VA', u'sitter': u'Emma C.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22311', u'street1': u'4560 Strutfield Lane #1402', u'lon': u'-77.1055', u'sitterid': u'242', u'lat': u'38.8356', u'state': u'VA', u'sitter': u'Farah', u'active': u'0'}, 
        {u'city': u'Annandale', u'zip': u'22003', u'street1': u'9109 Colt Lane', u'lon': u'-77.2588', u'sitterid': u'243', u'lat': u'38.813', u'state': u'VA', u'sitter': u'Matt', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'2703 Mt. Vernon Ave Apt 4', u'lon': u'-77.0592', u'sitterid': u'244', u'lat': u'38.8296', u'state': u'VA', u'sitter': u'Noah', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'1201 S Courthouse Rd', u'lon': u'-77.0791', u'sitterid': u'245', u'lat': u'38.8623', u'state': u'VA', u'sitter': u'Luisa', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'6A leadbeater St. ', u'lon': u'-77.0589', u'sitterid': u'246', u'lat': u'38.8348', u'state': u'VA', u'sitter': u'Ken', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'8524 Richmond Ave', u'lon': u'-77.1039', u'sitterid': u'247', u'lat': u'38.7256', u'state': u'VA', u'sitter': u'Jen', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'1601 King James Place', u'lon': u'-77.1024', u'sitterid': u'248', u'lat': u'38.824', u'state': u'VA', u'sitter': u'Neil', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'4701 Kenmore Ave.', u'lon': u'-77.1127', u'sitterid': u'249', u'lat': u'38.8282', u'state': u'VA', u'sitter': u'Cynthia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'100 Luna Park Dr. Apt # 179', u'lon': u'-77.0539', u'sitterid': u'250', u'lat': u'38.8375', u'state': u'VA', u'sitter': u'Laura D', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'211 N West St Apt 2', u'lon': u'-77.0539', u'sitterid': u'251', u'lat': u'38.8076', u'state': u'VA', u'sitter': u'Robbyn', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'311 Beverly Drive', u'lon': u'-77.0687', u'sitterid': u'252', u'lat': u'38.8347', u'state': u'VA', u'sitter': u'Justine', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'5731 Lawson Hill Ct.', u'lon': u'-77.0846', u'sitterid': u'253', u'lat': u'38.7952', u'state': u'VA', u'sitter': u'Taylor', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'6161 Morning Glory Rd', u'lon': u'-77.1398', u'sitterid': u'254', u'lat': u'38.7844', u'state': u'VA', u'sitter': u'Antony', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'506 E. Custis Avenue', u'lon': u'-77.052', u'sitterid': u'255', u'lat': u'38.8261', u'state': u'VA', u'sitter': u'Kate', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'2105 Mt Vernon Ave', u'lon': u'-77.0582', u'sitterid': u'256', u'lat': u'38.825', u'state': u'VA', u'sitter': u'Brianna', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'8500 Crossley Pl', u'lon': u'-77.0572', u'sitterid': u'257', u'lat': u'38.7272', u'state': u'VA', u'sitter': u'Shayne', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'2201 Mill Road Apt 315', u'lon': u'-77.0664', u'sitterid': u'258', u'lat': u'38.7989', u'state': u'VA', u'sitter': u'Branigan', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'1819 Duffield Lane', u'lon': u'-77.0624', u'sitterid': u'259', u'lat': u'38.7887', u'state': u'VA', u'sitter': u'Denisa', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'625 E Monroe Avenue', u'lon': u'-77.0506', u'sitterid': u'260', u'lat': u'38.8206', u'state': u'VA', u'sitter': u'Danny', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'724 South Saint Asaph Street', u'lon': u'-77.0471', u'sitterid': u'261', u'lat': u'38.7974', u'state': u'VA', u'sitter': u'Kable', u'active': u'0'}, 
        {u'city': u'Rockville', u'zip': u'20852', u'street1': u'5401 McGrath Blvd', u'lon': u'-77.1078', u'sitterid': u'262', u'lat': u'39.0493', u'state': u'MD', u'sitter': u'Beatrix D.', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'3061 Mount Vernon Avenue', u'lon': u'-77.0598', u'sitterid': u'263', u'lat': u'38.8331', u'state': u'VA', u'sitter': u'Katie O.', u'active': u'0'}, 
        {u'city': u'Springfield', u'zip': u'22153', u'street1': u'8116 North Numberland RD', u'lon': u'-77.2156', u'sitterid': u'264', u'lat': u'38.7355', u'state': u'VA', u'sitter': u'Meagan', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22207', u'street1': u'2217 N. Kentucky Street', u'lon': u'-77.1414', u'sitterid': u'265', u'lat': u'38.8927', u'state': u'VA', u'sitter': u'Beatrix B.', u'active': u'1'}, 
        {u'city': u'Springfield', u'zip': u'22152', u'street1': u'6706 Huntsman Blvd', u'lon': u'-77.2499', u'sitterid': u'266', u'lat': u'38.7704', u'state': u'VA', u'sitter': u'Bella', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'8501 Engleside Street', u'lon': u'-77.12', u'sitterid': u'267', u'lat': u'38.7261', u'state': u'VA', u'sitter': u'Cisco', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1111 North Royal Street', u'lon': u'-77.0409', u'sitterid': u'268', u'lat': u'38.8163', u'state': u'VA', u'sitter': u'Lidia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'3460 Martha Custis Drive', u'lon': u'-77.0835', u'sitterid': u'269', u'lat': u'38.8374', u'state': u'VA', u'sitter': u'Anya', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22312', u'street1': u'403 N Beauregard St', u'lon': u'-77.1357', u'sitterid': u'270', u'lat': u'38.8211', u'state': u'VA', u'sitter': u'Beatriz', u'active': u'0'}, 
        {u'city': u'Fort Washington', u'zip': u'20744', u'street1': u'6807 Bock Road', u'lon': u'-76.9766', u'sitterid': u'271', u'lat': u'38.7955', u'state': u'MD', u'sitter': u'Selma', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'233 Cameron Station Blvd', u'lon': u'-77.1205', u'sitterid': u'272', u'lat': u'38.8077', u'state': u'VA', u'sitter': u'EB', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'305 W. Myrtle St.', u'lon': u'-77.0677', u'sitterid': u'273', u'lat': u'38.8148', u'state': u'VA', u'sitter': u'Grace', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'6310 Brocketts Crossing', u'lon': u'-77.1614', u'sitterid': u'274', u'lat': u'38.7529', u'state': u'VA', u'sitter': u'Kyle', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'12 Leadbeater Street', u'lon': u'-77.0593', u'sitterid': u'275', u'lat': u'38.8349', u'state': u'VA', u'sitter': u'Brenda', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'6237 Gentle Lane', u'lon': u'-77.0848', u'sitterid': u'276', u'lat': u'38.781', u'state': u'VA', u'sitter': u'Keith', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1421 Oronoco Street', u'lon': u'-77.0542', u'sitterid': u'277', u'lat': u'38.8108', u'state': u'VA', u'sitter': u'Sally', u'active': u'0'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'4600 S. Four Mile Run Dr., #516', u'lon': u'-77.1074', u'sitterid': u'278', u'lat': u'38.8549', u'state': u'VA', u'sitter': u'Maria', u'active': u'1'}, 
        {u'city': u'Burke', u'zip': u'22015', u'street1': u'6000 Coffer Woods Ct', u'lon': u'-77.2905', u'sitterid': u'279', u'lat': u'38.7904', u'state': u'VA', u'sitter': u'Gina', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'205 Wesmond Drive', u'lon': u'-77.0544', u'sitterid': u'280', u'lat': u'38.8347', u'state': u'VA', u'sitter': u'Andrea H.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'3811 Maryl St', u'lon': u'-77.0997', u'sitterid': u'281', u'lat': u'38.7245', u'state': u'VA', u'sitter': u'Alexei', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22308', u'street1': u'1024 Croton Dr', u'lon': u'-77.0494', u'sitterid': u'282', u'lat': u'38.7274', u'state': u'VA', u'sitter': u'Miles', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'3904 Ivanhoe Lane', u'lon': u'-77.0991', u'sitterid': u'283', u'lat': u'38.7899', u'state': u'VA', u'sitter': u'Jacqueline', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'432 N. St. Asaph St', u'lon': u'-77.0454', u'sitterid': u'284', u'lat': u'38.8089', u'state': u'VA', u'sitter': u'Jesse', u'active': u'0'}, 
        {u'city': u'Ashburn', u'zip': u'20147', u'street1': u'20880 Isherwood Terrace, #300', u'lon': u'-77.5069', u'sitterid': u'285', u'lat': u'39.0389', u'state': u'VA', u'sitter': u'May', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'2101 Mill Road', u'lon': u'-77.0671', u'sitterid': u'286', u'lat': u'38.7994', u'state': u'VA', u'sitter': u'MollieW', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22306', u'street1': u'2704 Popkins Lane', u'lon': u'-77.0783', u'sitterid': u'287', u'lat': u'38.7645', u'state': u'VA', u'sitter': u'Fadia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22303', u'street1': u'2650 Fort Dr, Apt 302', u'lon': u'-77.0778', u'sitterid': u'288', u'lat': u'38.7897', u'state': u'VA', u'sitter': u'Jose', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20032', u'street1': u'5529-F Patrick Circle SW', u'lon': u'-77.0171', u'sitterid': u'289', u'lat': u'38.8456', u'state': u'DC', u'sitter': u'BeckyH', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'8504 Sky View Drive', u'lon': u'-77.1147', u'sitterid': u'290', u'lat': u'38.7267', u'state': u'VA', u'sitter': u'Ann', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22306', u'street1': u'4115 Casey Ct', u'lon': u'-77.1044', u'sitterid': u'291', u'lat': u'38.7641', u'state': u'VA', u'sitter': u'Katy', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22303', u'street1': u'2825 Fairhaven Ave', u'lon': u'-77.0807', u'sitterid': u'292', u'lat': u'38.787', u'state': u'VA', u'sitter': u'Iris', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'5846 Governors Hill Dr', u'lon': u'-77.0863', u'sitterid': u'293', u'lat': u'38.7917', u'state': u'VA', u'sitter': u'Kate-T', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'2922 Commonwealth Ave', u'lon': u'-77.0599', u'sitterid': u'294', u'lat': u'38.8311', u'state': u'VA', u'sitter': u'John M.', u'active': u'1'}, 
        {u'city': u'Arlington', u'zip': u'22207', u'street1': u'1740 N Culpeper St', u'lon': u'-77.1228', u'sitterid': u'295', u'lat': u'38.8919', u'state': u'VA', u'sitter': u'Keghley', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'5 E Oxford, Unit 1', u'lon': u'-77.0609', u'sitterid': u'296', u'lat': u'38.8265', u'state': u'VA', u'sitter': u'Anna F.', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'4233 Raleigh Ave. #401', u'lon': u'-77.104', u'sitterid': u'297', u'lat': u'38.8171', u'state': u'VA', u'sitter': u'Dani', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'6520 10th St', u'lon': u'-77.0546', u'sitterid': u'298', u'lat': u'38.7758', u'state': u'VA', u'sitter': u'Kyle G.', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22307', u'street1': u'6929 Randolph Macon Dr', u'lon': u'-77.0678', u'sitterid': u'299', u'lat': u'38.767', u'state': u'VA', u'sitter': u'Meschelle', u'active': u'0'}, 
        {u'city': u'Falls Church', u'zip': u'22042', u'street1': u'2945 Rosemary Lane', u'lon': u'-77.1901', u'sitterid': u'300', u'lat': u'38.8705', u'state': u'VA', u'sitter': u'Brionna', u'active': u'0'}, 
        {u'city': u'Washington', u'zip': u'20019', u'street1': u'4124 Ames St NE', u'lon': u'-76.943', u'sitterid': u'301', u'lat': u'38.8911', u'state': u'DC', u'sitter': u'Bri', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'5501 Butterworth Ct', u'lon': u'-77.1283', u'sitterid': u'302', u'lat': u'38.7608', u'state': u'VA', u'sitter': u'Keri', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'212 E Custis Ave', u'lon': u'-77.0574', u'sitterid': u'303', u'lat': u'38.8256', u'state': u'VA', u'sitter': u'GLG Cleaning', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22306', u'street1': u'7830 Liberty Springs Cir', u'lon': u'-77.0815', u'sitterid': u'304', u'lat': u'38.7449', u'state': u'VA', u'sitter': u'Terri', u'active': u'1'}, 
        {u'city': u'Washington', u'zip': u'20011', u'street1': u'5403 9th St NW Apt 4', u'lon': u'-77.0257', u'sitterid': u'305', u'lat': u'38.9554', u'state': u'DC', u'sitter': u'Isamar', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22315', u'street1': u'7112 Rock Ridge Lane', u'lon': u'-77.1472', u'sitterid': u'306', u'lat': u'38.7641', u'state': u'VA', u'sitter': u'Cheryl S.', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'4202 Javins Drive', u'lon': u'-77.1054', u'sitterid': u'307', u'lat': u'38.789', u'state': u'VA', u'sitter': u'Steve K.', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22309', u'street1': u'8130 Keeler St', u'lon': u'-77.12', u'sitterid': u'308', u'lat': u'38.7376', u'state': u'VA', u'sitter': u'Sandra', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22304', u'street1': u'4801 Kenmore Ave Apt 1122', u'lon': u'-77.1124', u'sitterid': u'309', u'lat': u'38.8281', u'state': u'VA', u'sitter': u'Melaina', u'active': u'1'}, 
        {u'city': u'Springfield', u'zip': u'22150', u'street1': u'7089 Spring Garden Dr Apt 102', u'lon': u'-77.1874', u'sitterid': u'310', u'lat': u'38.7731', u'state': u'VA', u'sitter': u'Chat', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22310', u'street1': u'6611 Berkshire Dr', u'lon': u'-77.0962', u'sitterid': u'311', u'lat': u'38.7741', u'state': u'VA', u'sitter': u'Colin', u'active': u'1'}, 
        {u'city': u'Washington', u'zip': u'20002', u'street1': u'1952 3rd Street NE', u'lon': u'-77.0024', u'sitterid': u'312', u'lat': u'38.9171', u'state': u'DC', u'sitter': u'Michael', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1201 Braddock Pl Apt 309', u'lon': u'-77.051', u'sitterid': u'313', u'lat': u'38.8152', u'state': u'VA', u'sitter': u'Dee-jayh', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22301', u'street1': u'1813 Leslie Ave', u'lon': u'-77.0538', u'sitterid': u'314', u'lat': u'38.8232', u'state': u'VA', u'sitter': u'Aaron', u'active': u'1'}, 
        {u'city': u'Springfield', u'zip': u'22152', u'street1': u'6702 Kenmont Place', u'lon': u'-77.2109', u'sitterid': u'315', u'lat': u'38.773', u'state': u'VA', u'sitter': u'Alicia', u'active': u'0'}, 
        {u'city': u'Alexandria', u'zip': u'22305', u'street1': u'3728 Edison St', u'lon': u'-77.0607', u'sitterid': u'316', u'lat': u'38.8397', u'state': u'VA', u'sitter': u'Farrah', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22302', u'street1': u'2500 N. Van Dorn St #1013', u'lon': u'-77.0997', u'sitterid': u'317', u'lat': u'38.8327', u'state': u'VA', u'sitter': u'Andrea R.', u'active': u'1'}, 
        {u'city': u'Vienna', u'zip': u'22182', u'street1': u'2246 Richelieu Dr', u'lon': u'-77.2404', u'sitterid': u'318', u'lat': u'38.8986', u'state': u'VA', u'sitter': u'Lara G.', u'active': u'1'}, 
        {u'city': u'Alexandria', u'zip': u'22314', u'street1': u'1207 Trinity Dr', u'lon': u'-77.0855', u'sitterid': u'319', u'lat': u'38.8133', u'state': u'VA', u'sitter': u'Andy H.', u'active': u'1'}, 
        {u'city': u'Arlington', u'zip': u'22204', u'street1': u'629 S Adams St', u'lon': u'-77.0841', u'sitterid': u'320', u'lat': u'38.8677', u'state': u'VA', u'sitter': u'Jeri', u'active': u'0'}]}

        time_off = [{"timeoff":{"295":{"2018-04-19":["allday"]},"289":{"2018-04-19":["allday"]},"310":{"2018-04-19":["allday"]},"7":{"2018-04-19":["allday"]},"290":{"2018-04-19":["allday"]},"313":{"2018-04-19":["allday"]}}},
        {u'timeoff': {u'313': {u'2018-04-19': [u'allday']}, u'310': {u'2018-04-19': [u'allday']}, u'289': {u'2018-04-19': [u'allday']}, u'7': {u'2018-04-19': [u'allday']}, u'295': {u'2018-04-19': [u'allday']}, u'290': {u'2018-04-19': [u'allday']}}}]

        self.time_off = time_off
        self.visit_data = visit_data
        self.sitter_data = sitter_data
        
        return visit_data,sitter_data,time_off

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
            for timeoff in time_off_set:
                for sitter_id in time_off_set[timeoff]:
                    if 'allday' or u'allday' in time_off_set[timeoff][sitter_id]["2018-04-19"]:
                        sitters_time_off.append(sitter_id)

        ##################
        #parse sitter data
        ##################
        all_sitter_info = {}
        for sitter in sitter_data[u'sitters']:
            #ignore all inactive sitters
            if sitter[u'active'] != u'0':
                #ignore sitters with all day off
                if sitter[u'sitterid'] not in sitters_time_off:
                    all_sitter_info[sitter[u'sitterid']] = {'latlon':(sitter[u'lat'],sitter[u'lon']),'address': sitter[u'street1']+','+sitter[u'city']+','+sitter[u'state']+sitter[u'zip'],'name':sitter[u'sitter']}

                        
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

##all_sitter_info[sitter[u'sitterid']] = {'latlon':(sitter[u'lat'],sitter[u'lon']),'address': sitter[u'street1']+','+sitter[u'city']+','+sitter[u'state']+sitter[u'zip'],'name':sitter[u'sitter']}

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
    
