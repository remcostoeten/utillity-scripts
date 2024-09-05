#!/bin/bash

# Inject All Script

# ===============================
# Source Alias and Function Injectors
# ===============================

# Source the Alias Injector
source "$(dirname "${BASH_SOURCE[0]}")/alias_injector.bash"

# Source the Function Injector
source "$(dirname "${BASH_SOURCE[0]}")/function_injector.bash"

 
