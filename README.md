# White balance calculation

## calculate_white_balance.py

This python script allows to calculate the white balance of a camera from an image. The script take only the center of the image to calculate the ratio for each channel. There are two inputs to the function. 1) The image file name; 2) A boolean to display a graph of the three channels along the width of the image. The ratios will be displayed in the terminal. 

## white_balance_target.py

This script creates numerical targets. The function takes as input one of the followings: `white_to_black` or `gray`. The first option creates a target with rectangles from white to gray to black. The second option gives an uniform gray target. The targets are saved in the folder `/targets`.