import os
import openai
import pyautogui
import time
import tkinter as tk
from tkinter import scrolledtext
import threading

# Set API key directly or from environment variable
api_key = os.getenv("OPENAI_API_KEY") or "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"
openai.api_key = api_key

class ChatbotGUI:
      def __init__(self, root):
                self.root = root
                self.root.title("AI Virtual Desktop Assistant")
                self.root.geometry("600x400")

        # Chat display area
                self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
                self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
                self.chat_display.config(state=tk.DISABLED)

        # Input field
                self.user_input = tk.Entry(root, width=70)
                self.user_input.grid(row=1, column=0, padx=10, pady=10)
                self.user_input.bind("<Return>", self.send_message)

        # Send button
                self.send_button = tk.Button(root, text="Send", command=self.send_message)
                self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Welcome message
                self.update_chat_display("Bot: Hello! I'm your AI assistant. How can I help you today?")

      def update_chat_display(self, message):
                self.chat_display.config(state=tk.NORMAL)
                self.chat_display.insert(tk.END, message + "\n")
                self.chat_display.see(tk.END)
                self.chat_display.config(state=tk.DISABLED)

      def send_message(self, event=None):
                user_message = self.user_input.get()
                if user_message.strip() == "":
                              return

                self.update_chat_display(f"You: {user_message}")
                self.user_input.delete(0, tk.END)

        # Process in a separate thread to keep GUI responsive
                threading.Thread(target=self.process_message, args=(user_message,), daemon=True).start()

      def process_message(self, user_message):
                try:
                              # Handle special commands
                              if user_message.lower() in ["exit", "quit"]:
                                                self.update_chat_display("Bot: Goodbye!")
                                                self.root.after(1000, self.root.destroy)
                                                return

                              # Send to OpenAI API
                              response = openai.ChatCompletion.create(
                                  model="gpt-4",
                                  messages=[{"role": "user", "content": user_message}]
                              )
                              reply = response.choices[0].message.content

            # Update chat display with bot response
                    self.root.after(0, lambda: self.update_chat_display(f"Bot: {reply}"))

                    # Handle desktop automation commands
                    if "open firefox" in user_message.lower():
                                      pyautogui.hotkey('ctrl', 'alt', 't')
                                      time.sleep(1)
                                      pyautogui.typewrite('firefox\n')

except Exception as e:
            self.root.after(0, lambda: self.update_chat_display(f"Bot: Error: {str(e)}"))

if __name__ == "__main__":
      root = tk.Tk()
      app = ChatbotGUI(root)
      root.mainloop()
