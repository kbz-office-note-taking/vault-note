### Features:

### Functional requirements
- currently zotify only supports cli usage. I may have to digest the project and modify to meet my requirement
- python lrc provider modules.
- youtube audio downloaders
	- yt-dlp implementation >> needs to embed album arts and metadata. Not sure yt-dlp can do that. 
	- Do research on other youtube music downloader modules that I can use with metadata embedded.
#### GUI implementations
##### visualization
![[april_music_downloader_implementation.excalidraw]]
- menubar, 
	- to be configurable music base directory, 
	- to select lyrics providers
- search bar >> search songs by names 
- url bar >> directly paste the spotify url 
- download buttons >> start download and restart downloader when the program hang
- song image icons
- music downloading progressbar in pyqt
- lyrics downloading services
	- lrcdl my modified version
	- syrics
	- other projects that I can easily use. 
	- put at least 3 services
- Metadata for selected item >> might not be possible.
### Application Process Flow
- Opening/Creating ==Music Downloader Widget from menubar==
- tell the user to setup the music providers and lyrics providers. 
	- if successful
		- go to the home page of downloader
	- else
		- will get to this page when the user enter the downloader window.
- User Search musics by name
	- returns relevent songs, album, artist names << currently zotify supports searching songs by names, I might have to tinker the cli usage by applying subprocess and terminal output. 
	- ==Or==
	- Directly Paste the spotify link to download
- If the connection to spotify api is successful
	- show the song downloading progressbar to user
	- after a song has been downloaded, show lrc file is being downloaded using which lrc provider. 
	- Then print output that song and lyrics downloading is completed. 
	- After closing the music downloader windows, reload the music files. 
- if not successful, 
	- try again for at least 3 times. 
		- if fail
			- suggest the user to use a vpn services. 
			- or you can suggest and integrate nekoray services to it. 
			- then try again the download >> ==restart downlod or press download again==
