#!/bin/bash
USER="hidenariyuda"
APP_NAME="runpod-style-bert-vits2-api"
VERSION=1.0.0

# VERSIONを目視で確認するのでy/Nで確認
echo "Is the version $VERSION?"
read -p "y/N: " yn
case "$yn" in [yY]*) ;; *) echo "interrapted" ; exit ;; esac

# git tag -a $VERSION -m "$VERSION"

# buildコマンド
sudo DOCKER_BUILDKIT=1 docker build --progress=plain . -f Dockerfile.runpod -t $USER/$APP_NAME:$VERSION

# pushコマンド
docker push $USER/$APP_NAME:$VERSION