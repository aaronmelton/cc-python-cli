#!/bin/bash

# GIT_REPO must contain URL to the repo in order to use docker push
# URL set to GitHub by default; Will need to change for GitLab use.
GIT_REPO="ghcr.io/{{ cookiecutter.project_slug }}"

ask() {
    # https://djm.me/ask
    local prompt default reply
    if [ "${2:-}" = "Y" ]; then
        prompt="Y/n"
        default=Y
    elif [ "${2:-}" = "N" ]; then
        prompt="y/N"
        default=N
    else
        prompt="y/n"
        default=
    fi
    while true; do
        # Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [$prompt] "
        # Read the answer (use /dev/tty in case stdin is redirected from somewhere else)
        read reply </dev/tty
        # Default?
        if [ -z "$reply" ]; then
            reply=$default
        fi
        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac
    done
}

build_image() {
    if [[ ! -z "$VERSION" ]]; then
        docker build --platform linux/amd64 -t $GIT_REPO:$TYPE -t $GIT_REPO:$VERSION -f Dockerfile .
    else
        docker build --platform linux/amd64 -t $GIT_REPO:$TYPE -f Dockerfile .
    fi
}

build_test() {
    docker build --platform linux/amd64 --target test -t $GIT_REPO:$TYPE -f Dockerfile .
}

prune_images() {
    echo
    if ask "Clean build images?" Y; then
        yes | docker image prune --filter "label=name="$GIT_REPO --filter "label=prune=true"
    else
        echo
    fi
}

push_image() {
    if [[ ! -z "$VERSION" ]]; then
        docker push $GIT_REPO:$TYPE
        docker push $GIT_REPO:$VERSION
    else
        docker push $GIT_REPO:$TYPE
    fi
}

echo "GitHub/GitLab Image Type"
echo "------------------------"
OPTIONS=("Code Check" "Development" "Test" "Production")
select opt in "${OPTIONS[@]}"
do
    export DOCKER_BUILDKIT=1
    export BUILDKIT_PROGRESS=plain
    case $opt in
        "Code Check")
            TYPE="code_check"
            build_test && yes | docker image prune --filter "label=name="$GIT_REPO --filter "label=prune=true" && docker image rm ghcr.io/{{ cookiecutter.project_slug }}:code_check
            ;;
        "Development")
            TYPE="development"
            build_test && build_image && prune_images
            ;;
        "Test")
            TYPE="test"
            if ask "Push new image to GitHub/GitLab when done?" Y; then
                build_test && build_image && push_image && prune_images
            else
                build_test && build_image && prune_images
            fi
            ;;
        "Production")
            TYPE="latest"
            read -p "Enter Version Number: " VERSION
            if ask "Is this correct? [$VERSION]" Y; then
                if ask "Push new image to GitHub/GitLab when done?" Y; then
                    build_test && build_image && push_image && prune_images
                else
                    build_test && build_image && prune_images
                fi
            fi
            ;;
        *) ;;
    esac
    break
done
