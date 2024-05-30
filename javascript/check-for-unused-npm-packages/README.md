# Cleanup Packages Script

This script is used to maintain the health of your project's dependencies. It checks for unused and outdated npm packages in your project.

Ensure that you have `depcheck` installed globally. If not, you can install it using the following command:

`npm install -g depcheck`

## Usage

To set up and run this script, you can use the following command in your terminal:

```bash
curl -s https://raw.githubusercontent.com/remcostoeten/utillity-scripts/master/javascript/check-for-unused-npm-packages/setup-cleanup-script.sh | bash
```

This command will:
1. Download the `cleanup-packages.sh` script.
2. Make the script executable.
3. Place the script in the `scripts` folder of your project.
4. Update your `package.json` file to include a script that runs the `cleanup-packages.sh` script.

## What it Does

1. **Check for unused dependencies**: The script uses `depcheck` to find and list any dependencies in your project that are not being used.
2. **Check for outdated packages**: The script uses `npm outdated` to find and list any dependencies in your project that are outdated.

### Script Content

```bash
#!/bin/bash

# Check for unused dependencies
echo "Checking for unused dependencies..."
depcheck

# Check for outdated packages
echo "Checking for outdated packages..."
npm outdated
```

### Setup Script

Create a setup script `setup-cleanup-script.sh` with the following content in the root directory of your project and give it executable permissions with `chmod +x setup-cleanup-script.sh`.

```bash
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
```

### Usage Instructions

1. **Download and run the setup script**:
   ```bash
   curl -s https://raw.githubusercontent.com/remcostoeten/utillity-scripts/master/javascript/check-for-unused-npm-packages/setup-cleanup-script.sh | bash
   ```

2. **Run the cleanup script**:
   ```bash
   npm run cleanup
   ```

This setup script will automate the entire process, making it easy to integrate the cleanup script into your project with a single command.