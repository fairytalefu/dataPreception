#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
class Mysql_Save():
	def getDataBaseVersion(self):
		# 打开数据库连接
		try:
			db = MySQLdb.connect("localhost","root","111","mysql" )
			# 使用cursor()方法获取操作游标 
			cursor = db.cursor()
			# 使用execute方法执行SQL语句
			cursor.execute("SELECT VERSION()")
			# 使用 fetchone() 方法获取一条数据库。
			data = cursor.fetchone()
			print "Database version : %s " % data
			# 关闭数据库连接
			db.close()
		except Exception,e:
			pass
	def mysql_Connect(self):
		try:
			# 打开数据库连接
			db = MySQLdb.connect("localhost","root","111","test" )
			# 使用cursor()方法获取操作游标 
			cursor = db.cursor()
			# 如果数据表已经存在使用 execute() 方法删除表。
			cursor.execute("DROP TABLE IF EXISTS GPSData")	
			# 创建数据表SQL语句
			sql = """CREATE TABLE GPSData (
			Date CHAR(100), 
			Lng  CHAR(20),
			Lat  CHAR(20),
			Temp CHAR(20),
			Irr  CHAR(20),
			Vnom CHAR(20),
			Inom CHAR(20),
			Power CHAR(20),
			Status CHAR(10),
			PRIMARY KEY (`date`)  
			  )"""
			cursor.execute(sql)
			#关闭数据库连接
			db.close()
		except Exception,e:
			print 'something unexpect error happen!'
			pass
	def insertData(self,GPS_Zigbee_Data):
		print '---------------'
		try:
			#打开数据库连接
			db = MySQLdb.connect("localhost","root","111","test" )
			print '---------**-----'
		except Exception,e:
			print 'can not connect to mysql!'
		#使用cursor()方法获取操作游标 
		cursor = db.cursor()
		print '---------&&&&--'
		#GPS_Zigbee_Data = ['2016-12-04 21:55:00','26.777','119.545','17.8','84','90.6','1.393','1']
		print 'ronghe de data',GPS_Zigbee_Data
	# SQL 插入语句  (GPS_Zigbee_Data[0], GPS_Zigbee_Data[1],GPS_Zigbee_Data[2], GPS_Zigbee_Data[3],GPS_Zigbee_Data[4],GPS_Zigbee_Data[5], GPS_Zigbee_Data[6],GPS_Zigbee_Data[7])('2016-12-04 21:20:00','26.777','119.545','17.8','84','90.6','1.393','1')
		sql = "INSERT INTO GPSData(Date,Lng, Lat, Temp, Irr, Vnom, Inom, Power,Status) VALUES ('%s', '%s', '%s','%s', '%s','%s', '%s', '%s','%s')" %(GPS_Zigbee_Data[0], GPS_Zigbee_Data[1],GPS_Zigbee_Data[2], GPS_Zigbee_Data[3],GPS_Zigbee_Data[4],GPS_Zigbee_Data[5],GPS_Zigbee_Data[6],GPS_Zigbee_Data[7],GPS_Zigbee_Data[8])
		try:	   
			#执行sql语句
		   	cursor.execute(sql)
		   #提交到数据库执行
		   	db.commit()
		except Exception,e:
			print 'something unexpect error happen!'
 			#发生错误时回滚
		   	db.rollback()
			print 'error'
			pass
		# 关闭数据库连接
		db.close()
def StoreData(GPS_Zigbee_Data):
		m_nMysql = Mysql_Save()
		#m_nMysql.mysql_Connect()
		print '*******------'
		m_nMysql.insertData(GPS_Zigbee_Data)
