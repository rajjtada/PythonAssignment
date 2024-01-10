import subprocess
import requests
import time

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"
    except Exception as e:
        return f"Error: {str(e)}"

def bytes_to_gb(bytes_value):
    gb_value = round(float(bytes_value) / (1024 ** 3), 2)
    return f"{gb_value} GB"

def is_internet_connected():
    try:
        result = run_command('ping google.com')
        return "Request timed out" not in result
    except Exception:
        return False

#1st Task    
def get_installed_software():
    result = run_command('wmic product get name')
    if not result:
        print("No software information available.")
    else:
        print(result)

#2nd Task
def get_internet_speed():
    if is_internet_connected():
        result = run_command('speedtest-cli --simple')
        if 'Cannot retrieve speedtest configuration' in result:
            print("Unable to retrieve internet speed.")
        else:
            print(result)
    else:
        print("Not connected to the internet. Unable to retrieve internet speed.")

#3rd Task
def get_screen_resolution():
    print(run_command('wmic desktopmonitor get screenwidth,screenheight'))

#4th Task
def get_cpu_model():
    print(run_command('wmic cpu get caption'))

#5th Task
def get_cpu_cores_threads():
    print(run_command('wmic cpu get numberofcores,numberoflogicalprocessors'))

#6th Task
def get_gpu_model():
    result = run_command('wmic path win32_videocontroller get caption')
    if not result:
        print("No GPU information available.")
    else:
        gpu_models = result.split('\n')[1:]
        for model in gpu_models:
            print(f"GPU Model: {model.strip()}")

#7th Task
def get_ram_size():
    result = run_command('wmic memorychip get capacity')
    if not result:
        print("No RAM information available.")
    else:
        capacity_lines = result.split('\n')[2:]
        capacities = [int(line.strip()) for line in capacity_lines if line.strip()]
        total_capacity = sum(capacities)
        print("RAM Size:", bytes_to_gb(total_capacity))

#8th Task
def get_screen_size():
    result = run_command('wmic desktopmonitor get screensize')
    if not result or "Invalid query" in result:
        print("Screen size information not available.")
    else:
        screensize_lines = result.split('\n')[1:]
        screensizes = [line.strip() for line in screensize_lines if line.strip()]
        print("Screen Size:", ', '.join(screensizes))

#9th Task
def get_mac_address():
    print(run_command('getmac'))

#10th Task
def get_public_ip():
    if is_internet_connected():
        try:
            response = requests.get('https://httpbin.org/ip')
            public_ip = response.json().get('origin')
            if public_ip:
                print("Public IP Address:", public_ip)
            else:
                print("Unable to retrieve public IP address.")
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.ConnectionError):
                print("Error: Unable to connect to the external service. Check your internet connection.")
            else:
                print(f"Error retrieving public IP address: {str(e)}")
    else:
        print("Not connected to the internet. Unable to retrieve public IP address.")

#11th Task
def get_windows_version():
    print(run_command('systeminfo | find "OS Name"'))

while(True):
    time.sleep(2)
    print("\n")
    print("Select the information you want to know:\n")
    print("1) Installed Softwares List\n2) Internet Speed\n3) Screen Resolution\n4) CPU Model\n5) Numbers of Cores and Threads of CPU\n6) GPU Model\n7) RAM Size\n8) Screen Size\n9) Wifi/Ethernet MAC Address\n10) Public IP Address\n11) Windows Version\n12) Exit.\n\n")
    choose = input("Enter your choice: ")

    if choose == "1":
        get_installed_software()

    elif choose == "2":
        get_internet_speed()

    elif choose == "3":    
        get_screen_resolution()

    elif choose == "4":
        get_cpu_model()

    elif choose == "5":
        get_cpu_cores_threads()

    elif choose == "6":
        get_gpu_model()

    elif choose == "7":
        get_ram_size()

    elif choose == "8":
        get_screen_size()

    elif choose == "9":
        get_mac_address()

    elif choose == "10":
        get_public_ip()

    elif choose == "11":
        get_windows_version()
        
    elif choose == "12":
        break
    
    else:
        print("Choose correct option") 
        continue   

