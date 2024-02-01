#!/bin/bash
#github: https://github.com/Haise777

cd "$(find ~/ -name "Cold-Darkness")"

# install all needed dependencies from pacman
sudo pacman -S --noconfirm \
	git linux-headers python-dbus-next qtile picom python kitty feh pacman-contrib rofi base-devel alsa-utils xorg-xrandr xorg-server\
	which noto-fonts-cjk noto-fonts-emoji noto-fonts python-psutil ttf-jetbrains-mono-nerd ttf-meslo-nerd || {
		echo "Failed to install needed packages from pacman"
		exit 1
}
echo

if [ ! -e "$HOME/.config" ]; then
	echo "User '.config' directory not found, creating one"
	mkdir "$HOME/.config"
fi

{
	echo "Copying all config files to ${HOME}/.config"
	\cp -r .config/* "$HOME/.config/"

	# Launch configuration options to the user
	python installation_options.py --install

} || { echo "Failed to copy config files"; exit 1; }

chmod u+x ~/.config/qtile/autostart.sh

echo "Creating 'cold-darkness' subdirectory in user's backgrounds directory"
mkdir -p "$HOME/.local/share/backgrounds/cold-darkness"
\cp wallpapers/* "$HOME/.local/share/backgrounds/cold-darkness/"

# install custom terminal
echo
echo "Install and setup the customized terminal emulator from the theme?"
echo "Emulator: zsh"
echo "Plugins: oh-my-zsh, zsh-autosuggestions, powerlevel10k"
echo "[y/n]"
while true; do
	read yn
	case $yn in
		[yY] ) ./optional/terminal/install_terminal.sh; break;;
		[nN] ) break;;
	esac
done

echo "Finished installing"
echo
echo " > You can safely delete this directory or you can keep it and run the installation_options.py script to reconfigure it"
echo
echo " > To set the wallpapers list this theme will use, put the images you want to use in the '$HOME/.local/share/backgrounds/cold-darkness' directory"
echo
echo " > You can change the login resolution by your ways or you can add a command to the '$HOME/.config/qtile/autostart.sh' script"
echo
echo "You will need to reboot to see effect"
echo "Reboot now? [y/N]"
read yn
case $yn in
	[yY] ) reboot;;
	*) exit 0;;
esac
