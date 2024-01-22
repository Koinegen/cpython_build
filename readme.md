# Cython + pyinstaller build example

 - Using python 3.11.4

1) Create venv
```bash
python3.11 -m venv .venv
```

2) Install requiremetns
```bash
sudo apt install python3-dev gcc libpython3.11
./.venv/bin/python -m pip install -r ./requirements.txt
```

3) Run build
```bash
chmod +x build.sh
./build.sh
```

4) Run app
```bash
chmod +x ./dist/hello
./dist/hello
```

PROFIT!



