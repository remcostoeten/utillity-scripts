colorize_logs() {
  grep --color=always -E "ERROR|WARN|INFO|DEBUG" "$1" | less -R
}

alias log=colorize_logs
