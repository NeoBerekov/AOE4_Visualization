from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

def snake_to_camel(snake_str, upper_case_first_letter=False):
    components = snake_str.split('_')
    if upper_case_first_letter:
        # 大驼峰式（UpperCamelCase）
        return ''.join(x.title() for x in components)
    else:
        # 小驼峰式（lowerCamelCase）
        return components[0] + ''.join(x.title() for x in components[1:])


@app.route('/api/solodata/rank/winrate', methods=['GET'])
def get_data():
    refresh = request.args.get('refresh',default='no', type=str).lower() == 'yes'
    refresh_all = request.args.get('refresh',default='no', type=str).lower() == 'all'
    rank = request.args.get('rank',default='overall', type=str).lower()
    if rank != 'overall':
        rank = snake_to_camel(rank,upper_case_first_letter=True)
    if refresh and ~refresh_all:
        import refresh
        refresh.refresh_data(rank) #refresh data
    elif refresh_all:
        import refresh
        refresh.refresh_data()

    # Determine the path of the json file
    file_path = 'rank_charts_' + rank + '.json'

    # Open the file and read its content
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Return the content of the file as a response
    return jsonify(data)

@app.route('/api/solodata/rank/games_count', methods=['GET'])
def get_data2():
    refresh = request.args.get('refresh',default='no', type=str).lower() == 'yes'
    refresh_all = request.args.get('refresh',default='no', type=str).lower() == 'all'
    rank = request.args.get('rank',default='overall', type=str).lower()
    if rank != 'overall':
        rank = snake_to_camel(rank,upper_case_first_letter=True)
    if refresh and ~refresh_all:
        import refresh
        refresh.refresh_data(rank)
    # Determine the path of the json file
    file_path = 'games_count_charts_' + rank + '.json'
    # Open the file and read its content
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Return the content of the file as a response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)




