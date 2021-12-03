import os, time, random, string, requests
from discord_webhook import DiscordWebhook

webhook_url = "" # Create a webhook and enter the URL here
os.system('cls' if os.name == 'nt' else 'clear')
input("\nClassic Discord Nitro Checker w/ webhooks by nasus#5311 | MIT License\nThis tool might be slow due to unavoidable and seemingly exponential ratelimits\nMake sure there are codes in your codes.txt file\n")
while True:
    with open("codes.txt") as f:
        code = f.readline().rstrip()
    url = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if url.status_code == 200:
        print(f"Valid Code | {code}")
        DiscordWebhook(url=webhook, rate_limit_retry=True, content=f"Valid code detected! @everyone discord.gift/{code}").execute()
    elif url.status_code == 404:
        print(f"Invalid Code | {code}")
        # remove line once used
        with open('codes.txt', 'r') as f:
            data = f.read().splitlines(True)
        with open('codes.txt', 'w') as t:
            t.writelines(data[1:])
    elif url.status_code == 429:
        rate = int(url.json()['retry_after']) + 1
        print(f"Ratelimited! {round(rate, 2)}")
        time.sleep(rate)
    else:
        print(f"Invalid Error! | Status code {url.status_code}")
