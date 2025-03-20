#!/bin/bash

## Using nc (Netcat) to send an HTTP GET request
# Usage: ./automated_netcat_http.sh <IP> <PORT>

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP> <PORT>"
    exit 1
fi

IP="$1"
PORT="$2"

# Create a temporary request file
REQUEST_FILE=$(mktemp)

# Write the HTTP request to the file
echo -e "GET / HTTP/1.1\r\nHost: anything\r\n\r\n" > "$REQUEST_FILE"

# Send the request using nc (Netcat)
nc "$IP" "$PORT" < "$REQUEST_FILE"

# Clean up the temporary file
rm -f "$REQUEST_FILE"
