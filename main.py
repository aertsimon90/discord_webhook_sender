import requests, os
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print(f"Discord Webhook Data Sender v1.0.0\nby aertsimon90\n")
url = input("Enter URL: ")
print("Lets write your message and press enter button to sending")
print("Enter exitnow to exit")
while True:
	a = input("$ ")
	if a == "exitnow":
		break
	data = {"content": str(a)}
	b = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
	print(f"Send √ [{b.status_code}]")
