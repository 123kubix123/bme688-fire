docker buildx build --platform linux/arm64/v8,linux/amd64 -t dynovski/sir_app:multiarch  -f Dockerfile . --push
