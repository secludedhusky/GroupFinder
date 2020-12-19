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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://nafc.link/images/951cf3a3.png)

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`


### Built With

* []()
* []()
* []()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CaseyK9/GroupFinder.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



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

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Casey Maxwell - [@HyenaLtd](https://twitter.com/HyenaLtd) - admin@doggidada.space

Project Link: [https://github.com/CaseyK9/GroupFinder](https://github.com/CaseyK9/GroupFinder)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





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

[ENG]
Requirements:
Python 3.7.2
pip install requests
pip install discord-webhook

(view Google how to install the requirements)
(doesn't work on Mac for some unknown reason as Python isn't available on MacOSX)

Run Esmée Group Finder.exe located in the Esmée Group Finder folder to open program.

Give it a few minutes to load, as it has to generate depencencies and open the file.

-Python Installation

I recommend installing Python requisites using chocolatey, which already comes with Windows 10.

View the Individual Step 2 installation method found here: https://chocolatey.org/install (or view below)

First, ensure that you are using an administrative shell - you can also install as a non-admin, check out Non-Administrative Installation.
Install with powershell.exe

NOTE: Please inspect https://chocolatey.org/install.ps1 prior to running any of these scripts to ensure safety. We already know it's safe, but you should verify the security and contents of any script from the internet you are not familiar with. All of these scripts download a remote PowerShell script and execute it on your machine. We take security very seriously. Learn more about our security protocols.
With PowerShell, you must ensure Get-ExecutionPolicy is not Restricted. We suggest using Bypass to bypass the policy to get things installed or AllSigned for quite a bit more security.

Run Get-ExecutionPolicy. If it returns Restricted, then run Set-ExecutionPolicy AllSigned or Set-ExecutionPolicy Bypass -Scope Process.
Now run the following command:

Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1%27))
Paste the copied text into your shell and press Enter.
Wait a few seconds for the command to complete.
If you don't see any errors, you are ready to use Chocolatey! Type choco or choco -? now, or see Getting Started for usage instructions.
Chocolatey
Installing Chocolatey
Chocolatey is software management automation for Windows that wraps installers, executables, zips, and scripts into compiled packages. Chocolatey integrates w/SCCM, Puppet, Chef, etc. Chocolatey is trusted by businesses to manage software deployments.

Ignore the newsletter sign up form
and then once Chocolatey is installed, run the following command from Command Prompt (Windows + R - Type in cmd and press Enter)

choco install python

[FR]
Exigences:
Python 3.7.2
demandes d'installation de pip
pip installer discord-webhook

(voir Google comment installer la configuration requise)
(ne fonctionne pas sur Mac pour une raison inconnue, Python n'étant pas disponible sur MacOSX)

Exécutez Esmée Group Finder.exe situé dans le dossier Esmée Group Finder pour ouvrir le programme.

Donnez-lui quelques minutes à charger, car il doit générer des dépendances et ouvrir le fichier.

-Python Installation

Je recommande d’installer les composants Python avec Chocolatey, qui est déjà fourni avec Windows 10.

Voir la méthode d’installation individuelle étape 2 trouvée ici: https://chocolatey.org/install (ou voir ci-dessous)

Premièrement, assurez-vous que vous utilisez un shell administratif - vous pouvez également installer en tant que non-administrateur, consultez Installation non administrative.
Installer avec Powershell.exe

REMARQUE: Veuillez inspecter https://chocolatey.org/install.ps1 avant d'exécuter l'un de ces scripts pour assurer la sécurité. Nous savons déjà que c'est sûr, mais vous devez vérifier la sécurité et le contenu de tout script provenant d'Internet que vous ne connaissez pas. Tous ces scripts téléchargent un script PowerShell distant et l'exécutent sur votre ordinateur. Nous prenons la sécurité très au sérieux. En savoir plus sur nos protocoles de sécurité.
Avec PowerShell, vous devez vous assurer que Get-ExecutionPolicy n'est pas restreint. Nous suggérons d’utiliser Bypass pour contourner la stratégie d’installation ou AllSigned pour un peu plus de sécurité.

Exécutez Get-ExecutionPolicy. S'il renvoie Reste restreint, exécutez le processus Set-ExecutionPolicy AllSigned ou Set-ExecutionPolicy Bypass -Scope.
Maintenant, lancez la commande suivante:

Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1%27))
Collez le texte copié dans votre shell et appuyez sur Entrée.
Attendez quelques secondes que la commande se termine.
Si vous ne voyez aucune erreur, vous êtes prêt à utiliser Chocolatey! Tapez choco ou choco -? maintenant ou consultez la rubrique Mise en route pour les instructions d'utilisation.
Chocolaté
Installation de Chocolatey
Chocolatey est une automatisation de la gestion des logiciels pour Windows qui englobe les installateurs, les exécutables, les fichiers zip et les scripts dans des packages compilés. Chocolatey intègre w / SCCM, Puppet, Chef, etc. Les entreprises font confiance à Chocolatey pour gérer les déploiements de logiciels.

Ignorer le formulaire d'inscription à la newsletter
et une fois que Chocolatey est installé, exécutez la commande suivante à partir de l'invite de commande (Windows + R - Tapez cmd et appuyez sur Entrée)

choco install python

[GER]
Bedarf:
Python 3.7.2
Pip-Installationsanforderungen
pip install discord-webhook

(Google zeigt an, wie die Anforderungen installiert werden.)
(Funktioniert unter Mac aus unbekannten Gründen nicht, da Python unter MacOSX nicht verfügbar ist.)

Führen Sie Esmée Group Finder.exe aus, das sich im Ordner Esmée Group Finder befindet, um das Programm zu öffnen.

Geben Sie ihm ein paar Minuten zum Laden, da es Abhängigkeiten erzeugen und die Datei öffnen muss.

-Python-Installation

Ich empfehle, Python-Requisiten mit chocolatey zu installieren, das bereits in Windows 10 enthalten ist.

Die einzelne Installationsmethode für Schritt 2 finden Sie hier: https://chocolatey.org/install (oder siehe unten)

Stellen Sie zunächst sicher, dass Sie eine Administrator-Shell verwenden. Sie können diese auch als Nicht-Administrator installieren. Informationen hierzu finden Sie unter Nicht-Administrator-Installation.
Installieren Sie mit powershell.exe

HINWEIS: Bitte überprüfen Sie https://chocolatey.org/install.ps1, bevor Sie eines dieser Skripts ausführen, um die Sicherheit zu gewährleisten. Wir wissen bereits, dass es sicher ist, aber Sie sollten die Sicherheit und den Inhalt von Skripten aus dem Internet überprüfen, mit denen Sie nicht vertraut sind. Alle diese Skripte laden ein Remote-PowerShell-Skript herunter und führen es auf Ihrem Computer aus. Wir nehmen die Sicherheit sehr ernst. Erfahren Sie mehr über unsere Sicherheitsprotokolle.
In PowerShell müssen Sie sicherstellen, dass Get-ExecutionPolicy nicht eingeschränkt ist. Wir empfehlen die Verwendung von Bypass, um die Richtlinie zu umgehen und die Installation zu starten, oder von AllSigned, um die Sicherheit zu erhöhen.

Führen Sie Get-ExecutionPolicy aus. Wenn Restricted zurückgegeben wird, führen Sie Set-ExecutionPolicy AllSigned oder Set-ExecutionPolicy Bypass -Scope Process aus.
Führen Sie nun den folgenden Befehl aus:

Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1%27))
Fügen Sie den kopierten Text in Ihre Shell ein und drücken Sie die Eingabetaste.
Warten Sie einige Sekunden, bis der Befehl ausgeführt wurde.
Wenn Sie keine Fehler sehen, können Sie Chocolatey verwenden! Typ Schoko oder Schoko -? Anweisungen zur Verwendung finden Sie unter Erste Schritte.
Schokoladig
Chocolatey installieren
Chocolatey ist eine Software-Management-Automatisierung für Windows, die Installationsprogramme, ausführbare Dateien, ZIP-Dateien und Skripts in kompilierte Pakete umschließt. Chocolatey integriert W / SCCM, Puppet, Chef usw. Chocolatey wird von Unternehmen für die Verwaltung von Softwarebereitstellungen als vertrauenswürdig eingestuft.

Ignorieren Sie das Newsletter-Anmeldeformular
Führen Sie nach der Installation von Chocolatey den folgenden Befehl über die Eingabeaufforderung aus (Windows + R - Geben Sie cmd ein und drücken Sie die Eingabetaste).

choco install python