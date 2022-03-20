from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.student import Student
from flask_app.models.mbe import MBE


@app.route('/new/mbe')
def new_mbe():
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['student_id']
    }
    return render_template('new_mbe.html',student=Student.get_by_id(data))


@app.route('/create/mbe',methods=['POST'])
def create_mbe():
    if 'student_id' not in session:
        return redirect('/logout')
    # if not MBE.validate_mbe(request.form):
    #     return redirect('/new/mbe')
    data = {
        "num_completed": request.form["num_completed"],
        "num_correct": request.form["num_correct"],
        "date_completed": request.form["date_completed"],
        "notes": request.form["notes"],
        "student_id": session["student_id"]
    }
    MBE.save(data)
    return redirect('/dashboard')


@app.route('/edit/mbe/<int:id>')
def edit_mbe(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("edit_mbe.html",edit=MBE.get_one(data),student=Student.get_by_id(student_data))


@app.route('/update/mbe',methods=['POST'])
def update_mbe():
    if 'student_id' not in session:
        return redirect('/logout')
    # if not MBE.validate_mbe(request.form):
    #     return redirect('/new/mbe')
    data = {
        "num_completed": request.form["num_completed"],
        "num_correct": request.form["num_correct"],
        "date_completed": request.form["date_completed"],
        "notes": request.form["notes"],
        "id": request.form['id']
    }
#     # "id" above may need to be student_id - need to figure this out; Update: it looks ok and seems to work
    MBE.update(data)
    return redirect('/dashboard')


@app.route('/show/mbe/<int:id>')
def show_mbe(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("show_mbe.html",mbe=MBE.get_one(data),student=Student.get_by_id(student_data))


@app.route('/destroy/mbe/<int:id>')
def destroy_mbe(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    MBE.destroy(data)
    return redirect('/dashboard')