echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/ZauteKm/VCVideoPlayBot /VCVideoPlayBot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/ZauteKm/VCVideoPlayBot -b $BRANCH /VCVideoPlayBot
fi
cd /VCVideoPlayBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
