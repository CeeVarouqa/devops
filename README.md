[![CI to Docker Hub](https://github.com/CeeVarouqa/devops/actions/workflows/docker.yml/badge.svg)](https://github.com/CeeVarouqa/devops/actions/workflows/docker.yml)
# DevOps Lab 1
## Selina Varouqa

# TimeZone Simple Application

This is a very simple application providing the time in a certain timezone.
Link for all timezones that can be shown there: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#### Example: 

Request:
```
curl http://url/?timezone=Europe/Moscow
```
Response:
```
{"time":"2021-08-23 22:44:58"}
```



The entire application is contained within the `main.py` file.

`requirements.txt` contains all required dependencies for this application.

`Dockerfile` contains Docker specification.


### Run the application in a Docker container

    docker run -p 8000:8000 ceevarouqa/inno_devops_lab1

### Build a Docker container

    docker build -t ceevarouqa/inno_devops_lab1 .

### Unit Tests
Unit tests are in test_application.py, it tests the application for Europe/Moscow timezone. 
for testing, /Europe/Moscow is in the end of the URL

### Github Actions CI
Github actions CI is set in feature/ci_docker_build.
Caching is used to optimize.


