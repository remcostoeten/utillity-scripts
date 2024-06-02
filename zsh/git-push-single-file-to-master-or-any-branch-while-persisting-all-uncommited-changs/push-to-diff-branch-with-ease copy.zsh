# I prefix my functions with fnc_ to make them easier to find

fnc_commit_file_to_master_with_message() {
    # Get the current branch name
    local current_branch=$(git rev-parse --abbrev-ref HEAD)

    # Stash all changes
    git stash --all

    # Checkout to the master branch
    git checkout master

    # Apply the changes of the specific file from the stash
    git checkout stash@{0} -- "$1"

    # Add the specific file to the staging area
    git add "$1"

    # Commit the changes
    git commit -m "$2"

    # Push the changes to the master branch
    git push origin master

    # Checkout back to the original branch
    git checkout $current_branch

    # Apply the stashed changes
    git stash pop
}

alias singlecommit="fnc_commit_file_to_master_with_message"
# Or alias pushfilemaster="fnc_commit_file_to_master_with_message"

# Usage:
# First argument is the file name, second is the commit message
# singlecommit "a-file-name.tsx" "Your commit message"
# or whatever alias you chose