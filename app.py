import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load BOTH the model and the scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get raw values from the form
    try:
        Area = float(request.form['Area'])
        Perimeter = float(request.form['Perimeter'])
        Major_Axis_Length = float(request.form['Major_Axis_Length'])
        Solidity = float(request.form['Solidity'])
        Extent = float(request.form['Extent'])
        Roundness = float(request.form['Roundness'])
        Aspect_Ration = float(request.form['Aspect_Ration']) 
        Compactness = float(request.form['Compactness'])

        # 2. Scale the specific features that were scaled during training
        # The scaler expects a list of lists: [[Area, Perimeter, Major_Axis_Length]]
        input_to_scale = np.array([[Area, Perimeter, Major_Axis_Length]])
        scaled_values = scaler.transform(input_to_scale)

        # Extract the scaled numbers
        s_Area = scaled_values[0][0]
        s_Perimeter = scaled_values[0][1]
        s_Major = scaled_values[0][2]

        # 3. Combine scaled values with the rest (which were never scaled)
        final_features = np.array([[s_Area, s_Perimeter, s_Major, Solidity, Extent, Roundness, Aspect_Ration, Compactness]])

        # 4. Predict
        prediction = model.predict(final_features)

        if prediction[0] == 0:
            res_text = "Your seed lies in Çerçevelik class"
        elif prediction[0] == 1:
            res_text = "Your seed lies in Ürgüp Sivrisi class"
        else:
            res_text = "Unknown Class"

        return render_template('predict.html', prediction_text=res_text)
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)