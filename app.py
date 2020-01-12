# Importing Flask and sqlalchemy
from flask import Flask, jsonify
import sqlite3
import sqlalchemy
import pandas as pd
import os
from sqlalchemy import create_engine
from pandas import DataFrame
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



#################################################
# Database Setup
#################################################
dbuser = 'postgres'
dbpassword = 'Pandas'
dbhost = 'localhost'
dbport = '5432'
dbname= 'metrics'
engine = create_engine(f"postgres://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")
Base.metadata.create_all(engine)
class Climate(Base):
    __tablename__ = 'metrics_data'
    id = Column(Integer, primary_key=True)
    year = Column(String)
    us_wildfire_count = Column(String)
    brazil_wildfire_count = Column(String)
    worldwide_oil_production = Column(String)
    oil_year_variance = Column(String)
    us_max_annual_temp_c = Column(String)
    brazil_max_annual_temp_c = Column(String)
    brazil_c02_emissions_ton = Column(String)
    us_c02_emissions_ton = Column(String)

#################################################
# Flask Routes
#################################################
app = Flask(__name__)



@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/total-climate-metrics<br/>"
        f"/api/v1.0/emissions<br/>"
        f"/api/v1.0/temperature<br/>"
        f"/api/v1.0/wildfires<br/>"
        )


@app.route("/api/v1.0/total-climate-metrics")
def climate():
    """Return a list of the database"""

    # Query the database completely
    session = Session(bind=engine)
    results = session.query(Climate.year, Climate.us_wildfire_count, Climate.brazil_wildfire_count, Climate.worldwide_oil_production, Climate.oil_year_variance, Climate.us_max_annual_temp_c, Climate.brazil_max_annual_temp_c, Climate.brazil_c02_emissions_ton, Climate.us_c02_emissions_ton).all()

    # close the session to end the communication with the database
    session.close()

    
    return jsonify(results)


@app.route("/api/v1.0/emissions")
def emission():
    """Return a list of oil production and c02 emissions"""

    # Query the database completely
    session = Session(bind=engine)
    results_2 = session.query(Climate.year, Climate.worldwide_oil_production, Climate.oil_year_variance, Climate.brazil_c02_emissions_ton, Climate.us_c02_emissions_ton).all()

    # close the session to end the communication with the database
    session.close()

    
    return jsonify(results_2)


@app.route("/api/v1.0/temperature")
def temp():
    """Return a list of oil production and temperatures"""

    # Query the database completely
    session = Session(bind=engine)
    results_3 = session.query(Climate.year, Climate.worldwide_oil_production, Climate.oil_year_variance, Climate.us_max_annual_temp_c, Climate.brazil_max_annual_temp_c).all()

    # close the session to end the communication with the database
    session.close()

    
    return jsonify(results_3)


@app.route("/api/v1.0/wildfires")
def fire():
    """Return a list of wildfires and temperature"""

    # Query the database completely
    session = Session(bind=engine)
    results_4 = session.query(Climate.year, Climate.us_wildfire_count, Climate.brazil_wildfire_count, Climate.us_max_annual_temp_c, Climate.brazil_max_annual_temp_c).all()

    # close the session to end the communication with the database
    session.close()

    
    return jsonify(results_4)



if __name__ == '__main__':
    app.run(debug=True)
