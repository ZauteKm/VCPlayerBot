echo "Cloning Repo...."
git clone https://github.com/ZauteKm/VCVideoPlayBot /VCVideoPlayBot
cd /VCVideoPlayBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
