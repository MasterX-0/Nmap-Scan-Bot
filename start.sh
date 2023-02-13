install(){
  clear
  apt install nmap git python3 python3-pip -y
  pip3 install -r requirements.txt
  clear
}

run(){
  python3 -m Nmap_Bot
 }
 
 install
 run
