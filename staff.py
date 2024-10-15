from flask import *
from database import *

staff=Blueprint('staff',__name__)

staff=Blueprint('staff',__name__)
@staff.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')

@staff.route('/adminhome')
def branch():
   return render_template('mangestaff.html')


@staff.route('/staffviewprofile', methods=['POST', 'GET'])
def staffviewprofile():
    data = {}
    qury2= "select * from staff where staff_id='%s'"%(session['sid'])
    print(qury2)
    res2=select(qury2)
    data['staff'] =res2
    return render_template('staffviewprofile.html',data=data)

@staff.route('/staffeditprofile', methods=['POST', 'GET'])
def staffeditprofile():
    data = {}
    s = "select * from staff where staff_id='%s'"%(session['sid'])
    data['staff'] = select(s)
    qry = "SELECT * FROM designation"
    data['designation'] = select(qry)

    if 'action' in request.args:
        action = request.args['action']
        did = request.args['did']

        if action == 'update':
            s = "SELECT * FROM staff WHERE staff_id='%s'" % (did)
            print(s)
            data['upd'] = select(s)

    if 'update' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        phone_number = request.form['phone_number']
        email = request.form['email']

        print(first_name, last_name, dob, phone_number, email)

        qry = "UPDATE staff SET first_name='%s', last_name='%s', dob='%s', phone_number='%s', email='%s' WHERE staff_id='%s'" % (first_name, last_name, dob, phone_number, email, did)
        update(qry)
        return '''<script>alert("Staff Updated");window.location="staffviewprofile"</script>'''

    return render_template('staffeditprofile.html', data=data)


@staff.route('/staffsendandviewcomplaints', methods=['POST', 'GET'])
def staffsendandviewcomplaints():
    data = {}
    s = "SELECT * FROM staffsendcomplaint"
    res=select(s)
    data['staffsendcomplaint'] = select(s)
    if 'submit' in request.form:
        complaint_details= request.form['complaint_details']
        qry = "INSERT INTO staffsendcomplaint VALUES(NULL,'%s','%s','pending',curdate())" % ( session['sid'],complaint_details)
        res1=insert(qry)
        return redirect(url_for('staff.staffsendandviewcomplaints'))
    return render_template('staffsendandviewcomplaints.html',data=data)
             

@staff.route('/staffmarkattendance',methods=['post','get'])
def staffmarkattendance():
    data={}
    s="select * from attendance"
    data['attendance']=select(s)
    
      
    if'submit'in request.form:
          date=request.form['date']
          status=request.form['status']
          qry="insert into attendance values(NULL,'%s','%s','%s')"%(session['sid'],date,status)
          insert(qry)
    return render_template('staffmarkattendance.html',data=data)

@staff.route('/staffviewnotification', methods=['POST', 'GET'])
def staffviewnotification():
    data = {}
    s = "SELECT * FROM notification"
    data['notification'] = select(s)
    return render_template('staffviewnotification.html',data=data)

@staff.route('/maintenance_sendcomplaint_staff', methods=['POST', 'GET'])
def maintenance_sendcomplaint_staff ():
    data = {}
    s = "SELECT * FROM complaint where sender_id='%s'"%(session['sid'])
    res=select(s)
    data['complaint'] = select(s)
    if 'submit' in request.form:
        complaint= request.form['complaint']
        qry = "INSERT INTO complaint VALUES(NULL,'%s','%s','pending',curdate())" % ( session['sid'],complaint)
        res1=insert(qry)
        return redirect(url_for('staff.maintenance_sendcomplaint_staff'))
    return render_template('manitenance_sendcomplaint_staff.html',data=data)
             
  
          