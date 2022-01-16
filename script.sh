#! /usr/bin/bash

# Logger for shell streaming
echo "Logging..."
if [ -f "logs.txt" ]
then
    rm "logs.txt"
else
    touch "logs.txt"
fi


# Makefile for C++ compiling
make all


# Python Webscraper
if [ -f "courses.txt" ]
then
    rm "courses.txt"

    # read -p "courses exist, would you like to reload all courses? (y/n): " RELOAD
    # if [ RELOAD == "y" ]
    # then
    #     echo "reloading courses..."
    #     python3 getClass_T.py
    #     echo "reload success" >> "logs.txt"
    # fi
fi

echo "adding new courses..."
python3 getClass_T.py
echo "adding success" >> "logs.txt"

# Launch UI
#python3 GUI.py

# C++ executable
./scheduler


# Python Webscraper
python3 getClassDetails.py