import streamlit as st
import pandas as pd
from extract_json import get_user_info_from_json

# Load the data
data = pd.read_excel('final_scores_file_forUse.xlsx')  

# Define a function for restaurant recommendation
def recommend_restaurant(location, parameter):
    filtered_data = data[data['Location'] == location]
    recommended_restaurant = filtered_data.nlargest(1, 'Sentiment_Score')['Restaurant Name'].values[0]
    return recommended_restaurant

# Create a function for the login page
def login():
    st.title('Login')

    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        user = get_user_info_from_json(email)
        if user and user['password'] == password:
            st.session_state['logged_in'] = True
            st.session_state['user'] = user
            st.experimental_rerun()
        else:
            st.error('Invalid email or password')

# Main application
def main_app():
    st.title('Restaurant Recommendation System')

    name = st.session_state['user']['name']
    email = st.session_state['user']['email']

    location = st.selectbox('Choose your location:', ['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar',
           'Kumaraswamy Layout', 'Rajarajeshwari Nagar', 'Vijay Nagar',
           'Uttarahalli', 'JP Nagar', 'South Bangalore', 'City Market',
           'Bannerghatta Road', 'BTM', 'Kanakapura Road', 'Bommanahalli',
           'Marathahalli', 'Electronic City', 'Wilson Garden', 'Shanti Nagar',
           'Richmond Road', 'Koramangala 5th Block', 'HSR',
           'Koramangala 7th Block', 'Bellandur', 'Sarjapur Road',
           'Whitefield', 'East Bangalore', 'Old Airport Road', 'Indiranagar',
           'Koramangala 1st Block', 'Frazer Town', 'MG Road', 'Brigade Road',
           'Lavelle Road', 'Church Street', 'Ulsoor', 'Residency Road',
           'Shivajinagar', 'Infantry Road', 'St. Marks Road',
           'Cunningham Road', 'Race Course Road', 'Commercial Street',
           'Vasanth Nagar', 'Domlur', 'Ejipura', 'Jeevan Bhima Nagar',
           'Old Madras Road', 'Koramangala 8th Block', 'Seshadripuram',
           'Kammanahalli', 'Koramangala 6th Block', 'Majestic',
           'Langford Town', 'Central Bangalore', 'Sanjay Nagar',
           'Brookefield', 'Varthur Main Road, Whitefield',
           'ITPL Main Road, Whitefield', 'KR Puram', 'Koramangala 2nd Block',
           'Koramangala 3rd Block', 'Koramangala 4th Block', 'Hosur Road',
           'Koramangala', 'RT Nagar', 'Banaswadi', 'Hennur', 'Nagawara',
           'Kalyan Nagar', 'HBR Layout', 'Thippasandra', 'CV Raman Nagar',
           'Kaggadasapura', 'New BEL Road', 'Hebbal', 'Kengeri',
           'Rammurthy Nagar', 'North Bangalore', 'Sankey Road',
           'Malleshwaram', 'Sadashiv Nagar', 'Rajajinagar', 'Yeshwantpur',
           'Basaveshwara Nagar', 'Yelahanka', 'West Bangalore'])
    parameter = st.selectbox('Choose your preference:', ['Cuisine', 'Price Range', 'Rating'])

    if st.button('Recommend'):
        recommendation = recommend_restaurant(location, parameter)
        st.write(f"Hi {name}, We recommend you order from {recommendation} for a delicious meal.")

# Check login state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user'] = None

if not st.session_state['logged_in']:
    login()
else:
    main_app()