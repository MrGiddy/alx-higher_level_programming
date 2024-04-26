#!/bin/bash
# Displays only the status code of response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
