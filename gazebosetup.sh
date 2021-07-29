sudo -s
cd ~/Desktop
rm -rf sciroc-wip
git clone "https://gitlab.com/smart_nyuad/sciroc-wip"
chmod -R +777 sciroc-wip
cd sciroc-wip
wget "https://raw.githubusercontent.com/pal-robotics/pal_docker_utils/master/scripts/pal_docker.sh"
chmod +777 pal_docker.sh
docker pull registry.gitlab.com/smart_nyuad/sciroc-wip:1.1
docker build -t registry.gitlab.com/smart_nyuad/sciroc-wip .
./pal_docker.sh -it -v /dev/snd:/dev/snd registry.gitlab.com/smart_nyuad/sciroc-wip
