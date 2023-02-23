import requests
import json
import streamlit as st
import random

# Set the title of the browser tab
st.set_page_config(page_title="Website Performance Analyzer :horse_racing:")

quotes = [
    "I cannot wait to win this match, friend!",
    "The championship is ours!",
    "Time to win, and stay alive!",
    "Good luck. Have fun. Don't die!",
    "I accept the challenge!",
    "Let's have fun, friend!",
    "This is going to be fun.",
    "We will defeat all of our enemies!",
    "Ready to go.",
    "Powered up and ready to go.",
    "I am ready. I hope you are too!",
    "This is my favorite part!",
    "Ready and excited.",
    "I was created for this! ..I think.",
    "I think we're going to do great, friend!",
    "Excellent. Time to destroy more opponents.",
    "You and me, friend!",
    "Come on friend, time to win!",
    "Grapple: locked and loaded.",
    "I just polished my grapple.",
    "A match a day keeps the doctor away! Just kidding, I'm made of metal.",
    "Let's make some new friends, and then destroy them.",
    "Today smells like victory! I love pretending to smell. Sniff sniff!"
    ]

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
    results = analyze(url)
    st.write('---')
    st.subheader('Website Performance Metrics:')
    for key, value in results.items():
        st.write(f'{key}: {value}')
    st.write('---')
    st.text(random.choice(quotes))
else:
    # If the URL is not provided, don't display any results
    #st.write('Enter a URL to analyze website performance')
    pass
