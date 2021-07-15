from flask import Flask,jsonify,request
from flask.signals import message_flashed

app=Flask(__name__)

data=[
    {
        'Contact':"9987644456",
        'Name':"Raju",
        'done':False,
        'id':1
    },
    {
        'Contact':"9876543222",
        'Name':'Rahul',
        'done':False,
        'id':2
    }
]
@app.route("/add-data",methods=["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data"
        },400)

    Contact={
        'id':data[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Conataact',""),
        'done':False
    }
    data.append(Contact)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })


if(__name__=="__main__"):
    app.run(debug=True)