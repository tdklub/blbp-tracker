from flask_app import app

from flask_app.controllers import students, essays, pts, mbes

if __name__ == "__main__":
    app.run(debug=True)