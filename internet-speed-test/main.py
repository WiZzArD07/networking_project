import speedtest

st = speedtest.Speedtest()

print("Finding best server...")

st.get_best_server()

download = st.download()
upload = st.upload()

ping = st.results.ping

result = {
    "download_mbps":
    round(download / 1_000_000, 2),

    "upload_mbps":
    round(upload / 1_000_000, 2),

    "ping_ms":
    round(ping, 2)
}

print(result)