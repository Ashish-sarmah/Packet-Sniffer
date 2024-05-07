# Packet-Sniffer
A packet sniffer made using scapy library in python that could filter packets and extract information.

To use the provided network_assgn.py script, follow these steps:
1. Run the Code:
   - Execute the network.py script using the following command:
           python network.py
   {NOTE}: if sniffed packets are loopback(localhost) do the following change in code: [step1] comment codeline 107 , [step2] uncomment codeline 110
2. Enter the Keyword:
   - When prompted, enter the keyword you want to search for in the network traffic.
3. Observe the Output:
   - The script will start sniffing packets and monitoring the network traffic.
   - Whenever a packet is found that contains the specified keyword, the script will output the following information in output.txt:
     - The entire packet content
     - Any cookies found in the packet
     - Any user credentials (username, userid, password, user) found in the packet
4. An Ouput.txt file will be generated which will contain the information regarding the packets based on you keyword.
   The file will contain the information regarding atmost 10 packets found only.

5. Packet Sniffing limit we have set to 100, But you change it by changing in 85th code line
6. As we know not every packet contains cookies, so it may happen no cookies are there in fetched packet, So you can run the code again and explicitly provide input word as 'cookie' or something else{you may want to search}.
 
Regarding the implementation:
1. extract_cookies(load):
   - This function extracts any cookies found in the header.
   - It parses the header, identifies the cookie information, and prints the extracted cookies in the key value readable format.
2. extract_cred(load):
   - This function takes the HTTP header of a packet as input and extracts any user credentials (username, userid, password, user) found in the header.
   - It searches for specific keywords (username, userid, password, user) in the header, extracts the corresponding values, and prints them in a readable format.
3. search(text, keyword):
   - This function takes the entire packet content as a string and a keyword as input.
   - It searches for the keyword (case-insensitive) in the packet content and returns `True` if the keyword is found, `False` otherwise.
By providing the desired keyword as input, the script will start sniffing the network traffic and output the packet content, cookies, and user credentials whenever a matching packet is found.


