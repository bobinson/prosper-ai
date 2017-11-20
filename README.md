Forked by [Nolyoly](https://steemit.com/@noly) to continue development of this project.

## About the Prosper-ai Project
Prosper-ai is a bot built with Node.JS for the Steemit social network. It decides which posts to vote for and casts votes on behalf of a registered user. 

This project is also made open-source with documentation on how to set it up on your own server. This means that you too can set up your own bot to run seperately from our Prosper-ai project. You own the server and control it 100%. You control the running of the bot and set the configuration.

The goal of this project is to develop a simple Steemit bot to bring rewards to great content creators as well as generating curation rewards for votes cast. This bot will be kept extremely simple with the hope that someone in the future will come along and make it better as I am very new to python.

Also, by keeping this code open source and well documented, we make it easy for anyone who wishes to fork this project and make it their own, or simply copy it and use it the way they would like!


# Using this bot
You may use this code to run your own bot if you want. You will need to install the correct dependencies though, that can be done using the guide below. Note: I'm using Ubuntu.

## Install Python with Piston
Install screen (We'll use this later).
```
sudo apt-get install screen
```
Install necessary Python packages.
```
sudo apt-get install python3
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install git make automake cmake g++ libssl-dev autoconf libtool
sudo apt-get install libboost-thread-dev libboost-date-time-dev libboost-system-dev libboost-filesystem-dev libboost-program-options-dev libboost-signals-dev libboost-serialization-dev libboost-chrono-dev libboost-test-dev libboost-context-dev libboost-locale-dev libboost-coroutine-dev libboost-iostreams-dev
sudo apt-get install doxygen perl libreadline-dev libncurses5-dev
```
### Install piston
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

## License and acknowledgements
All original programming is under the CC0 license and thus completely open and free to use in any capacity. It's in the spirit of the project that it is open to all. You are at your own liability if you use this software. We are not running a service and therefore are not required to provide a terms of service policy.

Contributions via pull request are very welcome, as are issues logged via the GitHub issue tracker. You can also suggest features. We encourage these submissions to be submitted via [Utopian.io](https://utopian.io/) though! It is another great Steem project that rewards open-source developers for all of their hard work. ;)

## Changelog
v 0.0.1
- 
