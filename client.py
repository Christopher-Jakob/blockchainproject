import getopt, sys, threading, socket

def usage(script):
    print("Usage: python " + script + " -l <listening port number> -p <connect server port>")

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