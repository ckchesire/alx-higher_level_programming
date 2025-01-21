#!/bin/bash
# Script takes a URL argument as input and sends request to URL.
curl -s "$1" | wc -c
