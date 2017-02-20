import time
import serial 
import re #split special Symbol from string 
class GetGpsData():
	def ReadSerial(self):
		sStr = 'GPRMC'
		flag = 1
		try:
			ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_ONE,bytesize=serial.SEVENBITS)
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
	def splitGps_Message(self,m_nGps):
		GMessage = re.split(',',m_nGps)
		count = 0#heat beat package
		if GMessage[2] == 'A' :
			return GMessage
		else:
			while count < 20:
				self.ReadSerial()
				count = count + 1
				print 'try to get gps data %d time(s)!'%(count)
			print 'faild to get gps data!'
		exit(-1)
	def parseMessage(self,message):
		uartData = []
		#---------parse Date------------------
		Time = message[1]
		h = str(int(Time[0]+Time[1])+8)
		m = Time[2]+Time[3]
		s = Time[4]+Time[5]
		time = h+':'+m+':'+s
		Day =  message[9]
		Year = '20'+Day[4]+Day[5]
		month = Day[2]+Day[3]
		day = Day[0]+Day[1]
		day_time = Year+'-'+month+'-'+day+' '
		date = day_time + time
		uartData.append(date)
		#-------parse latitute longtitute----------
		lat = message[3]
		lng = message[5]
		Lat = lat[0]+lat[1]+lat[4]+lat[2]+lat[3]+lat[5]+lat[6]+lat[7]+lat[8]+lat[9]
		Lng = lng[0]+lng[1]+lng[2]+lng[5]+lng[3]+lng[4]+lng[6]+lng[7]+lng[8]+lng[9]
		uartData.append(Lat)
		uartData.append(Lng)
		#print 'Prime:','Time:',date,'\n', 'Lat:',Lat,'\n', 'Lng:',Lng,'\n'		
		return uartData
#rmc ='$GPRMC,083921.00,A,2604.03336,N,11911.74094,E,1.043,,301116,,,A*71'\
def getGPSData():
	gpsdata = GetGpsData()
	rmc = gpsdata.ReadSerial()
	splitmessage = gpsdata.splitGps_Message(rmc)
	uartData = gpsdata.parseMessage(splitmessage)
	return uartData
#x= getGPSData()
#x = readSerial()
#print 'GRMC_EPOCH',x
#$GPRMC,083921.00,A,2604.03336,N,11911.74094,E,1.043,,301116,,,A*71
