# network-security-project
Project that determines the effectiveness of popular denial-of-service (DOS) attacks on Apache, Nginx, and Lighttpd web servers.


## Notes
- In order to switch between web servers, use `sudo systemctl stop [CURRENT WEB SERVER]` then switch `sudo systemctl start [OTHER WEB SERVER]`
- Originally we intended to upload the virtual machines that we used for our experiment, but the files were much to large to upload
- In order to setup an identical environment
  - Download Ubuntu 20.04 from [here](https://ubuntu.com/download/server)
  - Download VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads)
    - We used v6.1.22
  - To ensure network isolation, make sure to use "Host-only" adapter for all of the machines
