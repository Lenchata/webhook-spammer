import time
from discord_webhook import DiscordWebhook
times=input("How many times do i have to spam it?\n")
webhook_url=input("Webhook URL:\n")
delay=input("Delay (in seconds):\n")
content=input("Webhook message:\n")
webhook = DiscordWebhook(url=webhook_url, content=content)
for x in range(int(times)):
    time.sleep(float(delay))
    response = webhook.execute()
    print("x")
