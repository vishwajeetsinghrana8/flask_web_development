from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    person = "Vishwajeet"
    l1 = list(person)
    d1 = {"Name":"Vikas"}
    fruits = ["Mango","Banana","Peaches","Grapes"]    
    return render_template('base.html')

@app.route('/person/<name>')
def person(name):
    return render_template('person.html',name=name)

if  __name__ == "__main__":
    app.run(debug=True)
