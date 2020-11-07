
'''Defining Variables'''
PATH = r"C:\Windows\System32\drivers\etc\hosts"
DOMAINS = ["amazon","instagram","twitter","youtube"]
REDIRECT = "127.0.0.1"
allSites = [(f"www.{domain}.com",f"{domain}.com",f"https://www.{domain}.com") for domain in DOMAINS]

'''Block function to block defined sites when session starts'''
def block():
    global allSites,DOMAINS
    '''writing websites in the file'''
    with open(r"./details/blocked.txt","r+") as file:
        content = file.read()
        for site in allSites:
            for allDomains in site:
                if allDomains in content:
                    pass
                else :
                    file.write(f"{REDIRECT} {allDomains} \n")

'''Unblock function to unblock all the sites when session is ended'''
def unblock():
    global allSites
    allDomains = [domains for site in allSites for domains in site]
    with open(r"./details/blocked.txt","r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(url in line for url in allDomains):
                file.write(line)
        file.truncate()
