from flask import *
from database import *

maintenance=Blueprint('maintenance',__name__)

@maintenance.route('/main_home')
def main_home():
    return render_template('maintenance_home.html')



@maintenance.route('/maintenanceviewcomplaints', methods=['POST', 'GET'])
def maintenanceviewcomplaints():
    data = {}
    s = "SELECT * FROM complaint"
    data['complaint'] = select(s)
    return render_template('maintenanceviewcomplaints.html',data=data)

@maintenance.route('/maintenance_sendreply', methods=['POST', 'GET'])
def maintenance_sendreply():
    data = {}
    cid=request.args['cid']

    if 'submit' in request.form:
        reply=request.form['complaint_details']
        q1="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q1)
        return redirect(url_for("maintenance.maintenanceviewcomplaints"))
    return render_template('maintenance_sendreply.html',data=data)





#####################################view branch complaints###########################

@maintenance.route('/maintenance_viewcomplaints', methods=['POST', 'GET'])
def maintenanceviewcomplaint():
    data = {}
    s = "SELECT * FROM sendcomplaint"
    data['sendcomplaint'] = select(s)
    return render_template('maintenance_viewcomplaints.html',data=data)

@maintenance.route('/maintenancesendreply', methods=['POST', 'GET'])
def maintenancesendreplys():
    data = {}
    cid=request.args['cid']

    if 'submit' in request.form:
        reply=request.form['complaint']
        q1="update sendcomplaint set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q1)
        return redirect(url_for("maintenance.maintenanceviewcomplaint"))
    return render_template('maintenancesendreply.html',data=data)
