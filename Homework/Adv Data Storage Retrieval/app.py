# Instructions-------------------------------------------------------------------------------------------------------------------
# Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.
## Use FLASK to create your routes.

# Routes

## api/v1.0/precipitation
#-- Query for the dates and temperature observations from the last year.
#-- Convert the query results to a Dictionary using date as the key and tobs as the value.
#-- Return the json representation of your dictionary.

## /api/v1.0/stations
#-- Return a json list of stations from the dataset.

## /api/v1.0/tobs
#-- Return a json list of Temperature Observations (tobs) for the previous year

## /api/v1.0/<start> and /api/v1.0/<start>/<end>
#--  Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#- - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#-- When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Hints
#-- You will need to join the station and measurement tables, or match a measurement.station value for some of the analysis queries.
#-- Use Flask jsonify to convert your api data into a valid json response object.
#--------------------------------------------------------------------------------------------------------------------------------------

# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up db
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect Database into ORM classes (Station and Measurement)
Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.stations
Measurement = Base.classes.measurements

# Create session to db
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Set up Flask routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"- List of prior year tobs<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"- List of Station numbers and names<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"- List of prior year temperatures from all stations<br/>"
        f"<br/>"
        f"/api/v1.0/start<br/>"
        f"- When given the start date (YYYY-MM-DD), calculates the MIN/AVG/MAX temperature for all dates greater than and equal to the start date<br/>"
        f"<br/>"
        f"/api/v1.0/start/end<br/>"
        f"- When given the start and the end date (YYYY-MM-DD), calculate the MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"

    )

# Route - precipitation

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Return a list of tobs observations from prior year
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > prior_year).\
        order_by(Measurement.date).all()

    # Create a list of dicts with `date` and `tobs` as the keys and values
    tobs_list = []
    for item in tobs_data:
        row = {}
        row["date"] = tobs_data[0]
        row["tobs"] = tobs_data[1]
        tobs_list.append(row)

    return jsonify(tobs_list)


# Route - stations
@app.route("/api/v1.0/stations")
def stations():
    # Query for all stations
    stations_query = session.query(Station.name, Station.station).all()

    stations_list = []
    for station in stations_query:
        stations_list.append(station[1])

    return jsonify(stations_list)
# Route - tobs
@app.route("/api/v1.0/tobs")
def tobs():

    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > prior_year).\
        order_by(Measurement.date).all()

    # Create a list of dicts with `date` and `tobs` as the keys and values
    temp_list = []
    for result in temp_data:
        row = {}
        row["date"] = temp_data[0]
        row["tobs"] = temp_data[1]
        temp_list.append(row)

    return jsonify(temp_list)

# Route - start
@app.route("/api/v1.0/<start>")
def trip1(start):

    # Start from start date and go to end of data for TMin/TAvg/TMax temp
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    prior_year = dt.timedelta(days=365)

    start = start_date - prior_year
    end =  dt.date(2017, 8, 23)

    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start, Measurements.date <= end).all()

    trip = list(np.ravel(trip_data))
    return jsonify(trip)

# Route  - start/end
@app.route("/api/v1.0/<start>/<end>")
def trip2(start,end):

    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date= dt.datetime.strptime(end,'%Y-%m-%d')

    prior_year = dt.timedelta(days=365)

    start = start_date - prior_year
    end = end_date - prior_year

    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    trip = list(np.ravel(trip_data))
    return jsonify(trip)

# Set the debugging for app to run
if __name__ == "__main__":
    app.run(debug=True)
