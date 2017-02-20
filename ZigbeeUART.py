import time
import serial 
import re #split special Symbol from string 
class ZigBeeData():
	def readSerial(self):
		sStr = 'PV'
		flag = 1
		try:
			ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_ONE,bytesize=serial.SEVENBITS)
		except Exception,e:
			print('open serial failed.')
			exit(1)
		print("connected to: " + ser.portstr)
		while flag:
	    		line = ser.readline()
			try:		
				if line.index(sStr):
					flag = 0
					return line
			except Exception,e:
				pass
		ser.close()	
	def splitPv_Message(self,m_nPvData):
		PvMessage = re.split(',',m_nPvData)
		count = 0#heat beat package
		if PvMessage[1] == 'A' :
			return PvMessage
		else:
			while count <= 20:
				readSerial()
				count = count + 1
		print('can not get some message from ZigBee!Bye!')
		exit(1)
	def parsePvMessage(self,message):
 		ZigMessage = []
		#---------parse Temp------------------
		Temp = message[2]
		ZigMessage.append(Temp)
		#---------parse Irr------------------
		Irr  = message[3]
		ZigMessage.append(Irr)
		#---------parse Vmp------------------
		Vmp  = message[4]
		ZigMessage.append(Vmp)
		#---------parse Imp------------------
		Imp  = message[5]
		Imp1 = re.split('\r',Imp)
		ZigMessage.append(Imp1[0])
		#print 'Temp:',Temp,'\n', 'Irr:',Irr,'\n', 'Vmp:',Vmp,'\n','Imp',Imp,'\n'
		return ZigMessage
#rmc ='$PV,A,17.8,84,90.6,1.393'
def getZigBeeData():
	pvdata = ZigBeeData()
	rmc = pvdata.readSerial()
	splitMessage = pvdata.splitPv_Message(rmc)
	ZigMessage = pvdata.parsePvMessage(splitMessage)
#	print ZigMessage
	return ZigMessage
#getZigBeeData()
