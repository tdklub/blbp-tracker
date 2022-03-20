from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.student import Student
from flask_app.models.essay import Essay


@app.route('/new/essay')
def new_essay():
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['student_id']
    }
    return render_template('new_essay.html',student=Student.get_by_id(data))


@app.route('/create/essay',methods=['POST'])
def create_essay():
    if 'student_id' not in session:
        return redirect('/logout')
    if not Essay.validate_essay(request.form):
        return redirect('/new/essay')
    data = {
        "title": request.form["title"],
        "subject": request.form["subject"],
        "date_completed": request.form["date_completed"],
        "notes": request.form["notes"],
        "student_id": session["student_id"]
    }
    Essay.save(data)
    return redirect('/dashboard')


@app.route('/edit/essay/<int:id>')
def edit_essay(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("edit_essay.html",edit=Essay.get_one(data),student=Student.get_by_id(student_data))


@app.route('/update/essay',methods=['POST'])
def update_essay():
    if 'student_id' not in session:
        return redirect('/logout')
    if not Essay.validate_essay(request.form):
        return redirect('/new/essay')
    data = {
        "title": request.form["title"],
        "subject": request.form["subject"],
        "notes": request.form["notes"],
        "date_completed": request.form["date_completed"],
        "id": request.form['id']
    }
    # "id" above may need to be student_id - need to figure this out; Update: it looks ok and seems to work
    Essay.update(data)
    return redirect('/dashboard')


@app.route('/show/essay/<int:id>')
def show_essay(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("show_essay.html",essay=Essay.get_one(data),student=Student.get_by_id(student_data))


@app.route('/destroy/essay/<int:id>')
def destroy_essay(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Essay.destroy(data)
    return redirect('/dashboard')