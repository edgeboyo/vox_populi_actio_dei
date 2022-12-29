from flask import Flask, request

app = Flask(__name__)

# A list to store the input from users
inputs = []

@app.route('/submit', methods=['POST'])
def submit():
    # Get the input from the request
    user_input = request.form['input']
    # Add the input to the list
    inputs.append(user_input)
    return 'Success'

@app.route('/execute', methods=['GET'])
def execute():
    # Find the most popular input in the list
    most_popular = max(set(inputs), key=inputs.count)
    # Execute the command associated with the most popular input
    # Replace this with your own code to execute the command
    command_output = execute_command(most_popular)
    return command_output

def execute_command(command):
    # Replace this with your own code to execute the command
    return 'Executing command: {}'.format(command)

from collections import Counter

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    # Get a count of all the inputs
    input_counts = Counter(inputs)
    # Get the 3 most common inputs
    most_common = input_counts.most_common(3)
    # Return the leaderboard as a JSON response
    return jsonify(most_common)

if __name__ == '__main__':
    app.run()
 