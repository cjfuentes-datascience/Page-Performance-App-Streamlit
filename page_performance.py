import requests
import json
import streamlit as st


def analyze(url):
    # Set up the API request URL
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=mobile".format(url)

    # Send the API request and get the response as JSON data
    response = requests.get(api_url)
    data = json.loads(response.text)

    # Extract relevant performance metrics from the JSON data
    lighthouse_data = data['lighthouseResult']['audits']

    # Return the performance metrics
    return {
        "First Contentful Paint": lighthouse_data['first-contentful-paint']['displayValue'],
        "Speed Index": lighthouse_data['speed-index']['displayValue'],
        "Total Blocking Time": lighthouse_data['total-blocking-time']['displayValue']
    }


st.title("Website Performance Analyzer")

url = st.text_input('Enter the URL of the website to analyze:')

if url:
    results = analyze(url)
    st.subheader('Website Performance Metrics:')
    for key, value in results.items():
        st.write(f'{key}: {value}')
else:
    #st.write('Enter a URL to analyze website performance')
    pass