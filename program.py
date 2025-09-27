

    
import pyautogui
import time
import pyperclip
from openai import OpenAI# imp# Additional commented code removed for security
# import pyperclip  # for accessing clipboard
# from openai import OpenAI
# import os

# # Initialize the client with your API key
# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")  # Use environment variable for security
# )

client = OpenAI(
  api_key="",
)

def is_last_message_from_sender(chat_log, sender_name="<sender name>"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1925, 1745)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(1087, 310)
    pyautogui.dragTo(2740, 1571, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1994, 281)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "<prompt to train your ai>"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')










# import pyautogui
# import time
# import pyperclip  # for accessing clipboard
# from openai import OpenAI

# # Initialize the client with your API key
# client = OpenAI(
#     api_key="api key"  # ⚠️ keep secret, don’t hardcode in public code
# )

# # Small delay to give you time to switch to the correct screen
# time.sleep(3)

# def last_message_from_sender(chat_log: str,sender_name="Tushar Hole"):
#     messages = chat_log.strip().split("/2024] ")[-1]
#     if sender_name in messages:
#         return True
#     return False


#     # Step 1: Click on the icon
# pyautogui.click(1925, 1745)
# time.sleep(1)
# while True:

#     # Step 2: Drag to select text
#     pyautogui.moveTo(1087, 310)
#     pyautogui.dragTo(2740, 1571, duration=1, button='left')
#     time.sleep(1)

#     # Step 3: Copy selected text (Ctrl+C)
#     pyautogui.hotkey('ctrl', 'c')
#     pyautogui.click(2740, 1571)
#     time.sleep(2)

#     # Step 4: Get from clipboard
#     chat_history = pyperclip.paste()
#     print("Copied text:")
#     print(chat_history)
#     if last_message_from_sender(chat_history):
#         # Step 5: Send to OpenAI
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",  # fast + cheap model
#             messages=[
#                 {"role": "system", "content": "You are a person named Omkar who speaks Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like Omkar.(messages only)"},
#                 {"role": "user", "content": chat_history}
#             ]
#         )

#     # Step 6: Extract reply
#     answer = response.choices[0].message.content
#     print("Bot reply:")
#     print(answer)

#     # Step 7: Copy reply to clipboard
#     pyperclip.copy(answer)

#     # Step 8: Click at Point(x=1221, y=1632)
#     pyautogui.click(1221, 1632)
#     time.sleep(0.5)

#     # Step 9: Paste reply
#     pyautogui.hotkey("ctrl", "v")

#     # Step 10: Press Enter
#     pyautogui.press("enter")
