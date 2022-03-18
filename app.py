# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the xgbr regressor
filename = 'Chennai_model.pkl'
Regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        AREA = int(request.form['AREA'])
        INT_SQFT = int(request.form['INT_SQFT'])
        N_BEDROOM = float(int(request.form['N_BEDROOM']))
        N_ROOM = int(request.form['N_ROOM'])
        BUILDTYPE = int(request.form['BUILDTYPE'])
        MZZONE = float(request.form['MZZONE'])

        
        data = np.array([[AREA, INT_SQFT, N_BEDROOM, N_ROOM, BUILDTYPE, MZZONE]])
        my_prediction = Regressor.predict(data)
        
        return render_template('index.html', prediction_text='House Price is {} Rs'.format(my_prediction))

if __name__ == '__main__':
	app.run(debug=True)