# guru-spoc-sp
 
aws ses: serviço de email do aws
Adding user `marcelogalli'

>>no pc
criar ssh-keygen
ls ~/.ssh
cat ~/.ssh/id_ed25519.pub

>>no servidor
nano .ssh/authorized_keys > incluir a ssh-keygen
liberar as portas de acesso 80 para http

configurar o linux
1 - apt-get update && apt-get upgrade
2 - adduser guruspoc
3 - usermode -aG  sudo guruspoc
4 - id guruspoc
5 - rsync --archive --shown=guruspoc:guruspoc ~/.ssh /home/guruspoc
6 - install pacote docker
7 - sudo systemctl enable docker
8 - (verificar) sudo systemctl status docker
9 - (verificar) docker --version and docker compose version
10 - (firewall)sudo ufw status numbered
11 - sudo ufw allow 22/tcp
11 - sudo ufw enable
12 - sudo reboot
13 - (conferir)sudo ufw status numbered
14 - adicionando portas sudo ufw allow 80
14 - adicionando portas sudo ufw allow 443
14 - adicionando portas sudo ufw allow 81

>>install portainer
1 - sudo docker volume create portainer_data
2 - sudo docker network create guru_sp_nw
3 - sudo docker network ls
4 - sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --network=guru_sp_nw --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
5 - sudo docker ps
6 - sudo docker network inspect guru_sp_nw