## Circuitry-Based Sound

Circuitry-Based sound is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). 

It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic sound generators and processors and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and therefore was hold on-line.

Based on previous's semesters studies of logic chips for sound creation and its musical applications, the course focused on computer aided circuit design and professional PCB manufacturing processes to build custom-made instruments. Participants were guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allowed the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or breadboards. During the seminar, several experimenter boards for CMOS logic chips were designed and documented.

# Unconventional Electronic Sound

Besides the established ways of using electronics to synthesize sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like subtractive synthesis to generate audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Various parameters can be altered through connecting control signals, which offer a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered envelopes for volume, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and require often precision components.

## Logic CMOS Chips for Sound Creation

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. Especially the use of digital integrated logic circuits outside of their typical field of application, is a remarkable approach to build customized instruments for artistic sound production and interactive music.

[Logic CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute boolean functions. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like NOT, AND, OR, NAND, XOR, XNOR or implement multiplexers and registers. When logical operations and their relation to voltage and sound is understood, CMOS-logic chips are an inexhaustible, very simple and low cost source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds, variability and unpredictability. These circuits yield unexpected behavior, including randomness, while they produce the richness of analog sound. Due to its simplicity, the unconventional approach of building electronic sound systems can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge.

... most notably Nicolas Collins' „Handmade Electronic Music, The Art of Hardware Hacking" (2006).
(Artists Stanley Lunetta, "Lunetta Synthesizers")

## Basic Example of Unconventional Synthesis

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the following picture:

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/Multivibrator40106.jpg">

It shows a square wave sound generator that can be built with only three components:  
* inverting Schmitt trigger IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, whereas the positive trigger threshold differs from the negative trigger threshold. Feeding back the output voltage to its input and tying the input via a capacitor to ground creates a relaxation oscillator or astable multivibrator.


<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/schmt_inv_anim01.gif">

Since the frequency is determined through the capacitor C and the resistor R, a potentiometer instead of the latter enables pitch control. 
The frequency can be roughly calculated with this formula:

f = 0.72/RC

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear.

## CMOS Experimenter Board

The above example is documented in the IC's data sheet. It's recommendable to use data sheets for all active components used in projects.
Experiment!
Other examples to control the frequency can be a photoresistor, force-sensitive resistor (FSR) or flex sensor. 
Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


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
