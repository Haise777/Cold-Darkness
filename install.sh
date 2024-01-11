#!/bin/bash
#github: https://github.com/Haise777

if [ ! -e "../cold-darkness" ]; then
	echo "Installation script must be executed within its directory"
	exit 1
fi


# install all needed dependencies from pacman
sudo pacman -S --noconfirm git qtile picom python kitty feh rofi base-devel xorg-xrandr xorg-server noto-fonts-cjk noto-fonts-emoji noto-fonts python-psutil ttf-jetbrains-mono-nerd ttf-meslo-nerd || {
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
	python installation_options.py

} || { echo "Failed to copy config files"; exit 1; }

chmod u+x ~/.config/qtile/autostart.sh

echo "Creating 'cold-darkness' subdirectory in user's backgrounds directory"
mkdir -p "$HOME/.local/share/backgrounds/cold-darkness"
\cp wallpapers/* "$HOME/.local/share/backgrounds/cold-darkness/"

# install custom terminal
install_terminal () {
	sudo pacman -S --noconfirm zsh
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
	git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
	git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
	if [ -f "$HOME/.zshrc" ]; then
		echo
		echo "User already have a .zshrc file, do you want to override it?"
		echo "[y/n]"
		while true; do
			read yn
			case $yn in
				[yY] ) \cp -r optional/.* "$HOME/"; break;;
				[nN] ) break;;
			esac
		done
	else
		\cp -r optional/.* "$HOME/"
	fi
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

echo "Finished installing, you can safely delete this directory"
echo "To set the wallpapers list the theme will use, put the images you want to use in the '$HOME/.local/share/backgrounds/cold-darkness' directory"

echo "You will need to reboot to see effect"
echo "Reboot now? [y/N]"
read yn
case $yn in
	[yY] ) reboot;;
	*) exit 0;;
esac
