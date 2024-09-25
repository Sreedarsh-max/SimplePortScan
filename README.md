# SimplePortScan
This is a simple Python script for scanning ports on a specified IP address. It checks whether ports in a defined range are open or closed using the `socket` library.

## Features

- Scans a range of ports (default: 70 to 89).
- Validates the IP address format using the `IPy` library.
- Reports open and closed ports.

## Requirements

- Python 3.x
- IPy library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/simple-port-scanner.git
   cd simple-port-scanner
 
2.**Install the required library:**
   ```bash
   pip install IPy
  ```
## Usage
1.Run the script:
```bash
   python port_scanner.py
```
2.When prompted, enter the target IP address you wish to scan.
3.The script will display whether each port in the range is open or closed.
  

