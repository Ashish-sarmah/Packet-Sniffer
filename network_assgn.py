 
# For Detailed Explaination of Each Function Read Readme File: 

import sys
from scapy.all import *
def extract_cookies(load):
    if "http" in load:
        # Extract cookies from the HTTP headers
        headers = load.split('\r\n')
        cookies = {}
        for header in headers:
            if "cookie:" in header:
                cookie_data = header.split('cookie: ')[1].split(';')
                for cookie in cookie_data:
                    cookie_name, cookie_value = cookie.split('=',1)
                    cookies[cookie_name.strip()] = cookie_value.strip()
        # Print the extracted cookies
        if cookies:
            print()
            print("COOKIES:")
            print()
            for name, value in cookies.items():
                print(f"{name}:    {value}")
                print()
        else:
            print('NO COOKIES IS THERE')
                
                
def extract_cred(load):
    if "http" in load:
        # Extract cookies from the HTTP headers
        headers = load.split('\r\n')
        s=['username','userid','password']
        for i in range(0,len(s)):
            values=[]
            search_word=s[i]
            for header in headers:
                if(search_word in header):
                    data = header.split(search_word)[1].split(';')
                    values=values+data
            if values:
                print()
                print(search_word.upper())
                print()
                print()
                for value in values:
                    print(f"{search_word}: {value}\n")
                    print()
    
        

def search(text,keyword):
    import re
    # Search for the pattern within the text
    new_keyword=keyword.lower()
    new_keyword=new_keyword.split(" ")
    for kwrd in new_keyword:
        matches = re.search(kwrd, text)
        if(matches):
            return True
    return False



def packet_callback(packet):
     # Corrected variable name
    global Packet_count 
    packet_str = str(packet.show(dump=True))
    packet_str = packet_str.lower()
    x_y = x.lower()

    if search(packet_str, x_y):
        Packet_count += 1  # Corrected variable name

        print('**********************************************PACKET START****************************************************************')

        extract_cookies(packet_str)
        extract_cred(packet_str)

        print('***************************************************************************************************************************')
        print(packet_str)
        print('**********************************************PACKET END********************************************************************')
        print()
        print()
        if Packet_count >= 1000:
            sys.exit(0)

        
        
def get_all_interfaces():
    import scapy.all as scapy
    interfaces = scapy.get_if_list()
    for interface in interfaces:
        interface = scapy.ifaces[interface].name
    # print("Interfaces:", interfaces)
    return interfaces

def packet_sniffer():

    
    # interfaces =[]
    # interfaces.append("\\Device\\NPF_Loopback")
 
    # print(interfaces)
    
    #if Site is hosted online
    sniff(prn=packet_callback,store=0)
    
    ## If website is running on localhost Please Comment 107th code line and uncomment 110th
    # sniff(prn=packet_callback, iface="\\Device\\NPF_Loopback",store=0)
    
Packet_count=0    

if __name__ == "__main__":
    
    # Call the packet_sniffer function to start capturing packets
    keyword_inp = input("input Keyword You want to Search: ")
    global x
    x = keyword_inp
    
    
    sys.stdout = open('output.txt', 'w', encoding='utf-8')
    sys.stderr = open('output.txt', 'w', encoding='utf-8')
   
    packet_sniffer()