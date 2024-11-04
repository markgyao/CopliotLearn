#!/bin/bash
## Setup GitHub secrets using gh client
## gh auth login --with-token
## gh auth status
## bash setup_secret.sh

OWNER="markgyao"
REPO="CopliotLearn"

declare -A secrets
secrets=(
  ["TEST_SERVER_HOST"]="vschool.ddns.net"
  ["TEST_SERVER_USER"]="clpadmin"
  ["TEST_SERVER_SSH_KEY"]=""
  ["TEST_SERVER_SSH_PORT"]="22"
  ["PROD_SERVER_HOST"]="vschool.ddns.net"
  ["PROD_SERVER_USER"]="clpadminr"
  ["PROD_SERVER_SSH_KEY"]=""
  ["PROD_SERVER_SSH_PORT"]="22"
)

for secret_name in "${!secrets[@]}"; do
  secret_value="${secrets[$secret_name]}"
  echo -n "$secret_value" | gh secret set "$secret_name" --repo "$OWNER/$REPO"
  echo "Secret '$secret_name' set."
done

