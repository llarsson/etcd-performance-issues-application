#!/bin/bash

set -eo pipefail

TAG=${TAG:-latest}

REPO="repo-name-goes-here"
IMAGE="etcd-performance-issues-application"

python3 convert_images.py

docker build -t ${REPO}/${IMAGE}:${TAG} .
docker push ${REPO}/${IMAGE}:${TAG}
