#!/bin/bash
#github: https://github.com/Haise777

if [ ! -e "../Cold-Darkness" ]; then
	echo "Installation script must be executed within its directory"
	exit 1
fi


# install all needed dependencies from pacman
sudo pacman -S --noconfirm git qtile picom python kitty feh rofi base-devel xorg-xrandr xorg-server which noto-fonts-cjk noto-fonts-emoji noto-fonts python-psutil ttf-jetbrains-mono-nerd ttf-meslo-nerd || {
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
install_terminal () {
	sudo pacman -S --noconfirm zsh
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
	git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
	git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
	\cp -r optional/.* "$HOME/"
	echo
	echo "you will be prompted to enter your password in order to change the default terminal to .zsh"
	chsh -s "$(which zsh)"
}

echo
echo "Install and setup the customized terminal emulator from the theme?"
echo "Emulator: zsh"
echo "Plugins: oh-my-zsh, zsh-autosuggestions, powerlevel10k"
echo "[y/n]"
while true; do
	read yn
	case $yn in
		[yY] ) install_terminal; break;;
		[nN] ) break;;
	esac
done

echo "Finished installing"
echo "You can safely delete this directory or you can keep it and use the installation_options.py script to reconfigure it"
echo "To set the wallpapers list the theme will use, put the images you want to use in the '$HOME/.local/share/backgrounds/cold-darkness' directory"
echo "You can change the login resolution by your ways or you can add a command to the '$HOME/.config/qtile/autostart.sh' script"

echo "You will need to reboot to see effect"
echo "Reboot now? [y/N]"
read yn
case $yn in
	[yY] ) reboot;;
	*) exit 0;;
esac
