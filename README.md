# backend
## Initial setup

```bash
# clone and go to dir
git clone https://github.com/GDSC-Budget-App/backend && cd backend
# make virtual env, activate, and install dependencies
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

# Update local
```bash
# update with remote, ensure venv activated
git pull && source venv/bin/activate
# install/upgrade dependencies
pip install -r requirements.txt --upgrade
```

## Run
```py
python main.py
```
