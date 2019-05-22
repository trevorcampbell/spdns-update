mkdir ~/.spdns
cp spdns.py ~/.spdns
cp spdns-config.conf ~/.spdns

echo "cron 20 * * * * python3 ~/.spdns/spdns.py" >> /etc/crontab
