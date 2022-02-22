# .bash_profile

if [ $NAME == "fedora-toolbox" ]; then
	exec zsh
fi

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs