#!/bin/bash
# Displays the size of the body of a http response
curl -sI "$1" | grep -i "Content-Length" | grep -oE '[0-9]+'
