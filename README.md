# backend
## Initial setup

```bash
# clone and go to dir
git clone https://github.com/GDSC-Budget-App/backend && cd backend
# make virtual env, activate, and install deps
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

## Update local
```bash
# update with remote, activate venv
git pull && source venv/bin/activate
# install/upgrade deps
pip install -r requirements.txt --upgrade
```

## Run
```py
python main.py
```
