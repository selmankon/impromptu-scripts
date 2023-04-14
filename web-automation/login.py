import argparse
import requests

parser = argparse.ArgumentParser(description='Script to login to a web application')
parser.add_argument('url', type=str, help='URL of the web application to login')
parser.add_argument('--username', type=str, help='Username')
parser.add_argument('--password', type=str, help='Password')
args = parser.parse_args()

login_data = {
    'username': args.username,
    'password': args.password
}

response = requests.post(args.url, data=login_data)

if response.status_code == 200:
    print("[+] Login successful. Redirecting to the homepage...")
else:
    print("[!] Login failed. Incorrect username or password.")
    exit(1)
