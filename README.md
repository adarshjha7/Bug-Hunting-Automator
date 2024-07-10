This Python script is designed to automate a series of security tasks against a specified target, which can be either an IP address or a URL for **BUG BOUNTY HUNTERS**. Here's a breakdown of what each function in the script does:

1. ***Imports and Libraries Used:***
   - os: Standard library for interacting with the operating system.
   - nmap: Library for network discovery and security auditing.
   - subprocess: Module for spawning new processes, used here to run external commands.

2. ***Functions Defined:***

   - **perform_nmap_scan(target) Function:**
     - Uses the nmap library to perform a comprehensive scan (-A -p-).
     - Prints details of hosts, their states, protocols, open ports, and services discovered.
     - Example usage:
       python
       perform_nmap_scan("192.168.1.1")
       
     - Output example:
       
       Starting Nmap scan on 192.168.1.1...
       Host : 192.168.1.1 ()
       State : up
       ----------
       Protocol : tcp
       Port : 80    State : open
       Service : http
       ...
       

   - **perform_dirsearch(target) Function:**
     - Executes Dirsearch, a tool for web directory brute-forcing.
     - Uses subprocess to run dirsearch.py with specified arguments (-u, -e, -t, --timeout).
     - Example usage:
       python
       perform_dirsearch("http://example.com")
       
     - Output example (if error):
       
       Starting Dirsearch on http://example.com...
       Error running Dirsearch: Command '['python3', '/root/dirsearch/dirsearch.py', '-u', 'http://example.com', '-e', 'php,html,js', '-t', '100', '--timeout', '10']' returned non-zero exit status 2.
       

   - **perform_sqlmap(target) Function:**
     - Runs SQLMap, a tool for detecting and exploiting SQL injection vulnerabilities.
     - Uses subprocess to execute sqlmap with parameters (-u, --batch, --crawl, --random-agent).
     - Example usage:
       python
       perform_sqlmap("http://example.com")
       
     - Output example (if error):
       
       Starting SQLMap scan on http://example.com...
       Error running SQLMap: Command '['sqlmap', '-u', 'http://example.com', '--batch', '--crawl=3', '--random-agent']' returned non-zero exit status 1.
       

3. *Main Program Execution:*
   - Prompts the user to input a target IP address or URL.
   - Calls each function (perform_nmap_scan, perform_dirsearch, perform_sqlmap) sequentially with the user-provided target.
   - Handles exceptions raised during subprocess calls (subprocess.CalledProcessError) and prints relevant error messages if any of the tools encounter issues.

OUTPUT OF THE SCRIPT:
         
![au1](https://github.com/adarshjha7/Bug-Hunting-Automator/assets/98156564/3835a3d9-294d-4af8-9089-1250b75c99af)

![au2](https://github.com/adarshjha7/Bug-Hunting-Automator/assets/98156564/a013c63a-30fd-4962-803f-a966dfb9048c)

![au3](https://github.com/adarshjha7/Bug-Hunting-Automator/assets/98156564/737e3108-0dab-46fc-a3ff-acb9543aff1f)
