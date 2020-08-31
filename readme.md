# Circuitry-Based Sound

Circuitry-Based sound is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). 

It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic sound generators and processors and comparing different approaches on how to design electronic sound modules.

Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and therefore was hold on-line.

Based on previous's semesters studies of logic chips for sound creation and its musical applications, the course focused on computer aided circuit design and professional PCB manufacturing processes to build custom-made instruments. Participants were guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allowed the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or breadboards.

An end semester presentation completed this seminar with a concert performance carried out with the developed sound modules.

## Overview/Introduction

Besides the established ways of using electronics to synthesize sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below.

Analog synthesizers apply techniques like subtractive synthesis to generate audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Various parameters can be altered through connecting control signals, known as voltage control, either through patch cords or internally through a routing system with switches, which offer a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered envelopes for volume, filters or else. To obtain these functionalities, the hardware of analog synthesizers are therefor complex circuits, involving a high part count and require often precision components.

## Description

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. Especially the use of digital integrated logic circuits outside of their typical field of application, is a remarkable approach to build customized instruments for artistic sound production and interactive music.

[Logic CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute boolean functions. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like NOT, AND, OR, NAND, XOR, XNOR or implement multiplexers and registers.

When logical operations and their relation to voltage and sound is understood, CMOS-logic chips are an inexhaustible, very simple and low cost source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining various logic functions allows to generate a plethora of unique sounds. These circuits yield unexpected behavior, including randomness and produce the richness of analog sound. Adding circuit points for altering the sound through interaction allows to build customized and versatile instruments.

Compared with classical synthesizers, this DIY approach leads to experimental setups and surprisingly results that cannot only compete with (standard synthesizer systems) but are also more flexible and can be used much more easily in installative environments or live performances - Variability and unpredictability are

Furthermore, due to its simplicity, the unconventional approach of building electronic sound systems can be used for educational reasons, because most of its technical operations can easily be understood and relate to basic electronic knowledge.

... most notably Nicolas Collins' „N. Collins. Handmade Electronic Music, The Art of Hardware Hacking" (2006).

(Artists Stanley Lunetta, "Lunetta Synthesizers")

## build your own System

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the following picture:

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/SPICE_astabile_multivibrator.jpg" width=400>

It shows a square wave sound generator that can be built with only three components:  
* an inverting Schmitt trigger IC, e.g. CD40106, 
* a capacitor and 
* a resistor.

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, whereas the switching points for positive going signals differ from the switching points for negative going signals. Feeding back the output voltage to its input and tying the input via a capacitor to ground creates a relaxation oscillator or astable multivibrator.

Negative trigger threshold voltage
Positive trigger threshold voltage

Since the frequency is determined through the capacitor C and/or the resistor R, a potentiometer instead of the latter enables pitch control.
The frequency can be roughly calculated with this formula:

f = 0.72/RC

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula.


To control: photoresistor, force-sensitive resistor (FSR), flex sensor, or resistive fabric.
microcontroller, sensors.


## Authors


Zhen Bian <br />
Hangyan Chen <br />
Anna Helsen <br />
Jihye Jang <br />
Xingchen Liu <br />
Su Lu <br />
Ruoyi Qiu <br />
Christina Vinke <br />
Yunfei Zhang <br />

**Lorenz Schwarz** - *lecturer* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment

* Thanks to Dr. Paul Modler
