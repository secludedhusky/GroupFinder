<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/CaseyK9/GroupFinder">
    <img src="https://nafc.link/images/ff7592a0.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Group Finder</h3>

  <p align="center">
    A ROBLOX Group Finder designed to find unowned groups that have games and filter them by visits.
    <br />
    <a href="https://github.com/CaseyK9/GroupFinder"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CaseyK9/GroupFinder">View Demo</a>
    ·
    <a href="https://github.com/CaseyK9/GroupFinder/issues">Report Bug</a>
    ·
    <a href="https://github.com/CaseyK9/GroupFinder/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://nafc.link/images/951cf3a3.png)

ROBLOX Group Finder designed for finding unowned groups with games using ROBLOX's API. Due to ROBLOX's limiting of API requests, I have chosen to open source this to allow for the community to edit and continue to provide support for this. I have branched off from ROBLOX which makes this a useless program to me, but some people may find use for this. Since ROBLOX has made it so that you no longer have to pay for Premium/Builder's Club in order to claim unowned groups, this will be a very useful contribution to the community.


### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.7 or higher
  ```sh
  pip install requests
  ```
* Windows 10 v20H2 or later
* Ubuntu 20.04 LTS or later

### Disclaimer

We are not responsible for any bans from ROBLOX's services for usage of this.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CaseyK9/GroupFinder.git
   ```
2. Install NPM packages
   ```sh
   pip install requests
   ```
3. Configure proxies in `proxies.ini`
4. Run program
    ```sh
    py groupgame.py
    ```
5. Or run the Windows binary files located in the `Esmée Group Finder` folder.
```sh
cd '/Esmée Group Finder'
"Esmée Group Finder.exe"
```

<!-- USAGE EXAMPLES -->
## Usage

**To update to newer ROBLOX API**
```py
    def group(self):
        group = requests.get(f'https://groups.roblox.com/v1/groups/{self.groupID}', proxies=proxydict)

    def games(self):
        games = requests.get(f'https://games.roblox.com/v2/groups/{self.groupID}/games?accessFilter=All&sortOrder=Asc&limit=100', proxies=proxydict)

    def get_universal_id(self,placeID):
        a = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={placeID}', proxies=proxydict)

    def get_favorites(self):
        a = requests.get(f'https://games.roblox.com/v1/games/{self.universal_id}/favorites/count', proxies=proxydict)

    def get_votes(self):
        a = requests.get(f'https://games.roblox.com/v1/games/votes?universeIds={self.universal_id}', proxies=proxydict)

    def get_visits(self):
        a = requests.get(f'https://games.roblox.com/v1/games?universeIds={self.universal_id}', proxies=proxydict)
```
Change the above values replacing the request URLs with the new API version, carefull to leave the self values in their proper locations to maintain code syntax.

**To compile source code into binary**
```sh
pip install requirements.txt
py build_exe.py groupgame.py --dest=%UserProfile%
cd /d %UserProfile%
```
Change the above values to your destination and the script you'd like to compile. Executable will be named the same name as the python file.

**To add proxies**
1. Open proxies.ini
2. Clone @clarketm Proxy-List repo.
```sh
git clone https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
```
3. Open `proxy-list-raw.txt` and copy all content.
4. Paste all content from `proxy-list-raw.txt` into `proxies.ini`
5. Run program
```sh
py groupgame.py
```

**To filter results**
Run the program with certain attributes
```sh
py groupgame.py --favoritesCount=100 --upVotes=50 --downVotes=25 --visits=1500
```
Changing all arrtibutes to the number you want to filter or removing the ones you don't want to filter.

**To search for certain keywords**
Run the program with certain attributes
```sh
py groupgame.py --searchQuery=Tycoon
```
Changing the searchQuery attribute to your search terms.

**To change name of program**
```py
ctypes.windll.kernel32.SetConsoleTitleW('SC Group Finder by Esmée M. Veilleux')
os.system('color A0') # sets background
```
Change ConsoleTitle to the name of the program and the system color value to a C# color code.

_For more information, please refer to the [Documentation](https://caseymediallc.com/groupfinder)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/CaseyK9/GroupFinder/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Casey Maxwell - [@HyenaLtd](https://twitter.com/HyenaLtd) - admin@doggidada.space

Project Link: [https://github.com/CaseyK9/GroupFinder](https://github.com/CaseyK9/GroupFinder)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CaseyK9/GroupFinder.svg?style=for-the-badge
[contributors-url]: https://github.com/CaseyK9/GroupFinder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CaseyK9/GroupFinder.svg?style=for-the-badge
[forks-url]: https://github.com/CaseyK9/GroupFinder/network/members
[stars-shield]: https://img.shields.io/github/stars/CaseyK9/GroupFinder\.svg?style=for-the-badge
[stars-url]: https://github.com/CaseyK9/GroupFinder/stargazers
[issues-shield]: https://img.shields.io/github/issues/CaseyK9/GroupFinder.svg?style=for-the-badge
[issues-url]: https://github.com/CaseyK9/GroupFinder/issues
[license-shield]: https://img.shields.io/github/license/CaseyK9/GroupFinder.svg?style=for-the-badge
[license-url]: https://github.com/CaseyK9/GroupFinder/blob/master/LICENSE.txt
[product-screenshot]: https://nafc.link/images/951cf3a3.png