#!/usr/bin/env bash

dir="$HOME/.config/rofi/themes"
theme='nord'

## Run
rofi \
    rofi -modi clipboard:~/.config/rofi/clipboard/cliphist-rofi -show clipboard -theme ${dir}/${theme}.rasi    
