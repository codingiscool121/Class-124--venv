from flask import Flask, app, jsonify, request
#Initializing flask with an argument. Name= main process.
app = Flask(__name__)

potter= [
    {
        'id': 1,
        'title': 'Harry Potter and the Sorcercers Stone'
    },
    {'id': 2, 
    'title':'Harry Potter and the Chamber of Secrets'
    },
    {'id': 3,
    'title':'Harry Potter and the Prisoner of Azkaban'
    },
    {'id': 4,
    'title':'Harry Potter and the Goblet of Fire'
    },
    {'id': 5,
    'title':'Harry Potter and the Order of the Phoenix'
    },
    {'id': 6,
    'title':'Harry Potter and the Half-Blood Prince'
    },
    {'id': 7,
    'title':'Harry Potter and the Deathly Hallows'
    }
]

@app.route('/')

def home():
    return 'Soham'
#Post is for sending data/information
@app.route('/sendinfo', methods=['POST'])
def sendinfo():
    #Checking if the request has the right data
    if not request.json:
        return jsonify({'status': 'Error', 'Message': 'Please provide valid data.'}, 400)
    temp = {
        'id': potter[-1]['id'] + 1,
        'title': request.json['title'],
    }
    potter.append(temp)
    return jsonify({'status':'Success', 'Message': 'Data has successfully been added'})
    
#Get method gets info from the server/database
@app.route('/getinfo', methods=['GET'])
def getinfo():
    return jsonify({'data': potter})
    

#If the main process is running, then it will run the app.
if __name__ == '__main__':
    app.run(debug=True)

