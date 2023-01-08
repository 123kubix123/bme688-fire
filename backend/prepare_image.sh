docker buildx build --platform linux/arm64/v8,linux/amd64 -t dynovski/sir:multiarch --build-arg PROJECT_DIR=sir -f Dockerfile . --push

