from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)



@app.route('/api/solodata', methods=['GET'])
def get_data():
    refresh = request.args.get('refresh',default='no', type=str).lower() == 'yes'
    refresh_all = request.args.get('refresh',default='no', type=str).lower() == 'all'
    rank = request.args.get('rank',default='overall', type=str).lower()
    if refresh and ~refresh_all:
        import refresh
        refresh.refresh_data(rank) #refresh data
    elif refresh_all:
        import refresh
        refresh.refresh_data()

    # Determine the path of the json file
    file_path = 'charts_' + rank + '.json'

    # Open the file and read its content
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Return the content of the file as a response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)




