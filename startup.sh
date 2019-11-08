sudo apt-get update
#curls the cript from a webpage and then passes it through bash
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
echo "Preparing to log you out"
sleep 1
echo "Remember to log back in once the terminal closes"
sleep 1
echo "Logging you out in 3"
sleep 1
echo "Logging you out in 2"
sleep 1
echo "Logging you out in 1"
sleep 1
echo "Logging you out"
logout
