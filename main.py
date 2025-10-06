from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app, origins='*')

@app.route('/api/users', methods=['GET'])
def users():
      return jsonify(
            {
                  "users":[
                        'arpan',
                        'john',
                        'doe',
                        'Samanja',
                        'Tom and Samanja are friends',
                        'Samanja loves coding',
                        'Tom loves Samanja'
                  ]
            }

      )

if __name__=="__main__":
      app.run(debug=True, port=8080)


