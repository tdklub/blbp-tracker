from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Essay:
    db_name = 'blbp_tracker'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.subject = db_data['subject']
        self.date_completed = db_data['date_completed']
        self.notes = db_data['notes']
        self.student_id = db_data['student_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO essays (title, subject, date_completed, notes, student_id) VALUES (%(title)s,%(subject)s,%(date_completed)s,%(notes)s,%(student_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM essays;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_essays = []
        for row in results:
            print(row['date_completed'])
            all_essays.append( cls(row) )
        return all_essays
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM essays WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE essays SET title=%(title)s, subject=%(subject)s, date_completed=%(date_completed)s, notes=%(notes)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM essays WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_essay(essay):
        is_valid = True
        if len(essay['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","essay")
        if len(essay['subject']) < 3:
            is_valid = False
            flash("Subject must be at least 3 characters","essay")
        if essay['date_completed'] == "":
            is_valid = False
            flash("Please enter a date","essay")
        return is_valid