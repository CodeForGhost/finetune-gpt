import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = ""
completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::86hnKlVM",
    messages=[
        {"role": "system", "content": "You are an assistant describe about the ticket type, ticket subject, ticket description, resolution, ticket priority, ticket channel and customer satisfaction rating."},
        {"role": "user", "content": "3"}
    ]
)
print(completion.choices[0].message)
