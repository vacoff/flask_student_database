from flask import Flask, render_template, url_for, redirect
from mydb import DataBase
from datetime import datetime
from gen import StudentGen

app = Flask(__name__)

database = DataBase("demo")
#database.create_table()
#obj = StudentGen(20)
#for stud in obj.students:
#    database.insert(stud)

@app.route("/")
def index():
    
    student = database.select_all()
    return render_template("index.html", student = student)
 
@app.route("/info/<slug>") 
def info(slug):
    try:
        student = database.select_by_col({"slug": slug})[0]
        student_name = f"{student.pop('fname')} {student.pop('sname')}"
        student.pop("id")
        student.pop("slug")
        result = []
        for key, value in student.items():
            if key =="gender" and value=="m":
                result.append({"Gender":"Male"})
            elif key =="gender" and value=="f":
                result.append({"Gender":"Female"})
            elif key =="bdate":
                bdate = datetime.strptime(value,"%Y-%m-%d" )
                result.append({"Birthdate": str(bdate.strftime("%d.%m.%Y"))})
            else:
                result.append({key:value})
    except Exception as e:
        return e
    
   
    return render_template("info.html", data = result, name = student_name)


@app.errorhandler(500)
def internal_error(error):
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()


