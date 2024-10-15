from flask import *
from database import *
from detection import *

branch=Blueprint('branch',__name__)
@branch.route('/branchhome')
def branchome():
    return render_template('branchhome.html')

@branch.route('/detect', methods=['POST', 'GET'])
def detect():
    branch_id=session['bid']
    if "submit" in request.form:
        detection(branch_id)
    return render_template('detect_weapon.html')
        
        


@branch.route('/managestaff', methods=['POST', 'GET'])
def managestaff():
    data = {}
    s = "SELECT * FROM staff"
    data['staff'] = select(s)

    qry="select * from designation" 
    data['designation']=select(qry)
    if request.method == 'POST' and 'submit' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        phone_number = request.form['phone_number']
        email = request.form['email']
        user_name=request.form['user_name']
        password=request.form['password']
        designation_name=request.form['designation_name']
        print(first_name, last_name, dob, phone_number, email,designation_name)
        q="INSERT INTO login VALUES(NULL,'%s','%s','staff')" %(user_name,password)
        res=insert(q)
        qry = "INSERT INTO staff VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')" % (res,designation_name,session['bid'],first_name,last_name,dob,phone_number,email)
        insert(qry)
        return '''<script>alert("staff Added");window.location="managestaff"</script>'''
    if 'action' in request.args:
            action = request.args['action']
            did = request.args['did']

            if action == 'delete':
                q = "DELETE FROM staff WHERE staff_id='%s'" %(did)
                delete(q)
                return '''<script>alert("staff Removed");window.location="managestaff"</script>'''
            
            elif action == 'update':
                s = "SELECT * FROM staff where staff_id='%s'"%(did)
                data['upd'] = select(s)

            
            if 'update' in request.form:
                first_name = request.form['first_name']
                last_name=request.form['last_name']
                dob=request.form['dob']
                phone_number = request.form['phone_number']
                email = request.form['email']

                print(first_name,last_name,dob, phone_number, email)
                qry = "UPDATE staff SET first_name='%s', last_name='%s', dob='%s', phone_number='%s', email='%s' WHERE staff_id='%s'" % (first_name, last_name, dob, phone_number, email, did)
                update(qry)
                return '''<script>alert("Staff Updated");window.location="managestaff"</script>'''
    return render_template('managestaff.html', data=data)


@branch.route('/viewattendance', methods=['POST', 'GET'])
def viewattendance():
    data = {}
    s = "SELECT * FROM attendance"
    data['attendance'] = select(s)
    return render_template('viewattendance.html',data=data)

@branch.route('/viewnotification', methods=['POST', 'GET'])
def viewnotification():
    data = {}
    s = "SELECT * FROM notification"
    data['notification'] = select(s)
    return render_template('viewnotification.html',data=data)


@branch.route('/branchsendandviewcomplaints', methods=['POST', 'GET'])
def branchsendandviewcomplaints():
    data = {}
    s = "SELECT * FROM complaints"
    res=select(s)
    data['complaints'] = select(s)
    if 'submit' in request.form:
        complaint_details= request.form['complaint_details']
        qry = "INSERT INTO complaints VALUES(NULL,'%s','%s','pending',curdate())" %( session['bid'],complaint_details)
        res1=insert(qry)
        return redirect(url_for('branch.branchsendandviewcomplaints'))
    return render_template('branchsendandviewcomplaints.html',data=data)

@branch.route('staffsendandviewcomplaints', methods=['POST', 'GET'])
def staffsendandviewcomplaints():
    data = {}
    s = "SELECT * FROM staffsendcomplaint"
    data['staffsendcomplaint'] = select(s)
    return render_template('staffsendandviewcomplaints.html',data=data)

@branch.route('staffsendandviewcomplaints', methods=['POST', 'GET'])
def branchsendreply():
    data = {}
    cid=request.args['cid']

    if 'update' in request.form:
        reply=request.form['reply']
        q1="update complaints set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q1)
        return redirect(url_for("branch.staffsendandviewcomplaints"))
    return render_template('staffsendandviewcomplaints.html',data=data)



@branch.route('/maintenance_sendcomplaint_branch', methods=['POST', 'GET'])
def maintenance_sendcomplaint_branch ():
    data = {}
    s = "SELECT * FROM sendcomplaint where sender_id='%s'"%(session['bid'])
    res=select(s)
    data['sendcomplaint'] = res
    if 'submit' in request.form:
        complaint= request.form['complaint']
        qry = "INSERT INTO sendcomplaint VALUES(NULL,'%s','%s','pending',curdate())" % ( session['bid'],complaint)
        res1=insert(qry)
        return redirect(url_for('branch.maintenance_sendcomplaint_branch'))
    return render_template('maintenance_sendcomplaint_branch.html',data=data)

@branch.route('branchviewcomplaints', methods=['POST', 'GET'])
def branchviewcomplaints():
    data = {}
    s = "SELECT * FROM staffsendcomplaint"
    data['staffsendcomplaint'] = select(s)
    return render_template('branchviewcomplaints.html',data=data)

@branch.route('branchsendreplay', methods=['POST', 'GET'])
def branchsendreplay():
    data = {}
    cid=request.args['cid']

    if 'submit' in request.form:
        reply=request.form['complaint_details']
        q1="update staffsendcomplaint set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q1)
        return redirect(url_for("branch.branchviewcomplaints"))
    return render_template('branchsendreplay.html',data=data)




             