# remote-control-with-email-service



<span style="font-weight: bold;">Content:</span>
<ul>
    <li><a href="#try-our-app">Try our app</a></li>
    <li><a href="#build-app">Build the app from source codes</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
</ul>

## 1. Try our app
<h5 id="try-our-app"></h5>

Get the lastest version of our app by following these steps
```bash
curl -fsSL github.com/htrvu/remote-control-with-email-service/releases/download/v1.9/G8-Remote-Control.zip -O
unzip -q G8-Remote-Control.zip -d G8-Remote-Control
```

## 2. Build the app from source codes
<h5 id="build-app"></h5>

Firstly, you must have `python`,`pyinstaller`, and `pyqt5` installed. Then, follow these steps:

### 2.1. Clone this repository
```bash
git clone https://github.com/htrvu/remote-control-with-email-service remote-control-with-email-service
cd remote-control-with-email-service
```

### 2.2. Build the source codes

```bash
cd ./src/ # path to client folder
pyinstaller main.spec

cd .. # path to source folder

mkdir ./G8-Remote-Control
mkdir ./G8-Remote-Control/ui

mv ./src/dist/G8-Remote-Control.exe ./G8-Remote-Control/G8-Remote-Control.exe 
cp -r ./src/ui/assets ./G8-Remote-Control/ui

rm -rf ./src/dist  ./src/build
```


## 3. Screenshots
<h5 id="screenshots"></h5>