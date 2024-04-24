import pandas as pd
import numpy as np
import random
import string
from faker import Faker

fake = Faker()

# Specialist types
doc_data = pd.read_csv("datasets/Disease_Specialist.csv", encoding='latin1', names=['Disease', 'Specialist'])
specialities = doc_data['Specialist'].unique()

# Hospitals
# Hospitals
hospitals = [
    {"name": "All India Institute of Medical Sciences - Delhi", "city": "New Delhi"},
    {"name": "Medanta The Medicity", "city": "Gurugram"},
    {"name": "Apollo Hospital - Chennai", "city": "Chennai"},
    {"name": "The Christian Medical College", "city": "Vellore"},
    {"name": "PGIMER - Postgraduate Institute of Medical Education and Research", "city": "Chandigarh"},
    {"name": "P. D. Hinduja National Hospital & Medical Research Centre", "city": "Mumbai"},
    {"name": "Breach Candy Hospital", "city": "Mumbai"},
    {"name": "Kokilaben Dhirubhai Ambani Hospital & Medical Research Institute", "city": "Mumbai"},
    {"name": "Sir Ganga Ram Hospital", "city": "New Delhi"},
    {"name": "Indraprastha Apollo Hospital", "city": "New Delhi"},
    {"name": "Apollo Hospital - Secunderabad", "city": "Secunderabad"},
    {"name": "Max Super Speciality Hospital, Saket", "city": "New Delhi"},
    {"name": "Jawaharlal Institute of Postgraduate Medical Education and Research", "city": "Puducherry"},
    {"name": "Apollo Hospitals - Belapur", "city": "Navi Mumbai"},
    {"name": "Fortis Flt. Lt. Rajan Dhall Hospital", "city": "New Delhi"},
    {"name": "Manipal Hospital Old Airport Road", "city": "Bengaluru"},
    {"name": "King Edward Memorial Hospital", "city": "Mumbai"},
    {"name": "Apollo Hospitals - Bannerghatta Road", "city": "Bengaluru"},
    {"name": "Jaslok Hospital and Research Centre", "city": "Mumbai"},
    {"name": "Bombay Hospital & Medical Research Centre", "city": "Mumbai"},
    {"name": "Safdarjung Hospital", "city": "New Delhi"},
    {"name": "Fortis Memorial Research Institute", "city": "Gurugram"},
    {"name": "Fortis Hospital Mulund", "city": "Mumbai"},
    {"name": "Care Institute Of Medical Science", "city": "Ahmedabad"},
    {"name": "Saifee Hospital", "city": "Mumbai"},
    {"name": "Lilavati Hospital And Research Centre", "city": "Mumbai"},
    {"name": "Aster CMI Hospital", "city": "Bengaluru"},
    {"name": "Nanavati Max Super Speciality Hospital", "city": "Mumbai"},
    {"name": "BGS Gleneagles Global Hospitals", "city": "Bengaluru"},
    {"name": "Kauvery Hospital", "city": "Chennai"},
    {"name": "All India Institute of Medical Sciences - Raipur", "city": "Raipur"},
    {"name": "Apollomedics Super Speciality Hospital", "city": "Lucknow"},
    {"name": "Yashoda Hospitals - Somajiguda", "city": "Hyderabad"},
    {"name": "Gleneagles Global Hospitals", "city": "Hyderabad"},
    {"name": "AMRI Hospital - Salt Lake", "city": "Kolkata"},
    {"name": "Fortis Hiranandani Hospital", "city": "Navi Mumbai"},
    {"name": "Madras Medical Mission Hospital", "city": "Chennai"},
    {"name": "Dr. L H Hiranandani Hospital", "city": "Mumbai"},
    {"name": "Global Hospitals", "city": "Mumbai"},
    {"name": "Fortis Hospital Nagarbhavi", "city": "Bengaluru"},
    {"name": "Ruby Hall Clinic, Sassoon Road", "city": "Pune"},
    {"name": "Aster Medcity", "city": "Kochi"},
    {"name": "Ruby General Hospital", "city": "Kolkata"},
    {"name": "Apollo Hospital - Jubilee Hills", "city": "Hyderabad"},
    {"name": "Lok Nayak Hospital", "city": "Delhi"},
    {"name": "CARE Hospitals - Banjara Hills", "city": "Hyderabad"},
    {"name": "Fortis Malar Hospital", "city": "Chennai"},
    {"name": "Dr. Ram Manohar Lohia Hospital", "city": "New Delhi"},
    {"name": "Apollo Hospitals - Ahmedabad", "city": "Ahmedabad"},
    {"name": "Apollo Specialty Hospitals - Vanagaram", "city": "Chennai"},
    {"name": "Gleneagles Global Health City", "city": "Chennai"},
    {"name": "Institute of Post Graduate Medical Education and Research", "city": "Kolkata"},
    {"name": "Yashoda Hospital - Secunderabad", "city": "Secunderabad"},
    {"name": "MGM Healthcare", "city": "Chennai"},
    {"name": "Sri Ramachandra Medical Centre", "city": "Chennai"},
    {"name": "Sir H. N. Reliance Foundation Hospital and Research Centre", "city": "Mumbai"},
    {"name": "Artemis Hospital Gurgaon", "city": "Gurugram"},
    {"name": "Ramaiah Memorial Hospital", "city": "Bengaluru"},
    {"name": "Sterling Hospital Ahmedabad", "city": "Ahmedabad"},
    {"name": "All India Institute of Medical Sciences - Rishikesh", "city": "Rishikesh"},
    {"name": "SMS Hospital", "city": "Jaipur"},
    {"name": "SIMS Hospital", "city": "Chennai"},
    {"name": "Kohinoor Hospital", "city": "Mumbai"},
    {"name": "Sunshine Hospitals", "city": "Secunderabad"},
    {"name": "Dr. Mehta's Hospitals", "city": "Chennai"},
    {"name": "Ahmedabad Institute of Medical Services", "city": "Ahmedabad"},
    {"name": "Manipal Hospital Whitefield", "city": "Bengaluru"},
    {"name": "Continental Hospitals", "city": "Hyderabad"},
    {"name": "Amrita Hospital, Kochi", "city": "Kochi"},
    {"name": "BLK - Max Super Specialty Hospital", "city": "New Delhi"},
    {"name": "CritiCare Asia Hospitals & Research Center", "city": "Mumbai"},
    {"name": "All India Institute of Medical Sciences - Patna", "city": "Patna"},
    {"name": "P.D. Hinduja Hospital and Medical Research Centre, Khar Facility", "city": "Mumbai"},
    {"name": "A.A.Rahim Memorial District Hospital Kollam", "city": "Kollam"},
    {"name": "Yashoda Hospital - Malakpet", "city": "Hyderabad"},
    {"name": "Christian Medical College and Hospital (CMC)", "city": "Ludhiana"},
    {"name": "Rabindranath Tagore International Institute Of Cardiac Sciences", "city": "Kolkata"},
    {"name": "MGM New Bombay Hospital", "city": "Navi Mumbai"},
    {"name": "HOSMAT Multi Speciality Hospital", "city": "Bengaluru"},
    {"name": "All India Institute of Medical Sciences - Bhubaneswar", "city": "Bhubaneswar"},
    {"name": "Prince Aly Khan Hospital", "city": "Mumbai"},
    {"name": "Apollo Gleneagles Hospitals", "city": "Kolkata"},
    {"name": "MIOT International", "city": "Chennai"},
    {"name": "Aakash Hospital", "city": "Chennai"},
    {"name": "Meitra Hospital, Calicut", "city": "Kozhikode"},
    {"name": "Anugrah Narayan Magadh Medical College & Hospital", "city": "Gaya"},
    {"name": "Mazumdar Shaw Medical Center", "city": "Bengaluru"},
    {"name": "Billroth Hospitals", "city": "Chennai"},
    {"name": "Sanjay Gandhi Postgraduate Institute of Medical Sciences", "city": "Lucknow"},
    {"name": "KIMS Hospital", "city": "Secunderabad"},
    {"name": "Aster MIMS Hospital", "city": "Kozhikode"},
    {"name": "KMC Hospital", "city": "Mangaluru"},
    {"name": "St. John's Medical College Hospital", "city": "Bengaluru"},
    {"name": "American Oncology Institute, Nallagandla", "city": "Hyderabad"},
    {"name": "Asian Institute Of Gastroenterology", "city": "Hyderabad"},
    {"name": "Fortis Escorts Heart Institute", "city": "New Delhi"},
    {"name": "Narayana Institute of Cardiac Sciences", "city": "Bengaluru"},
    {"name": "Rainbow Children’s Hospital & BirthRight, Marathahalli", "city": "Bengaluru"},
    {"name": "Ramaiah Narayana Heart Centre", "city": "Bengaluru"},
    {"name": "Tata Memorial Hospital", "city": "Mumbai"}
]

# Generate healthcare providers data
providers = []
for i in range(500):
    name = fake.name()
    specialist = random.choice(specialities)
    hospital = random.choice(hospitals)
    experience = random.randint(5, 25)
    days = random.sample(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], random.randint(3, 7))
    timings = {day: f"{random.randint(8, 10)}:00 AM - {random.randint(4, 8)}:00 PM" for day in days}
    providers.append({
        'name': name,
        'specialist': specialist,
        'hospital': hospital['name'],
        'city': hospital['city'],
        'experience': experience,
        'timings': str(timings)
    })

# Create a DataFrame from the list of providers
providers_df = pd.DataFrame(providers)

# Save the DataFrame to a CSV file
providers_df.to_csv('datasets/providers.csv', index=False)