# Rendering scripts for the paper "Volume Scattering Probability Guiding"
### [Project Page](https://kehanxuuu.github.io/vspg-website/) | [Paper](https://kehanxuuu.github.io/vspg-website/static/pdfs/volume_scattering_probability_guiding_sa24.pdf) | [Renderer Code](https://github.com/kehanxuuu/vspg-pbrt-v4/) | [Scenes](https://github.com/kehanxuuu/vspg-scenes/)

<img src="teaser.jpg" alt="teaser" width="1024"/>

This repository contains scripts to generate the renderings in the paper and the [supplementary viewer](https://kehanxuuu.github.io/vspg-website/vspg-supplemental/index.html).

It is an extension of the [rendering scripts](https://github.com/sherholz/rendering-scripts). Please refer to its documentation for the dependencies.

# Instructions

* Build and install the [renderer code](https://github.com/kehanxuuu/vspg-scenes/), then create a hyperlink in the root directory named `pbrt-renderer` pointing to the `install` folder.

* Download the [scenes](https://github.com/kehanxuuu/vspg-scenes/), then create a hyperlink in the root directory named `pbrt-scenes` pointing to this folder.

* Run:
``` bash
# Equal-SPP experiments
PYTHONPATH=$PYTHONPATH:$PWD python3 runPBRTVSPGEqualSPP.py

# Equal-time experiments
PYTHONPATH=$PYTHONPATH:$PWD python3 runPBRTVSPGEqualTime.py
```