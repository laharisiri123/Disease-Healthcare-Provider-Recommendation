
# In[108]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
from collections import Counter


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS with * for all origins
# In[109]:


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS with * for all origins


# In[110]:

pd.set_option('display.max_colwidth', None)

# In[111]:

dis_sym_data = pd.read_csv("datasets/Disease_symptoms.csv")

# **Finding unique values across all the symptoms column**

# In[114]:

columns_to_check = []
for col in dis_sym_data.columns:
    if col != 'Disease':
        columns_to_check.append(col)

# In[115]:
symptoms = dis_sym_data.iloc[:, 1:].values.flatten()
symptoms = list(set(symptoms))


# **Convert Symptoms to Binary Columns**

# In[116]:

for symptom in symptoms:
    dis_sym_data[symptom] = dis_sym_data.iloc[:, 1:].apply(lambda row: int(symptom in row.values), axis=1)

dis_sym_data_v1 = dis_sym_data.drop(columns=columns_to_check)

# In[117]:

dis_sym_data_v1 = dis_sym_data_v1.loc[:, dis_sym_data_v1.columns.notna()]

# In[119]:

dis_sym_data_v1.columns = dis_sym_data_v1.columns.str.strip()

# In[120]:

symptom_names = dis_sym_data_v1.columns[1:].tolist()

# Printing the array of symptom names
# print(symptom_names)

# **Training Models to predict disease**

# In[121]:

var_mod = ['Disease']
le = LabelEncoder()
for i in var_mod:
    dis_sym_data_v1[i] = le.fit_transform(dis_sym_data_v1[i])


# In[122]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Split data into train and test, keeping 2 rows per disease in test set
test_data = pd.DataFrame(columns=dis_sym_data_v1.columns)
train_data = pd.DataFrame(columns=dis_sym_data_v1.columns)

for disease in dis_sym_data_v1['Disease'].unique():
    disease_data = dis_sym_data_v1[dis_sym_data_v1['Disease'] == disease]
    test_part = disease_data.sample(n=2, random_state=42)
    train_part = disease_data.drop(test_part.index)
    test_data = pd.concat([test_data, test_part], ignore_index=True)
    train_data = pd.concat([train_data, train_part], ignore_index=True)

# Separate features and target
X_train = train_data.drop(columns="Disease")
y_train = train_data['Disease']
X_test = test_data.drop(columns="Disease")
y_test = test_data['Disease']

# Convert target variable to categorical
y_train = y_train.astype('category')
y_test = y_test.astype('category')


# **Model Generation**

# In[123]:


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_and_evaluate_models(model,X_train, X_test, y_train, y_test):
    results = {}
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    results[model_name] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
    
    print(f"{model_name} Results:")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1-Score: {f1:.3f}")
    print()
    
    return results

# In[124]:

algorithms = {'Logistic Regression': 
              {"model": LogisticRegression()},
              
              'Decision Tree': 
              {"model": tree.DecisionTreeClassifier()},
              
              'Random Forest': 
              {"model": RandomForestClassifier()},
              
              'SVM':
              {"model": svm.SVC(probability=True)},
              
              'NaiveBayes' :
              {"model": GaussianNB()},
              
              'K-Nearest Neighbors' :
              {"model": KNeighborsClassifier()},
             }

# In[125]:

for model_name, values in algorithms.items():
    train_and_evaluate_models(values["model"],X_train, X_test, y_train, y_test)

# **Map Description and Specialist for the Disease Predicted**

# In[126]:

doc_data = pd.read_csv("datasets/Disease_Specialist.csv",encoding='latin1', names=['Disease','Specialist'])

# In[128]:
specialist_names = doc_data['Specialist'].unique()

# In[130]:

des_data = pd.read_csv("datasets/Disease_Description.csv")

# **Test with Unknown Data**

# In[132]:
test_col = []
for col in dis_sym_data_v1.columns:
    if col != 'Disease':
        test_col.append(col)

test_data = {}
symptoms = []
predicted = []

def test_input(input_symptoms):
    symptoms.clear()
    predicted.clear()

    for symptom in input_symptoms:
        symptoms.append(symptom)

    # print("Symptoms you have:", symptoms)

    for column in test_col:
        test_data[column] = 1 if column in symptoms else 0

    test_df = pd.DataFrame(test_data, index=[0])
    print("Predicting Disease based on 6 ML algorithms...")

    for model_name, values in algorithms.items():
        predict_disease = values["model"].predict(test_df)
        predict_disease = le.inverse_transform(predict_disease)
        predicted.extend(predict_disease)

    disease_counts = Counter(predicted)
    percentage_per_disease = {disease: (count / 6) * 100 for disease, count in disease_counts.items()}
    result_df = pd.DataFrame({"Disease": list(percentage_per_disease.keys()),
                               "Chances": list(percentage_per_disease.values())})
    result_df = result_df.merge(doc_data, on='Disease', how='left')
    result_df = result_df.merge(des_data, on='Disease', how='left')

    # Display top 3 diseases with highest chances
    top_3_results = result_df.sort_values(by='Chances', ascending=False).head(3)

    return top_3_results


# In[134]:
# Create a DataFrame from the list of providers
providers_df = pd.read_csv("datasets/providers.csv")

# Create a DataFrame from the list of user ratings
user_ratings_df = pd.read_csv("datasets/user_ratings.csv")

# Algorithm for Recommending doctors
import ast  # Import the ast module to convert string to dictionary

def recommend_providers(specialist, providers_df, user_ratings_df, selected_cities=None, selected_timings=None, experience_weight=0.6, rating_weight=0.4):
    # Filter providers by specialist type
    specialist_providers = providers_df[providers_df['specialist'] == specialist]

    # Filter by selected cities
    if selected_cities:
        specialist_providers = specialist_providers[specialist_providers['city'].isin(selected_cities)]

    # Filter by selected timings
    if selected_timings:
        # Convert the 'timings' column from string to dictionary
        specialist_providers['timings'] = specialist_providers['timings'].apply(ast.literal_eval)

        # Filter by selected timings
        specialist_providers = specialist_providers[specialist_providers['timings'].apply(lambda x: any(timing in selected_timings for timing in x.keys()))]

    # Merge with user ratings data
    specialist_providers = specialist_providers.merge(user_ratings_df.groupby('name')['rating'].mean().reset_index(), how='left', on='name')

    # Fill NaN ratings with the mean rating
    specialist_providers['rating'] = specialist_providers['rating'].fillna(specialist_providers['rating'].mean())

    # Round ratings to 1 decimal place
    specialist_providers['rating'] = specialist_providers['rating'].round(1)

    # Calculate experience and rating norms, handling NaN values
    specialist_providers['experience_norm'] = specialist_providers['experience'].rank(method='dense', ascending=True) / len(specialist_providers)
    specialist_providers['rating_norm'] = specialist_providers['rating'].rank(method='dense', ascending=True) / len(specialist_providers)

    # Calculate weighted score
    specialist_providers['weighted_score'] = (experience_weight * specialist_providers['experience_norm']) + (rating_weight * specialist_providers['rating_norm'])

    # Sort by weighted score (descending)
    sorted_providers = specialist_providers.sort_values(by=['weighted_score'], ascending=False)

    # Select top 5 providers
    top_providers = sorted_providers.head(5)

    return top_providers

# In[140]:

def get_symptom_and_city_data():
    symptoms = [{'value': symptom, 'label': symptom.replace('_', ' ').title()} for symptom in symptom_names]
    cities = [{'value': city, 'label': city} for city in providers_df['city'].unique()]
    return {'symptoms': symptoms, 'cities': cities}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symptoms = data['symptoms']
    city = data['city']
    timings = data['timings']

    # Call the test_input function directly after importing the notebook
    top_results = test_input(symptoms)

    # Convert the top results and top doctors to a list of dictionaries
    result_dicts = []
    for _, row in top_results.iterrows():
        disease = row['Disease']
        chances = row['Chances']
        specialist = row['Specialist']
        description = row['Description']

        # Assuming you have defined the recommend_providers function in the notebook
        top_doctors = recommend_providers(specialist, providers_df, user_ratings_df, city, timings)

        doctors = [
            {
                'name': doc['name'],
                'hospital': doc['hospital'],
                'city': doc['city'],
                'experience': doc['experience'],
                'rating': doc['rating']
            }
            for _, doc in top_doctors.iterrows()
        ]

        result_dicts.append({
            'Disease': disease,
            'Chances': chances,
            'Specialist': specialist,
            'Description': description,
            'Doctors': doctors[:5]  # Take only the top 5 doctors
        })

    return jsonify(result_dicts)

@app.route('/data', methods=['GET'])
def get_data():
    data = get_symptom_and_city_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
