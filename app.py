from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID = "Mridhul_S_06022004"
EMAIL = "mridhula.s2021@vitstudent.ac.in"
ROLL_NUMBER = "21BLC1144"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)

    lowercase_alphabets = [char for char in alphabets if char.islower()]
    if lowercase_alphabets:
        highest_lowercase_alphabet.append(max(lowercase_alphabets))

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

