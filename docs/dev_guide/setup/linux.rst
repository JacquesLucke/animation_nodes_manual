Setup Environment on Linux
==========================


Ubuntu 18.04 (based operating systems)
======================================

1. Clone the git repository

``git clone https://github.com/JacquesLucke/animation_nodes_manual``

2. Install python3.6 and cython3

``sudo apt install python3.6 python3-numpy cython3``

3. Change your addons directory in config.py (change USERNAME to your username)

``addonsDirectory = "/home/USERNAME/.config/blender/2.79/scripts/addons"``

4. Then compile

``python3.6 setup.py --noversioncheck``
