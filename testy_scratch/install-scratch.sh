cd ~
apt-get install p7zip-full
curl -sL https://deb.nodesource.com/setup_13.x | bash -
apt-get install -y nodejs
npm install electron@4.1.4 --save-dev
ls ~/node_modules/electron/dist
rm -rf /tmp/scratch-desktop
mkdir /tmp/scratch-desktop
wget -O /tmp/scratch-desktop.exe 'https://downloads.scratch.mit.edu/desktop/Scratch%20Desktop%20Setup%203.6.0.exe'
7za x -aoa -y /tmp/scratch-desktop.exe -o/tmp/scratch-desktop
cp -rf ~/node_modules/electron/dist/* /tmp/scratch-desktop/
ln -fsr /tmp/scratch-desktop/electron /tmp/scratch-desktop/scratch-desktop
mkdir ~/scratch
mv /tmp/scratch-desktop ~/scratch

