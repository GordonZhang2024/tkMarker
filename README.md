# ![logo](https://gordonzhang.pythonanywhere.com/static/tkMarker.png) tkMarker

A light weight Markdown editor using **Tkinter**




[![Static Badge](https://img.shields.io/badge/Download%20-%20tkMarker?style=for-the-badge&logo=github&labelColor=black&color=blue&link=https%3A%2F%2Fgithub.com%2FGordonZhang2024%2FtkMarker%2Freleases)](https://github.com/GordonZhang2024/tkMarker/releases)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GordonZhang2024/tkMarker/python-app.yml)
![GitHub forks](https://img.shields.io/github/forks/GordonZhang2024/tkMarker)
![GitHub Repo stars](https://img.shields.io/github/stars/GordonZhang2024/tkMarker)
![GitHub watchers](https://img.shields.io/github/watchers/GordonZhang2024/tkMarker)

[website](https://gordonzhang.pythonanywhere.com/projects/tkMarker/)

## 🚀 Features
- [x] Markdown preview
- [x] Basic markdown syntax support
- [x] GitHub flavored Markdown support (beta)
- [x] Auto refresh
- [x] **It's really fast!**
- [ ] Code highlight
- [ ] Auto complete

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

*Click the <keyboard>Preview</keyboard> Button, then the editor will open the preview in the web browser.*

## License
MIT License

---

### Give it a try! I know you'll like it.

---
*This is a software with **ABSOLUTELY NO WARRANTY**.*

*Feel free to report an issue.*
**You are welcomed to start a pull request.**
