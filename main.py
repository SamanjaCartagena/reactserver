from flask import Flask, jsonify, request
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app, origins='*')

user_list=[
      'arpan',
      'john',
      'doe',
      'Samanja',
      'Tom and Samanja are friends',
      'Samanja loves coding',
      'Tom loves Samanja'
]

@app.route('/api/users', methods=['GET'])
def users():
    """
    Handles GET requests to the /api/users endpoint.
    """
    return jsonify({"users": user_list})

      
@app.route('/api/users', methods=['POST'])
def handle_post_request():
    """
    Handles POST requests to the /submit_data endpoint.
    """
    if request.is_json:
        data = request.get_json()
        # Process the received JSON data
        print(f"Received JSON data: {data}")
        user_list.append(data.get("name"))
        return jsonify({"message": "Data received successfully!", "data": data}), 200
    else:
        # Handle non-JSON data, e.g., form data
        data = request.form
        print(f"Received form data: {data}")
        return jsonify({"message": "Form data received successfully!", "data": dict(data)}), 200
    

if __name__=="__main__":
      app.run(debug=True, port=8080)


