# System Information Retrieval Script

This Python script allows users to retrieve various system information on a Windows system using `WMIC` commands and external services.

## Prerequisites

- Ensure that Python is installed on your system.
- Install required Python libraries:

    ```bash
    pip install requests
    ```

## Usage

1. Run the script:

    ```bash
    python SystemDetails.py
    ```

2. The script will display a menu with options to retrieve different system information.

3. Choose the desired option by entering the corresponding number.

4. The script will display the requested system information.

5. Repeat the process as needed or choose option 12 to exit the script.

## Features

1. **Installed Software List (`get_installed_software`):**
    - Retrieves and displays a list of installed software on the system.

2. **Internet Speed Test (`get_internet_speed`):**
    - Checks for internet connectivity and performs a speed test using `speedtest-cli`.

3. **Screen Resolution (`get_screen_resolution`):**
    - Retrieves and displays the screen width and height.

4. **CPU Model (`get_cpu_model`):**
    - Retrieves and displays the CPU model information.

5. **Number of CPU Cores and Threads (`get_cpu_cores_threads`):**
    - Retrieves and displays the number of CPU cores and logical processors.

6. **GPU Model (`get_gpu_model`):**
    - Retrieves and displays GPU model information.

7. **RAM Size (`get_ram_size`):**
    - Retrieves and displays the total RAM size in gigabytes.

8. **Screen Size (`get_screen_size`):**
    - Retrieves and displays the screen size.

9. **Wi-Fi/Ethernet MAC Address (`get_mac_address`):**
    - Retrieves and displays the MAC address.

10. **Public IP Address (`get_public_ip`):**
    - Checks for internet connectivity and fetches the public IP address using an external service.

11. **Windows Version (`get_windows_version`):**
    - Retrieves and displays the Windows OS version.

## Note

- Ensure the system is connected to the internet for tasks involving internet speed, public IP, and external services.

- The script incorporates a 2-second pause between iterations to enhance user experience.
