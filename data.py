import sys
import datetime
from ZigbeeUART import *
from UART import * 
from SVMTest import *
from saveToMysql import *
from uploadUbidot import *
class StoreDataBase():
	def Ronghe_Data(self,zigdata,uartData):
		zig_length = len (zigdata)
		print zigdata
		uart_length = len(uartData)
		print uartData
		if zig_length and uart_length:
			label = svm_pvfault_detect(zigdata)
			print label
			zigdata.append(str(label[0]))
			print zigdata
			GPS_Zigbee_Data = uartData + zigdata
			return GPS_Zigbee_Data
		else:
			print 'Can not get both zigdata and uartdata!'
			exit(-1)
	def creatTable_mysql(self):
		m_nMysql = Mysql_Save()
		m_nMysql.mysql_Connect()
	def Save_Data(self,GPS_Zigbee_Data):
		m_nMysql = Mysql_Save()
		m_nMysql.insertData(GPS_Zigbee_Data)

def Power(t):
	zigdata = getZigBeeData()
	Power = float(zigdata[0]) * float(zigdata[1])*t
	zigdata.append(Power)
	return zigdata
def timeInterval(t1,t2)
	
if __name__ == "__main__":
	#zigdata = Power()
	zigdata = getZigBeeData()
	uartData = getGPSData()
	S_Data = StoreDataBase()
	n_flag = 1
	GPS_Zigbee_Data = S_Data.Ronghe_Data(zigdata,uartData)
	print 'ronghe de data',GPS_Zigbee_Data
	if n_flag == 1:
		S_Data.creatTable_mysql()
	#GPS_Zigbee_Data = ['2016-12-04 22:55:00','26.777','119.545','17.8','84','90.6','1.353','1']
	#print 'Create Table Successfully!'
	StoreData(GPS_Zigbee_Data)
	postData_Ubidots(GPS_Zigbee_Data)
	#S_Data.Save_Data(GPS_Zigbee_Data1)
	#print 'Insert into Table Successfully!'
