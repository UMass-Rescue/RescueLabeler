# Rescue Labeler

![Test Cases](https://github.com/UMass-Rescue/RescueLabeler/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/UMass-Rescue/RescueLabeler/branch/master/graph/badge.svg?token=X91OV1AX3O)](https://codecov.io/gh/UMass-Rescue/RescueLabeler)



## API

Non Docker build command

```bash
source labeler_api/run_debug_app.sh
```

Docker build commands

API Compose

```bash
docker-compose -f docker-compose.api.yml build

# Testing
docker-compose -f docker-compose.api.yml run

# Deployment
docker-compose -f docker-compose.api.yml up
```


API Standalone Container:

```bash
docker build -t labeler_api:latest labeler_api
docker run -it -p 80:80 labeler_api
```

## CLI

Todo...

## Client Web app

Todo...


## Author

Jagath Jai Kumar
