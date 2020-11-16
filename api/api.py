import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

test_coord = [
    {'id': 0,
     'coords':    [
         [
             -8.616714477539062,
             41.14812272307602
         ],
         [
             -8.60302448272705,
             41.14812272307602
         ],
         [
             -8.60302448272705,
             41.156362715411504
         ],
         [
             -8.616714477539062,
             41.156362715411504
         ],
         [
             -8.616714477539062,
             41.14812272307602
         ]
     ]
     }]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Runnify2 Route Generator API</h1><p>This site is a prototype API for generating routes.</p>"

# request a route with an id


@app.route('/api/v1/route', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for route in test_coord:
        if route['id'] == id:
            results.append(route)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
