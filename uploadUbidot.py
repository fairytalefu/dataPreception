from ubidots import ApiClient
import math
import time
class PostDataToUbidots():
	def postTemp(self,Temp_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			# Get a Ubidots Variable
			Temp_variable = api.get_variable('581b254f76254250326a2d51')
			time.sleep(1)
			# Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put an artificial signal here:
			Temp_response = Temp_variable.save_value({"value": Temp_Data})
			print (Temp_response)		
			time.sleep(3)
    
	def postIrr(self,Irr_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			Irr_variable = api.get_variable('58466add7625420de33bedcd')
			time.sleep(1)
			Irr_response = Irr_variable.save_value({"value": Irr_Data})
			print Irr_response		
			time.sleep(3)
    	
	def postVmp(self,Vmp_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			Vmp_variable = api.get_variable('581b2f887625420434ecd29c')
			time.sleep(1)
			Vmp_response = Vmp_variable.save_value({"value": Vmp_Data})
			print Vmp_response		
			time.sleep(3)
    	
	def postImp(self,Imp_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			Imp_variable = api.get_variable('581b2f957625420481362b11')
			time.sleep(1)
			Imp_response = Imp_variable.save_value({"value": Imp_Data})
			print Imp_response		
			time.sleep(3)
    	
	def postStatus(self,Status_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			Status_variable = api.get_variable('58466a2e7625420ada1399c4')
			time.sleep(1)
			Status_response = Status_variable.save_value({"value": Status_Data})
			print Status_response		
			time.sleep(3)
	def postPower(self,Power_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			Power_variable = api.get_variable('58466a2e7625420ada1399c4')
			time.sleep(1)
			Power_response = Power_variable.save_value({"value": Power_Data})
			print Power_response		
			time.sleep(3)	
	def postGPS(self,GPS_Data):
			api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')
			GPS_variable = api.get_variable('582288d27625427f1c7f729b')
			time.sleep(1)
			GPS_response = GPS_variable.save_value({"value":21,
			"context":
			{
			"lat": GPS_Data[0],
			"lng": GPS_Data[1]}
			})
			print GPS_response
			time.sleep(3)
def postData_Ubidots(Data):	
	# Create an ApiClient object
	#['2016-12-07 10:09:55', '26.0403297', '119.117366', '17.8', '84', '90.6', '1.393', '2.0']
	GPS_Data = [] 
	GPS_Data.append(Data[1])
	GPS_Data.append(Data[2])
	pdtu = PostDataToUbidots()
	pdtu.postTemp(Data[3])
	pdtu.postIrr(Data[4])
	pdtu.postVmp(Data[5])
	pdtu.postImp(Data[6])
	pdtu.postPower(Data[6])#power
	pdtu.postStatus(Data[7])
	pdtu.postGPS(GPS_Data)
#Data = ['2016-12-07 10:09:55', '26.0403297', '119.117366', '17.8', '84', '90.6', '1.393', '2.0']
#postData_Ubidots(Data)
