import streamlit as st
import pandas as pd

@st.cache_data 
def load_data():
    return pd.read_excel('final_scores_file_forUse.xlsx')

data = load_data()  

@st.cache_data  
def recommend_restaurant(location, parameter):
    filtered_data = data[data['Location'] == location]
    top_3_restaurants = filtered_data.nlargest(3, 'Sentiment_Score')['Restaurant Name'].values
    if parameter == 'Cuisine':
        return top_3_restaurants[0]
    elif parameter == 'Price Range':
        return top_3_restaurants[1]
    elif parameter == 'Rating':
        return top_3_restaurants[2]

def main_app():
    st.title('Restaurant Recommendation System')

    if 'location' not in st.session_state:
        st.session_state['location'] = 'Banashankari'  
        st.session_state['parameter'] = 'Cuisine'  

    location = st.selectbox('Choose your location:', 
                            ['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar', 'Kumaraswamy Layout', 
                             'Rajarajeshwari Nagar', 'Vijay Nagar', 'Uttarahalli', 'JP Nagar', 'South Bangalore', 
                             'City Market', 'Bannerghatta Road', 'BTM', 'Kanakapura Road', 'Bommanahalli', 
                             'Marathahalli', 'Electronic City', 'Wilson Garden', 'Shanti Nagar', 'Richmond Road', 
                             'Koramangala 5th Block', 'HSR', 'Koramangala 7th Block', 'Bellandur', 'Sarjapur Road', 
                             'Whitefield', 'East Bangalore', 'Old Airport Road', 'Indiranagar', 'Koramangala 1st Block', 
                             'Frazer Town', 'MG Road', 'Brigade Road', 'Lavelle Road', 'Church Street', 'Ulsoor', 
                             'Residency Road', 'Shivajinagar', 'Infantry Road', 'St. Marks Road', 'Cunningham Road', 
                             'Race Course Road', 'Commercial Street', 'Vasanth Nagar', 'Domlur', 'Ejipura', 
                             'Jeevan Bhima Nagar', 'Old Madras Road', 'Koramangala 8th Block', 'Seshadripuram', 
                             'Kammanahalli', 'Koramangala 6th Block', 'Majestic', 'Langford Town', 'Central Bangalore', 
                             'Sanjay Nagar', 'Brookefield', 'Varthur Main Road, Whitefield', 'ITPL Main Road, Whitefield', 
                             'KR Puram', 'Koramangala 2nd Block', 'Koramangala 3rd Block', 'Koramangala 4th Block', 
                             'Hosur Road', 'Koramangala', 'RT Nagar', 'Banaswadi', 'Hennur', 'Nagawara', 'Kalyan Nagar', 
                             'HBR Layout', 'Thippasandra', 'CV Raman Nagar', 'Kaggadasapura', 'New BEL Road', 'Hebbal', 
                             'Kengeri', 'Rammurthy Nagar', 'North Bangalore', 'Sankey Road', 'Malleshwaram', 
                             'Sadashiv Nagar', 'Rajajinagar', 'Yeshwantpur', 'Basaveshwara Nagar', 'Yelahanka', 'West Bangalore'], 
                            index=['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar', 'Kumaraswamy Layout', 
                             'Rajarajeshwari Nagar', 'Vijay Nagar', 'Uttarahalli', 'JP Nagar', 'South Bangalore', 
                             'City Market', 'Bannerghatta Road', 'BTM', 'Kanakapura Road', 'Bommanahalli', 
                             'Marathahalli', 'Electronic City', 'Wilson Garden', 'Shanti Nagar', 'Richmond Road', 
                             'Koramangala 5th Block', 'HSR', 'Koramangala 7th Block', 'Bellandur', 'Sarjapur Road', 
                             'Whitefield', 'East Bangalore', 'Old Airport Road', 'Indiranagar', 'Koramangala 1st Block', 
                             'Frazer Town', 'MG Road', 'Brigade Road', 'Lavelle Road', 'Church Street', 'Ulsoor', 
                             'Residency Road', 'Shivajinagar', 'Infantry Road', 'St. Marks Road', 'Cunningham Road', 
                             'Race Course Road', 'Commercial Street', 'Vasanth Nagar', 'Domlur', 'Ejipura', 
                             'Jeevan Bhima Nagar', 'Old Madras Road', 'Koramangala 8th Block', 'Seshadripuram', 
                             'Kammanahalli', 'Koramangala 6th Block', 'Majestic', 'Langford Town', 'Central Bangalore', 
                             'Sanjay Nagar', 'Brookefield', 'Varthur Main Road, Whitefield', 'ITPL Main Road, Whitefield', 
                             'KR Puram', 'Koramangala 2nd Block', 'Koramangala 3rd Block', 'Koramangala 4th Block', 
                             'Hosur Road', 'Koramangala', 'RT Nagar', 'Banaswadi', 'Hennur', 'Nagawara', 'Kalyan Nagar', 
                             'HBR Layout', 'Thippasandra', 'CV Raman Nagar', 'Kaggadasapura', 'New BEL Road', 'Hebbal', 
                             'Kengeri', 'Rammurthy Nagar', 'North Bangalore', 'Sankey Road', 'Malleshwaram', 
                             'Sadashiv Nagar', 'Rajajinagar', 'Yeshwantpur', 'Basaveshwara Nagar', 'Yelahanka', 'West Bangalore'].index(st.session_state['location']))

    parameter = st.selectbox('Choose your preference:', ['Cuisine', 'Price Range', 'Rating'])

    if st.button('Recommend'):
        st.session_state['location'] = location
        st.session_state['parameter'] = parameter

        recommendation = recommend_restaurant(st.session_state['location'], st.session_state['parameter'])
        st.write(f"We recommend you order from {recommendation} for a delicious meal. Considering your preference as {st.session_state['parameter']}.")

main_app()
