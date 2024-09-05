#!/bin/bash

# Alias Injector Script

# ===============================
# Define the base directory
# ===============================
alias_dir="$(dirname "${BASH_SOURCE[0]}")/aliasses"

# ===============================
# Source All Alias Files
# ===============================

# Source General Aliases
source "$alias_dir/general_aliasses.bash"

# Source Navigation Aliases
source "$alias_dir/navigation_aliases.bash"

# Source Development Aliases
source "$alias_dir/development_aliases.bash"

# Source Git Aliases
source "$alias_dir/git_aliases.bash"

