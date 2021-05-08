# network-security-project
Project that determines the effectiveness of popular denial-of-service (DOS) attacks on Apache, Nginx, and Lighttpd web servers.


## Notes
- In order to switch between web servers, use `sudo systemctl stop [CURRENT WEB SERVER]` then switch `sudo systemctl start [OTHER WEB SERVER]`
- To ensure network isolation, make sure to use "Host-only" adapter for all of the machines
