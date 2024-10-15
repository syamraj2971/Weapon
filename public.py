from flask import *
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route("/login",methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['user_name']
		passs=request.form['password']
		q="select * from login where user_name='%s' and password='%s'"%(uname,passs)
		res=select(q)
		print(res)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))
			
			
			elif res[0]['user_type']=='branch':
				qry1="select * from branch where login_id='%s'"%(session['lid'])
				res1=select(qry1)
				if res1:
						session['bid']=res1[0]['branch_id']
						return redirect(url_for('branch.branchome'))

			elif res[0]['user_type']=="maintenance":
				q="select * from maintenance where login_id='%s'"%(session['lid'])
				re=select(q)
				if re:
					session['m_id']=re[0]['maintenance_id']	
					return redirect(url_for('maintenance.main_home'))
                    
			elif res[0]['user_type']=='staff':
				qry2="select * from staff where login_id='%s'"%(session['lid'])
				res2=select(qry2)
				if res2:
					session['sid']=res2[0]['staff_id']
					return redirect(url_for('staff.staffhome'))
			else:
				flash("Invalid User")

	return render_template('login.html')