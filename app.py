from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # allow cross-origin

'''
This is the main file of the backend. It contains the API for the frontend to call.
'''


def snake_to_camel(snake_str, upper_case_first_letter=False):
    # convert snake case to camel case
    components = snake_str.split('_')
    if upper_case_first_letter:
        # UpperCamelCase
        return ''.join(x.title() for x in components)
    else:
        # lowerCamelCase
        return components[0] + ''.join(x.title() for x in components[1:])


@app.route('/api/solodata/rank/winrate', methods=['GET'])
def get_win_rate_data():
    refresh = request.args.get('refresh', default='no', type=str).lower() == 'yes'
    refresh_all = request.args.get('refresh', default='no', type=str).lower() == 'all'
    rank = request.args.get('rank', default='overall', type=str).lower()
    if rank != 'overall':
        rank = snake_to_camel(rank, upper_case_first_letter=True)
    if refresh and ~refresh_all:
        import refresh
        refresh.refresh_data(rank)  # refresh data of given rank
    elif refresh_all:
        import refresh
        refresh.refresh_data()  # refresh all data

    # Determine the path of the json file
    file_path = 'rank_charts/rank_charts_' + rank + '.json'

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Return the content of the file as a response
    return jsonify(data)


@app.route('/api/solodata/rank/games_count', methods=['GET'])
def get_games_count_data():
    refresh = request.args.get('refresh', default='no', type=str).lower() == 'yes'
    refresh_all = request.args.get('refresh', default='no', type=str).lower() == 'all'
    rank = request.args.get('rank', default='overall', type=str).lower()
    if rank != 'overall':
        rank = snake_to_camel(rank, upper_case_first_letter=True)
    if refresh and ~refresh_all:
        import refresh
        refresh.refresh_data(rank)
    file_path = 'games_count_charts/games_count_charts_' + rank + '.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/api/solodata/refreshAll', methods=['GET'])
def refresh_all():  # refresh all data as test/initialization function
    import refresh
    refresh.refresh_data()
    return 'refresh all data'


if __name__ == '__main__':
    app.run(debug=True)
