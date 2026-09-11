import argparse
import hashlib
import hmac
import json
import requests


def post_data(secret_key, url, data):
    headers = {
        "Content-Type": "application/json",
    }
    payload = json.dumps(data)
    signature = hmac.new(
        secret_key.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    headers["X-HMAC-Signature"] = signature

    response = requests.post(url, headers=headers, data=payload)
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--secret-key", type=str, required=True)
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--data", type=str, required=False, default=None)

    args = parser.parse_args()

    if args.data is None:
        with open("data.json", "r") as f:
            data = json.load(f)
    else:
        data = json.loads(args.data)

    response = post_data(args.secret_key, args.url, data)
    print(response.status_code, response.json(), response.text)
    exit(0)
