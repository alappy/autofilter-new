echo "Cloning Repo...."
git clone -b mizo https://github.com/ZauteKm/Sensiari.git /Sensiari
cd /Sensiari
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
