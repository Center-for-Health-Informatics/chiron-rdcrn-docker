## Install Chiron RDCRN Website Using Docker

1. Install Docker and Docker Compose
    - https://docs.docker.com/get-docker/
    - for Windows and Mac, you can install Docker Desktop which includes both Docker and Docker Compose
    
    
2. Clone this repository
   - you must have git installed
   - as an alternative, you could simply copy the file `docker-compose.yaml` to your system
```shell
git clone https://github.com/Center-for-Health-Informatics/chiron-rdcrn-docker.git
```

3. Run the docker-compose file
```shell
cd chiron_rdcrn_docker
docker compose up
```

4. view in browser
   - after starting up (may take several minutes), your site should be available on port 8008
   - open a web browser and open http://localhost:8008
   
## Modifications

- to change the port to something besides 8008, edit nginx ports in `docker-compose.yaml`

   
