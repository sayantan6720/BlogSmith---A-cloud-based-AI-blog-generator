# BlogSmith: A Cloud-based AI Blog Generator

**BlogSmith** is a cloud-based blog generation tool that leverages AI to automatically generate blog content based on a given topic. This project utilizes **AWS Bedrock** and **Streamlit** to generate and display blogs, with the option to save them in an S3 bucket.

## Features

- Generate blog content using the **LLaMA 3 70B** model from **AWS Bedrock**.
- Save generated blog content directly to an **S3 bucket**.
- User-friendly interface built using **Streamlit**.
- Real-time blog generation triggered through a **Lambda** function.
- Simple and clean UI to enter blog topics and view generated content.

## Project Structure

### 1. `app.py`
This file handles the backend blog generation using AWS Bedrock and the storage of the generated blog in an S3 bucket.
- **Key Functions:**
  - `blog_generation_using_bedrock`: Generates blog content based on a given topic using the Bedrock LLaMA model.
  - `save_blog_in_s3`: Saves the generated blog in a specified S3 bucket.
  - `lambda_handler`: Handles the Lambda function invocation, receives a blog topic, and stores the generated blog in S3.

### 2. `UI.py`
This file defines the initial user interface for generating blogs using **Streamlit**.
- The user can input a blog topic, and upon clicking "Generate," the system triggers the blog generation and displays the content.

## How It Works

1. **User Input**: The user provides a blog topic through the UI.
2. **AI Blog Generation**: The backend, powered by AWS Bedrock's LLaMA model, generates the blog.
3. **Save to S3**: The generated blog is stored in an AWS S3 bucket.
4. **Display Blog**: The blog content is displayed in the UI with formatting and animations.

