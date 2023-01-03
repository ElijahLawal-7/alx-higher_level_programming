#!/bin/bash
# displays all HTTP methods acceptable by server
curl -sI $1 | grep Allow | cut -d ' ' -f2-
