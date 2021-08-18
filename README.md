# Socket file transferring

A client-server socket file transferring using Python with no GUI.


# Installation and Running

Steps to install and run the software:
1. Clone the repository to your local machine.
2. Run **server.py** file by typing `python server.py` in terminal in the cloned folder. After running the file, the program will print the IP address and port number to the terminal.
3. Run **client.py** to transfer the file to the server by typing `python client.py <FILENAME> <HOST> <PORT>` in the terminal in the folder where the file is located.

After running the client file, the status will be printed to the terminal, and the file will be saved in the folder **received files**.

## Packages needed 

The software uses simple standard python packages such as **socket** for transferring data through sockets and **os** for accessing modifying files in the directory of the software.

## Features

The software can transfer file from one server to another server through socket programming.
