#!/bin/bash

echo "======================================================================================================"
echo "================================ Stop previous projects and delete it ================================"
echo "======================================================================================================"
cd
sudo systemctl stop gunicorn
rm -rf webdevlab
ls -la

echo "======================================================================================================"
echo "================================ Clone repository from github ========================================"
echo "======================================================================================================"
git clone git@github.com:MdSamsuzzohaShayon/webdevlab.git
ls -la


echo "======================================================================================================"
echo "================================ Deploy Django ======================================================="
echo "======================================================================================================"
cd /home/shayon/webdevlab/server
python3 -m venv .venv
source .venv/bin/activate
echo "# Django Dot Environment" > .env
nano .env
nano core/settings.py
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
# gunicorn core:application --check-config
deactivate
cd

echo "======================================================================================================"
echo "================================ Deploy Nuxt.js ======================================================"
echo "======================================================================================================"
cd /home/shayon/webdevlab/client
echo "# Nuxt.js Dot Environment" > .env
nano .env
nano nuxt.config.ts
nano utils/keys.t
npm install --legacy-peer-deps
npm run build
npm run generate
sudo rm -rf /var/www/html
sudo cp -r .output/public /var/www/html
cd
ls -la