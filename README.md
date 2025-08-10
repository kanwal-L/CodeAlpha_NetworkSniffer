CodeAlpha Internship - Task 1  
Basic Network Sniffer

Name: LARAIB KAWNAL  



   ⁜ Task Description
For this task, I had to create a simple Python program that can:
- Capture network traffic packets in real time
- Analyze the captured packets to understand their structure
- Learn how data flows in a network and basic protocols
- Display details like:
  - Source IP address
  - Destination IP address
  - Protocol number
  - Packet length


   ⁜ How I Made It
I used Python's **socket** and **struct** libraries to directly capture raw packets from the network.  
This method avoids the need for external libraries like Scapy and works on Windows, as long as the script is run with **administrator rights**.

 The script:
1. Creates a raw socket
2. Binds it to the local machine's IP
3. Reads incoming packets
4. Extracts the IP header information
5. Displays Source IP, Destination IP, Protocol, and Length


 ⁜ Requirements
- Python 3.x
- Windows OS
- Run Command Prompt or PowerShell as **Administrator**



  ⁜ How to Run
1. Open PowerShell/Command Prompt **as Administrator**  
2. Go to the folder where `network_sniffer.py` is located:
   ```powershell
   cd "path\



