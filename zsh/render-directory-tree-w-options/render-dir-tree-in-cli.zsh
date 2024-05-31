# Define the function
tree_with_options() {
  # Define the file type arrays
  local programming_languages=("py" "java" "c" "cpp")
  local frontend_languages=("tsx" "ts" "jsx" "js" "css" "scss" "html")
  local backend_languages=("js" "ts" "py" "java")
  local images_assets=("gif" "bmp" "jpg" "jpeg" "png" "svg")
  local configuration_files=("csv" "txt" "md" "mdx" "yml" "json" "yaml")

  # Define the excluded directories
  local excludedirs=("node_modules" "dist" ".next" ".contentlayer")

  # Initialize variables
  local include_filetypes=()
  local exclude_dirs=()
  local tree_command="tree"

  # Parse the arguments
  while [[ $# -gt 0 ]]; do
    case $1 in
      -inc)
        shift
        include_filetypes=("${(@s/,/)1}")
        ;;
      -ex)
        shift
        exclude_dirs=("${(@s/,/)1}")
        ;;
      *)
        echo "Invalid option: $1"
        return 1
        ;;
    esac
    shift
  done

  # Add include filetypes to the tree command
  if [[ ${#include_filetypes[@]} -gt 0 ]]; then
    for filetype in "${include_filetypes[@]}"; do
      tree_command+=" -P '*.${filetype}'"
    done
  fi

  # Add exclude directories to the tree command
  if [[ ${#exclude_dirs[@]} -gt 0 ]]; then
    for dir in "${exclude_dirs[@]}"; do
      tree_command+=" --prune -I '${dir}'"
    done
  fi

  # Execute the tree command and copy the output to the clipboard
  eval $tree_command | tee >(pbcopy)
}

# Usage examples:
# tree_with_options -inc tsx,jsx
# tree_with_options -ex node_modules,dist
