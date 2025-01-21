#!/bin/bash
# Script takes in a URL and display all HTTP methods the server will accept
curl -sI "$1"
