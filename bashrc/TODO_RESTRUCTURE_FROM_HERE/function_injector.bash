#!/bin/bash

# Function Injector Script

# ===============================
# Define the base directory
# ===============================
function_dir="$(dirname "${BASH_SOURCE[0]}")/functions"

# ===============================
# Source All Function Files
# ===============================

# Source Catcopy Function
source "$function_dir/catcopy_faunction.bash"
``
# Source Copypwd Function
source "$function_dir/copypwd_function.bash"

# Source Countdown Timer Function
source "$function_dir/countdown-timer.bash"

# Source Directory Size Calculator Function
source "$function_dir/dir_size_calculator.bash"

# Source Colorize Logs Function
source "$function_dir/colorize_logs.bash"

# Source Move Except Function
source "$function_dir/move_except.bash"

 
