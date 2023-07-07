# Yuzu/Ryujinx Saves Backup Script
![GitHub all releases](https://img.shields.io/github/downloads/StevensND/emuswitch-backup/total?label=Total%20Downloads&link=https%3A%2F%2Fgithub.com%2FStevensND%2Femuswitch-backup%2Freleases)

A script made in [Python](https://www.python.org/downloads/) by me [u/StevenssND](https://www.reddit.com/user/StevenssND) (Reddit profile).

This script allows you to perform an auto backup of your saves in Yuzu or Ryujinx emulator (Nintendo Switch). If you have any questions or problems, contact me on Reddit or [Discord](https://discord.gg/7MMv4yGfhM). My user is: stevenss. / Stevens#5210

Do you like this script and want to support me?. Here is my [Ko-fi](https://ko-fi.com/stevenss)

Also if you want to know when a new Yuzu EA release is published, you can use this [Discord bot](https://github.com/StevensND/yuzuea-bot)

## How this script works?.

**Since 16 June 2023, install [Python](https://www.python.org/downloads/) is optional (you can use .exe files instead)**. So this means that you no longer need it.

**If you are using [this famous repack](https://i.imgur.com/Mp6n7la.png)**, please read [this post](https://github.com/StevensND/emuswitch-backup/blob/main/Repack%20Save%20Data%20Location.md) before start.

- For **Yuzu version**, watch this [video guide](https://youtu.be/hMvg9PJdD08). So ... The first step is to **tell the script where your Yuzu folder is located**.

If you use the `Appdata folder` instead of `user folder`, you will have to tell the script where Appdata folder is located. For `user folder` you only need to tell the script where is your  emulator folder located (the folder with all Yuzu files). 

For instance, in my case it will be something like: `D:\Emuladores\Yuzu\Yuzu EA`. I have yuzu.exe, yuzu-cmd.exe etc etc here.

Then the script will look for a file named "qt-config.ini" located inside the config folder of your Yuzu folder. Once located, it will read the same file and will automatically find the path where your saves are located. Subsequently, it will make a .zip file containing all your saves. 
 
 This way seems to me the most correct and organized. I also did it this way due to sometimes Yuzu can create another folder of your saves totally different from the one you had originally. The same thing happens if you do a full clean Yuzu installation. Credits to [u/Maxlastbreath](https://www.reddit.com/user/Maxlastbreath/) for the idea of getting the saves path this way.
 
 - For **Ryujinx version**, first ot all, watch [this guide](https://github.com/StevensND/emuswitch-backup/blob/main/EXE%20Files%20Guide/Ryujinx%20Guide.md). So ... it will do the same. However, this time we don't need the qt-config.ini file. Ryujinx uses another method to save your saves totally different from Yuzu.

**Finally**, all you have to do is select an output path. A .zip file will be generated with all your saves. When you need them, simply extract the .zip and make sure to place the saves in the right directory.

If you're going to use Python and .py files instead, check [this folder](https://github.com/StevensND/emuswitch-backup/tree/main/Python%20Guide) and read the guides to know all the steps that you need to do.

## When you should do a backup?.

**ALWAYS** backup before updating your emulator/game or before reverting to a previous update. This is really important and will avoid save losts.

Also, this is always up to you but I like to do my backups before start the game and when I finish. 

You can also do it by time intervals (ex: every 15 mins, every 30 mins, every hour ...) or before an important moment in the game where you don't want to lose your progress in case something bad happens.
