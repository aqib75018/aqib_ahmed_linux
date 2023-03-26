curl https://capital.com/fr/graphique-de-ltc-eur > /home/ec2-user/projet_linux/ltc_eur.txt
price=$(cat /home/ec2-user/projet_linux/ltc_eur.txt | grep -oP '(?<="h2 sharesNameVal__price js-price-sell">)[^<]+')
echo "$(date),$price" >> /home/ec2-user/projet_linux/prix.csv
sudo fuser -k 8050/tcp
/usr/bin/python3 /home/ec2-user/projet_linux/aqibahmed.py
