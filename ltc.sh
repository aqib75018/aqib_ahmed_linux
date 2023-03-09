curl https://www.coingecko.com/fr/pi%C3%A8ces/litecoin > /home/ec2-user/projet_linux/ltc_eur.txt
cat /home/ec2-user/projet_linux/ltc_eur.txt | grep -m 1 -oP '(?<="price.price">)[^<]+' | tr -d '$' | tr ',' '.' >> /home/ec2-user/projet_linux/prix.csv
sudo fuser -k 8050/tcp
/usr/bin/python3 /home/ec2-user/projet_linux/aqibahmed.py
