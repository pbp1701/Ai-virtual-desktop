FROM nvidia/cuda:12.2.0-base-ubuntu20.04

RUN apt-get update && apt-get install -y \
    xfce4 xfce4-goodies tightvncserver \
        firefox wget curl git python3 python3-pip python3-tk \
            x11vnc xvfb net-tools supervisor lxde \
                xterm novnc websockify \
                    fonts-dejavu

                    ENV DISPLAY=:1
                    ENV DEBIAN_FRONTEND=noninteractive

                    RUN pip3 install --upgrade pip && \
                        pip3 install flask openai pyautogui pytesseract opencv-python

                        COPY ./app /app
                        WORKDIR /app

                        EXPOSE 8080 5901

                        CMD ["/app/startup.sh"]
