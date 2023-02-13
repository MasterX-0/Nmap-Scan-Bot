install(){
  clear
  apt install nmap git python3 python3-pip -y
  git clone https://github.com/Dilum125/Nmap-Scan-Bot
  cd Nmap-Scan-Bot
  pip3 install -r requirements.txt
  clear
}

run(){
  python3 -m Nmap_Bot
 }
 
 install
 run
