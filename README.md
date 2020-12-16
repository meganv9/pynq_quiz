## PYNQ Quiz Information

### PYNQ Benefits
PYNQ offers a lot of unique features and capabilities. We highlight some of those benefits below: 
 - Open Source
 - Access to Hardware libraries like they are software libraries
 - Not required to download extra software
 - Easy project installation with pip install command
 - Highly customization and flexible 
     - Create Pynq Images for custom boards (Created via Petalinux BOOT.BIN file)
     - Add any RTL based IP to overlay   
     
---

### PYNQ-Z2 Highlights
The Z2 board has many features that can be used for your design. Here is an overview of some the capabilities: 

| Overview | Memory & storage   | Power |
|:------|:------|:------|
|<ul><li>650MHz ARM® Cortex® -A9 dual-core processor</li><li>Programmable logic <ul> <li>13,300 logic slices, each with four 6-input LUTs and 8 flip-flops</li><li>630 KB block RAM</li><li> 220 DSP slices</li><li>On-chip Xilinx analog-to-digital converter (XADC)</li></ul> </li><li>Programmable from JTAG, Quad-SPI flash, and MicroSD card</li></ul>|<ul><li>512MB DDR3 with 16-bit bus @ 1050Mbps</li><li>16MB Quad-SPI Flash with factory programmed 48-bit globally unique EUI-48/64™ compatible identifier</li><li>MicroSD slot</li></ul>|<ul><li>USB or 7V-15V external power regulator</li></ul>|

 | USB & Ethernet | Audio & Video | Switches, Push-buttons, & LEDS | Expansion Connectors |
 |:------|:------|:------|:------|
 |<ul><li>Gigabit Ethernet PHY</li><li>Micro USB-JTAG Programming circuitry</li><li>Micro USB-UART bridge</li><li>USB 2.0 OTG PHY (supports host only)</li></ul>|<ul><li>2x HDMI ports (input and output)</li><li>24bit I2S DAC with 3.5mm TRRS jack</li><li>Line-in with 3.5mm jack</li></ul>|<ul><li>4 push-buttons</li><li>2 slide switches</li><li>4 LEDs</li><li>2 RGB LEDs</li></ul>|<ul><li>2x Pmod ports <ul><li>16 Total FPGA I/O (8 pins on Pmod A are shared with Raspberry Pi connector)</li></ul></li><li>Arduino Shield compatible connector</li><ul><li>24 Total FPGA I/O</li><li>6 Single-ended 0-3.3V Analog inputs to XADC</li></ul><li>Raspberry Pi connector</li><ul><li>28 Total FPGA I/O (8 pins are shared with Pmod A)</li></ul></ul>|

The Z2 board can be powered via a Micro-USB port, an external power supply, or battery. And PYNQ-Z2 supports MicroSD, Quad SPI Flash, and JTAG boot modes. You can dive more deeply into the features and capabilites of the PYNQ-Z2 in the manual below:   
Reference Manual: https://d2m32eurp10079.cloudfront.net/Download/PYNQ_Z2_User_Manual_v1.1.pdf

---   

### Video: Setting up PYNQ-Z2 and Running Hello World
You can run through the following video to run a "Hello World" tutorial.    
To download the "Hello World" notebook, you will need to be connected to the Wifi Router. These steps are explained in the video above.    
The link below will direct you how to download the notebook. Make sure to open a Terminal in the Jupyter Notebook (The steps are also outlined in the video above): <br> <br>
**https://github.com/Xilinx/PYNQ-HelloWorld/blob/master/README.md**

[Watch the Video](https://www.youtube.com/embed/RiFbRf6gaK4)

### Additional Resources
You can also look up more information and material on PYNQ at the following links

[PYNQ Resource Website](http://www.pynq.io/):

 - Projects, community projects posted
 - Source code
 - Boot images

[PYNQ Readthedocs](https://pynq.readthedocs.io/en/latest/getting_started.html):

 - Guides for getting started
 - Jupyter Notebooks
 - Overlays
