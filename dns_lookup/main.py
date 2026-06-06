import socket

def lookup(domain):
    try:
        ip = socket.gethostbyname(domain)

        return {
            "domain": domain,
            "ip": ip
        }

    except socket.gaierror:
        return {
            "error": "Domain not found"
        }


domain = input(
    "Enter domain: "
)

print(lookup(domain))