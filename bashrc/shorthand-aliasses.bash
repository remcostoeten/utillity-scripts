# General
alias rmrf='rm -rf'
alias exit='exit'
alias rebuild='$RMALL; bun i; bun run build'
alias restart='$RMALL; bun i; code .; bun run dev'
alias build='bun run build'
alias install='bun install'
alias rebuildnpm='$RMALL ; npm install --force ; npm run build'
alias restartnpm='$RMALL ; npm install --force ; npm run dev'

# Open bash configuration
alias bashrc='vim ~/.bashrc'
alias editbash='code ~/.bashrc'
alias sourcebash='source ~/.bashrc'

# Git
alias g='git'
alias push='git push'
alias pull='git pull'
alias newbranch='git checkout -b'
alias checkout='git checkout'
alias commitpush='git add . && git commit -m "$1" && git push'
# Navigating directories
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../'
alias ......='cd ../../../../../'

# Vscode relate
alias code="code-insiders"
alias codex='code .; exit'

# Project directories
alias dev="cd $DEV_DIR"
alias run='code .; bun run dev'

# Drizzle
alias drizzle='drizzle-kit'
alias gen='bun run drizzle-kit generate'
alias migrate='bun run drizzle-kit migrate'
alias dbpush='bun run drizzle-kit push'
