#!/bin/bash

# Check if inside a git repository, if not, initialize one
if ! git rev-parse --is-inside-work-tree &> /dev/null; then
    echo "Initializing a new Git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

# Check if repository is connected, if not, ask user for URL and set it as origin
if ! git ls-remote --get-url origin &> /dev/null; then
    echo "Please provide the repository URL: "
    read repository_url
    git remote add origin $repository_url
fi

function commit_and_push() {
    git add .
    git commit -m "Automatic commit"
    git branch -M main
    git push origin main

    if [ $? -ne 0 ]; then
        git push origin main --force
    fi
}

while true; do
    commit_and_push
    sleep 1800
done