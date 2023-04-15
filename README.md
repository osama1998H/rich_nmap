## rich\_nmap

`rich_nmap` is a Python-based command-line tool that provides a user-friendly interface for running Nmap scans and displaying the results. With its intuitive table output, color-coded information, and loading indicator, `rich_nmap` aims to make network scanning a smoother experience for both beginners and experienced users.

## Features

*   Easy-to-use interface for running Nmap scans
*   Table-based output for scan results
*   Color-coded information for better readability
*   OS detection support (requires root privileges)
*   Loading indicator during scans

## Installation

Clone the repository or download the source code:

```python
git clone https://github.com/osama1998H/rich_nmap.git
```

 Change into the `rich_nmap` directory:

```plaintext
cd rich_nmap
```

Install the required packages:

```plaintext
sudo pip install -r requirements.txt
```

**Note**: Make sure to install the requirements for all users, including root, as OS detection requires root privileges.

Usage  
Run the script:

```plaintext
python rich_nmap.py
```

*   Enter the target (IP or domain) and Nmap options when prompted.
*   View the formatted results in a table-based output.  
     

## Contributing

  
We welcome contributions to rich_nmap! If you're interested in improving the tool, adding new features, or fixing bugs, please feel free to submit a pull request or open an issue to discuss your ideas. We appreciate your support in making `rich_nmap` better for everyone.
