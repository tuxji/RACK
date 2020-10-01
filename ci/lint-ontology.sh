#!/usr/bin/env bash

set -euo pipefail

sudo apt-add-repository ppa:swi-prolog/stable
sudo apt-get update -qq --yes
sudo apt-get install -qq --yes swi-prolog

cd RACK-Ontology
./assist/bin/check
