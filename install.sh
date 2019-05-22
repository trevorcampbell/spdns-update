mkdir ~/.spdns
cp spdns.py ~/.spdns
cp spdns-config.conf ~/.spdns

(crontab -l 2>/dev/null; echo "*/1 * * * * python3 ~/.spdns/spdns.py &> ~/.spdns/logfile.log") | crontab -
