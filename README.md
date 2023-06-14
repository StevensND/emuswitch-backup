# Yuzu/Ryujinx Saves Backup Script
A script made in [Python](https://www.python.org/downloads/) by me [u/StevenssND](https://www.reddit.com/user/StevenssND) (Reddit profile).

This script allows you to perform an auto backup of your saves in Yuzu or Ryujinx emulator (Nintendo Switch). If you have any questions or problems, contact me on Reddit or Discord: stevenss. / Stevens#5210

Do you like this script and want to support me?. Here is my [Ko-fi](https://ko-fi.com/stevenss)

Btw: I tried to make this same script in a .bat file but it is not working as I want (I don't find it user friendly: the GUI when selecting the output path is a bit complicated to use).

Also if you want to know when a new Yuzu EA release is published, you can use this [Discord bot](https://github.com/StevensND/yuzuea-bot)

## How this script works?.

First of all, make sure you have [Python](https://www.python.org/downloads/) installed on your PC.

- In **Yuzu version**, it will look for a file named "qt-config.ini" located inside the config folder. Once located, it will read the same file and will automatically find the path where your saves are located. Subsequently, it will make a .zip file containing all your saves. [All steps here](https://github.com/StevensND/emuswitch-backup/blob/main/YUZU.md)
 
 This way seems to me the most correct and organized. I also did it this way since sometimes Yuzu creates another folder of your saves totally different from the one you had originally. The same thing happens if you do a full clean Yuzu installation. Credits to [u/Maxlastbreath](https://www.reddit.com/user/Maxlastbreath/) for the idea of getting the saves path this way.
 
 - In **Ryujinx version**, it will do the same. However, this time we don't need the qt-config.ini file. Ryujinx uses another method to save your saves totally different from Yuzu. [All steps here](https://github.com/StevensND/emuswitch-backup/blob/main/RYUJINX.md)

**Finally**, all you have to do is select an exit path. A .zip file will be generated with all your saves. When you need them, simply extract the .zip and make sure to place the saves in the right directory.

## When you should do a backup?.

**ALWAYS** backup before updating your emulator/game or before reverting to a previous update. This is really important and will avoid save losts.

Also, this is always up to you but I like to do my backups before start the game and when I finish. 

You can also do it by time intervals (ex: every 15 mins, every 30 mins, every hour ...) or before an important moment in the game where you don't want to lose your progress in case something bad happens.
