import socket

def check_connection(
    host="8.8.8.8",
    port=53,
    timeout=3
):
    try:
        socket.setdefaulttimeout(timeout)

        socket.create_connection(
            (host, port)
        )

        return True

    except OSError:
        return False


if check_connection():
    print("Internet connection is active.")
else:
    print("No internet connection.")