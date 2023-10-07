import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
file_id = "file-gQnFyLnj2mNspsRAUJqLdqgG"
response = openai.FineTuningJob.create(
    training_file=file_id, model="gpt-3.5-turbo")
print(response)
# job_id = "ftjob-0l8dKSiL0OqhefjiIIUgJOXf"
