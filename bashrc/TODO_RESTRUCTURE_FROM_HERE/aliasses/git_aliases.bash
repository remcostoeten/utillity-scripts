# ===============================
# Git Aliases
# ===============================

# Basic Git shortcuts
alias g='git'
alias master='git checkout master'
alias main='git checkout main'
alias newbranch='git checkout -b'
alias pull='git pull'
alias push='git push'
alias fetch='git fetch'

# Commit with a message
alias commit='git commit -m'

# Commit and push with a single command
alias gcp='git commit -m "$1" && git push'

# ===============================
# Advanced Git Aliases
# ===============================

# Commit with a message and optional files
# Usage: gc "commit message" file1.txt file2.txt ...
gc() {
  if [ -z "$1" ]; then
    echo "Usage: gc \"commit message\" [file1 file2 ...]"
    return 1
  fi

  local commit_message=$1
  shift  # Shift removes the first argument, so the remaining are file names

  git commit -m "$commit_message" "$@"
}

# Commit all changes with a message and push
# Usage: gcpall "commit message"
gcpall() {
  if [ -z "$1" ]; then
    echo "Usage: gcpall \"commit message\""
    return 1
  fi

  git add .
  git commit -m "$1"
  git push
}

 
