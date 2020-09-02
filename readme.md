# Circuitry-Based Sound

Circuitry-Based sound is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). 

It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic sound generators and processors and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and therefore was hold on-line.

Based on previous's semesters studies of logic chips for sound creation and its musical applications, the course focused on computer aided circuit design and professional PCB manufacturing processes to build custom-made instruments. Participants were guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allowed the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or breadboards. During the seminar, several experimenter boards for CMOS logic chips were designed and documented.

# Unconventional Electronic Sound
## Classical Sound Synthesis

Besides the established ways of using electronics to synthesize sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like subtractive synthesis to generate audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Various parameters can be altered through control signals, which offer a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered envelopes for volume, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and require often precision components.

## Logic CMOS Chips for Sound Creation

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. Especially the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music.

[Logic CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute boolean functions. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like NOT, AND, OR, NAND, XOR, XNOR or implement multiplexers and registers. When logical operations and their relation to voltage and sound is understood, CMOS-logic chips are an inexhaustible, very simple and low cost source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds. These circuits yield a high variability but also unpredictable behavior, including randomness, while they produce the richness of analog sound. Due to its simplicity, the unconventional approach of building electronic sound systems can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably Nicolas Collins' „Handmade Electronic Music, The Art of Hardware Hacking" (2006).

## Basic Example of Unconventional Synthesis

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the following picture:

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/Multivibrator40106.jpg">

It shows a square wave sound generator that can be built with only three components:  
* inverting Schmitt trigger IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, whereas the positive trigger threshold differs from the negative trigger threshold. Feeding back the output voltage to its input and tying the input via a capacitor to ground creates a relaxation oscillator or astable multivibrator.

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/schmt_inv_anim01.gif">

The frequency can be roughly calculated with this formula:

$$f=\frac{0,72}{RC}$$

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear.

Since the frequency is determined through the capacitor C and the resistor R, a potentiometer instead of the latter enables pitch control. Other ways of controling the frequency may be a photoresistor, force-sensitive resistor (FSR) or flex sensor. Adding circuit points to alter the sound through interaction allows building customized and versatile instruments. The above example is documented in the IC's data sheet. It's recommendable to use data sheets for all active components used in projects.


## CMOS Experimenter Board

The goal of this project is to offer versatile experimenter boards for testing and examining standard CMOS chips for musical applications. Its a building block aproach. Each layout is desigend for different circuits and functionalities. It is possible to modifiy and change circuits through sockets that are used for component placement.
The boards are provided with mounting holes that match the according [case](https://github.com/clswa/Circuitry-Based-Sound/tree/master/Case "Case"). Jumper cables can be used as patch cords.

### CD40106

The CD40106 hex Schmitt trigger inverter offers six inverters that can be wired externaly to generate square waves. The board allows to setup an offset resistor for use with potentiometers in order to prevent zero resistance between output and input and can be populated alternatively with photoresistors.

Image

[CD40106 Data Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")

### CD4093

The CD4093 is a NAND Schmitt trigger and provides 2 inputs. The IC generated square waves when the first input is set high and the second input is wired as the CD40106. Bringing the 1 input to low inhibits oscillations. Therfore, interconnecting outputs and the first inputs creates gating effects. Bringing the first input to high via a push button works like a keyboard.

[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")

### CD4022

counter, waveshaper, Reset function

[CD4022](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")

### CD4046

Phase locked loop

[CD4046](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")

### Mixer

Summing operational amplifier.mixing signals together


### Trigger Board

A PCB with push buttons for setting inputs to high or low

## Case

The case offers a surface with mounting holes for the experimenter boards



## Power Supply

works with 9V guitar effect units PSUs

## Bill of Material

A [list](https://github.com/clswa/Circuitry-Based-Sound/tree/master/PCB_Hardware/BOM "Bill of Material") of required components.

Potentiometers
Switches

## Authors

Zhen Bian  
Hangyan Chen  
Anna Helsen  
Jihye Jang  
Xingchen Liu  
Su Lu  
Ruoyi Qiu  
Christina Vinke  
Yunfei Zhang  

**Lorenz Schwarz** - *lecturer* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment

* Thanks to Dr. Paul Modler
