https://gchq.github.io/CyberChef/

What is an origin in a URL?
Create a diagram for Same Origin Policy

Secret Sauce

Read JavaScript 
Search for hidden end-points, insecure programming logic and secret keys. 

Setup

- Kali Linux
- Firefox for work
- Brave for research
- Download Burp Suite
- Configure Firefox to route traffic through proxy

Page 48 Bug Bounty Bootcamp The Guide to Finding and Reporting Web Vulnerabilities 

-  install Burp’s certificate on Firefox 
- Test setup : page 51

Burp

- Intruder - Automate attacks
- Repeater - Manipulate individual requests
- Decoder - Decode encoded content
- Comparer - Compare requests and responses

- Play with Proxy Page 52
- Intruder Page 54
- Repeater page 56
- Decode - 57
- Comparer - 58

Recon

Google Dorking

- site
- inurl
- intitle
- link
- filetype
- wildcard
- Quotes
- |
- -

https://www.exploit-db.com/google-hacking-database/

- whois
- Reverse whois https://viewdns.info/reversewhois/
- nslookup domain-name
- Reverse IP lookup
- netrange
- ASN
- crt.sh https://crt.sh/?q=facebook.com&output=json
- Censys, and Cert Spotter 

Subdomain Enumeration

- Sublist3r, SubBrute, Amass, and Gobuster can enumerate

You can build a tool that combines the results of multiple tools to achieve the best results.

https://github.com/danielmiessler/SecLists/

https://github.com/assetnote/commonspeak2

Remove duplicates:
sort -u wordlist1.txt wordlist2.txt

Subdomain brute-forcing:
gobuster dns -d target_domain -w wordlist

find subdomain based on patterns:

https://github.com/infosec-au/altdns/

Use the knowledge of tech stack:

jenkins.domain.com

 You can find subdomains
of subdomains by running enumeration tools recursively: add the results of your
first run to your Known Domains list and run the tool again.

 Nmap or Masscan for active scanning.

Shodan

Censys and Project Sonar. Combine the information you gather from different databases for the best results. With
these databases, you might also find your target’s IP addresses, certificates,
and software versions.

    Dirsearch or Gobuster for directory brute-forcing.

./dirsearch.py -u scanme.nmap.org -e php

gobuster dir -u target_url -w wordlist

https://github.com/FortyNorthSecurity/EyeWitness/
https://github.com/dxa4481/Snapper/
https://www.zaproxy.org/

site:s3.amazonaws.com COMPANY_NAME
site:amazonaws.com COMPANY_NAME
amazonaws s3 COMPANY_NAME
amazonaws bucket COMPANY_NAME
amazonaws COMPANY_NAME
s3 COMPANY_NAME

https://buckets.grayhatwarfare.com/
https://github.com/nahamsec/lazys3/



