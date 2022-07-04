import socket

def client():
    serverHost = socket.gethostname()   # host name
    serverPort = 2000 # port number

    client = socket.socket()    
    client.connect((serverHost, serverPort))    # server connect
    sentence = input(" Input your sentence in lowercase here: ")    # input from user

    while sentence.lower().strip() != 'quit':
        client.send(sentence.encode())   # send sentence to server
        modifiedSentence = client.recv(1024).decode()   # receive sentence from server

        print('Sentence received from server: ' + modifiedSentence)  # show modified sentence from server

        sentence = input(" Input your sentence in lowercase here: ")    # more input from user
    
    client.close()  # close the connection

if __name__ == '__main__':
    client()