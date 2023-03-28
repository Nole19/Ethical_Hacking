# Pentesting Tools Collection


* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [DNS and ARP spoof](#dns-and-arp-spoof)
* [Keylogger](#keylogger)
* [Replace and download](#replace-and-download)
* [Disclaimer](#disclaimer)


## General Information
-This repository contains a collection of different scripts and programs related to penetration testing. These tools can be used for various purposes such as keylogger(keylogger folder) installation, Man in the middle attack(replace_and_download folder), DNS and ARP spoofing(Spoof folder).


## Technologies Used
- Python 
- Libraries: scapy
NetfilterQueue
pynput
bs4
base64
socket


## DNS and ARP spoof
Description
This script allows an attacker to redirect network traffic by spoofing DNS and ARP requests. It can be used to intercept communication, steal sensitive information or execute attacks such as phishing.

Usage
Clone the repository to your local machine
```bash
$ git clone https://github.com/Nole19/Ethical_Hacking/tree/main/Spoof
```
It contains 5 files. 
DNS spoofing script is file named dns_spoof.py.To run we need put next command: 
```bash
$ python dns_spoof.py
```

In this example it connected with "Man in the middle (MITM)" – The interception of communications between users and a DNS server in order to route users to a different/malicious IP address. We can connect with our file download_execute_report. In this example written backdoor named lazagne.exe. With help of this file we can force the victim to download. The it will be executed and wrotten in computer boot. So, even after restart it'll work. 



ARP spoofing is file named arpspoof.py. But first we need to run network_scanner.py for scanning all networks with mac adresses:
```bash
$ python network_scanner.py
```

We'll get all information about networks above us. This information we need to use in file arpspoof.py. Put victim mac and yours. Then we can run file:
```bash
$ python run arpspoof.py
```
This is also a Man in the Middle (MitM) attack that allows attackers to intercept communication between network devices. So, the router thinks that we are actually victim. And we are getting all information between router and victim. 



At the same directory we have file named arpspoofing_detector.py. It helps to detect if somebody attacking you. To run this file: 
```bash
$ python arpspoofing_detector.py
```


## Keylogger

Description
This script installs a keylogger on a target machine to capture the user's keystrokes. It can be used to steal sensitive information such as passwords, credit card numbers or other personal data.

Usage
Clone the repository to your local machine
```bash
$ git clone https://github.com/Nole19/Ethical_Hacking/tree/main/keylogger
```
It works with our email. So, we need to create your mail for this and put inside file zlogger.py with password. And all information will send to our email.
To turn on run the following command:
```bash
$ python zlogger.py
```


## Replace and download

Description
This script allows an attacker to intercept communication between two parties by placing themselves between them. It can be used to steal sensitive information such as login credentials, financial data or other confidential information.

Usage
Clone the repository to your local machine
```bash
$ git clone https://github.com/Nole19/Ethical_Hacking/tree/main/replace_and_download
```

Run the file:
```bash
$ python replace_download.py
```
For this you need to be connected to the same network with victim. Only after this you can replace file with yours.

## Features
Here you can find different types of malwares and scripts.
- Keylogger. It sends all info to your mail. You should add mail and password in file 
- Network attacks. Scanner of networks. Arp and dns spoofing.
- Replace and download. Replaces inside network files to download. Works with backdoor 
- Valnurability scanner. Scans your system for different malware



## Disclaimer
These tools are intended for educational and ethical purposes only. The use of these tools for malicious purposes is strictly prohibited. The authors of these tools are not responsible for any damages caused by the misuse of these tools. Use at your own risk.
