#!/bin/bash

# Set the OpenAI API key as an environment variable
export OPENAI_API_KEY="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"

# Change to the app directory
cd "$(dirname "$0")/app"

# Check which mode is requested
if [ "$1" == "--gui" ]; then
    echo "Starting GUI chatbot..."
        python3 gui_chatbot.py
        elif [ "$1" == "--simple-gui" ]; then
            echo "Starting simple GUI chatbot..."
                python3 simple_gui_chatbot.py
                else
                    echo "Starting command-line chatbot..."
                        python3 chatbot.py
                        fi
