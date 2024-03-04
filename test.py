import os
import requests
print ("Hello")
print ("Good to know")
print ("Leo the badass")
print ("Hola, Como Estas")


def main():
    for x in range(1,5):
        print (x)
    
    url = "https://google.com"
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    print(r.is_redirect)
    print (r.url)




if __name__ == "__main__":
    main()