#! HoneyBadgers MedSolution
#! Block Chain Server

#! Python 3

import getopt, sys, threading, socket

thread_list = []

def usage(script):
    print("Usage: python " + script + " -l <listening port number>")



def server(blk_chn_port):
    thread_count = 0

    # create server object
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #bind socket to a host and known good port
    server_sock.bind(('localhost', int(blk_chn_port)))
    print("past bind")
    while True:
        #listen for connection
        print ("waiting for connecion...")

        server_sock.listen(5)
        blk_chn_sock, addr = server_sock.accept()

        print ("Connection from", addr)

        # maintain thread count and names them
        process_Name = "p" + str(thread_count)
        print("prcoess name: " + process_Name);
        thread_count = thread_count + 1
        thread_list.append(process_Name)

        threading.Thread(target=handler, args=[blk_chn_port, addr]).start()

def handler(client_sock, addr):
    print ("Connected")


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "")
        if (len(args) == 1):
            server(args[0])
        else:
            usage(sys.argv[0])
    except:
        usage(sys.argv[0])
