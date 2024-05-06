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

