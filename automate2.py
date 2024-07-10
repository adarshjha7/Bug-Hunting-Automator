import os
import nmap
import subprocess

def perform_nmap_scan(target):
    nm = nmap.PortScanner()
    print(f"Starting Nmap scan on {target}...")
    nm.scan(hosts=target, arguments='-A -p-')  # Comprehensive scan
    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print("----------")
            print(f"Protocol : {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port : {port}\tState : {nm[host][proto][port]['state']}")
                print(f"Service : {nm[host][proto][port]['name']}")

def perform_dirsearch(target):
    print(f"Starting Dirsearch on {target}...")
    dirsearch_path = "/root/dirsearch/dirsearch.py"
    try:
        subprocess.run(["python3", dirsearch_path, "-u", target, "-e", "php,html,js", "-t", "100", "--timeout", "10"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Dirsearch: {e}")

def perform_sqlmap(target):
    print(f"Starting SQLMap scan on {target}...")
    try:
        subprocess.run(["sqlmap", "-u", target, "--batch", "--crawl=3", "--random-agent"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running SQLMap: {e}")

if _name_ == "_main_":
    target = input("Enter target IP address or URL (e.g., 192.168.1.1 or http://example.com): ")

    # Perform Nmap scan
    perform_nmap_scan(target)

    # Perform Dirsearch for web directory enumeration
    perform_dirsearch(target)

    # Perform SQLMap scan for SQL injection vulnerabilities
    perform_sqlmap(target)