#!/bin/bash
# Send POST req. with quety parameters
curl -s -d "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
