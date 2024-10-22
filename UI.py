import streamlit as st
import requests
import json

# Set the title of the page
st.title("Generate a Blog")

# Create an input field for the blog topic
blog_topic = st.text_input("Enter a blog topic:")

# API URL (replace with your actual API Gateway URL for invoking the Lambda function)
api_url = "https://qrse1i29dj.execute-api.us-east-1.amazonaws.com/dev/blog-generation"  # Replace with your actual API Gateway URL

# Create a button to generate the blog
if st.button("Generate"):
    if blog_topic:
        # Prepare the payload to send to the Lambda function
        payload = {
            "blog_topic": blog_topic
        }
        
        # Set up the headers (optional, but "Content-Type" is usually required)
        headers = {
            "Content-Type": "application/json"
        }

        try:
            # Make the POST request to the API Gateway (which invokes the Lambda)
            response = requests.post(api_url, data=json.dumps(payload), headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                response_data = response.json()  # Parse the JSON response
                
                # Display the success message and the generated blog
                st.write("Blog generated successfully!")
                st.markdown(response_data['blog_content'], unsafe_allow_html=True)
                
            else:
                st.write(f"Error: {response.status_code}")
                st.write(f"Details: {response.text}")
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please enter a blog topic.")
