#!/bin/bash
#github: https://github.com/Haise777

cd "$(find "$HOME/" -name "Cold-Darkness")"

# Arguments processing
linux_headers="linux-headers"
case "$1" in
	"--no-lheaders") linux_headers="";;
	"" ) echo > /dev/null;;
	* ) "Invalid passed argument"; exit 1;;
esac


# Script introduction
rs='\033[0m'
cyan='\033[0;36m'

printf "\n${cyan}"
printf ' _________        .__       .___ ________                __                                \n'
printf ' \_   ___ \  ____ |  |    __| _/ \______ \ _____ _______|  | __ ____   ____   ______ ______\n'
printf ' /    \  \/ /  _ \|  |   / __ |   |    |  \\\\__  \\\\_  __ \  |/ //    \_/ __ \ /  ___//  ___/\n'
printf ' \     \___(  <_> )  |__/ /_/ |   |    `   \/ __ \|  | \/    <|   |  \  ___/ \___ \ \___ \ \n'
printf '  \______  /\____/|____/\____ |  /_______  (____  /__|  |__|_ \___|  /\___  >____  >____  >\n'
printf '         \/                  \/          \/     \/           \/    \/     \/     \/     \/ \n'
printf "${rs}\n"
printf "                         A minimal to install and nice ${cyan}Qtile${rs} theme\n"
printf "                             Theme and script made by \033[1;36m\033[4;36mHaise777${rs}\n\n"




# install all needed dependencies from pacman
sudo pacman -S --noconfirm \
	git python-dbus-next qtile picom python kitty feh pacman-contrib rofi base-devel alsa-utils xorg-xrandr xorg-server\
	which noto-fonts-cjk noto-fonts-emoji noto-fonts python-psutil ttf-jetbrains-mono-nerd ttf-meslo-nerd "$linux_headers" || {
		echo "Failed to install needed packages from pacman"
		exit 1
	}
echo


# Checks if user '.config' exists
if [ ! -e "$HOME/.config" ]; then
	echo "User '.config' directory not found, creating one"
	mkdir "$HOME/.config"
fi


# Copy all files config to user '.config'
{
	echo "Copying all config files to ${HOME}/.config"
	\cp -r .config/* "$HOME/.config/"

	# Launch configuration options to the user
	python installation_options.py --install

} || { echo "Failed to copy config files"; exit 1; }
chmod u+x "$HOME/.config/qtile/autostart.sh"


# Create a dedicated default wallpaper's folder
{
echo "Creating 'cold-darkness' subdirectory in user's backgrounds directory"
mkdir -p "$HOME/.local/share/backgrounds/cold-darkness"
\cp wallpapers/* "$HOME/.local/share/backgrounds/cold-darkness/"
} || { exit 1; }


# Give the choice to install a custom terminal configuration
echo
echo "Want to install and setup a powerful terminal costumization?"
echo "Interpreter: zsh"
echo "Terminal costumization that comes with nice, already set up plugins and better alternatives for the default shell commands"
echo "to enhance your terminal experience"
echo "[y/n]"
while true; do
	read yn
	case $yn in
		[yY] ) {
			sudo pacman -S --noconfirm zsh curl make wget gcc unzip
			if [ ! -e TerminalConfig_Linux ]; then
				git clone https://github.com/Haise777/TerminalConfig_Linux
			fi
			chmod u+x TerminalConfig_Linux/install.sh
			TerminalConfig_Linux/install.sh --powerline
			\cp -r optional/custom-terminal/.config/* "$HOME/.config"

		}; break;;
		[nN] ) break;;
	esac
done


# Finish script section
function print_manual_entry() {
	awk -v var="$1" '/>/{i++}i==var{print; exit}' MANUAL
	echo
}

echo "Finished installing"
echo
print_manual_entry 1
print_manual_entry 2
print_manual_entry 3
print_manual_entry 4
print_manual_entry 5
printf "You can read more about the above by reading the ${cyan}MANUAL${rs} file\n\n"
echo "You will need to reboot to see effects"
echo "Reboot now? [y/N]"
read yn
case $yn in
	[yY] ) reboot;;
	*) exit 0;;
esac
