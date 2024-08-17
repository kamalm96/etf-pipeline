from flask import jsonify, request
import subprocess
import pandas as pd
from app import app, engine


@app.route("/run-etl", methods=["POST"])
def run_etl():
    try:
        subprocess.run(["python", "scripts/run_etl.py"])
        return jsonify({"message": "ETL process completed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/weather-data", methods=["GET"])
def get_weather_data():
    df = pd.read_sql("SELECT * FROM weather_data", engine)
    return df.to_json(orient="records")
