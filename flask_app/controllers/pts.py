from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.student import Student
from flask_app.models.pt import PT


@app.route('/new/pt')
def new_pt():
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['student_id']
    }
    return render_template('new_pt.html',student=Student.get_by_id(data))


@app.route('/create/pt',methods=['POST'])
def create_pt():
    if 'student_id' not in session:
        return redirect('/logout')
    if not PT.validate_pt(request.form):
        return redirect('/new/pt')
    data = {
        "title": request.form["title"],
        "type": request.form["type"],
        "date_completed": request.form["date_completed"],
        "notes": request.form["notes"],
        "student_id": session["student_id"]
    }
    PT.save(data)
    return redirect('/dashboard')


@app.route('/edit/pt/<int:id>')
def edit_pt(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("edit_pt.html",edit=PT.get_one(data),student=Student.get_by_id(student_data))


@app.route('/update/pt',methods=['POST'])
def update_pt():
    if 'student_id' not in session:
        return redirect('/logout')
    if not PT.validate_pt(request.form):
        return redirect('/new/pt')
    data = {
        "title": request.form["title"],
        "type": request.form["type"],
        "notes": request.form["notes"],
        "date_completed": request.form["date_completed"],
        "id": request.form['id']
    }
#     # "id" above may need to be student_id - need to figure this out; Update: it looks ok and seems to work
    PT.update(data)
    return redirect('/dashboard')


@app.route('/show/pt/<int:id>')
def show_pt(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student_data = {
        "id":session['student_id']
    }
    return render_template("show_pt.html",pt=PT.get_one(data),student=Student.get_by_id(student_data))


@app.route('/destroy/pt/<int:id>')
def destroy_pt(id):
    if 'student_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    PT.destroy(data)
    return redirect('/dashboard')