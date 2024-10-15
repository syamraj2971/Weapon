from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')
@admin.route('/managedesignation',methods=['post','get'])
def managedesignation():
      data={}
      s="select * from designation"
      data['desig']=select(s)
      
      if'submit'in request.form:
          designation_name=request.form['designation_name']

          print(designation_name)
     
          qry="insert into designation values(NULL,'%s')"%(designation_name)
          insert(qry)
          return '''<script>alert("Designation Added");window.location="managedesignation"</script>'''
      if 'action' in request.args:
           action=request.args['action']
           desigid=request.args['did']

      else:
           action=None

      if action=='delete':
           q="delete from designation where designation_id='%s'"%(desigid)
           delete(q)
           return '''<script>alert("Designation Removed");window.location="managedesignation"</script>'''
      if action=='update':
           s="select * from designation where designation_id='%s'"%(desigid)
           data['upd']=select(s)
      if'update'in request.form:
          designation_name=request.form['designation_name']

          print(designation_name)
     
          qry="update designation set designation_name='%s' where designation_id='%s'"%(designation_name,desigid)
          update(qry)
          return '''<script>alert("Designation Updated");window.location="managedesignation"</script>'''
      return render_template('managedesignation.html',data=data)



@admin.route('/managebranch', methods=['POST', 'GET'])
def managebranch():
    data = {}
    s = "SELECT * FROM branch"
    data['branch'] = select(s)

    if 'submit' in request.form:
        branch_name = request.form['branch_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        place = request.form['place']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        user_name=request.form['user_name']
        password=request.form['password']
        print(branch_name, phone_number, email, place)
        q="INSERT INTO login VALUES(NULL,'%s','%s','branch')" %(user_name,password)
        res=insert(q)
        qry = "INSERT INTO branch VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s')" % (res,branch_name, phone_number, email, place,latitude,longitude)
        insert(qry)
        return '''<script>alert("Branch Added");window.location="managebranch"</script>'''

    if 'action' in request.args:
            action = request.args['action']
            did = request.args['did']

            if action == 'delete':
                q = "delete from branch where branch_id='%s'"%(did)
                delete(q)
                return '''<script>alert("Branch Removed");window.location="managebranch"</script>'''

            elif action == 'update':
                s = "SELECT * FROM branch where branch_id='%s'"%(did)
                data['upd'] = select(s)

            if 'update' in request.form:
                branch_name = request.form['branch_name']
                phone_number = request.form['phone_number']
                email = request.form['email']
                place = request.form['place']
                # latitude = request.form['latitude']
                # longitude = request.form['longitude']
                # print(branch_name, phone_number, email, place,latitude, longitude)

                qry = "UPDATE branch SET branch_name='%s', phone_number='%s', email='%s', place='%s' WHERE branch_id='%s'" % (branch_name, phone_number, email, place, did)
                update(qry)
                return '''<script>alert("Branch Updated");window.location="managebranch"</script>'''

    return render_template('managebranch.html', data=data)


@admin.route('/viewstaff', methods=['POST', 'GET'])
def viewstaff():
    data = {}
    s = "SELECT * FROM staff inner join branch using(branch_id)"
    data['staff'] = select(s)
    return render_template('viewstaff.html',data=data)

@admin.route('/adminviewcomplaints', methods=['POST', 'GET'])
def adminviewcomplaints():
    data = {}
    s = "SELECT * FROM complaints"
    data['complaints'] = select(s)
    return render_template('adminviewcomplaints.html',data=data)

@admin.route('/adminsendreply', methods=['POST', 'GET'])
def adminsendreply():
    data = {}
    cid=request.args['cid']

    if 'submit' in request.form:
        reply=request.form['complaint_details']
        q1="update complaints set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q1)
        return redirect(url_for("admin.adminviewcomplaints"))
    return render_template('adminsendreply.html',data=data)


@admin.route('/adminsendnotification', methods=['POST', 'GET'])
def adminsednotification():
     data = {}
     s = "SELECT * FROM notification"
     res=select(s)
     data['notification'] = select(s)
     if 'submit' in request.form:
        title= request.form['title']
        notification_details=request.form['notification_details']
        qry = "INSERT INTO notification VALUES(NULL,'%s','%s',curdate())" %( title,notification_details)
        res1=insert(qry)
        return '''<script>alert("notification added");window.location="adminsendnotification"</script>'''

     return render_template('adminsendnotification.html',data=data)
      
 


@admin.route('/admin_viewrequest',methods=['get','post'])
def admin_viewrequest():
	data={}
 
	q="select * from request inner join user using (user_id)"
	res=select(q)
	data['requestss']=res

	return render_template('admin_viewrequest.html',data=data)


@admin.route('/admin_viewlocation',methods=['get','post'])
def admin_viewlocation():
	data={}

	q="select * from location inner join user using (user_id)"
	res=select(q)
	data['location']=res

	return render_template('admin_viewlocation.html',data=data)


@admin.route('/admin_fileupload',methods=['get','post'])
def admin_fileupload():

	data={}

	q="select * from images"
	res=select(q)
	data['img']=res
	
	if "submit" in request.form:
		img=request.files['images']
		
		path="static/"+str(uuid.uuid4())+img.filename
		img.save(path)
		
		
		q="INSERT INTO `images` VALUES(null,'%s')"%(path)
		print(q)
		insert(q)
		return redirect(url_for('admin.admin_fileupload'))


	return render_template('admin_fileupload.html',data=data)


@admin.route('/maintenancehome')
def maintenancehome():
	return render_template('maintenancehome.html')

@admin.route('/managemaintenance', methods=['POST', 'GET'])
def managemaintenance():
    data = {}
    s = "SELECT * FROM maintenance"
    data['maintenance'] = select(s)

    if request.method == 'POST' and 'submit' in request.form:
        company_name = request.form['company_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        user_name=request.form['user_name']
        password=request.form['password']
        print(company_name,phone_number, email)
        q="INSERT INTO login VALUES(NULL,'%s','%s','maintenance')" %(user_name,password)
        res=insert(q)
        qry = "INSERT INTO maintenance VALUES(NULL,'%s','%s','%s','%s')" % (company_name,phone_number,email,res)
        insert(qry)
        return '''<script>alert("maintenance Added");window.location="managemaintenance"</script>'''
    if 'action' in request.args:
            action = request.args['action']
            did = request.args['did']

            if action == 'delete':
                q = "DELETE FROM maintenance WHERE maintenance_id='%s'" %(did)
                delete(q)
                return '''<script>alert("maintenance Removed");window.location="managemaintenance"</script>'''
            
            elif action == 'update':
                s = "SELECT * FROM maintenance where maintenance_id='%s'"%(did)
                data['upd'] = select(s)

            
            if 'update' in request.form:
                company_name= request.form['company_name']
                phone_number = request.form['phone_number']
                email = request.form['email']

                print(company_name, phone_number, email)
                qry = "UPDATE maintenance SET company_name='%s', phone_number='%s', email='%s' WHERE maintenance_id='%s'" % (company_name, phone_number, email, did)
                update(qry)
                return '''<script>alert("maintenance Updated");window.location="managemaintenance"</script>'''

    return render_template('managemaintenance.html', data=data)




@admin.route('/admin_managepolice', methods=['POST', 'GET'])
def admin_managepolice():
    data = {}
    s = "SELECT * FROM police"
    data['police'] = select(s) 

    if request.method == 'POST' and 'submit' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        place = request.form['place']
        user_name = request.form['user_name']
        password = request.form['password']
        print(first_name, last_name, phone_number, email, place)

        qry1 = "INSERT INTO login VALUES (null,'%s', '%s', 'police')" % (user_name, password)
        res=insert(qry1) 

        qry = "INSERT INTO police VALUES (NULL,'%s','%s','%s','%s','%s','%s')" % (res, first_name, last_name, phone_number, email, place)
        insert(qry)  

        return '''<script>alert("Police added");window.location="admin_managepolice"</script>'''

    if 'action' in request.args:
            action = request.args['action']
            did = request.args['pid']

            if action == 'delete':
                q = "DELETE FROM police WHERE police_id='%s'" %(did)
                delete(q)
                return '''<script>alert("police Removed");window.location="admin_managepolice"</script>'''
            
            elif action == 'update':
                s = "SELECT * FROM police where police_id='%s'"%(did)
                data['upd'] = select(s)

            
            if 'update' in request.form:
                first_name= request.form['first_name']
                last_name=request.form['last_name']
                phone_number = request.form['phone_number']
                email = request.form['email']
                place=request.form['place']

                print(first_name,last_name, phone_number,email,place)
                qry = "UPDATE police SET first_name='%s',last_name='%s', phone_number='%s', email='%s',place='%s' WHERE police_id='%s'" % (first_name,last_name, phone_number,email,place, did)
                update(qry)
                return '''<script>alert("police Updated");window.location="admin_managepolice"</script>'''

    return render_template('admin_managepolice.html', data=data)
