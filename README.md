# prosper-ai
A bot for steemit.

## About
This is a bot I'm working on to help minnows grow. It's currently in it's infant stage. I will be building this as I am learning Python.

# Using this bot
You may use this code to run your own bot if you want. You will need to install the correct dependencies though, that can be done using the guide below. Note: I'm using Ubuntu.

## Install python with all piston the prerequisites
```
sudo apt-get install python3
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install git make automake cmake g++ libssl-dev autoconf libtool
sudo apt-get install libboost-thread-dev libboost-date-time-dev libboost-system-dev libboost-filesystem-dev libboost-program-options-dev libboost-signals-dev libboost-serialization-dev libboost-chrono-dev libboost-test-dev libboost-context-dev libboost-locale-dev libboost-coroutine-dev libboost-iostreams-dev
sudo apt-get install doxygen perl libreadline-dev libncurses5-dev
```
## Install piston
```
sudo pip3 install steem-piston
```
Just paste all of theese commands into your terminal one by one to intsall piston with all of the prerequisites

## Run your bot
To run your bot, you first need to navigate to the bots folder

you do that by typing
```
cd <folder location>
```
You will then you need to run your bot:
```
screen python3 bot.py
```
By using that command you're attaching the python script to a screen. So you can close your terminal and log out.

Each time you want to know how the bot is doing you type:
```
screen -r
```
If you want to detach the screen use keyboard shortcut ctrl+a+d
If you want to close the script use keyboard shortcut ctrl+c
