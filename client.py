#! HoneyBadgers MedSolution
#! Block Chain Server

#! Python 3
# Server needs to be started before you can connect clients.

# run in terminal: python3 client.py -l <Port> -p <Port>
# -l port number has to be unique
# -p port number has to be same as port number used in server

# port specified after -l will be used to send listen for requests, we might not need this...to be decided.
# port specified after -p is used to connect to server.



import getopt, sys, threading, socket

def usage(script):
    print("Usage: python3 " + script + " -l <listening port number> -p <connect server port>")

def client(l_port, c_port):

    try:
        blk_chn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        blk_chn_sock.connect(("localhost", int(l_port)))
        # blk_chn_sock.send(str(c_port).encode())

        print("I am connected")

    except:
        print("Something")

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:p:")
        if len(opts) == 2:
            if opts[0][0] == '-l' and opts[1][0] == '-p':
                client(opts[1][1], opts[0][1])
            else:
                usage(sys.argv[0])
        else:
            usage(sys.argv[0])
    except getopt.GetoptError:
        usage(sys.argv[0])