#################################################
# import dependencies
#################################################
from flask import Flask, render_template, jsonify, redirect

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# sqlite : connect to the existing database
#################################################

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
OTU = Base.classes.otu
Samples = Base.classes.samples
SamplesMetadata = Base.classes.samples_metadata
session = Session(engine)


#################################################
# Flask Routes
#################################################

# render index.html
@app.route("/")
def index():

    sample_list_v = names()
    print(sample_list_v)

    return render_template("index.html")

# list of sample names
@app.route("/names")
def names():

    samples_cols_list = Samples.__table__.columns.keys()
    sample_list = samples_cols_list[1:]
    return jsonify(sample_list)

# list of otu descriptions
@app.route("/otu")
def otu():

    otu_desc = session.query(OTU.lowest_taxonomic_unit_found).all()
    otu_descriptions = [i[0] for i in otu_desc]
    return jsonify(otu_descriptions)

# metadata for a specific sample
@app.route('/metadata/<sample>')
def metadata(sample):

    results = session.query(SamplesMetadata).filter(SamplesMetadata.SAMPLEID == sample[3:]).all()
    dict1 = {}
    for k,v in results[0].__dict__.items():
        if ('AGE' in k or 'BBTYPE' in k or 'ETHNICITY' in k or 'GENDER' in k or 'LOCATION' in k or 'SAMPLEID' in k):
            dict1[k] = v

    return jsonify(dict1)

# washing frequency for a specific sample
@app.route('/wfreq/<sample>')
def wfreq(sample):

    results = session.query(SamplesMetadata.WFREQ).filter(SamplesMetadata.SAMPLEID == sample[3:]).all()
    print(results)
    return jsonify(results[0][0])

# otu_id's and corresponding sample count in descending order
# for a specific sample
@app.route('/samples/<sample>')
def samples(sample):

    results = session.query(Samples.otu_id,getattr(Samples, sample)).order_by(getattr(Samples, sample).desc()).all()

    dict1 = {}
    list1 = []
    list2 = []
    list3 = []
    for x in results:
        if(x[1] > 0):
            list1.append(x[0])
            list2.append(x[1])
    dict1['otu_id'] = list1
    dict1['sample_values'] = list2
    list3.append(dict1)
    list3

    return jsonify(list3)

# Allow Access to control headers
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run()

# Initiate the Flask app
if __name__ == "__main__":
    app.run(debug=True)
