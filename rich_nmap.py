import os
import sys
import nmap
import threading
import time
from yaspin import yaspin
from rich.table import Table
from rich import print as rprint

def run_nmap_scan(target, options='-sn'):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=options)
    return nm

def display_summary(scan_results, os_detection=False):
    table = Table(title="Summary of Nmap Scan")
    table.add_column("Host")
    table.add_column("Hostname")
    table.add_column("Port", style="cyan")
    table.add_column("Service")

    for host in scan_results.all_hosts():
        hostname = scan_results[host].hostname()
        if 'tcp' in scan_results[host]:
            for port, info in scan_results[host]['tcp'].items():
                table.add_row(host, hostname, str(port), info['name'])

    rprint(table)

    if os_detection:
        os_table = Table(title="OS Detection")
        os_table.add_column("Host")
        os_table.add_column("OS", style="magenta")
        os_table.add_column("Accuracy", style="green")

        for host in scan_results.all_hosts():
            if 'osclass' in scan_results[host]:
                os_info = scan_results[host]['osclass']['osfamily']
                accuracy = scan_results[host]['osclass']['accuracy']
                os_table.add_row(host, os_info, accuracy)

        rprint(os_table)

def spinner_func(stop_event):
    with yaspin(text="Scanning...", color="yellow") as spinner:
        while not stop_event.is_set():
            time.sleep(0.1)  # Add a small delay to control the spinner speed

def main(target, options='-sn'):
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_func, args=(stop_event,))

    spinner_thread.start()
    scan_results = run_nmap_scan(target, options)
    stop_event.set()
    spinner_thread.join()

    os_detection = '-O' in options.split()
    display_summary(scan_results, os_detection=os_detection)

if __name__ == "__main__":
    target = input("Enter the target (IP or domain): ")
    options = input("Enter Nmap options (leave empty for default '-sn'): ")

    if not options:
        options = '-sn'

    if '-O' in options.split() and os.geteuid() != 0:
        sys.exit("This script must be run as root for OS detection.")

    main(target, options)
