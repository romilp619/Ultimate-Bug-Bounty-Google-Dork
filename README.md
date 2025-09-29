# Ultimate Bug Bounty Google Dork Generator v2.0

A focused, interactive CLI tool to speed up reconnaissance for authorized security testing and bug-bounty programs by generating Google dorks and automating multi-search flows.

> **Important — Use responsibly:** this tool is for **authorized** testing only. Do **not** run it against systems you do not own or do not have written permission to test.


## About

This repository contains `ultimate_bug_bounty_dork_generator_final.py` — an interactive Python CLI that:

- Maintains a curated list of high-value / bug-bounty domains.
- Provides a comprehensive set of Google dork templates grouped by category.
- Supports single- and multi-domain automation:
  - Multiple dorks on a single domain
  - A single dork across many domains
- Can open generated dorks in your default browser for manual review.

The script is intended for information-gathering **only** and does **not** perform intrusion or exploitation steps.

---

## Features

- Domain-based dork templates (LFI, RCE, SQLi-prone params, API doc locators, etc.)
- External reconnaissance dorks (paste sites, cloud buckets, drive links, etc.)
- Random domain selection from built-in `DOMAINS`
- Multi-search automation with interrupt handling (Ctrl+C)
- Category browsing and bulk generation
- Auto-open queries in browser
- Dependency-free: uses Python standard library (tested with Python 3.8+)

---

## Quick demo (interactive session)

```bash
$ python3 ultimate_bug_bounty_dork_generator_final.py

======================================================================
Ultimate Bug Bounty Google Dork Generator v2.0
======================================================================

Options:
1. Generate dork for specific domain
2. Generate dork for random domain
3. List all domains
4. Generate multiple random dorks
5. Auto search single dork (opens browser)
6. Browse dorks by category
7. Generate dork by category name
8. Bulk generate all dorks for a domain
9. Multi-search automation
10. Exit

Enter your choice (1-10): 9

🚀 Multi-Search Automation Options:
1. Multiple dorks on single domain
2. Single dork on multiple domains
3. Back to main menu

Enter your choice (1-3): 1
Enter domain name (or press Enter for random):
# (tool picks a random domain and prompts to select category numbers)


```

## Installation

```bash

1. Clone the repo

git clone https://github.com/<yourusername>/ultimate-bug-bounty-dorkgen.git
cd ultimate-bug-bounty-dorkgen

2.(Optional) Create & activate virtual environment:

python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows (PowerShell)

3. Run the script

python3 ultimate_bug_bounty_dork_generator_final.py



```

