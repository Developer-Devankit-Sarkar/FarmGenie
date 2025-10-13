import ee
from flask import Flask, request, render_template, Response
from flask_cors import CORS

ee.Authenticate()
ee.Initialize(project='dark-yen-474211-d5')

soil_ph = ee.Image("OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M")
depth_band = soil_ph.select('b1')
app = Flask(__name__)
CORS(app, resources={r"/foo": {"origins": "*"}})

@app.route("/get-soilpH", methods=["POST", "GET"])
def getsoilph():
    if request.method == "POST":
        print(request.form)
        # point = ee.Geometry.Point([float(request.form["longitude"]), float(request.form["latitude"])])
        # ph_value = depth_band.sample(point, scale=250).first().getInfo()
        # return Response(ph_value)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
