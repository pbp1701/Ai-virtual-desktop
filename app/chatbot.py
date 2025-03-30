import os
import openai
import pyautogui
import time

# Set API key directly or from environment variable
api_key = os.getenv("OPENAI_API_KEY") or "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"
openai.api_key = api_key

while True:
      user_input = input("You: ")
      if user_input.lower() in ["exit", "quit"]:
                break

      response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[{"role": "user", "content": user_input}]
      )
      reply = response.choices[0].message.content
      print("Bot:", reply)

    if "open firefox" in user_input.lower():
              pyautogui.hotkey('ctrl', 'alt', 't')
              time.sleep(1)
              pyautogui.typewrite('firefox\n')
