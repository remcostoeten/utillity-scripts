#!/bin/bash

# Check for unused dependencies
echo "Checking for unused dependencies..."
depcheck

# Check for outdated packages
echo "Checking for outdated packages..."
npm outdated
