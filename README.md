# Ender Bot Discord
A Formidable Discord Bot with some good features!

## Features:
- [x] Fun commands
- [ ] Moderation commands
- [ ] Music commands
- [ ] Auto-Moderation commands

## How to install:
I strongly do not recommend self-hosting the bot.But if you want to try it out yourself, you can do so by following the instructions below.

1. Clone the repository. You can do this by `git clone https://github.com/nav-github01001/EnderDBot.git`.
2. Change to the directory. You can do this by `cd EnderDBot`.
3. Install the dependencies. You can do this by `python -m pip install -r requirements.txt` if you are in Linux
    or `py -3.x -m pip install -r requirements.txt`(where **x** is the version of python you have installed) if you are in Windows. 
4. Create a new file called `config.json` and put the follows
    ```json
    {"token": "YOUR_TOKEN_HERE",
     "wavelink_config":{
            "wavelink_ip":"YOUR_WAVELINK_SERVER_IP_HERE",
            "wavelink_port":"YOUR_WAVELINK_SERVER_PORT_HERE",
            "wavelink_password": "YOUR_WAVELINK_SERVER_PASSWORD_HERE"
        }
    }
    ```
5. Run the bot! You can do this by `python bot.py` if you're in Linux or `py -3.x bot.py`(where **x** is the version of python you have installed) if you are in Windows. .
