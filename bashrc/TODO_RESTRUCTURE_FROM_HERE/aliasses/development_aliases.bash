# Development Aliases

# ===============================
# Next.js Specific Aliases (using Bun by default)
# ===============================

# Start the development server using Bun
alias start='bun run dev'

# Clean up and rebuild the project with Bun
alias rmbuild='rm -rf node_modules; rm -rf .next'
alias rebuild='rmbuild; bun install; bun run dev'

# Open the project in VSCode and start the Bun development server
alias run='code .; start'

# Optional: Aliases for npm and pnpm if needed
alias startnpm='npm run dev'
alias startpnpm='pnpm run dev'

alias rebuildnpm='rmbuild; npm install; npm run dev'
alias rebuildforcenpm='rmbuild; npm install --force; npm run dev'

alias rebuildpnpm='rmbuild; pnpm install; pnpm run dev'

# ===============================
# Docker Specific Aliases
# ===============================

# Stop and start Docker containers
alias dstop='docker-compose down'
alias dstart='docker-compose up'

