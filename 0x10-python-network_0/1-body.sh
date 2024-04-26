#!/bin/bash
# Displays the body of a http response
curl -sI "$1" -L | grep -iq "200 OK" && curl -s "$1" -L
