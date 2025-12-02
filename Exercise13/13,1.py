from flask import Flask, Response
import json

app = Flask(__name__)

def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route("/prime_number/<int:number>", methods=["GET"])
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": prime(number)
    }
    return Response(json.dumps(result), mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)