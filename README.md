# Deny and Conquer

## Dependencies

- Python 3.6+

## Module Installation / Setup

```git clone <repo-url>```

```cd <repo-folder>```

To install requirements, you may run any of the following
- `pip install -r requirements.txt`
- `pip3 install -r requirements.txt`
- `python - m pip install -r requirements.txt`
- `python3 -m pip install -r requirements.txt`

## Running The Program
change the IP address on `line 13 of server.py` and `line 7 of client.py`

To run the program 
1.  `python server.py` or alternatively `python3 server.py`
2. `python main.py` or `python3 main.py`

## Files Description 

- `server.py` has the server socket and a list of players 
- `Player.py` contains the Player class that is passed between the client and the server, also has the functions getting positions and information of players 
- `client.py` contains the Network class that is used for managing the client 
- `main.py` has the client socket and the logic for drawing and communicating with the server 
- `requirements.txt` contains libraries that need to be installed before running the program
