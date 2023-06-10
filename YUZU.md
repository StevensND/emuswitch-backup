# What is required?
- [Python](https://www.python.org/downloads/)
- [7-Zip](https://7-zip.org/download.html) or WinRAR to extract the .zip file.
- [Script](https://github.com/StevensND/emuswitch-backup/releases)

## Steps

- If you use the **`user` folder method** used in step 2 of this [guide](https://www.reddit.com/r/NewYuzuPiracy/comments/13gh9ts/yuzu_totk_complete_setup_guide_60_fps_cutscenes/), you will have to place the `scripts` folder inside this folder. Your `user` folder should [look like this](https://i.gyazo.com/d3a4c687dc4d479be384b5062263c905.png). **PLEASE:** Make sure the `scripts` folder is inside or the script will not work. 

An example of the correct path would be: `D:\yuzu-windows-msvc-early-access\user`.  You have to place the `scripts` folder inside this path. **Note that this route doesn't have to be yours.**

Here's a [video](https://youtu.be/cfIAvwgcC4Y) with the steps using the `user` folder method .

- If you use the **`Appdata/Roaming/yuzu` folder method**, you will have to place the `scripts` folder inside this folder.

An example of the correct path would be: `C:\Users\Stevens\AppData\Roaming\yuzu`.  You have to place the `scripts` folder inside this path. 

Here's a [video](https://youtu.be/GE0icekcD2U) with the steps using the `AppData` folder method. 

Remember to press the `Windows + R` keys (you don't have to press the `+`) and type `%appdata%` to access to the folder.

Then just open the `scripts` folder and run `Saves Backup Yuzu.py`

Finally, you'll get a .zip file. Open it and you will see a folder with a lot of 0's. Open that folder and you'll see another folder inside. Open it too and inside that folder you'll see more folders. These folders contain your saves inside so when you need them, just copy & paste them in the right path and you're done.

## How do I know which method I am using?

On your keyboard, press the `Windows + R` keys (you don't have to press the `+`) and type `%appdata%`. 

You will see this path: `AppData/Roaming`. If in this path there is a folder named `yuzu`, then you are using this method. Otherwise, you are using the other one.

## How to identify your save for a specific game

Just open Yuzu and take a look at the numbers below game's name. Here's an [example](https://i.gyazo.com/b135919f26ebf1d0cc29f46c3c5ac092.png) of what I'm talking about.

Ignore 0x. The rest of the numbers must match. So ... For The Legend Of Zelda: Tears Of The Kingdom the folder name will be: `0100F2C0115B6000`

## How to restore your saves

Just watch this [video](https://youtu.be/g_BkuE1erIw). In the video I show you how to do a clean installation of Yuzu (Yuzu Early Access in this case), but you can also keep in mind these steps in case Yuzu is bugged and has generated a new folder for your saves. If this is your case, watch the video starting around minute 2:40.
