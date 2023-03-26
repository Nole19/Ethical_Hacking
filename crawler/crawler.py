import requests


def get_response(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "vkino.fun"
with open("/home/nole19/Downloads/files-and-dirs-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = get_response(test_url)
        if response:
            print("[+] Discovered URL  --> " + test_url)

