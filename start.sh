echo "Cloning Repo...."
git clone -b master https://github.com/dqanshi/autofilter-new /autofilter-new
cd /Sensiari
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
