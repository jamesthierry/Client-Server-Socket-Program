import socket
import select
import asyncio

read_list = []
async def acceptClient(server):
    global read_list
    while True:
        conn, address = server.accept() # accept a new connection
        read_list.append(conn)
        print("Connection from: " + str(address))


def server():
    # get the hostname
    serverHost = socket.gethostname()   # host name 
    serverPort = 2000 # port number

    server = socket.socket()    
    server.bind(('', serverPort))   # binding port number

    server.listen(1)
    asyncio.gather

    conn, address = server.accept() # accept a new connection
    read_list = [conn]
    print("Connection from: " + str(address))
    while True:
        ready_read, _, _ = select.select(read_list, [], [], 10)
        print(ready_read)
        for connection in ready_read:
            sentence = connection.recv(1024).decode()
            if not sentence:
                break
            print("Message from client: " + str(sentence))
            modifiedSentence = str(sentence).upper()    # convert lowercase sentence to uppercase sentence
            print("Sending modified sentence: " + str(modifiedSentence))
            connection.send(modifiedSentence.encode())    # send modified sentence to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server()