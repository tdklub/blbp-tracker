from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class MBE:
    db_name = 'blbp_tracker'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.num_completed = db_data['num_completed']
        self.num_correct = db_data['num_correct']
        self.date_completed = db_data['date_completed']
        self.notes = db_data['notes']
        self.student_id = db_data['student_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO mbes (num_completed, num_correct, date_completed, notes, student_id) VALUES (%(num_completed)s,%(num_correct)s,%(date_completed)s,%(notes)s,%(student_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mbes;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_mbes = []
        for row in results:
            print(row['date_completed'])
            all_mbes.append( cls(row) )
        return all_mbes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM mbes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE mbes SET num_completed=%(num_completed)s, num_correct=%(num_correct)s, date_completed=%(date_completed)s, notes=%(notes)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM mbes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    # @staticmethod
    # def validate_mbe(mbe):
    #     is_valid = True
    #     if len(essay['title']) < 3:
    #         is_valid = False
    #         flash("Title must be at least 3 characters","essay")
    #     if len(essay['subject']) < 3:
    #         is_valid = False
    #         flash("Subject must be at least 3 characters","essay")
    #     if essay['date_completed'] == "":
    #         is_valid = False
    #         flash("Please enter a date","essay")
    #     return is_valid

    # Need to figure out how to validate integers