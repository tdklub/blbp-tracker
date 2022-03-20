from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.student import Student
from flask_app.models.essay import Essay
from flask_app.models.mbe import MBE
from flask_app.models.pt import PT
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not Student.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Student.save(data)
    session['student_id'] = id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    student = Student.get_by_email(request.form)
    if not student:
        flash("Invalid Email or Password","login")
        return redirect('/')
    if not bcrypt.check_password_hash(student.password, request.form['password']):
        flash("Invalid Email or Password","login")
        return redirect('/')
    session['student_id'] = student.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'student_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['student_id']
    }
    return render_template("dashboard.html", student=Student.get_by_id(data), essays=Essay.get_all(), pts=PT.get_all(), mbes=MBE.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')