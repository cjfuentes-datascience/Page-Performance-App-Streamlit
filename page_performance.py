import requests
import json
import streamlit as st

# Set the title of the browser tab
st.set_page_config(page_title="Website Performance Analyzer :horse_racing:")

# Define a function to analyze the website performance
def analyze(url):
    # Set up the API request URL using the provided website URL
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=mobile".format(url)

    # Send the API request to the Google PageSpeed API and get the response as JSON data
    response = requests.get(api_url)
    data = json.loads(response.text)

    # Extract relevant performance metrics from the JSON data received from the API
    lighthouse_data = data['lighthouseResult']['audits']

    # Return the performance metrics as a dictionary
    return {
        "First Contentful Paint": lighthouse_data['first-contentful-paint']['displayValue'],
        "Speed Index": lighthouse_data['speed-index']['displayValue'],
        "Time to Interactive": lighthouse_data['interactive']['displayValue'],
        "Largest Contentful Paint": lighthouse_data['largest-contentful-paint']['displayValue'],
        "Cumulative Layout Shift": lighthouse_data['cumulative-layout-shift']['displayValue'],
        "Total Blocking Time": lighthouse_data['total-blocking-time']['displayValue']
        #"First Input Delay": lighthouse_data['first-input-delay']['displayValue']
    }

# Set the title for the Streamlit web app
st.title("Website Performance Analyzer :horse_racing:")

# Get the URL of the website to analyze from the user
url = st.text_input('Enter the URL of the website to analyze:')
#st.write('---')

# If the URL is provided, analyze the website performance and display the results
if url:
    st.write('---')
    results = analyze(url)
    st.subheader('Website Performance Metrics:')
    for key, value in results.items():
        st.write(f'{key}: {value}')
    st.write('---')

else:
    # If the URL is not provided, don't display any results
    #st.write('Enter a URL to analyze website performance')
    pass

st.text("That's all folks!")
