## Installation

**NOTE**: Python 3.7 or higher is required


```bash
# clone the repo
$ git clone https://github.com/ZetrextJG/Auto-Deutch.git

#Iinstall python3 and python3-pip if thery are not installed
$ https://www.python.org/

```


# Download and Install Tesseract 32 bit or 64 bit version WINDOWS:
```bash
$ https://github.com/UB-Mannheim/tesseract/wiki
# Add tesseract folder to PATH (default: C://Program Files//Tesseract-OCR)
```


# Intall tesseract 32 bit or 64 bit version LINUX:
```bash
$ sudo apt-get update
$ sudo apt-get install tesseract-ocr
$ sudo apt-get install libtesseract-dev
```


```bash
# Install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```bash
$ python3 auto-deutch.py

# Wait for the GUI to pop up
# Press the green button to start screen capturing and select wanted area
# Wait for the webbrowser to pop up with your translation

# Enjoy
```

## Settings
```bash
$ python3 auto-deutch.py --pln 1
# This command runs appliaction in experimental mode that translates text straight to Polish language.
```


## CREDITS

Screen capturing with tkinter by stack-overflow user Brett Lapierre