from application import app, pdb, ds
from flask import redirect
from flask import url_for
from flask import flash
from flask import render_template, make_response, jsonify
import json
from flask.ext.login import login_user
from flask import request
from application.forms.login import LoginForm
#from application.models.user import User
#from application.models.nurse import Nurse
from application.models.user import User, Patient
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user


@app.route('/')
def site_index():
    if current_user.is_authenticated():
        # redirect, load a different template...
        print "PATIENTS!"
        print current_user.patients

        return redirect("dashboard")
        #return render_template('site/dashboard.html')
    return render_template('site/index.html')
    #return redirect('login')

@app.route('/dashboard')
def staff_dashboard():

    print "CURRENTLY IN THE DASHBOARD BRUH."
    print current_user.patients
    print current_user.patients.count()

    return render_template('site/dashboard.html')

    #return render_template('site/dashboard.html')


@app.route('/dashboard/patients/<int:patient_id>/', methods=['GET'])
def fetch_patient(patient_id):
    """ Fetch the requested patient from the database! """
    try:
        selected_patient = Patient.query.filter_by(id=patient_id).first()
        #print selected_patient.diagnoses

        patient_diag = selected_patient.diagnoses

        print patient_diag

        table = ds['patient']
        select_user = table.find_one(id=patient_id)

        print selected_patient, select_user
        json_user = jsonify(select_user)
        print json_user
        select_user['diagnoses'] = []
        #select_user['diagnoses'].append(patient_diag[0])
        #select_user['diagnoses'].extend(patient_diag)
        print "Trying to get a response."
       # response = json.dumps(selected_patient)
        return jsonify(select_user)

       # print response
        #response.content_type='application/json'

        #return render_template('site/dashboard_doctor.html', )
        #return response
    except:
        print "Error!"

@app.route('/login', methods=['GET', 'POST'])
def site_login():
    form = LoginForm()
    if form.validate_on_submit():
        print "Attempting to login"
        print "In the login statement."
        #user = User.query.filter_by(staff_id=request.form['staff_id']).first()
        print "Queried."

        try:
            #user = User.objects.get(email=request.form['email'])
            print "In the login statement."
            user2 = User.query.filter_by(staff_id=request.form['staff_id']).first()
            print "Queried."

            print user2

            if user2.verify_password(request.form['password']):

                print "SUCCESS!"

                print "Attempting to actually login!"
                login_user(user2)
                print "Logged in?"
                flash('Logged in successfully.', 'success')

                print "CORRECT!"
                return redirect(request.args.get('next') or url_for('site_index'))
            else:
                print "ERROR"
                flash('Username or password is incorrect', 'error')

        except:
            flash('Username or password is incorrect', 'error')


    return render_template('site/login.html', form=form)


@app.route('/logout')
@login_required
def site_logout():
    logout_user()
    return redirect(url_for('site_index'))


@app.route('/register', methods=['GET', 'POST'])
def site_register():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            #user = User.objects.get(email=request.form['email'])
            nurse = User.objects.get(staff_id=request.form['staff_id'])
            if nurse:
                flash('This email address is already in use.', 'error')
            return render_template('site/login.html', form=form)

        except:
            user = User()
            user.email = request.form['staff_id']
            user.username = request.form['staff_id']
            user.staff_id=request.form['staff_id']
            user.set_password(request.form['password'])
            pdb.session.add(user)
            pdb.session.commit()
            

            flash('Successfully registered', 'success')
            return redirect(url_for('site_index'))
    
    return render_template('site/login.html', form=form)
