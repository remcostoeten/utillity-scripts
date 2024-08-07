# Function to commit all changes with a provided message
# Usage: c <commit message>
gitcommit() {
  if [ -z "$1" ]; then
    echo "Usage: gitcommit <commit message>"
    return 1
  fi
  git add .
  git commit -m "$*"
}

# Alias for the function to make it easier to call
alias c=gitcommit

# Function to commit specific files with a provided message
# Usage: gm <commit message> <file1> [<file2> ...]
gitcommitfiles() {
  if [ "$#" -lt 2 ]; then
    echo "Usage: gitcommitfiles <commit message> <file1> [<file2> ...]"
    return 1
  fi

  # Extract the commit message
  local commit_message="$1"
  shift  # Remove the first argument (commit message) from the list

  # Add specified files to staging
  git add "$@"

  # Commit with the provided message
  git commit -m "$commit_message"
}

# Alias for the function to make it easier to call
alias cm=gitcommitfiles
