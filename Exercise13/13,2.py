from flask import Flask, Response
import json
import mariadb

app = Flask(__name__)

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='bootsandcats',
    database='flight_game',
    autocommit=True)


@app.route("/airport/<icao>", methods=["GET"])
def get_airport_data(icao):
    icao = icao.strip().upper()

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    row = cursor.fetchone()
    cursor.close()

    if row:
        result = {
            "ICAO": icao, 
            "Name": row["name"],
            "Location": row["municipality"]}
    else:
        result = {
            "error": "Airport not found"}

    return Response(json.dumps(result), mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)