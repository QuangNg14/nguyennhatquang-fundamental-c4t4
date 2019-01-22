from flask import Flask, render_template, request, redirect, url_for
from models.classModels import *
from mlab import *
connect()
app = Flask(__name__)



@app.route('/abc')
def abc():
    return "Day laf abc"

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        dataGet_person = Person.objects()   #lay tu database ve 
        return render_template('index.html', data = dataGet_person)



@app.route('/add',methods = ["GET","POST"])
def indextest():
    # if request.method == "GET": #truy cap vao bat ki trang nao thi deu la GET 
    #     dataGet_school = School.objects()
    #     return render_template("indextest.html", data = dataGet_school)
    # elif request.method == "POST":
    #     form = request.form #nguoi dung nhap data(username, password,...) va lay ra o form 
    #     name = form["name"]
    #     location = form["location"]
    #     age = form["age"]
    #     student = form["student"]
    #     postNewSchool = School(name = name, location = location, age = age, student = student) #nap cac gia tri vao postnewschool
    #     postNewSchool.save()
    #     dataGet_school = School.objects()
    #     return render_template('result.html', data = dataGet_school)
    if request.method == "GET":
        dataGet_person = Person.objects()
        return render_template('indextest.html', data = dataGet_person)
    elif request.method == "POST":
        # lay data sau khi nhap vao o form 
        form = request.form
        name = form["name"]
        age = form["age"]
        height = form["height"]
        weight = form["weight"]
        postNewPerson = Person(name=name, age=age, weight=weight, height=height, status=False)
        postNewPerson.save()
        # lay ra tu database 
        dataGet_person = Person.objects() 
        # return render_template('result.html', data = dataGet_person)
        return redirect(url_for("index")) #chay method GET cua def index() o ben tren 

@app.route('/editUser/<userId>',methods = ["GET","POST"])
def editUser(userId):
    return userId

@app.route('/deleteUser/<userId>',methods = ["GET","POST"])
def deleteUser(userId): #userId tu mlab
    userGet = Person.objects.get(id=userId)
    userGet.delete()  #xoa dong vua bam 
    return redirect(url_for("index")) #chay method GET cua def index() o ben tren 

if __name__ == '__main__':
  app.run(port=8000, debug=True)
 