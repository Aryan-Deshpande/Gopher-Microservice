import openai
import os

prompt = "hey there would you like"
openai.api_key= os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt="joe is a", 
    max_tokens=100)

content = response.choices[0].text.split(".")
print(content)