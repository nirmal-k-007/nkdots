#!/usr/bin/env bash

dir="$HOME/.config/rofi/themes"
theme='nord'

## Run
rofi \
    -show drun \
    -theme ${dir}/${theme}.rasi
