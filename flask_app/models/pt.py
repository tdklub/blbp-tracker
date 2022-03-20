from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class PT:
    db_name = 'blbp_tracker'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.type = db_data['type']
        self.date_completed = db_data['date_completed']
        self.notes = db_data['notes']
        self.student_id = db_data['student_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO pts (title, type, date_completed, notes, student_id) VALUES (%(title)s,%(type)s,%(date_completed)s,%(notes)s,%(student_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pts;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_pts = []
        for row in results:
            print(row['date_completed'])
            all_pts.append( cls(row) )
        return all_pts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE pts SET title=%(title)s, type=%(type)s, date_completed=%(date_completed)s, notes=%(notes)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pts WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_pt(pt):
        is_valid = True
        if len(pt['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","pt")
        if len(pt['type']) < 3:
            is_valid = False
            flash("Type must be at least 3 characters","pt")
        if pt['date_completed'] == "":
            is_valid = False
            flash("Please enter a date","pt")
        return is_valid