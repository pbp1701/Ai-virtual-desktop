#!/bin/bash
vncserver :1 -geometry 1280x720 -depth 24
websockify --web=/usr/share/novnc/ --cert=/app/self.pem 8080 localhost:5901 &

# Check if GUI mode is requested via environment variable
if [ "$USE_GUI" = "true" ]; then
    echo "Starting GUI chatbot..."
        python3 gui_chatbot.py &
        else
            echo "Starting command-line chatbot..."
                python3 chatbot.py &
                fi

                bash
