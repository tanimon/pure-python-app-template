#! /usr/bin/env bash

# Exit on error
set -e

poetry export --with server -f requirements.txt --output server/server/handlers/requirements.txt
cd iac && cdk deploy --require-approval never -vv
