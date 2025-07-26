import boto3 # boto3 is the AWS SDK for Python
import json 
import os
from botocore.exceptions import ClientError
import requests 
import pandas as pd
import re #regular expression
import logging
from typing import List, Dict, Any, Tuple
from tqdm import tqdm #progress bar
import jsonschema


#Sources : https://archive.org/details/bhagavadgitaasitisoriginal1972edition
#https://archive.org/details/bhagavadgitaorig0000unse
#https://gitapress.org/bookdetail/gita-shankarbhashya-hindi-10

CHAPTER_INFO = {
    "chapters": [
        {"number": 1, "name": "Arjuna Visada Yoga", "total_shlokas": 47},
        {"number": 2, "name": "Sankhya Yoga", "total_shlokas": 72},
        {"number": 3, "name": "Karma Yoga", "total_shlokas": 43},
        {"number": 4, "name": "Jnana Yoga", "total_shlokas": 42},
        {"number": 5, "name": "Karma Sanyasa Yoga", "total_shlokas": 29},
        {"number": 6, "name": "Dhyana Yoga", "total_shlokas": 47},
        {"number": 7, "name": "Jnana Vijnana Yoga", "total_shlokas": 30},
        {"number": 8, "name": "Aksara Brahma Yoga", "total_shlokas": 28},
        {"number": 9, "name": "Raja Vidya Yoga", "total_shlokas": 34},
        {"number": 10, "name": "Vibhuti Yoga", "total_shlokas": 42},
        {"number": 11, "name": "Visvarupa Darsana Yoga", "total_shlokas": 55},
        {"number": 12, "name": "Bhakti Yoga", "total_shlokas": 20},
        {"number": 13, "name": "Ksetra Ksetrajna Vibhaga Yoga", "total_shlokas": 35},
        {"number": 14, "name": "Gunatraya Vibhaga Yoga", "total_shlokas": 27},
        {"number": 15, "name": "Purusottama Yoga", "total_shlokas": 20},
        {"number": 16, "name": "Daivasura Sampad Vibhaga Yoga", "total_shlokas": 24},
        {"number": 17, "name": "Sraddhatraya Vibhaga Yoga", "total_shlokas": 28},
        {"number": 18, "name": "Moksa Sanyasa Yoga", "total_shlokas": 78}
    ]
}



#AWS client
class AWSCient:
    def __init__(self, region_name='eu-west-1'):
        self.s3_client = boto3.client('s3', region_name=region_name)
        self.textract_client = boto3.client('textract', region_name=region_name)

    def list_s3_doccuments(self,bucet_name, prefix):
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']
                        if obj['Key'].endswith('.json') and not obj['Key'].endswith('/')]    
                return []
        except ClientError as e:
            print(f"Error accessing S3:{e}")
            return []  

    def get_object(self,bucket_name, file_key):
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=file_key)
            return response['Body'].read().decode('utf-8')
        except ClientError as e:
            print(f"Error getting object from S3: {e}")
            return None

    ##Claude API client to invoke the Claude model
class ClaudeAPI:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
    def invoke_claude_model(self,prompt):
        try:
            payload = {
                "model": "bedrock-2023-05-31",
                "max_tokens": 20000,
                "temperature": 0.1,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            } 

            header = {
                'Content-Type': 'application/json',
            }

            response = requests.post(self.api_endpoint, json=payload, headers=headers)

            if response.status_code == 200:
                claude_response = response.json()

                if 'content' in claude_response and isinstance(claude_response['content'],list):
                    return claude_response['content'][0]['text']
                elif 'completion' in claude_response:
                    return claude_response['completion']
                elif 'body' in claude_response:
                    body = json.loads(claude_response['body'])
                    if 'content' in body and isinstance(body['content'],list):
                        return body['content'][0]['text']
                    elif 'completion' in body:
                        return body['completion']
                    
                print(f"Unexpected response format: {response.text}")
                return None
            
        except Exception as e:
             print(f"Error invoking Claude model: {e}")
             return None
        
##Load the chapter information from the JSON file
with open('bhagvad_gita_meta_data.json', 'r') as f:
    chapter_info = json.load(f)

#Function to call the Claude API
def claude_call(system_content, user_content, temperature=0.1,max_tokens=300):
    prompt = f"System: {system_content}\nUser: {user_content}"
    claude_api = ClaudeAPI('https://URL') ## Replace actual url of api gateway
    response = claude_api.invoke_claude_model(prompt)
    return response.strip() if response else ""

##Function to generate a summary of a chapter..
def generate_chapter_summary(chapter_number, chapter_name):
    system_content = f"""You are an expert on the Bhagavad Gita. Provide a comprehensive analysis of Chapter {chapter_number}: {chapter_name} strictly in JSON format with the following structure and no other format:
    {{
        "summary": "Brief summary of the chapter",
        "main_theme": "The overarching theme of the chapter",
        "philosophical_aspects": ["List of key philosophical concepts addressed"],
        "life_problems_addressed": ["List of life problems or questions this chapter helps address"],
        "yoga_type": "The primary type of yoga (if any) discussed in this chapter (e.g., Bhakti Yoga, Karma Yoga, etc.)"
    }}"""
    user_content= f"Provide a comprehensive analysis of Chapter {chapter_number}: {chapter_name} of the Bhagavad Gita as specified."

    response = claude_call(system_content, user_content, temperature=0.7, max_tokens=500)

response = response.strip('`')
if response.startswith('json'):
    response = response[4:].strip()

try:
    return json.loads(response)
except json.JSONDecodeError as e:
    print(f"Error parsing JSOn for chapter {chapter_number} summary: {e}")
    print("Raw response:", response)
    #Return a default structure in case of error
    return {
            "summary": "Error generating summary",
            "main_theme": "Error generating main theme",
            "philosophical_aspects": ["Error generating philosophical aspects"],
            "life_problems_addressed": ["Error generating life problems addressed"],
            "yoga_type": "Error generating yoga type"
    }

#Function to check if chapter is complete based on the number of shlokas
def is_chapter_complete(shloka_count):
    system_content = "You are an expert on the Bhagavad Gita. Determine if the given number of shlokas completes Chapter 1."
    user_content = f"Does {shloka_count} shlokas complete Chapter 1 of the Bhagavad Gita? Respond with only 'Yes' or 'No'."
    response = claude_call(system_content, user_content, temperature=0.1, max_tokens=10)
    return response.lower() == "yes"
# Function to generate detailed graph schema information about a shloka
