# Disease Prediction and Doctor Recommendation System

## **Problem Statement**

The medical industry faces significant challenges, including difficulties in accessing accurate disease diagnosis, finding highly qualified and experienced healthcare providers tailored to individual needs and preferences, and the high costs associated with misdiagnosis or delayed treatment.

Specifically, the problems addressed by this project are:

1. **Difficulty in Accurate Disease Diagnosis**: For many individuals, especially those in underserved or remote areas, accessing medical testing facilities for accurate disease diagnosis can be challenging and costly.

2. **Limited Access to Specialized Healthcare Providers**: Finding healthcare providers with the appropriate expertise and specialties can be a daunting task, particularly in areas with limited healthcare resources. Additionally, identifying providers who meet individual preferences, such as location and preferred timings, adds another layer of complexity.

3. **High Costs of Misdiagnosis and Delayed Treatment**: Misdiagnosis or delayed treatment can lead to complications, adverse health outcomes, and increased healthcare costs due to prolonged treatment or additional interventions.

The goal of this project is to develop a comprehensive medical assistant platform that empowers individuals to make informed decisions about their healthcare needs by providing accurate disease predictions and personalized recommendations for highly qualified healthcare providers.

## **Solution**

The proposed solution is a powerful medical assistant platform that utilizes advanced machine learning techniques and data-driven approaches to address the aforementioned problems. The platform consists of the following key components:

1. **Disease Prediction Module**: This module employs supervised machine learning classification algorithms, such as Logistic Regression, Decision Trees, Random Forests, Support Vector Machines, Naive Bayes, and K-Nearest Neighbors, to predict potential diseases based on the user's reported symptoms. The algorithms are trained and evaluated on a dataset containing symptom-disease mappings, with the best-performing model selected for disease prediction.

2. **Healthcare Provider Recommendation Module**: This module recommends highly qualified and experienced healthcare providers based on the predicted disease's specialty, user-selected location, and preferred timings. It calculates a weighted score for each provider based on their experience and user ratings, and recommends the top providers with the highest weighted scores.

3. **User Interface**: The platform provides a user-friendly interface, developed using React.js, where users can input their symptoms and preferences (location and preferred timings). The predicted diseases and recommended healthcare providers are then displayed to the user.

4. **Backend Framework**: Flask, a Python-based web framework, is used to handle HTTP requests and responses, facilitate data processing, and integrate the machine learning models and recommendation algorithms.

The key steps involved in the solution are as follows:

1. The user inputs their symptoms and preferences (location and preferred timings) through the user interface.

2. The disease prediction module analyzes the user's reported symptoms and predicts the potential underlying disease or condition using the trained machine learning model.

3. Based on the predicted disease, the healthcare provider recommendation module filters the provider database to identify specialists in the relevant field.

4. The filtered providers are further narrowed down based on the user's location and preferred timings.

5. A weighted score is calculated for each remaining provider, taking into account their experience and user ratings.

6. The top providers with the highest weighted scores are recommended to the user, along with their relevant details (name, hospital, city, experience, and ratings).

7. The user can then make an informed decision and choose the most suitable healthcare provider based on the provided recommendations and their individual preferences.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Flask (Python-based web framework)
- **Machine Learning Libraries**: scikit-learn (Python)
- **Data Processing**: Pandas (Python)

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

- Thanks to the Google team for giving oppurtunity to work on in this impressive project.
- The disease and symptom data are sourced from online resource - Kaggle.
- Hospital data are sourced from Newsweek website
