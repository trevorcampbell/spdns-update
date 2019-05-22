mkdir ~/.spdns
cp spdns.py ~/.spdns
cp spdns-config.conf ~/.spdns

echo "1 * * * * python3 ~/.spdns/spdns.py > ~/.spdns/logfile.log" >> /etc/crontab
