# What is required?
- [Python](https://www.python.org/downloads/)
- [7-Zip](https://7-zip.org/download.html) or WinRAR to extract the .zip file.
- [Script](https://github.com/StevensND/emuswitch-backup/releases)

## Things to keep in mind

Ryujinx doesn't generate a folder of your saves by itself, you will have to do it by yourself. To do so, run Ryujinx and search for the game you would like to backup your save. Then right click and click on `Open User Save Directory`. 

A folder with your save will be generated automatically. If you pay attention to the path, it will be something similar to `bis\user save\000000000000000000000003\0`. For each game, the number `00000000000000000003` will be different and it will not match with the other games.

From this moment, you will be able to use the script and it will generate the backup of your saves without having to do this step again.

## Steps

- If you use the **`portable` folder method** used in option 1 of this [guide](https://github.com/Ryujinx/Ryujinx/wiki/Ryujinx-Setup-&-Configuration-Guide#portable-mode), you will have to place the `scripts` folder inside `portable\bis\user\save` path. **PLEASE:** Make sure the `scripts` folder is inside or the script will not work. 

An example of the correct path would be: `D:\Ryujinx\publish\portable\bis\user\save`.  You have to place the `scripts` folder inside this path. **Note that this route doesn't have to be yours.**

- If you use the **`Appdata/Roaming/Ryujinx` folder method**, you will have to place the  `scripts` folder inside `AppData\Roaming\Ryujinx\bis\user\save` path.

An example of the correct path would be: `C:\Users\Stevens\AppData\Roaming\Ryujinx\bis\user\save`.  You have to place the `scripts` folder inside `AppData\Roaming\Ryujinx\bis\user\save` path

Here's a [video](https://www.youtube.com/watch?v=TKDavf48n8g) with all the steps. In the video I'm using the AppData folder method but steps are the same for the portable folder method. Just paste the scripts folder into the portable folder.

Then just open the `scripts` folder and run `Saves Backup Ryujinx.py`

## How do I know which method I am using?

On your keyboard, press the `Windows + R` keys (you don't have to press the `+`) and type `%appdata%`. 

You will see this path: `AppData/Roaming`. If in this path there is a folder named `Ryujinx`, then you are using this method. Otherwise, you are using the other one.

