# Disease Prediction and Doctor Recommendation System

This project is a web application that predicts the disease based on the symptoms entered by the user and recommends doctors and specialists for the predicted disease. The application uses machine learning models to predict the disease and a recommendation algorithm to suggest suitable doctors based on the user's city and preferred timings.

## Features

- Predict disease based on user-provided symptoms
- Recommend doctors and specialists for the predicted disease
- Filter doctors by city and preferred timings
- Display disease description and chances of having the disease
- Show doctor details including name, hospital, city, experience, and rating

## Technologies Used

- Python
- Flask
- React.js
- Scikit-learn
- Pandas
- Numpy
- Seaborn
- Matplotlib

## Installation

1. Clone the repository:

```

git clone https://github.com/laharisiri123/Disease-Healthcare-Provider-Recommendation.git

```

2. Install the required Python packages:

```

pip install -r requirements.txt

```

3. Install the required Node.js packages for the React app:

```

cd frontend
npm install

```

## Usage

1. Start the Flask server:

```

python3 disease_healthprovider_recommendation.py

```

2. In a separate terminal, start the React development server:

```

cd frontend
npm run dev

```

3. Open your web browser and navigate to `http://localhost:<PORTNUMBER>` to access the application.

4. Enter your symptoms, select the city, and preferred timings (optional).

5. Click the "Submit" button to get the disease prediction and recommended doctors.

## Acknowledgments

- The disease and symptom data are sourced from online resource - Kaggle.
- Hospital data are sourced from Newsweek website
- The healthcare provider and user ratings data generated synthetically for demonstration purposes.
