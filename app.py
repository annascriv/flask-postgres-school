from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://annascriven@localhost/school_db"

db = SQLAlchemy(app)

class Student(db.Model):
    # __tablename__= 'student'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

    def __repr__(self):
        {'id':self.id,
         'first_name':self.first_name,
         'last_name':self.last_name,
         'age':self.age,
         'subject':self.subject}
        
class Subjects(db.Model):
    # __tablename__= 'subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(1))

    def __repr__(self):
        {'id':self.id,
         'subject':self.subject}
        
class Teachers(db.Model):
    # __tablename__= 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

    def __repr__(self):
        {'id':self.id,
         'first_name':self.first_name,
         'last_name':self.last_name,
         'age':self.age,
         'subject':self.subject}
        

# teachers = Teachers.query.all()
# subjects = Subjects.query.all()

# list_of_subjects = []

# for teach, subj in teachers, subjects:
#     if teach.subject==subj.id:
#         list_of_subjects.append({
#             "teach.first_name":teach.subject
#         })

# print(list_of_subjects)

@app.route('/students', methods = ['GET'])
def get_students():
    students = Student.query.all()
    teachers = Teachers.query.all()
    student_list = []

    for stud in students:
        student_list.append(
            {
             "id": stud.id,
             "first_name": stud.first_name,
             "last_name": stud.last_name,
             "age":stud.age,
             "class": {
                 "subject": stud.subject,
                            }
        }
        )
    return jsonify(student_list)

@app.route('/teachers', methods = ['GET'])
def get_teachers():
    teachers = Teachers.query.all()
    teacher_list = []

    for teach in teachers:
        teacher_list.append(
            {
                "first_name": teach.first_name,
                "last_name":teach.last_name,
                "age":teach.age,
                "subject":teach.subject
            }
        )
    return jsonify(teacher_list)

@app.route('/subjects', methods = ['GET'])
def get_subjects():
    subjects = Subjects.query.all()
    subject_list = []

    for subj in subjects:
        subject_list.append(
            {
                "id":subj.id,
                "subject":subj.subject
            }
        )
    return jsonify(subject_list)



app.run(debug=True)
