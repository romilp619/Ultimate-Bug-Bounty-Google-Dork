#!/usr/bin/env python3
"""
Ultimate Bug Bounty Google Dork Generator v2.0
Author: Security Research Tool
Description: Comprehensive Google dorks with multi-search automation and multiple domain support
"""

import random
import time
import webbrowser
import urllib.parse
import signal
import sys
import os

# Complete list of bug bounty domains
DOMAINS = [
    "1inch.io", "99taxi.com", "a2hosting.com", "aave.com", "abn-amro.com", 
    "acer.com", "activision.com", "addictinggames.com", "adobe.com", "adorama.com",
    "afterpay.com", "agoda.com", "agriculture.gov", "airbnb.com", "akamai.com",
    "aldi.com", "alfa-romeo.com", "alienware.com", "amazon.com", "amd.com",
    "americanexpress.com", "angular.io", "apple.com", "armor.ag",
    "asda.com", "asus.com", "atlassian.com", "audi.com", "auth0.com",
    "automattic.com", "avalanche.network", "aws.amazon.com", "azure.microsoft.com",
    "balancer.fi", "bankofamerica.com", "barclays.com", "battlenet.com",
    "bentley.com", "bestbuy.com", "bhphotovideo.com", "bigcommerce.com", "binance.com",
    "bitcoin.org", "bitfinex.com", "bitget.com", "bitstamp.net", "bittrex.com",
    "blizzard.com", "bluehost.com", "bmw.com", "bnbchain.org", "booking.com",
    "bosch.com", "bootstrap.com", "bugcrowd.com", "bunnycdn.com",
    "bybit.com", "cabify.com", "canonical.com", "cardano.org", "cashapp.com",
    "cdc.gov", "cdnjs.com", "census.gov", "chainlink.network", "chase.com",
    "cheapflights.com", "checkpoint.com", "chime.com", "chrysler.com", "cia.gov",
    "cisco.com", "citibank.com", "citroen.com", "cloud.google.com", "cloudflare.com",
    "coindcx.com", "coinbase.com", "coincheck.com", "coinswitch.co", "commerce.gov",
    "compound.finance", "coolmathgames.com", "corsair.com", "costco.com", "crazygames.com",
    "creditkarma.com", "crowdstrike.com", "crypto.com", "curve.fi", "cyberark.com",
    "dailymotion.com", "datadog.com", "defense.gov", "dell.com", "dhs.gov",
    "didi.com", "digitalocean.com", "discover.com", "discord.com", "dlive.tv",
    "docker.com", "dreamhost.com", "dropbox.com", "dyson.com", "ea.com",
    "ebay.com", "ed.gov", "elastic.co", "electrolux.com", "energy.gov",
    "epicgames.com", "epa.gov", "espn.com", "etrade.com", "ethereum.org",
    "etsy.com", "expedia.com", "facebook.com", "fastly.com", "fbi.gov",
    "ferrari.com", "fiat.com", "fidelity.com", "fifa.com", "fly.io",
    "fontawesome.com", "ford.com", "fortinet.com", "foxsports.com", "friv.com",
    "ftx.com", "gamejolt.com", "gate.io", "gatsbyjs.org", "ge.com",
    "gemini.com", "github.com", "gitlab.com", "gm.com",
    "godaddy.com", "gog.com", "gojek.com", "google.com", "gov.au",
    "gov.ca", "gov.sg", "gov.uk", "grab.com", "grafana.com",
    "greengeeks.com", "hackerone.com", "hackenproof.com", "handelsbanken.com", "heroku.com",
    "hhs.gov", "hilton.com", "homedepot.com", "homeaway.com", "honda.com",
    "hostelworld.com", "hostgator.com", "hostinger.com", "hotels.com", "hotwire.com",
    "hsbc.com", "huobi.com", "hud.gov", "humblebundle.com", "hyundai.com",
    "ibm.com", "immunefi.com", "ing.com", "inmotion.com", "instagram.com",
    "intel.com", "interactivebrokers.com", "interior.gov", "intigriti.com", "irs.gov",
    "itch.io", "jaguar.com", "jitsi.org", "jquery.com", "jsdelivr.com",
    "justice.gov", "kayak.com", "keycdn.com", "kia.com", "kizi.com",
    "klarna.com", "kongregate.com", "kraken.com", "kucoin.com", "kubernetes.io",
    "labor.gov", "lamborghini.com", "lancia.com", "landrover.com", "lastminute.com",
    "lending.com", "lendingclub.com", "lenovo.com", "lg.com", "linode.com",
    "linkedin.com", "lloyds.com", "logitech.com", "lowes.com", "lyft.com",
    "magento.com", "makerdao.com", "marriott.com", "maserati.com", "mastercard.com",
    "maxcdn.com", "mazda.com", "meet.google.com", "mercedes-benz.com", "meta.com",
    "mexc.com", "microsoft.com", "miniclip.com", "mint.com", "mitsubishi.com",
    "mixer.com", "mlb.com", "momondo.com", "mongodb.com", "monzo.com",
    "mozilla.org", "msi.com", "n26.com", "namecheap.com", "nasa.gov",
    "nba.com", "nerdwallet.com", "netflix.com", "netlify.com", "newgrounds.com",
    "newrelic.com", "nextjs.org", "nfl.com", "nhl.com", "nih.gov",
    "nissan.com", "noaa.gov", "nordea.com", "nsf.gov", "nsa.gov",
    "nuxtjs.org", "nvidia.com", "okx.com", "okta.com", "ola.com",
    "openbugbounty.org", "oracle.com", "orbitz.com", "origin.com", "paloaltonetworks.com",
    "pancakeswap.finance", "panasonic.com", "paypal.com", "peugeot.com", "philips.com",
    "pinterest.com", "pnc.com", "poki.com", "polkadot.network", "poloniex.com",
    "polygon.technology", "porsche.com", "priceline.com", "prometheus.io", "prosper.com",
    "pubg.com", "qualys.com", "quadpay.com", "railway.app", "rapid7.com",
    "razer.com", "rbc.com", "reactjs.org", "reddit.com", "redhat.com",
    "renault.com", "render.com", "revolut.com", "riotgames.com", "robinhood.com",
    "roblox.com", "rockstargames.com", "rollsroyce.com", "sainsburys.co.uk", "salesforce.com",
    "samsung.com", "santander.com", "schwab.com", "scotiabank.com", "seb.com",
    "sec.gov", "sentinelone.com", "sezzle.com", "shopify.com", "siemens.com",
    "signal.org", "siteground.com", "skype.com", "skyscanner.com", "slack.com",
    "snapchat.com", "sofi.com", "solana.com", "sony.com", "spotify.com",
    "splitit.com", "square.com", "squarespace.com", "staples.com", "state.gov",
    "steam.com", "steelseries.com", "stripe.com", "subaru.com", "sushiswap.org",
    "svelte.dev", "swedbank.com", "synack.com", "synopsys.com", "synthetix.io",
    "target.com", "td.com", "tdameritrade.com", "teams.microsoft.com", "telegram.org",
    "tenable.com", "tesla.com", "tesco.com", "tigerdirect.com", "tiktok.com",
    "toyota.com", "transportation.gov", "travelocity.com", "treasury.gov", "trivago.com",
    "tumblr.com", "twitch.tv", "twitter.com", "uber.com", "ubisoft.com",
    "ubs.com", "udemy.com", "unicredit.it", "uniswap.org", "unity.com",
    "unocoin.com", "unpkg.com", "unrealengine.com", "uplay.com", "usbank.com",
    "usgs.gov", "usps.com", "va.gov", "valvesoftware.com", "vanguard.com",
    "varonis.com", "venmo.com", "veracode.com", "vercel.com", "viber.com",
    "vimeo.com", "visa.com", "volkswagen.com", "volvo.com", "vrbo.com",
    "vuejs.org", "vultr.com", "waitrose.com", "walmart.com", "wazirx.com",
    "webex.com", "webull.com", "weebly.com", "wellsfargo.com", "whatsapp.com",
    "whirlpool.com", "whitehat.com", "whitehouse.gov", "wix.com", "woocommerce.com",
    "wordpress.com", "x.com", "y8.com", "yearn.finance", "yeswehack.com",
    "youtube.com", "zebpay.com", "zoom.us"
]

# Comprehensive Google dork templates organized by category
DORK_CATEGORIES = {
    "PHP Files": 'site:"{}" ext:php inurl:?',
    "API Endpoints": 'site:"{}" inurl:api | site:*/rest | site:*/v1 | site:*/v2 | site:*/v3',
    "Juicy Extensions": 'site:"{}" ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess | ext:json',
    "High % inurl keywords": 'inurl:conf | inurl:env | inurl:cgi | inurl:bin | inurl:etc | inurl:root | inurl:sql | inurl:backup | inurl:admin | inurl:php site:"{}"',
    "Server Errors": 'inurl:"error" | intitle:"exception" | intitle:"failure" | intitle:"server at" | inurl:exception | "database error" | "SQL syntax" | "undefined index" | "unhandled exception" | "stack trace" site:"{}"',
    "XSS Prone Parameters": 'inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:"{}"',
    "Open Redirect Parameters": 'inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:& inurl:http site:"{}"',
    "SQLi Prone Parameters": 'inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:"{}"',
    "SSRF Prone Parameters": 'inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:& site:"{}"',
    "LFI Prone Parameters": 'inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:& site:"{}"',
    "RCE Prone Parameters": 'inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:& site:"{}"',
    "File Upload Endpoints": 'site:"{}" "choose file"',
    "API Documentation": 'inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:"{}"',
    "Login Pages": 'inurl:login | inurl:signin | intitle:login | intitle:signin | inurl:secure site:"{}"',
    "Test Environments": 'inurl:test | inurl:env | inurl:dev | inurl:staging | inurl:sandbox | inurl:debug | inurl:temp | inurl:internal | inurl:demo site:"{}"',
    "Sensitive Documents": 'site:"{}" ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx intext:"confidential" | intext:"Not for Public Release" | intext:"internal use only" | intext:"do not distribute"',
    "Sensitive Parameters": 'inurl:email= | inurl:phone= | inurl:name= | inurl:user= inurl:& site:"{}"',
    "Adobe Experience Manager": 'inurl:/content/usergenerated | inurl:/content/dam | inurl:/jcr:content | inurl:/libs/granite | inurl:/etc/clientlibs | inurl:/content/geometrixx | inurl:/bin/wcm | inurl:/crx/de site:"{}"'
}

# External reconnaissance dorks (don't need domain substitution)
EXTERNAL_DORKS = {
    "Disclosed XSS/Redirects": 'site:openbugbounty.org inurl:reports intext:"{}"',
    "Google Groups": 'site:groups.google.com "{}"',
    "Pastebin Leaks": 'site:pastebin.com "{}"',
    "JSFiddle Leaks": 'site:jsfiddle.net "{}"',
    "CodeBeautify Leaks": 'site:codebeautify.org "{}"',
    "CodePen Leaks": 'site:codepen.io "{}"',
    "AWS S3 Buckets": 'site:s3.amazonaws.com "{}"',
    "Azure Blob Storage": 'site:blob.core.windows.net "{}"',
    "Google APIs": 'site:googleapis.com "{}"',
    "Google Drive": 'site:drive.google.com "{}"',
    "Azure DevOps": 'site:dev.azure.com "{}"',
    "OneDrive": 'site:onedrive.live.com "{}"',
    "DigitalOcean Spaces": 'site:digitaloceanspaces.com "{}"',
    "SharePoint": 'site:sharepoint.com "{}"',
    "AWS S3 External": 'site:s3-external-1.amazonaws.com "{}"',
    "AWS S3 Dualstack": 'site:s3.dualstack.us-east-1.amazonaws.com "{}"',
    "Dropbox Shares": 'site:dropbox.com/s "{}"',
    "Box Shares": 'site:box.com/s "{}"',
    "Google Docs": 'site:docs.google.com inurl:"/d/" "{}"',
    "JFrog Artifactory": 'site:jfrog.io "{}"',
    "Firebase": 'site:firebaseio.com "{}"',
    "Security.txt": 'site:*/security.txt "bounty"'
}

# Global flag for handling interrupts
interrupted = False

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    """Display the main menu banner and options"""
    clear_screen()
    print("=" * 70)
    print("Ultimate Bug Bounty Google Dork Generator v2.0")
    print("=" * 70)
    print()
    print("Options:")
    print("1. Generate dork for specific domain")
    print("2. Generate dork for random domain")
    print("3. List all domains")
    print("4. Generate multiple random dorks")
    print("5. Auto search single dork (opens browser)")
    print("6. Browse dorks by category")
    print("7. Generate dork by category name")
    print("8. Bulk generate all dorks for a domain")
    print("9. Multi-search automation")
    print("10. Exit")
    print()

def signal_handler(sig, frame):
    """Handle Ctrl+C interrupt gracefully"""
    global interrupted
    interrupted = True
    print("\n\n🛑 Interrupted! Returning to main menu...")

def generate_dork(domain, category):
    """Generate Google dork for a specific domain and category"""
    if category in DORK_CATEGORIES:
        return DORK_CATEGORIES[category].format(domain)
    elif category in EXTERNAL_DORKS:
        return EXTERNAL_DORKS[category].format(domain)
    else:
        return f"Unknown category: {category}"

def search_google(dork):
    """Open Google search with the dork"""
    encoded_dork = urllib.parse.quote(dork)
    url = f"https://www.google.com/search?q={encoded_dork}"
    webbrowser.open(url)

def random_domain():
    """Get a random domain from the list"""
    return random.choice(DOMAINS)

def display_categories():
    """Display all available dork categories"""
    print("\n=== DOMAIN-BASED DORK CATEGORIES ===")
    for i, category in enumerate(DORK_CATEGORIES.keys(), 1):
        print(f"{i:2d}. {category}")

    print("\n=== EXTERNAL RECONNAISSANCE DORKS ===")
    for i, category in enumerate(EXTERNAL_DORKS.keys(), len(DORK_CATEGORIES) + 1):
        print(f"{i:2d}. {category}")

def get_category_by_number(number):
    """Get category name by its number"""
    all_categories = list(DORK_CATEGORIES.keys()) + list(EXTERNAL_DORKS.keys())
    if 1 <= number <= len(all_categories):
        return all_categories[number - 1]
    return None

def get_all_categories():
    """Get all category names as a list"""
    return list(DORK_CATEGORIES.keys()) + list(EXTERNAL_DORKS.keys())

def parse_category_selection(input_str):
    """Parse comma-separated category numbers and return category names"""
    try:
        numbers = [int(x.strip()) for x in input_str.split(',')]
        categories = []
        all_categories = get_all_categories()

        for num in numbers:
            if 1 <= num <= len(all_categories):
                categories.append(all_categories[num - 1])
            else:
                print(f"⚠️  Invalid category number: {num}")

        return categories
    except ValueError:
        print("⚠️  Please enter valid numbers separated by commas")
        return []

def parse_domain_selection(input_str):
    """Parse comma-separated domains and return domain list"""
    domains = [domain.strip() for domain in input_str.split(',')]
    return [d for d in domains if d]  # Remove empty strings

def multi_search_dorks(domain, categories):
    """Search multiple dorks with 3-second intervals on single domain"""
    global interrupted
    interrupted = False

    # Set up signal handler for Ctrl+C
    original_handler = signal.signal(signal.SIGINT, signal_handler)

    try:
        print(f"\n🚀 Starting automated search for: {domain}")
        print(f"📋 Selected categories: {', '.join(categories)}")
        print(f"⏱️  Opening {len(categories)} dorks with 3-second intervals...")
        print("\n💡 Press Ctrl+C to return to main menu\n")

        for i, category in enumerate(categories, 1):
            if interrupted:
                break

            try:
                dork = generate_dork(domain, category)
                print(f"[{i}/{len(categories)}] 🔍 {category}")
                print(f"    Dork: {dork}")

                search_google(dork)
                print(f"    ✅ Opened in browser!")

                if i < len(categories) and not interrupted:
                    print(f"    ⏳ Waiting 3 seconds before next search...\n")
                    for j in range(30):  # 30 * 0.1 = 3 seconds, but check interrupted more frequently
                        if interrupted:
                            break
                        time.sleep(0.1)
                    if not interrupted:
                        print()  # New line after countdown

            except Exception as e:
                print(f"    ❌ Error opening dork: {e}")
                continue

        if not interrupted:
            print(f"\n🎉 Completed! Opened {len(categories)} dorks for {domain}")

    finally:
        # Restore original signal handler
        signal.signal(signal.SIGINT, original_handler)

    if interrupted:
        return "interrupted"
    else:
        input("\nPress Enter to continue...")
        return "completed"

def multi_domain_single_dork(domains, category):
    """Search single dork across multiple domains with 3-second intervals"""
    global interrupted
    interrupted = False

    # Set up signal handler for Ctrl+C
    original_handler = signal.signal(signal.SIGINT, signal_handler)

    try:
        print(f"\n🎯 Starting automated search across {len(domains)} domains")
        print(f"📋 Selected category: {category}")
        print(f"🌐 Target domains: {', '.join(domains)}")
        print(f"⏱️  Opening {len(domains)} dorks with 3-second intervals...")
        print("\n💡 Press Ctrl+C to return to main menu\n")

        for i, domain in enumerate(domains, 1):
            if interrupted:
                break

            try:
                dork = generate_dork(domain, category)
                print(f"[{i}/{len(domains)}] 🌐 {domain}")
                print(f"    Category: {category}")
                print(f"    Dork: {dork}")

                search_google(dork)
                print(f"    ✅ Opened in browser!")

                if i < len(domains) and not interrupted:
                    print(f"    ⏳ Waiting 3 seconds before next search...\n")
                    for j in range(30):  # 30 * 0.1 = 3 seconds, but check interrupted more frequently
                        if interrupted:
                            break
                        time.sleep(0.1)
                    if not interrupted:
                        print()  # New line after countdown

            except Exception as e:
                print(f"    ❌ Error opening dork: {e}")
                continue

        if not interrupted:
            print(f"\n🎉 Completed! Opened {len(domains)} dorks for category: {category}")

    finally:
        # Restore original signal handler
        signal.signal(signal.SIGINT, original_handler)

    if interrupted:
        return "interrupted"
    else:
        input("\nPress Enter to continue...")
        return "completed"

def multi_search_menu():
    """Handle the multi-search automation menu"""
    print("\n🚀 Multi-Search Automation Options:")
    print("1. Multiple dorks on single domain")
    print("2. Single dork on multiple domains")
    print("3. Back to main menu")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            # Multiple dorks on single domain (existing feature)
            domain = input("Enter domain name (or press Enter for random): ").strip()
            if not domain:
                domain = random_domain()

            display_categories()
            print("\n💡 Enter category numbers separated by commas (e.g., 1,3,5,12,25)")
            print("💡 You can select as many categories as you want!")

            category_input = input("\nEnter category numbers: ").strip()
            if category_input:
                selected_categories = parse_category_selection(category_input)
                if selected_categories:
                    result = multi_search_dorks(domain, selected_categories)
                    return  # Return to main menu regardless of result
                else:
                    print("No valid categories selected.")
                    input("Press Enter to continue...")
                    return
            else:
                print("No categories selected.")
                input("Press Enter to continue...")
                return

        elif choice == "2":
            # Single dork on multiple domains (new feature)
            print("\n💡 Enter domain names separated by commas (e.g., tesla.com,apple.com,microsoft.com)")
            domains_input = input("Enter domain names: ").strip()

            if domains_input:
                selected_domains = parse_domain_selection(domains_input)
                if selected_domains:
                    display_categories()
                    try:
                        cat_num = int(input("\nEnter single category number: "))
                        category = get_category_by_number(cat_num)
                        if category:
                            result = multi_domain_single_dork(selected_domains, category)
                            return  # Return to main menu regardless of result
                        else:
                            print("Invalid category number.")
                            input("Press Enter to continue...")
                            return
                    except ValueError:
                        print("Please enter a valid number.")
                        input("Press Enter to continue...")
                        return
                else:
                    print("No valid domains entered.")
                    input("Press Enter to continue...")
                    return
            else:
                print("No domains entered.")
                input("Press Enter to continue...")
                return

        elif choice == "3":
            return

        else:
            print("Invalid choice. Please enter 1-3.")

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            domain = input("Enter domain name: ").strip()
            display_categories()
            try:
                cat_num = int(input("\nEnter category number: "))
                category = get_category_by_number(cat_num)
                if category:
                    dork = generate_dork(domain, category)
                    print(f"\nDomain: {domain}")
                    print(f"Category: {category}")
                    print(f"Google Dork: {dork}")
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Please enter a valid number.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            domain = random_domain()
            display_categories()
            try:
                cat_num = int(input("\nEnter category number: "))
                category = get_category_by_number(cat_num)
                if category:
                    dork = generate_dork(domain, category)
                    print(f"\nRandom domain: {domain}")
                    print(f"Category: {category}")
                    print(f"Google Dork: {dork}")
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Please enter a valid number.")
            input("\nPress Enter to continue...")

        elif choice == "3":
            print(f"\nTotal domains: {len(DOMAINS)}")
            print("\nAll domains:")
            for i, domain in enumerate(DOMAINS, 1):
                print(f"{i:3d}. {domain}")
            input("\nPress Enter to continue...")

        elif choice == "4":
            try:
                count = int(input("How many random dorks to generate? "))
                display_categories()
                cat_num = int(input("\nEnter category number: "))
                category = get_category_by_number(cat_num)
                if category:
                    print()
                    for i in range(count):
                        domain = random_domain()
                        dork = generate_dork(domain, category)
                        print(f"{i+1}. Domain: {domain}")
                        print(f"   Category: {category}")
                        print(f"   Dork: {dork}")
                        print()
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Please enter valid numbers.")
            input("\nPress Enter to continue...")

        elif choice == "5":
            domain = input("Enter domain name (or press Enter for random): ").strip()
            if not domain:
                domain = random_domain()

            display_categories()
            try:
                cat_num = int(input("\nEnter category number: "))
                category = get_category_by_number(cat_num)
                if category:
                    dork = generate_dork(domain, category)
                    print(f"\nSearching Google for: {domain}")
                    print(f"Category: {category}")
                    print(f"Dork: {dork}")
                    search_google(dork)
                    print("Opened in browser!")
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Please enter a valid number.")
            input("\nPress Enter to continue...")

        elif choice == "6":
            display_categories()
            input("\nPress Enter to continue...")

        elif choice == "7":
            domain = input("Enter domain name: ").strip()
            if domain:
                print("\nAvailable categories:")
                all_categories = get_all_categories()
                for category in all_categories:
                    print(f"- {category}")

                category_name = input("\nEnter exact category name: ").strip()
                if category_name in all_categories:
                    dork = generate_dork(domain, category_name)
                    print(f"\nDomain: {domain}")
                    print(f"Category: {category_name}")
                    print(f"Google Dork: {dork}")

                    if input("\nOpen in browser? (y/n): ").lower().startswith('y'):
                        search_google(dork)
                        print("Opened in browser!")
                else:
                    print("Category not found. Please use exact category name.")
            input("\nPress Enter to continue...")

        elif choice == "8":
            domain = input("Enter domain name: ").strip()
            if domain:
                print(f"\n=== ALL DORKS FOR {domain.upper()} ===\n")

                print("DOMAIN-BASED DORKS:")
                print("-" * 50)
                for i, (category, template) in enumerate(DORK_CATEGORIES.items(), 1):
                    dork = generate_dork(domain, category)
                    print(f"{i:2d}. {category}")
                    print(f"    {dork}")
                    print()

                print("\nEXTERNAL RECONNAISSANCE DORKS:")
                print("-" * 50)
                for i, (category, template) in enumerate(EXTERNAL_DORKS.items(), len(DORK_CATEGORIES) + 1):
                    dork = generate_dork(domain, category)
                    print(f"{i:2d}. {category}")
                    print(f"    {dork}")
                    print()
            input("\nPress Enter to continue...")

        elif choice == "9":
            multi_search_menu()

        elif choice == "10":
            clear_screen()
            print("Happy Bug Hunting! 🐛💰🚀")
            break

        else:
            print("Invalid choice. Please enter 1-10.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
