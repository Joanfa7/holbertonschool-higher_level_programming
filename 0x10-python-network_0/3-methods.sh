#!/bin/bash
# Delete
curl -sI OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
