
# STARTING THIS PROJECT - removing the .git folder

- first of all, clone the repo onto your desktop using
    git clone https://github.com/ryancarneyy/HaCK-backend
- then, navigate into the repository using cd
- once you are in the HaCK-backend repository in the terminal, run
     rm -rf .git
- This will remove the .git folder from your project, so you can now run 
    git init to make a new empty repository inside of the folder!

# Setting up a working node server - IMPLEMENTATION RELEASED


- Take the folder backend (containing index.js), and put the folder directly into your project folder which you have made. Your project folder will hold 2/3 folders: 
    - backend
    - frontend (containing react project)
    - pico code (if you choose to contain a copy of your pico code on your actual computer)
        - to edit pico code directly, use thonny to edit the files that are currently on the pico

- you will be able to send and recieve messages using MQTT protocol, using the node server (index.js) as the middle man between the frontend React site and the MQTT broker
- WHEN IN YOUR BACKEND FOLDER: run npm i to install all dependencies

# .env file inside of backend folder

- In order to connect your mqtt, make a file called .env inside of this folder, where your CONNECT_URL, MQTT_USER, and MQTT_PASS will be stored
    - create variables with these names, that contain a string of these
        - THESE VARIABLES SHOULD NOT BE STRINGS, JUST PLAIN TEXT
        - CONNECT_URL: contains a of the url for the MQTT broker
            - THIS URL SHOULD CONTAIN: mqtts://urlofyourbroker.edu:8883
        - CONNECT_USER: contains the username of the credential you created for your node server
        - MQTT_PASS: contains the password of the credential that you created for your node server
- With these set up, you will be able to run your node server through port 8000, which will subscribe to 2 topics, 'temp' and 'ultrasonic', which you will be able to change if you please.
    - run the node server by running 
        "node index.js" in your backend directory which you have taken off of my github
    - if you see "subscribed to temp" and "subscribed to ultrasonic" you should be good and connected! 




# Setting up your frontend connection to your node server!

- Run npm start just like normal in order to start your frontend
- I have given you functions to send and recieve data through mqtt broker. You have to decide how to implement them.
- When you run npm start, you should see there is a message that pops up in the node server's console, which says frontend has connected to socket. Once you see this message you should be good to go.

# Using connections.py for your Pico W

- You will be able to use 2 functions in connections.py
    - One for connection to the MQTT broker (connect_mqtt) and one for connecting to WIFI (connect_internet)

    - connect_mqtt(mqtt_server, mqtt_user, mqtt_pass):

        - mqtt_server: the server url which you have obtained by making a free serverless MQTT Broker on HIVEMQ
            - Should look something like: '37##616##db7#bd1##cac997eb01##13.s1.eu.hivemq.cloud'

        - mqtt_user:
            - This is the name of the user you create when you make a credential
                - The purpose of this is just to have a unique user in which the MQTT Broker can understand where the message is coming from 
                - Ex: username = 'pico' when creating credentials for the Raspberry Pi Pico W to send something

        - mqtt_pass:
            - This is the password that goes along with your mqtt_user
            - Just for the broker to validate the user
            - Make this whatever you want, just write it down

        - RETURNS client, which you can use 
            - client.subscribe(b"topic") to subscribe to a topic of your choice
            - client.publish(b"topic", b"message") to publish a message with a topic of your choice
            - client

    - connect_internet( ssid, password ):
        
        - ssid: 
            - This is the name of the wi-fi network you are trying to connect to

        - password:
            - this is the password of the wi-fi network you are trying to connect to


    