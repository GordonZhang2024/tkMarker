# ![logo](https://gordonzhang.pythonanywhere.com/static/tkMarker.png) tkMarker

Tutorial project: A light weight text editor

[![Static Badge](https://img.shields.io/badge/Download%20-%20tkMarker?style=for-the-badge&logo=github&labelColor=black&color=blue&link=https%3A%2F%2Fgithub.com%2FGordonZhang2024%2FtkMarker%2Freleases)](https://github.com/GordonZhang2024/tkMarker/releases)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GordonZhang2024/tkMarker/python-app.yml)
![GitHub forks](https://img.shields.io/github/forks/GordonZhang2024/tkMarker)
![GitHub Repo stars](https://img.shields.io/github/stars/GordonZhang2024/tkMarker)
![GitHub watchers](https://img.shields.io/github/watchers/GordonZhang2024/tkMarker)



 ![screenshot](https://github.com/GordonZhang2024/tkMarker/assets/159539185/0b343372-8f77-446c-a11c-4b3ced5d31ed)


## Installation
### Installing the dependencies
###### GNU/Linux
This project requires **Tkinter**.
To install it, type command:
```bash
$ sudo apt-get install python-tk # On Debian based GNU/Linux distributions
$ sudo dnf install python3-tkinter # On Fedora based GNU/Linux distributions
```
### Installing tkMarker
###### GNU/Linux
First, you need to [download a release](https://github.com/GordonZhang2024/tkMarker/releases) and extract the source tarball.
Then, type command:
```bash
$ pip install -r requiremonts.txt
$ ./install.sh
```
> [!IMPORTANT]
> Please use Python >= 3.8

###  Creating desktop icon
Write this to `~/.local/share/applications/tkmarker.desktop`
```
[Desktop Entry]
Name=tkMarker
Exec=/home/<your-user-name>/.local/bin/tkmarker
Type=Application
Icon=<path/to/tkMarker>/static/tkMarker.png
Categories=Development;
Keywords=Markdown;
```

## Usage
Type command:
```bash
$ tkmarker &
```
You will see the editor.


## License
MIT License

---
*This is a software with **ABSOLUTELY NO WARRANTY**.*

*Feel free to report an issue.*
**You are welcomed to start a pull request.**
