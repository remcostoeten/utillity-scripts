# Cleanup Packages Script

This script is used to maintain the health of your project's dependencies. It checks for unused and outdated npm packages in your project.

Ensure that you have `depcheck` installed globally. If not, you can install it using the following command:

```bash
npm install -g depcheck
```

## Usage

To run this script, first, you need to download it into your project. You can do this by running the following command in your terminal:

```bash
curl -O https://raw.githubusercontent.com/remcostoeten/utillity-scripts/master/javascript/check-for-unused-npm-packages/cleanup-packages.sh
```

Next, you need to make the script executable. You can do this by running the following command:

`chmod +x cleanup-packages.sh`

Finally, you can run the script by running the following command:

```bash
./cleanup-packages.sh
```

Easiest would be to place the script in a lib or script folder in your projects and then modify the `package.json` file to include a script that runs the script. For example:

```json
"scripts": {
  "cleanup": "node ./scripts/cleanup-packages.sh"
}
```

Or depending on how strict your project is implement this in your pipelines, or pre commit hooks.

## What it Does

1. **Check for unused dependencies**: The script uses `depcheck` to find and list any dependencies in your project that are not being used.

2. **Check for outdated packages**: The script uses `npm outdated` to find and list any dependencies in your project that are outdated.
