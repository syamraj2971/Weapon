from flask import * 
from database import* 
import uuid

api=Blueprint('api',__name__)

@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q1="select * from login where user_name='%s' and `password`='%s'"%(u,p)
	print(q1)
	res=select(q1)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)

@api.route('/userregister')
def userregister():
	data={}
	f=request.args['fname']
	l=request.args['lname']
	
	pl=request.args['place']
	
	ph=request.args['phone']
	e=request.args['email']
	
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(NULL,'%s','%s','user')"%(u,p)
		lid=insert(q)
		r="insert into user values(NULL,'%s','%s','%s','%s','%s','%s')"%(lid,f,l,pl,ph,e)
		insert(r)
		print(r)
		data['status']="success"
	return str(data)



@api.route('/Viewrequest')
def Viewrequest():
	data={}

	q="SELECT * FROM request INNER JOIN `branch` ON `request`.`user_id`=`branch`.`branch_id` ORDER BY request_id DESC "
	print(q)

	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="Viewrequest"
	return str(data)


@api.route('/UserViewrequest')
def UserViewrequest():
	data={}
	
	
	q="SELECT * FROM request INNER JOIN `branch` ON `request`.`user_id`=`branch`.`branch_id` "
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="UserViewrequest"
	return str(data)

# @api.route('/UserViewrequestupdate')
# def UserViewrequestupdate():
# 	data={}
# 	rid=request.args['rid']
# 	q="update request set status='Forward To Police' where request_id='%s'"%(rid)
# 	update(q)
# 	data['status']='success'
# 	data['method']="UserViewrequestupdate"
# 	return str(data)


@api.route('/public_view_videos')
def public_view_videos():
	data={}

	rid=request.args['rid']

	q="select * from request  where request_id='%s'"%(rid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="public_view_videos"
	return str(data)


@api.route('/Viewemergency')
def Viewemergency():
	data={}

	q="SELECT * FROM emergency  INNER JOIN `branch` ON `emergency`.`user_id`=`branch`.`branch_id`"
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="Viewemergency"
	return str(data)

# @api.route('/updatepasslocation')
# def updatepasslocation():
# 	data={}
# 	logid=request.args['logid']
# 	lati=request.args['latti']
# 	longi=request.args['longi']
# 	q="select * from location where user_id=(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s')" %(logid)
# 	res1=select(q)
# 	if res1:
# 		q="update location set latitude='%s' , longitude='%s' where user_id=(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s')" %(lati,longi,logid) 
# 		update(q)
# 		print(q)
# 	else:

# 		q="insert into location values(null,(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s'),'%s','%s')" %(logid,lati,longi)
# 		print(q)
# 		insert(q)

# 	q="select * from emergency  inner join `branch` ON `emergency`.`user_id`=`branch`.`branch_id` INNER JOIN location ON `branch`.`branch_id`=`location`.`user_id` where status='pending' and emergency.user_id=(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s')" %(logid)
# 	res=select(q)
# 	q="update emergency set status='sendsms' where user_id=(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s')" %(logid)
	
# 	update(q)
# 	if res:
# 		data['name']=res[0]['branch_name']
# 		data['lati']=res[0]['latitude']
# 		data['longi']=res[0]['longitude']
# 		data['status']='success'
# 	else:
# 		data['status']='failed'
# 	data['method']="updatepasslocation"
# 	return str(data)


@api.route('/user_upload_file',methods=['get','post'])
def user_upload_file():
	data={}
	title=request.form['reason']
	img=request.files['video']

	path="static/video"+str(uuid.uuid4())+img.filename
	img.save(path)
	logid=request.form['lid']
	
	q="INSERT INTO `request` VALUES(null,(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s'),'%s','%s','0','pending','Video')"%(logid,title,path)
	print(q)
	id=insert(q)
	data['status'] ='success'

	data['method'] ='user_upload_file'
	return  str(data)


@api.route('/viewemergencyss')
def viewemergencyss():
	data={}
	
	q="SELECT * FROM emergency  INNER JOIN `branch` ON `emergency`.`user_id`=`branch`.`branch_id`"
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="viewemergencyss"
	return str(data)


@api.route('/Addemergency',methods=['get','post'])
def Addemergency():
	data={}

	em=request.args['emergency']
	latitude=request.args['latitude']
	longitude=request.args['longitude']
	log_id=request.args['log_id']
	q="insert into emergency values(null,(select branch_id from branch where login_id='%s'),'%s','%s','%s','pending')"%(log_id,em,latitude,longitude)
	insert(q)
	data['status']='success'
	data['method']="Addemergency"
	return str(data)



@api.route('/upload_audio',methods=['get','post'])
def upload_audio():
	data={}
	title=request.form['title']
	img=request.files['audio']

	path="static/video"+str(uuid.uuid4())+img.filename
	img.save(path)
	logid=request.form['logid']
	
	q="INSERT INTO `request` VALUES(null,(SELECT `branch_id` FROM `branch` WHERE `login_id`='%s'),'%s','%s','0','pending','Audio')"%(logid,title,path)
	print(q)
	id=insert(q)
	data['status'] ='success'

	data['method'] ='upload_audio'
	return  str(data)


# @api.route('/view_complaint')
# def view_complaint():
# 	data={}
# 	login_id=request.args['login_id']
# 	q="select * from complaints  where sender_id=(select branch_id from branch where login_id='%s')"%(login_id)
# 	res=select(q)
	
# 	data['data']=res
# 	data['status']="success"
# 	data['method']='view_complaint'
# 	return str(data)

# @api.route('/send_complaint')
# def send_complaint():
# 	data={}
# 	login_id=request.args['login_id']
# 	complaint=request.args['complaint']
# 	q="insert into complaints values(null,(select branch_id from branch where login_id='%s'),'%s','pending',curdate())"%(login_id,complaint)
# 	insert(q)
# 	data['status']="success"
# 	data['method']="send_complaint"
# 	return str(data)


# @api.route('/policeview_complaint')
# def policeview_complaint():
# 	data={}

# 	q="select * from complaints INNER JOIN `branch` ON `complaint`.`user_id`=`branch`.`branch_id`"
# 	res=select(q)
	
# 	data['data']=res
# 	data['status']="success"
# 	data['method']='policeview_complaint'
# 	return str(data)


@api.route('/imgses')
def imgses():
	data={}
	rid=request.args['rid']

	q="select * from request  where request_id='%s'"%(rid)
	res=select(q)
	
	data['data']=res
	data['status']="success"
	data['method']='imgses'
	return str(data)

# @api.route('/send_reply')
# def send_reply():
# 	data={}
# 	rep=request.args['rep']
# 	cid=request.args['cid']

# 	q="update complaints set replay='%s' where compliant_id='%s'"%(rep,cid)
# 	update(q)
# 	data['status']="success"
# 	data['method']='send_reply'
# 	return str(data)






