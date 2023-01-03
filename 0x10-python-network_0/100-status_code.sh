#!/bin/bash
# prints status code
curl -so /dev/null -w "%{http_code}" $1
