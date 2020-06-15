# Kivy

Kivy is a Python GUI building tool.

## Installation

Download and install Kivy: [Kivy Installation Page](https://kivy.org/#download)

```
pip install kivy

OR

pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
```
Ensure that XLAUNCH is running and that display variable is set
```
sudo apt update
sudo apt upgrade
sudo apt install x11-apps python3-pip python3-virtualenvwrapper python3-tkpython3-venv

export _TMP_NS="\$(tail -1 /etc/resolv.conf | cut -d' ' -f2)"
export _TMP_HOST=$(if [ $WSL_INTEROP ]; then echo $_TMP_NS; else echo "localhost"; fi)
echo -e "export WSL_HOST=$_TMP_HOST" >> ~/.profile
echo -e "export DISPLAY=\$WSL_HOST:0" >> ~/.profile
echo -e "export VIRTUALENVWRAPPER_PYTHON=$(which python3)" >> ~/.profile
echo -e "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.profile
wget https://raw.githubusercontent.com/JetBrains/clion-wsl/master/ubuntu_setup_env.sh && bash ubuntu_setup_env.sh&& rm -f ubuntu_setup_env.sh 

```

^^^ this from Ex0 Toolchain

## Usage

```bash
python main.py
```
