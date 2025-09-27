import os
from openai import OpenAI

# Initialize the client with your API key
command="""
Krtik Girme DPES: Manchester and differential manchester code
[6:31 pm, 25/08/2025] Krtik Girme DPES: Ky ahe
[6:31 pm, 25/08/2025] Krtik Girme DPES: Assl tr pathav
[7:00 pm, 25/08/2025] Omkar Hole: Nahi azuk kele
[7:02 pm, 25/08/2025] Krtik Girme DPES: Barr
[7:02 pm, 25/08/2025] Krtik Girme DPES: Kelyaver pathav
[12:43 am, 10/09/2025] Krtik Girme DPES: Apala seat no ky ahe re
[12:43 am, 10/09/2025] Krtik Girme DPES: Sangto ka
[2:00 am, 10/09/2025] Omkar Hole: Azuk nahi ala
[3:26 pm, 10/09/2025] Krtik Girme DPES: 4th sem
[3:27 pm, 10/09/2025] Omkar Hole: Mahit nahi
"""
client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Make a request
response = client.chat.completions.create(
    model="gpt-4o-mini",  # fast + cheap model
    messages=[
        {"role": "system", "content": "You are a person named Omkar who speaks Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like Omkar."},
        {"role": "user", "content": command}
    ]
)

# Print the reply
print(response.choices[0].message.content)