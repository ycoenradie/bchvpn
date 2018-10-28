# Bitcoin Cash VPN
Setup a prepaid VPN connection paying in Bitcoin Cash 

## Prerequisites
The project has been built and tested on an Ubuntu 16.04 server.

## Installation
```
# Become root
sudo su -

# Update system and install dependecnies
apt-get update
apt-get upgrade
apt-get install nginx certbot nodejs openvpn python3

# Clone source
git clone git@github.com:ycoenradie/bchvpn.git
mv bchvpn/ /usr/local/git_tree

# Configure OpenVPN
bash /usr/local/git_tree/openvpn-install.sh

# Make WEB and API parts run automagically at boot.
sed -i -e 's/exit 0//'
cat >> rc.local
screen -dmS bchvpn_web bash -c /usr/local/git_tree/bchvpn_web/start_web.sh
screen -dmS bchvpn_api bash -c /usr/local/git_tree/bch_vpn/start_api.sh
exit 0
```

## Operation
You can connect to the WEB daemon like this:
```
sudo su -
screen -r bchvpn_web
```

And to the API daemon like this:
```
sudo su -
screen -r bchvpn_web
```

Regularly cleanup expired users with:
```
/usr/local/git_tree/cleanup_users.sh
```

## Clients
macOS: https://tunnelblick.net/downloads.html
