import requests
import time

url = input(
    "Enter URL: "
)

try:
    start = time.time()

    response = requests.get(
        url,
        timeout=10
    )

    end = time.time()

    print({
        "status_code":
        response.status_code,

        "response_time_ms":
        round(
            (end-start)*1000,
            2
        )
    })

except Exception as e:
    print(e)