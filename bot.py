import os
from openai import OpenAI

# Initialize the client with your API key
command="""
test commands
"""
client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Make a request
response = client.chat.completions.create(
    model="gpt-4o-mini",  # fast + cheap model
    messages=[
        {"role": "system", "content": "<your prompt to train AI>"},
        {"role": "user", "content": command}
    ]
)

# Print the reply
print(response.choices[0].message.content)
