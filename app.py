from flask import Flask, jsonify, request, redirect, url_for, session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'knowledgeshelf'

@app.route('/')
def index():
    session.pop('name', None)
    return "<h1>Welcome to flask tutorial</h1>"

@app.route('/home', methods=['GET','POST'])
def home():
    return "<h1>Welcome to home page.</h1>"

@app.route('/person', methods=['GET','POST'], defaults={'name': 'Knowledge Shelf'})
@app.route('/person/<string:name>', methods=['GET','POST'])
def person(name):
    session['name'] = name
    return "<h1>Hi, {}. Welcome to person page</h1>".format(name)

@app.route('/json')
def json():
    # if 'name' in session:
    l1 = [10,20,30,40]
    name = session['name']
    # else:
    #     name = 'Name is not available'
    return jsonify({"key1":"Value1", "key3":[10,20,30,40], 'name':name})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi, {}. You are from {}. You are on the query page.</h1>'.format(name, location)

@app.route('/theform', methods=['GET','POST'])
def theform():

    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" value="Submit">
                </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        # return '<h1>Hi, {}. You are from {}. You have submitted the form sucessfully!!!.</h1>'.format(name, location)
        return redirect(url_for('person', name=name, location=location))

# @app.route('/process', methods=["POST"])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return '<h1>Hi, {}. You are from {}. You have submitted the form sucessfully!!!.</h1>'.format(name, location)

@app.route('/requestjson', methods=["POST"])
def requestjson():

    data = request.get_json()

    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result':'Sucessful!', "name":name, "location":location, "randomlist":randomlist[2]})


if  __name__ == "__main__":
    app.run()