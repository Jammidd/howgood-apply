# Job Applier

Posts applicant JSON to an apply API, signed with HMAC-SHA256 (`X-HMAC_Signature`).

## Setup

```bash
pip install requests
```

## Customize

Edit `data.json` with your applicant fields (name, email, resume URL, etc.). The file is sent as the request body.

To send a one-off payload without editing the file, pass JSON to `--data`.

## Run

```bash
python main.py --secret-key YOUR_SECRET --url https://example.com/apply
```

Inline payload:

```bash
python main.py --secret-key YOUR_SECRET --url https://example.com/apply --data '{"name": "Jane Doe"}'
```

Prints the HTTP status code and response body.
