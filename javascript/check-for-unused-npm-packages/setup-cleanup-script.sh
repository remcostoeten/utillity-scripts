#!/bin/bash

# Find the scripts directory, excluding certain directories
scripts_dir=$(find . -type d -name scripts -not -path "./.dist/*" -not -path "./node_modules/*" -not -path "./build/*" -print -quit)

# If the scripts directory doesn't exist, check for a src directory
if [ -z "$scripts_dir" ]; then
  if [ -d "src" ]; then
    scripts_dir="src/scripts"
  else
    scripts_dir="scripts"
  fi
fi

# Create the scripts directory if it doesn't exist
mkdir -p $scripts_dir

# Download the cleanup-packages.sh script into the scripts directory
curl -o $scripts_dir/cleanup-packages.sh https://raw.githubusercontent.com/remcostoeten/utillity-scripts/master/javascript/check-for-unused-npm-packages/cleanup-packages.sh

# Make the script executable
chmod +x $scripts_dir/cleanup-packages.sh

# Update package.json to include the cleanup script
if [ -f package.json ]; then
  # Use jq to update package.json
  if command -v jq &> /dev/null; then
    jq '.scripts.cleanup = "bash ./'$scripts_dir'/cleanup-packages.sh"' package.json > tmp.$$.json && mv tmp.$$.json package.json
  else
    # If jq is not installed, use sed to update package.json
    sed -i.bak 's/"scripts": {/"scripts": {\n    "cleanup": "bash .\/'$scripts_dir'\/cleanup-packages.sh",/' package.json
  fi
else
  echo "package.json not found. Please ensure you are in the root directory of your project."
fi

echo "Setup complete. You can now run the cleanup script using 'npm run cleanup'."