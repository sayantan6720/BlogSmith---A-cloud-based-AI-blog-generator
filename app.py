import boto3
import botocore.config
import json
from datetime import datetime

def blog_generation_using_bedrock(blogtopic:str)->str:
    prompt = f"""<s>[INST]Human: Write a 200 word blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9,
    }

    try:
        # Create a client to the Bedrock runtime
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1", 
                               config=botocore.config.Config(read_timeout=300, retries={"max_attempts": 3}))
        
        # Invoke the model
        response = bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama3-70b-instruct-v1:0")
        #Reading the response
        response_content = response.get('body').read()
        #Deserializing the JSON response to python dictionary
        response_data = json.loads(response_content)
        print(response_data)
        #Extracting the blog from the response
        blog_details = response_data['generation']

    
    except Exception as e:
        print(f"Error in generating the blog:{e}")
        return ""
    
    
def save_blog_in_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client("s3")
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print(f"Blog saved successfully to S3 bucket")
    except Exception as e:
        print(f"Error in saving the blog in S3")
        


def lambda_handler(event, context):
    event = json.loads(event['body'])
    blogtopic = event['blog_topic']

    generate_blog = blog_generation_using_bedrock(blogtopic)

    if generate_blog:
        #Creating a S3 bucket and a folder to store the blog
        current_time = datetime.now().strftime("%H:%M:%S")
        s3_key = f"{blogtopic}/{current_time}.txt"
        s3_bucket = "blog-output-bucket-bedrock"
        save_blog_in_s3(s3_key, s3_bucket, generate_blog)

        return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Blog generated and saved successfully!',
            'blog_content': generate_blog,  # Return the blog content
            's3_key': s3_key
        })
    }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Error in generating the blog')
        }
    
    
