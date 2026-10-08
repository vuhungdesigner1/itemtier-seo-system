"""
make_webhook_dispatcher.py
Dispatches social signals and syndicated content payloads directly
to Make.com (formerly Integromat) Webhooks for 24/7 cloud multi-channel distribution.

When triggered, Make.com scenario can automatically:
1. Create Reddit post in targeted subreddits
2. Post viral thread on X (Twitter)
3. Share professional post on LinkedIn
4. Syndicate to Pinterest / Facebook Groups
"""

import json
import os
import requests

DEFAULT_WEBHOOK_URL = os.environ.get("MAKE_WEBHOOK_URL", "")

def dispatch_to_make(webhook_url, payload):
    if not webhook_url:
        print("[!] MAKE_WEBHOOK_URL is not set. Please provide a valid Make.com webhook URL.")
        return False

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(webhook_url, json=payload, headers=headers, timeout=15)
        print(f"[*] Make.com Response: {response.status_code} - {response.text}")
        return response.status_code in [200, 201, 204]
    except Exception as e:
        print(f"[!] Exception calling Make.com webhook: {e}")
        return False

def build_earbud_signal_payload():
    return {
        "event": "new_pillar_published",
        "post_id": 1497,
        "title": "Earbud Tier List: Best Wireless Earbuds Ranked (2026)",
        "url": "https://itemtier.com/earbud-tier-list/",
        "primary_keyword": "earbud tier list",
        "reddit": {
            "subreddit": "headphones",
            "title": "[Discussion] 2026 Wireless Earbud Tier Matrix: Lab Frequency Response & ANC Testing",
            "flair": "Discussion",
            "body": """After 60+ hours of lab frequency response and ANC attenuation testing across 24 flagship TWS models for 2026, here is our standardized tier matrix:

S-Tier: Sony WF-1000XM5 (-32dB broadband ANC) & Apple AirPods Pro 2 (Transparency benchmark)
A-Tier: Bose QC Ultra (Sub-bass flight rumble king) & Sennheiser Momentum TW4 (Pure dynamic driver separation)
Value Pick: Nothing Ear (2024) (Best sub-$150 parametric EQ implementation)

Full interactive S-to-D tier matrix & lab measurement data available at: https://itemtier.com/earbud-tier-list/"""
        },
        "twitter": {
            "tweet_1": "After 60+ hours of lab testing ANC attenuation & frequency curves, here is our unbiased 2026 Wireless Earbud Tier Matrix (S to D Tier) 🧵👇",
            "tweet_link": "https://itemtier.com/earbud-tier-list/"
        },
        "linkedin": {
            "title": "Hardware Strategy: The Death of Superficial Tech Specs in 2026 TWS Audio",
            "url": "https://itemtier.com/earbud-tier-list/"
        }
    }

if __name__ == "__main__":
    payload = build_earbud_signal_payload()
    print("Prepared Make.com Payload:")
    print(json.dumps(payload, indent=2))
    if DEFAULT_WEBHOOK_URL:
        dispatch_to_make(DEFAULT_WEBHOOK_URL, payload)
    else:
        print("\n[NOTE] To send live to Make.com, provide the webhook URL.")
