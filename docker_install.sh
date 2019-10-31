#curls the script from a webpage and then passes it through bash
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
restart shell/terminal
# hello-world example
docker run --rm hello-world
