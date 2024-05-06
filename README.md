# Dynmap "Invalid Modellist" Fix
Python script for fixing model errors after running Dynmap-Block-Scan, if "Invalid modellist patch for box" warnings appear in Minecraft server console log.

## Scenario
For dedicated Minecraft servers, there exists a mod called [Dynmap](https://github.com/webbukkit/dynmap) which can be used to create and run a website hosting dynamic web maps of the worlds on the server. However, in order for Dynmap to properly understand and render non-standard blocks and textures, a mod called [DynmapBlockScan](https://github.com/webbukkit/DynmapBlockScan) can be run to to scan the serverfiles and generate models for Dynmap. Here-in lies the problem, sometimes DynmapBlockScan generates definitions in the model files that Dynmap struggles with, for one reason or another. This can lead to console log warnings anywhere from the hundreds, to the hundreds of thousands. 

## Solution
This python script was created to parse the Minecraft dedicated server logfile, identify mods with offending model data in the renderdata textfiles, extract the line number and delete it from in relevant target file.

## Additional Info
I successfully tested the script on Windows 11 using Python 3.11, then successfully implemenented the script on my Minecraft server running Ubuntu 22.04, with Python 3.10.6.

## Usage
At the bottom of the script, define the location of the source logfile and the renderdata directory, either using absolute path or relative path with respect to the location of the python script.

Below that is a dry-run flag, if you want to test (file permissions, paths, etc).

The script will print an output of the mods and the associated target file lines (to be) deleted.

## Examples
Dry Run:
```
eski@minecraft:~$ python3 dynmap-test.py
Would delete lines [4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22] from renderdata/oceansdelight-models.txt in a real run
Would delete lines [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290] from renderdata/fwaystones-models.txt in a real run
Would delete lines [3] from renderdata/adventurez-models.txt in a real run
Would delete lines [154, 155, 156, 157, 158, 159, 160, 161, 162] from renderdata/winterly-models.txt in a real run
Would delete lines [3, 4, 5, 6] from renderdata/hybrid-aquatic-models.txt in a real run
```

Implementatiom Run:
```
eski@minecraft:~$ python3 dynmap-test.py
Deleted lines [4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22] from renderdata/oceansdelight-models.txt
Deleted lines [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290] from renderdata/fwaystones-models.txt
Deleted lines [3] from renderdata/adventurez-models.txt
Deleted lines [154, 155, 156, 157, 158, 159, 160, 161, 162] from renderdata/winterly-models.txt
Deleted lines [3, 4, 5, 6] from renderdata/hybrid-aquatic-models.txt
```
