# pre-install-script


## Pre-requisites
* virtualenv
```
pip install virtualenv
```

## Setup

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Execute everything with just one command
```
curl -sL https://pre-install-script.s3.amazonaws.com/preinstall.sh > preinstall.sh && bash preinstall.sh
```

