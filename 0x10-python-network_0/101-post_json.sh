#!/bin/bash
# Script to send a JSON POST request to URL passed
curl -s -H "Content-Type: application/json" -d "$(cat $2)" "$1"
