import os
import openai

# Set API key directly or from environment variable
api_key = os.getenv("OPENAI_API_KEY") or "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"
openai.api_key = api_key

print(f"Using API key: {api_key[:10]}...")

try:
      # Try the newer API format
      try:
                response = openai.chat.completions.create(
                              model="gpt-4",
                              messages=[{"role": "user", "content": "Hello, this is a test."}]
                )
                print("Using new API format")
                print(f"Response: {response.choices[0].message.content}")
except AttributeError:
          # Try the older API format
          response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": "Hello, this is a test."}]
          )
          print("Using old API format")
          print(f"Response: {response.choices[0].message.content}")
except Exception as e:
      import traceback
      print(f"Error: {str(e)}")
      print(traceback.format_exc())
