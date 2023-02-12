# DadTube
#### Video Demo:  <URL HERE>

## Project Description
This project was created as a request from my dad, Poobalan Govender, who downloads educational videos off youtube to share with learners as a supplement to his teachings. He has a problem with downloading multiple youtube videos, and having tried applications from the internet, they were not able to function the way that is required. 


## Contents
1. [Why](#why)
2. [Installation](#installation)
3. [Usage](#usage)
5. [Software files](#software-files)
6. [Todo](#todo)


## Why

This project eases the downloading process, by making the ability to select and download videos nearly fully autonomous. Ease of use is achieved by the following:
1. Having the window being the topmost window at all times. This avoids switching between applications after selecting the videos. Being a small window, it is easily positioned on the browser while having full access to the browser and the software. 
2. Having the user copy the url of the video to the clipboard. This can be done from the youtube site, a google search page or anywhere that the link is available. This functionality allows the software to "grab" the url from the clipboard.
3. Having a button to copy the link from the clipboard, and start the download process in one step. The makes the only user interaction being the copying of the URL and the clicking of the button. 
4. Having the software download the highest resolution video in the desired format automatically.
5. Having the software download to the folder that it is executed from. This means that the user can create folders and copy the software to that folder to begin downloading to that folder. It avoids the user having to set folders in the system, and intuitively allows the user to download files to a single location, or by relocating the software, download to a new location.
6. Having the entire software available as a single executable. This makes it easy to move as well as easy to share.

## Installation

The software is contained in a single file called `dadtube.exe`

There is nothing else to install on windows. Just run the program from the folder you wish to download videos to.

## Usage

### Starting a download

![Main Menu](https://user-images.githubusercontent.com/109963236/211187623-f74cf28f-5335-4dfd-9ebb-d0ecf3dae751.png)

The user selects and copies the url of the video that is on Youtube. The user then clicks on the `Add to Queue` button on the software window, and the highest resolution video in mp4 format is downloaded to the folder that the software is executed from. All downloads are started on background threads so the window is fully functional during downloading.

1. To guage if the download has started - In the folder where the software executable is located, the name of the video that has started downloading will become visible. It will have an initial size of 0.

2. To guage if the download has completed - The video filesize will now be changed. Please note that if the software is stopped, or power or connectivity has been interrupted during the download, the incorrect filesize may appear.

## Software files
### 1. dadtube.exe

This file is the single executable that has all dependencies for execution. 

## Todo

The following is a list of features that if implemented, would provide good progression in the evolvement of the software. It would add features and essential services like downlad status tracking, that would benefit the user.

### Download status tracking

Once a download is started, the user will be able to visually see the progress of a download. It is excluded from the first version as the focus is on usability, and having too large a screen that is on top of the browser will hamper functionality.

### Queue

This will allow the user to add links that can be queued. At the moment, the user is responsible for ensuring that just a few threads are started to avoid congestion. By queueing, only a set number of downloads are active, but items in the queue are started the moment an active download completes. This allows the user to batch downloads.

### Notifications

Visual notifications of download status changes would enable the user to see the progress better.

### Database

Having a database of downloads will allow the user to trace previous downloads and have other metadata available for the user such as links to playlists and channels.

### Playlist and channel downloading

This feature will allow the user to download all the videos of a playlist or channel without having to manually download each one. This will save a lot of time and effort.