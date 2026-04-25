# BruteWave

BruteWave is a simple Python proof-of-concept brute force utility targeting login endpoints for Instagram, Snapchat, and Facebook.

> **Warning:** This tool is intended for educational use only. Unauthorized access to accounts or systems is illegal and unethical.

## Requirements

- Python 3.8+
- `requests`
- `colorama`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python BruteWave.py
```

Follow the prompts to choose a target platform and provide a username/email and a path to a password wordlist.

## Notes

- Instagram brute forcing is simulated through the script’s login flow and may be blocked by rate limits or security protections.
- Snapchat support is intentionally simulated and not a working brute-force implementation.
- Facebook brute forcing uses the mobile login endpoint and may not work reliably.

## File structure

- `BruteWave.py` — main script
- `wordlist.txt` — example wordlist file
- `requirements.txt` — project dependencies
- `LICENSE` — project license
