This script allows you to pause/unpause SelfControlApp (https://github.com/SelfControlApp/selfcontrol/). It works by running the blocking script every minute for a duration of 1 minute and allowing you to stop the next blocking duration. 

# Installation
Follow the instructions on SelfControlApp (https://github.com/SelfControlApp/selfcontrol/) to install the application

Download this repository using git clone

Create and save a blocklist

Run `sudo crontab -e` and insert the following line
`*/1 * * * *  /usr/bin/python3 $PATH_TO_SCRIPT --config $PATH_TO_BLOCKLIST`

# Usage
If you would like to pause blocking sites, run the following script
`nohup python set_env.py &`
