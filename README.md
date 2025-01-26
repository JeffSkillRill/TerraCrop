# Crop Recommendation System Using Machine Learning 🌱

This project is a crop recommendation system based on environmental factors like nitrogen (N), phosphorus (P), potassium (K), pH level, rainfall, and temperature. It predicts the best crop to grow in a given region based on these inputs.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

## Overview

The Crop Recommendation System is built using Flask for the backend and machine learning to predict the best crop based on user inputs such as nitrogen (N), phosphorus (P), potassium (K), pH, rainfall, and the temperature of the region. The system fetches real-time humidity data from the OpenWeather API.

The user inputs the temperature manually, and the system calculates the best crop based on the provided environmental data.

## Installation

### Prerequisites

To run the project, you need the following installed:

- Python 3.x
- `pip` (Python's package installer)

### Steps to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/JeffSkillRill/TerraCrop
    ```
2. Navigate into the project directory:
    ```bash
    cd crop-recommendation-system
    ```
3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Open a browser and go to `http://127.0.0.1:5000/` to access the Crop Recommendation System.

3. Enter the required values for Nitrogen (N), Phosphorus (P), Potassium (K), pH, Rainfall, and City name. The system will fetch real-time humidity data and use the temperature you provide to predict the best crop for the area.

4. The predicted crop will be displayed after you click the **Submit** button. You can also click **Reinput Values** to reset the form and make new predictions.

## How It Works

The system uses machine learning models to predict the best crop for a given location based on environmental factors.

- **Model Loading**: The trained machine learning model, StandardScaler, and MinMaxScaler are loaded from pickle files.
- **API Interaction**: The system uses OpenWeather API to fetch the real-time humidity for the entered city.
- **Data Preprocessing**: The input values are scaled using the MinMaxScaler and StandardScaler before making predictions with the loaded model.
- **Crop Prediction**: The system returns the best crop to grow based on the model’s output, which is mapped to a specific crop in the dictionary.

### Machine Learning Model

The model was trained to predict crop suitability based on environmental factors using the following crops:

- Rice
- Maize
- Jute
- Cotton
- Coconut
- Papaya
- Orange
- Apple
- Muskmelon
- Watermelon
- Grapes
- Mango
- Banana
- Pomegranate
- Lentil
- Blackgram
- Mungbean
- Mothbeans
- Pigeonpeas
- Kidneybeans
- Chickpea
- Coffee

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeather API for providing real-time weather data.
- scikit-learn for the machine learning tools and models.
- Flask for the web framework used in this project.