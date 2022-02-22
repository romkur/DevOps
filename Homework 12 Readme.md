### Hadoop cluster in docker
1. Pull images 

         docker pull romkur/headnode:latest
         docker pull romkur/worker:latest
2. Download docker-compose.yml and Makefile
3. Run in directory with docker-compose.yml and Makefile

         make run
         
5. Wait when cluster start
6. See http://localhost:9870 for NameNode or http://localhost:8088 for ResourceManager.
