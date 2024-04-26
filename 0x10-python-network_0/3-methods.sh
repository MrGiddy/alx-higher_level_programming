#!/bin/bash
# Displays all HTTP methods accepted by server
curl -sI -X OPTIONS "$1" | grep -i '^allow:' | sed 's/^allow: //i'
