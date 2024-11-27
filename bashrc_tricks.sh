#! /bin/bash
# .bashrc
#Easy resource monitor aliases
alias checkCPU="top -b -n 1 -u \$USER | awk 'NR>7 { sum += \$9; } END { print sum; }'"
alias checkRAM='top -b -n 1 -u $USER | awk '\''NR>7 { mem=$6; unit=substr(mem,length(mem),1); value=substr(mem,1,length(mem)-1); if (unit=="m") value*=1024; else if (unit=="g") value*=1024*1024; else value+=0; sum+=value; } END { printf "%.2f GB\n", sum / 1024 / 1024; }'\'''
alias numprocess="ps -u dhanuska | sed 1d | wc -l"
alias usage="echo CPU%; checkCPU; echo num_procs; numprocess;echo mem;checkRAM;"

# Terminal customization (cursor layout and colors)
#Can switch out the 好 with whatever floats ur boat (including emojis)

#Colors
export TERM=xterm-color
export GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
export CLICOLOR=1
LS_COLORS='di=1;36:ln=35:so=32:pi=1;36:ex=32:or=40;31;01:bd=34;46:cd=34;43:su=30;41:sg=30;46:tw=30;42:ow=30;43';
export LS_COLORS

export COLOR_NC='\e[0m' # No Color
export COLOR_BLACK='\e[0;30m'
export COLOR_GRAY='\e[1;30m'
export COLOR_RED='\e[0;31m'
export COLOR_LIGHT_RED='\e[1;31m'
export COLOR_GREEN='\e[0;32m'
export COLOR_LIGHT_GREEN='\e[1;32m'
export COLOR_BROWN='\e[0;33m'
export COLOR_YELLOW='\e[1;33m'
export COLOR_BLUE='\e[0;34m'
export COLOR_LIGHT_BLUE='\e[1;34m'
export COLOR_PURPLE='\e[0;35m'
export COLOR_LIGHT_PURPLE='\e[1;35m'
export COLOR_CYAN='\e[0;36m'
export COLOR_LIGHT_CYAN='\e[1;36m'
export COLOR_LIGHT_GRAY='\e[0;37m'
export COLOR_WHITE='\e[1;37m'

alias ls="ls --color='auto'"

case $TERM in
     xterm*|rxvt*)
         TITLEBAR='\[\033]0;\u ${NEW_PWD}\007\]'
          ;;
     *)
        TITLEBAR=""
          ;;
esac

UC=$COLOR_WHITE               # user's color
[ $UID -eq "0" ] && UC=$COLOR_RED   # root's color

PS1="$TITLEBAR\n\[${UC}\]\u@helmholtz \[${COLOR_LIGHT_BLUE}\]\${PWD} \[${COLOR_BLACK}\] \n\[${COLOR_LIGHT_GREEN}\]好 \[${COLOR_NC}\] "
