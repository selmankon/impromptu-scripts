import requests

files = {
    #              (FILE_NAME, FILE_CONTENTS, FILE_MIMETYPE)
    "uploaded_file": ("phpinfo.php", b"<?php phpinfo() ?>", "application/x-httpd-php")
}

response = requests.post("https://example.com", files=files)

if response.status_code == 200:
    print("[+] File uploaded successfully!")
else:
    print("[!] File upload failed. Status code:", response.status_code)
    exit(1)
