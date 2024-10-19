#!/usr/bin/env python3
import sys
import os
import requests

url = "https://www.google.com"

def main():
    print(f"Accessing URL: {url}")
    if requests.get(url).status_code == 200:
        print("Success")
    else:
        print("Failed")

if __name__ == "__main__":
    main()