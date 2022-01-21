# Python CLI
- Python 3.8.3
## Installation
Create virtual environment for python.
```bash
virtualenv venv
```
Activating the virtual environment.
```bash
source ../venv/scripts/activate
```
Install list of packages inside requirements.txt
```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
python main.py -t json
python main.py -t text
python main.py -o test.json
python main.py -t json -o testing.json
```
## Help
```bash
python main.py -h
```
