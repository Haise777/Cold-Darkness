#!/bin/bash

# install custom terminal

sudo pacman -S --noconfirm zsh zsh-autosuggestions zsh-syntax-highlighting lsd
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
\cp -r ./.zshrc "$HOME/"
\cp -r ./.p10k.zsh "$HOME/"
\cp -r ./.config/* "$HOME/.config/"
\cp -r ./custom/*.zsh ~/.oh-my-zsh/custom/
echo
echo "you will be prompted to enter your password in order to change the default terminal to .zsh"

while true; do
{
	chsh -s "$(which zsh)"
} || { echo "Error, probably invalid password"; continue; }
break
done

echo "Finished installing terminal"
