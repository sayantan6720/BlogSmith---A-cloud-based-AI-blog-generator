import streamlit as st
import requests
import json
import time

# CSS for custom styling and fade-in animation
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .fade-in-text {
        font-size: 18px;
        font-weight: 400;
        color: #e5e5e5;
        background-color: #262730;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        animation: fadeIn ease 1.5s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    }
    .blog-title {
        font-size: 24px;
        font-weight: bold;
        color: #F39C12;
        margin-top: 10px;
    }
    .title {
        font-size: 24px;
        color: #F39C12;
        text-align: center;
        margin-bottom: 30px;
    }
    .generate-btn {
        background-color: #E74C3C;
        color: white;
        font-size: 16px;
        padding: 8px 20px;
        border-radius: 5px;
        margin-top: 10px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to simulate "fade-in effect" and format the title
def fade_in_effect_with_title(text):
    placeholder = st.empty()  # Create an empty placeholder to update the content

    # Split the content into title and body (assuming title is in the first line)
    title, body = text.split('\n', 1) if '\n' in text else (text, '')

    # Format the title and body
    title_html = f"<div class='blog-title'>{title}</div>"
    body_html = f"<div class='fade-in-text'>{body}</div>"

    # Display the formatted title and body
    placeholder.markdown(title_html + body_html, unsafe_allow_html=True)

# Set the title of the page with a styled header
st.markdown("<h1 class='title'>Generate a Blog</h1>", unsafe_allow_html=True)

# Create an input field for the blog topic
blog_topic = st.text_input("Enter a blog topic:")

# API URL (replace with your actual API Gateway URL for invoking the Lambda function)
api_url = "https://qrse1i29dj.execute-api.us-east-1.amazonaws.com/dev/blog-generation"

# Create a button to generate the blog
if st.button("Generate"):
    if blog_topic:
        # Show loading spinner
        with st.spinner('Generating your blog...'):
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
                    
                    # Display the success message
                    st.success("Blog generated successfully!")
                    
                    # Display the blog content with a fade-in effect and proper title formatting
                    fade_in_effect_with_title(response_data['blog_content'])
                    
                else:
                    st.error(f"Error: {response.status_code}")
                    st.write(f"Details: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a blog topic.")
