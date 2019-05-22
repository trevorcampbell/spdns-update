mkdir ~/.spdns
cp spdns.py ~/.spdns
cp spdns-config.conf ~/.spdns

(crontab -l 2>/dev/null; echo "*/30 * * * * python3 ~/.spdns/spdns.py 2>&1 | /usr/bin/logger") | crontab -
