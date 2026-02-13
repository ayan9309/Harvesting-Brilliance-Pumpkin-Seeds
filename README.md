# 🌱 SeedGenomics: Advanced Morphological Analysis

![Status](https://img.shields.io/badge/Status-Operational-success?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask)
![ML](https://img.shields.io/badge/Model-Random%20Forest-orange?style=flat-square)
![Accuracy](https://img.shields.io/badge/Accuracy-98.8%25-green?style=flat-square)

**SeedGenomics** is an intelligent, web-based classification system designed to distinguish between pumpkin seed varieties (*Çerçevelik* and *Ürgüp Sivrisi*) with high precision. 

Moving beyond traditional manual inspection, this project leverages machine learning to analyze quantitative morphological features—such as Area, Perimeter, and Aspect Ratio—processing them through a custom **Inference Engine** to provide instant taxonomic classification.

---

## 🚀 Features

* **⚡ Real-Time Inference:** Optimized Flask backend delivers predictions in **<20ms**.
* **🧠 Advanced AI Model:** Powered by a **Random Forest Classifier** optimized via Grid Search, achieving **98.8% accuracy**.
* **🎨 Modern UI/UX:** Features a premium **Glassmorphism** design with a split-screen layout (Dark Mode Dashboard + Light Mode Input).
* **📊 Visual Inference Engine:** A custom-built visualizer that simulates the algorithmic processing of geometric data with pulse animations.
* **📱 Responsive Design:** Fully functional across desktop and mobile devices.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Custom Glassmorphism & Animations), JavaScript
* **Backend:** Python 3.x, Flask Web Framework
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Data Processing:** Jupyter Notebook (`.ipynb`)

---

## 📂 Project Structure

Ensure your project folder matches this structure exactly:

```text
SeedGenomics/
│
├── static/
│   └── css/
│       └── style.css          # Custom styling for Glassmorphism & Animations
│
├── templates/
│   ├── index.html             # Main Dashboard & Input Interface
│   └── predict.html           # Result Display Card
│
├── app.py                     # Main Flask Application Server
├── model_building.ipynb       # Jupyter Notebook for Training & Analysis
├── model.pkl                  # Trained Random Forest Model (Auto-generated)
├── scaler.pkl                 # Feature Scaler (Auto-generated)
├── Pumpkin_Seeds_Dataset.xlsx # Raw Dataset Source
└── README.md                  # Project Documentation

⚙️ Installation & Setup
1. Prerequisites
Ensure you have Python installed. You will also need the following libraries:

Bash
pip install flask scikit-learn pandas numpy openpyxl
2. Train the Model
Before running the app, you must generate the trained model file.

Open model_building.ipynb in VS Code or Jupyter.

Run all cells to process the dataset and train the Random Forest.

Verify that model.pkl and scaler.pkl have appeared in your project folder.

3. Run the Application
Open your terminal in the project folder and run:

Bash
python app.py
4. Access the Interface
Open your web browser and navigate to the local server address shown in the terminal (usually):
http://127.0.0.1:5000/

🧠 How It Works
Data Input: The user enters geometric values (e.g., Area: 56276, Perimeter: 888.24) into the web form.

Preprocessing: The backend loads the saved MinMaxScaler (scaler.pkl) to normalize the inputs to the same scale used during training.

Inference: The data is passed to the Random Forest model (model.pkl), which predicts the class (0 for Çerçevelik, 1 for Ürgüp Sivrisi).

Visualization: The frontend triggers a "Processing Geometry" animation state while the server computes the result.

Result: The final classification is displayed on a clean result card with a confidence summary.

🔮 Future Scope
Computer Vision Integration: Implementing CNNs to allow users to upload images of seeds for automatic feature extraction.

Mobile Application: Developing a React Native version for on-field usage by farmers.

IoT Connectivity: Linking the software with automated sorting machinery for industrial applications.

📝 License
This project is developed for educational purposes as part of the Artificial Intelligence Internship Program.

Developed by Mohamadayan Desai