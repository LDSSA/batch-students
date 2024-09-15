#!/usr/bin/env bash
set -x
set -e

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo Copying notebook...
curl $NOTEBOOK_URL -H "Authorization: Token $PORTAL_TOKEN" -o "Exercise notebook.ipynb"

echo Grading
ldsagrader portal grade --notebook_path="Exercise notebook.ipynb" --grading_url=$PORTAL_GRADING_URL --checksum_url=$PORTAL_CHECKSUM_URL --token=$PORTAL_TOKEN