# Circuitry-Based Sound




"Circuitry-Based Sound" is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic instruments and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and is partially held online.

The course is covering electrical and electronic basics, computer aided circuit design and professional PCB manufacturing processes with the aim of building custom-made instruments. The emphasis is on studies of logic chips for sound creation and its musical applications. Participants are guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allows the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or solderless breadboards.

The following is a documentation of the seminar's study materials and findings.

# Unconventional Electronic Sound

Aside from the established way of using electronics to generate and process sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis "subtractive synthesis") to produce audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Parameters can be altered through control signals. This offers a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered [envelopes](https://en.wikipedia.org/wiki/Envelope_(music) "envelope") for amplifiers, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and often require precision components.

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. In particular the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music. The required components are easy to source and low cost. What makes these types of chips even more handy is that they don't need much external components and wiring. They can be used for generating and processing sound without large expenditure.

## CMOS Chips for Sound Creation

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS-chips.jpg">


[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute Boolean functions. Complementary metal–oxide–semiconductor (CMOS) is a technique where p-type and n-type MOSFETs are used for manufacturing logic gates. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter"), [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "Or gate"), [NAND](https://en.wikipedia.org/wiki/NAND_gate "NAND gate"), [XOR](https://en.wikipedia.org/wiki/XOR_gate "XOR gate"), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate "XNOR gate") or implement [multiplexers](https://en.wikipedia.org/wiki/Multiplexer "multiplexer"), [counters](https://en.wikipedia.org/wiki/Counter_(digital) "counter"), dividers, [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop") and [registers](https://en.wikipedia.org/wiki/Shift_register "shift register"). When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds and temporal music structures, while they produce the richness of analog sound. These circuits also yield unpredictable behavior, produce rhythmic glitches or digital noise.

Due to its simplicity, CMOS chips can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably [Nicolas Collins'](https://en.wikipedia.org/wiki/Nicolas_Collins "Collins") „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer [David Tudor](https://de.wikipedia.org/wiki/David_Tudor "David Tudor") (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions. Stanley Lunetta (1937 - 2016), avant-garde composer and artist, incorporated in the 70s digital electronics into his compositions and sound art sculptures and shared his techniques with other artists. In the experimental music community, CMOS synthesizers are therefore often referred to as "Lunettas".

## Basic Example

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_Fritzing.jpg">

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the picture above:

It shows a [square wave](https://en.wikipedia.org/wiki/Square_wave "square wave") sound generator that can be built with only three components, jumper wires and a power supply:
* inverting [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger "Schmitt trigger") IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, while the positive trigger threshold differs from the negative one, which is called hysteresis. Feeding the output back to its input via a resistor and connecting a capacitor between the input and ground, known as RC circuit, creates a relaxation oscillator or [astable multivibrator](https://en.wikipedia.org/wiki/Multivibrator#Astable_multivibrator "astable multivibrator"). The resistor limits the current for charging the capacitor and both together determine the [charging time](https://en.wikipedia.org/wiki/RC_time_constant "RC time constant").

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_Oscillator.gif">

The frequency can be roughly calculated with this formula, where V<sub>P</sub> is the positive trigger threshold voltage and V<sub>N</sub> the negative trigger threshold voltage:

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Formula.jpg">

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa. The frequency is determined through the capacitor C and the resistor R. Therefore, a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer "potentiometer") instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting [photoresistors](https://en.wikipedia.org/wiki/Photoresistor "photoresistor"), [force-sensitive resistors](https://en.wikipedia.org/wiki/Force-sensing_resistor "FSR") (FSR) or [flex sensors](https://en.wikipedia.org/wiki/Flex_sensor "flex sensor"). Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


## Logic Control

A logic gate is a single input - output device, designed to carry out a specific [Boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), mapped to two voltage levels. Over time, the two alternating voltage levels may form a periodic rectangular waveform and the speed of switching between the two levels is perceived as pitch. Aperiodic switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on- and off-states is by default close to 1:1, a 50% [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle "duty cycle"). Further circuitry is needed to change this ratio, which alters the ratio of the harmonic components to the fundamental.




In digital electronics 2-level logic, [binary numbers](https://en.wikipedia.org/wiki/Binary_number "binary number") are represented by two defined voltage levels that are specified by the used technology and circuit. Everything below a certain voltage threshold level is recognized as 0 and everything above a certain threshold level is recognized as 1. A voltage level in between the two thresholds is not defined and will produce false output triggers. The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF".

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square-Wave.jpg">

### Pull-up and Pull-down Resistors

When external circuits or devices are added to a logic input, care must be taken to keep the inputs in a defined state. When switches or transistors are used to control a logic gate, they can physically disconnect the inputs. For example, when a normally-open push button is in its default position, the high impedance input is open. This causes the pin to act like an antenna that is very susceptible to electromagnetic noise and forces the output to do unwanted operations like generating random highs or lows. This is called "floating" and introduces undesired effects.

To avoid this unpredicted behavior, a resistor should be connected to ground or to the high voltage, so that the input pin will see a defined state even when nothing else is connected, for example when a switch is opened. The pin will be able to accept an input signal when the switch is closed. A connection to V<sub>CC</sub> is called "pull-up" and a connection to ground "pull-down". For CMOS-logic, the resistor values can be several thousand ohms.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/pull-up_pull-down.jpg">

Even unused logic gates can cause problems since coupled-in interference voltages result in unwanted triggers and excess current draw. If a proper operation is desired, all unused inputs should not be left floating and connected together to GND or V<sub>CC</sub>.



## Electronic Components

The following is a list of CMOS chips and other integrated circuits for sound creation and processing. This list will be constantly extended during the seminar. It outlines for each chip its main applications and gives a short explanation. Pinout, functional diagram, truth tables and some basic example circuits are also shown. However, the overview is not completed with these examples and the main approach is to find variations, modifications or new creative combinations for experimental sound and music. Please refer to the manufacturer's technical data sheet for more detailed information.



### CD40106

The inverter is a basic part in digital electronics and performs the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub> and vice versa. The CD40106 hex Schmitt trigger inverter offers six separate inverters in one chip. The Schmitt trigger action permits unlimited rise and fall times on the input. The chip can be wired externally to build one or more square wave oscillators (see illustration). When using a potentiometer for frequency control, a resistor should be placed in series in order to prevent too low resistance between output and input.

*Applications:*
* Square Wave Generator
* Inverting Buffer


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106.jpg>

Truth table for NOT
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

"1" = High Level  
"0" = Low Level


[CD40106 Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")

### CD4093

The CD4093 contains 4 NAND Schmitt triggers, each providing 2 inputs and 1 output.

It acts as a square wave oscillator when the inputs are connected to form an inverter. The last two rows of the truth table indicate that one input has to be set to a logical high in order to attain inversion of the signal being present at the other input. When one of the inputs is wired like the CD40106 in the previous example, while the remaining input is set to high, the CD4093 generates square waves too. In this configuration, oscillation can be inhibited by setting the input to a logical low. This way, the input acts as a control input for gating the oscillator.

*Applications:*
* Square Wave Generator
* Gated Oscillator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093.jpg>

Truth table for NAND

|A|B|J=A NAND B|
|----|----|:----:|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|





[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")



### CD4070

The CD4070 contains four Exclusive-OR logic gates. Each gate has two inputs and one output. The output is high when only one of the inputs is high and the other is low and vice versa. If both inputs are high or low, the output is low. If two square wave signals are connected to the input, the output extracts the difference which results in a frequency mixer like output signal. Frequency doubling can be achieved if one square wave is applied directly to one input and connected via a resistor to its second input with a capacitor to ground. The rising and falling edge of an incoming square wave force the output to high, hence doubles the incoming frequency. The pulse width of the output signal depends on the chosen values and is shorter than the width of the input signal; approximately the length of the RC time constant. Shifting a tone up by an octave may only sound satisfactorily within a small value range.

CD4077 is the Exclusive-NOR version.

*Applications:*
* Digital Frequency Mixer
* Frequency Doubler



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070.jpg>

Truth table for XOR (CD4070)

|A|B|Y = A XOR B|
|----|----|:----:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

Truth table for XNOR (CD4077)

|A|B|Y = A XNOR B|
|----|----|:----:|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|


[CD4070 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4077b.pdf?ts=1606308007892&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4070")


### CD4015

CD4015 IC consists of two four stage shift registers.

A shift register is built of a series of interconnected [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop"). A flip-flop or latch is a bistable multivibrator circuit. This means it has two stable states which represent either 0 or 1. The state of a flip-flop can be controlled by a clock. The value to be stored is based on the signal's input state at the transition of the clock signal. A flip-flop is used to store 1 bit. In a shift register the incoming serial input data **D** is transferred to a parallel output register **Qn**. More specifically, when a memory content is stored in the first flip-flop, it is shifted to the next one, synchronized to the rising edge of a dedicated clock signal **CL**. A logical high at the reset pin is setting all outputs to zero. The reset pin should be set to low for a continuous operation.


*Applications:*
* Sequencer
* Noise Generator
* Linear-feedback Shift Register (LFSR)


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4015.jpg>

Truth table for four stage shift register

|CL|D|R|Q1|Qn|
|:----:|:----:|:----:|:----:|:----:|
|/|0|0|0|Qn-1|
|/|1|0|1|Qn-1|
|⧹|X|0|Q1|Qn|
|X|X|1|0|0|

X   = Don't Care Case  
/   = Rising Edge  
⧹   = Falling Edge  

LFSR:
A linear feedback shift register (LFSR) can be used for generating deterministic pseudorandomness. In terms of electronic sound production it can be used to build a noise source. An LFSR consists of n numbers of flip-flops which are connected in series to form a shift register as described for the CD4015. This shift register is controlled by a clock that triggers the shift process. Two junctions at a specific position within that chain of flip-flops are directed into an XOR logic gate. The resulting value is fed back into the first register. The number of stages can be extended by connecting multiple devices. The produced values are determined by the shift register's current states and total length. Since the states are finite it will repeat after a certain number of steps. The goal is to choose those taps that form the longest possible sequence of zeros and ones before they repeat. Other implementations of an LFSR exist and work similarly. To activate an LFSR each stage needs to be loaded with an initial value. This is called the seed. By using an XOR function for the feedback, having the value 0 in all flip-flops is forbidden. By using an XNOR function it is forbidden to set all flip-flops to 1. A maximum-length sequence is therefor 2<sup>n</sup> - 1. Additional operations can be introduced to produce a length of 2<sup>n</sup>. No matter if XOR or XNOR functions are used, the sequences will have the same length, while the succession of values differs. The duration of one cycle is determined by the clock frequency. When looked at a shift register from the viewpoint of a musician, the long LFSR arrangements will create white and pink noise when controlled with a high frequency (several ten thounds of hertz). Shorter cycles produce grainy tones, stuttering textures or short noise loops.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LFSR.jpg>

The Xilinx application note XAPP210 (V1.3) shows a table for maximum length sequences, which is presented here for up to 24 bits:

|n|taps from||n|taps from|
|:----:|:----:|:----:|:----:|:----:|
|3|3,2||14|14,5,3,1|
|4|4,3||15|15,14|
|5|5,3||16|16,15,13,4|
|6|6,5||17|17,14|
|7|7,6||18|18,11|
|8|8,6,5,4||19|19,6,2,1|
|9|9,5||20|20,17|
|10|10,7||21|21,19|
|11|11,9||22|22,21|
|12|12,6,4,1,||23|23,18|
|13|13,4,3,1||24|24,23,22,17|





Depending on the desired operation, other applicable devices may be CD4094, CD4014, CD4021 which are all 8-stage shift registers.
 

[CD4015 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4015b.pdf?ts=1607676770686&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4015")


### CD4022

CD4022 and CD4017 ICs implement a binary counter/divider function with 8 outputs in the CD4022 and 10 outputs in the CD4017. The positive edge of an incoming square wave, usually referred to as "clock signal", triggers successively the outputs. "Carry out" is outputting one cycle over 8 (CD4022) respectively 10 (CD4017) clock pulses. A logical high at "clock inhibit" pauses the counting process. A logical high at the "reset" pin sets the counter pulse back to the first output.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_anim.gif>


*Applications:*
* Sequencer
* Staircase Wave Form Generator
* Wave Shaper


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_animated.gif>



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Timing_Diagram.jpg>

[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")

### CD4040

This IC performs frequency division and comes with 12 outputs in the CD4020 and the CD4040 versions and 7 outputs in the CD4022 version, whereby the CD4020 is a 14-stage device. Output stages 2 and 3 (divide by 4 and 8) are not accessible. The CD4024 has 3 pins without internal connection (pin 8, 10, 13). If a square wave is applied to the input, each output creates square waves at half the frequency of its preceding output, at which the first output Q1 applies its division to the input signal and oscillates at a rate at one half, Q2 at one quarter, Q3 at one eighth Q4 at one sixteenth and so on. Several units can be cascaded for higher counting.

Control input "reset" triggers all output stages to "low". For continuous frequency division it should be kept at a logical low.


*Applications:*
* Frequency Divider
* Sub Octave Generator
* Representation of Binary Numbers

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040.jpg>


In terms of generating sound, each output producing one octave lower than its previous output, respectively input.


The timing diagram shows the relation of voltage levels between all outputs of the CD4024 IC, a 7-output stage version:
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Timing_Diagram.jpg>

[CD4040 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4040b.pdf?ts=1600261370155&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4040B "CD4040")

### CD4046


Phase locked loop

*Applications:*
* Tone Distortion
* Pitch Tracking
* Frequency Multiplication
* Voltage Controlled Square Wave Generator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046.jpg>

[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")


### CD4051

CD405x Multiplexer/Demultiplexer series comes in a 16 DIP package and is useful for switching and routing analog or digital signals.
CD4051 is a switch in a single pole octal throw configuration with three binary control inputs for setting the contacts. CD4052 can be used for multiplexing one differential channel in a double-pole quad-throw configuration and has two binary control inputs. CD4053 offers individual control over 3 channels in a single-pole double-throw configuration with an independent binary control input for each channel.

All channels are off when inhibit input is set to "high" (active low).

*Applications:*
* Wave Shaper
* Digitally-controlled Analog Switching
* Signal Routing

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_animated.gif>

Truth table for the CD4051
|C|B|A|ON CHANNEL(S)|
|----|----|----|:----:|
|0|0|0|0|
|0|0|1|1|
|0|1|0|2|
|0|1|1|3|
|1|0|0|4|
|1|0|1|5|
|1|1|0|6|
|1|1|1|7|

[CD4051 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4051b.pdf?ts=1599079621658&ref_url=https%253A%252F%252Fwww.google.com%252F "CD405xB")



### CD4066

Quad Bilateral Switch

IC CD4066 includes four identical digitally controlled switches for analog or digital signals.
Inputs and outputs are interchangeable as with conventional switches. Each switch can be controlled independently by a control input.

control logic 1 = switch on  
control logic 0 = switch off


*Applications:*
* Signal Gating
* Signal Routing


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_anim.gif>



[CD4066 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4066b.pdf?ts=1608449210166&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4066")


### CD4060

14 stage ripple-carry binary counter/divider and oscillator. Q1, Q2, Q3 and Q11 are not connected to the outside of the package.



*Applications:*
* Frequency Divider
* Square Wave Generator





<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4060.jpg>



[CD4060 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4060b.pdf "CD4060")


### CD4013
 
The CD4013 IC flip-flop is called a D flip-flop type to characterize its behavior, while D stands for "data" or "delay". It contains two identical D flip-flop arrangements. The device stores a digital state 0 or 1, which is accessible at the output **Q**. The second output **/Q** presents the inverse of **Q**. The control input **Clock** transfers the input state **D** to the output **Q** respectively **/Q**. The CD4013 is positive-edge-triggered, which means that the positive-going transition of a clock impulse triggers the device to hold the state that is present at the input and provides it at the output until the next positive-going clock signal. The additional control inputs **Set** and **Reset** have priority over the clock. With a high level on the **Set** input, the output follows its state and goes low with a high level on the **Reset** input, ignoring **D** and **Clock**.



*Applications:*
* Frequency Divider
* Counter
* Toggle Switch

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4013.jpg>


D flip-flop truth table

|C|D|R|S|Q|/Q|
|:----:|:----:|:----:|:----:|:----:|:----:|
|/|0|0|0|0|1|
|/|1|0|0|1|0|
|⧹|X|0|0|no change|no change|
|X|X|1|0|0|1|
|X|X|0|1|1|0|
|X|X|1|1|1|1|

X   = Don't Care  
/   = Rising Edge  
⧹   = Falling Edge  



[CD4013 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4013b.pdf?ts=1609946760296&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4013")


### CD4018 (under construction)

Divide-By-'N' Counter

When the outputs are fed back to the input Data, divide by 10, 8, 6, 4, 2, is calculated. For odd numbers 9, 7, 5, 3, simply use CD4011 or CD4093 to NAND two corresponding output stages and feed the inverted result back into Data. By combining multiple devices, higher divide-by functions can be calculated. Preset enable will transfer Data on the input Jam to its corresponding /Q (inverted). A logical high on the reset input causes all /Q Outputs to high.


Divide by 9: **/Q4** & **/Q5** via 1/2 CD4011 connected to input Data  
Divide by 7: **/Q3** & **/Q4** via 1/2 CD4011 connected to input Data  
Divide by 5: **/Q**2 & **/Q3** via 1/2 CD4011 connected to input Data  
Divide by 3: **/Q1** & **/Q2** via 1/2 CD4011 connected to input Data  

Divide by 10: **/Q5** connected to input Data  
Divide by 8: **/Q4** connected to input Data  
Divide by 6: **/Q3** connected to input Data  
Divide by 4: **/Q2** connected to input Data  
Divide by 2: **/Q1** connected to input Data  





*Applications:*
* Divide by 10, 8, 6, 4, 2
* Divide by 9, 7, 5, 3
* Chord Generator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4018.jpg>

FUNCTIONAL TRUTH TABLE FOR CD4018

|Clock|Reset|Preset Enable|Jam Input|/Qn|
|:----:|:----:|:----:|:----:|:----:|
|⧹|0|0|X|/Qn|
|/|0| 0| X|/Dn|
|X| 0| 1| 0|1|
|X| 0| 1| 1|0|
|X| 1| X| X|1|

/Dn = Data input for that stage  
X   = Don't Care  
/   = Rising Edge  
⧹   = Falling Edge  


[CD4018 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4018b.pdf?ts=1610571153497&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4018B "CD4018")

### LM386 - Power Operational Amplifier (under construction)

Although not part of the CMOS logic familiy this ubiquitous power op amp is a very versatile component when it comes to amplification or driving small speakers.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM386.jpg>

[LM386 Data Sheet](https://www.ti.com/lit/ds/symlink/lm386.pdf?ts=1613028335418&ref_url=https%253A%252F%252Fwww.google.com%252F "LM386")

### 555 Timer (under construction)


Note: The bipolar version (NE555) and the CMOS version (TLC555, LMC555) have the same pinout and are exchangeable. The CMOS version consumes significantly less power.

*Applications:*
* Frequency Divider
* Timer
* Pulse Delay
* Square Wave Generator
* Pulse Width Modulator

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Timer.jpg>

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Astable_Operation.jpg>
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Bistable_Operation.jpg>
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Monostable_Operation.jpg>


[LMC555 Data Sheet](https://www.ti.com/lit/ds/symlink/lmc555.pdf?ts=1609974121158&ref_url=https%253A%252F%252Fwww.google.com%252F "LMC555")


## Mixing

There are two ways of mixing signals together, active and passive mixing. Active mixing involves components, such as operational amplifiers, that need a power supply. Passive mixing works without an additional power supply, but introduces a voltage drop.

### Passive Mixing

Passive mixing is a very simple method that can be accomplished by using resistors for each source. The mixing resistors work as a voltage divider network and lower the amplitude of each signal. Therefore, the passive mixer doesn't give the sum of all input signals but the average. Small resistance values will drain more current and create distortion. Good values are between 10kΩ - 50kΩ. The advantage of this method is its low part count. To avoid attenuation and interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/passive_mixing.jpg>




### Active Mixing

For most audio applications it is desired to control the portion of each input signal in the sum of the output mix. For this, another class of active electronic components can be used, the [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier "op amp") (op amp). The basic wiring is shown below. Besides its function as a mixer with gain control over every individual input by adding voltage dividers or potentiometers, it can also be used to achieve a desired output gain by modifying the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inversed. To undo inversion, a second stage following the shown circuit can be used.


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Summing_Inverting_OpAmp.jpg>

## Passive Filters

Tone control, modifying the frequency spectrum of a signal or creative equalization are very important processes when working with audio. A filter is frequency-selective and passes only a desired range of frequencies, which is called the pass band. Outside of this pass band, frequencies are attenuated or ideally completely reduced. The boundary between pass and stop band is called cutoff frequency. The simplest way to shape an electronic signal is the use of a combination of resistor and capacitor, an RC element. This forms a first order filter. The circuit can be considered as a frequency dependent potential divider. A band-pass filter can be built with two RC elements, as a combination of a high-pass and a low-pass configuration. Since no amplifying components are involved, the amplitude of the output is lower than the input amplitude. When a filter is designed with two passive components, the transition from pass to stop band is rather smooth. For instance, a first order low-pass filter will have a 6dB/octave roll-off with increasing frequency. Unfortunately, the properties of passive filters are not sufficient to achieve a higher steepness or musical effects like resonance, which requires active filter designs. However, the simplicity and the low part count make this method very attractive for subtle tone control.


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Passive_Filter.jpg>


## Potentiometers


A potentiometer is a passive, mechanical component inside a housing. It consists of a resistive track and a movable contact, called wiper, whose position along the resistive element can be set with an actuator. The two ends of the resistive element and the end of the wiper can be accessed from outside the housing. The total resistance between the end terminals can be gradually divided into two resistance values between the respective ends of the element and the wiper.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Actuator.jpg>
a) housing, b) terminals, c) actuator, d) resistive track, e) wiper

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Equivalent.jpg>


If one end and the wiper are used, the potentiometer forms a variable resistor.
A variable voltage divider circuit can be configured by connecting a voltage (supply voltage or signal) to one of the outside pins, while the remaining outside pin is connected to GND. A voltage can be tapped at the middle pin that can be adjusted by setting the actuator. For instance, from one end point location to the other, the input voltage can be scaled from minimum to maximum. This can be used for volume control.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Volume_Control_Variable.jpg>

## Voltage Starve

"Voltage starve" or "voltage sag" can be used as an unconventional modulation technique for experimental music. It describes the effect that low supply voltage and limited current have on a circuit's behavior. Especially battery powered guitar pedals create unique dynamic distortion when the battery's voltage and current delivering capacity is unstable due to aging factors.

Changing the supply voltage will have different effects on a signal, depending on the actual circuit and the used components. Bypassing capacitors will mitigate these effects. For instance, the hysteresis thresholds in Schmitt trigger elements vary with the supply voltage. Lowering the supply voltage affects the frequency and the signal amplitude of Schmitt trigger oscillators. 

When working with an adjustable power supply or an according circuit, the impacts of limited current and voltage levels around or below the minimum requirements of an IC can be examined. A similar performance can be simulated with a simple series resistor in the power rail. 500Ω - 10kΩ potentiometers may be worth experimenting with to create odd sounds.

## Bill of Material

A list with parts that can be used for this project, is available in the folder [BOM](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/BOM/Readme.md#bill-of-material "Bill of Material")
All parts can be substituted with alternative components and equivalent foot prints.


## Requirements

Helpful tools and useful materials:


* Small mixing desk.
* Active loudspeakers.
* Worktables.
* Screw drivers.
* ESD electronic diagonal cutter.
* Precision cutter.
* Stranded wires.
* Crocodile clips.
* Laboratory power supply & connectors (preferable 4mm banana laboratory connectors).
* Jumper cables and jumper wires.
* Digital multimeter (DVM).
* Digital storage oscilloscope (DSO).
* Temperature-controlled soldering station.
* Breadboards.
* 9V Batteries.
* Battery clips.
* Good light conditions.


# Projects

The artistic range of applications for electronic projects in the fields of experimental sound, interactive music and sound art is quite large. The next sections feature works made in the context of this seminar.

## CMOS Experimenter Boards

During the summer semester 2020, experimenter boards for CMOS logic chips and a prototype of a corresponding musical interface were conceived and built. The boards and interfaces were used for a group live performance in front of the Federal Prosecutor's office in Karlsruhe.

The motivation behind this project was to produce a set of PCBs to evaluate logic ICs for sound creation and composition in artistic and educational fields. The idea of providing a CMOS experimenter board was initiated particularly with regard to today's availability of PCB manufacturers and affordable prizes. PCB prototyping and production is now completely based on computer aided electronic design (EDA) while manufacturers offer professional quality at very low costs, even for small board quantities.

Each PCB is designed around individual standard CMOS chips and their particular functions in order to create sound. The boards provide inlets and outlets, testing points, sockets, vias and pads for changing values of electronic parts and wiring alternative external circuitry. The modules can be easily extended and interconnected. This allows the user to manipulate circuit points with potentiometers, buttons, switches or sensors and to apply control voltages at appropriate input points.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS_Synthesizer.jpg">

It simplified prototyping and made customized configurations highly flexible. The experimenter boards can serve as sound modules for interactive music in live performance or installative environments as well as for algorithmic compositions. By combining several boards with different logic functions, complex switching performance can be achieved, ranging from modulated frequencies and interesting audio spectra to slow, rhythmic pulses or tone sequences. Audio and control signals are exchanged between boards via jumper cables or wires. A wide range of circuit examples with CMOS chips can be found on DIY websites and are a subject of discussion in various internet forums. These circuits can be a good basis for experimenting with CMOS chips. In addition, it is recommendable to use data sheets for all active components used in electronic projects. Power supply for the boards should comply with the power ratings of the used ICs, which is typically between 3V - 18V DC. LED series resistors need to be calculated accordingly. For the experimenter console, 9V power supply for guitar effects work well.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Experimenter_Modules.jpg">

Furthermore, the project includes laser-cutting files for a desktop console on which the boards can be mounted with screws. A power supply can be connected through the frame via banana connectors and distributed to each board.


<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/acrylic_transparent.jpg">




## Authors

Zhen Bian  
Yinxuan Chen  
Hangyan Chen  
Haram Choi  
Hongyu Guo  
Jeongmin Han  
Anna Helsen  
Jihye Jang  
Minsu Kim  
Jung Eun Lee  
Sangyi Lee  
Xingchen Liu  
Su Lu  
Victoria Mikhaylova  
Jiun-You Ou  
Ruoyi Qiu  
Vivian Reuter  
Arno Schlipf  
Florian Schwarz  
Christina Vinke  
Julian Vollmert  
Dakang Wang  
Huiyeon Yun  
Rui Zhang  
Yunfei Zhang  
Xinyi Zhao  
Pei Zhou  

**Lorenz Schwarz** - *lecturer*

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Bread_Board.jpg">

## License

The content of this documentation is licensed under the [Creative Commons Attribution 3.0 Unported license](https://creativecommons.org/licenses/by/3.0/ "CC BY 3.0"), software is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. Copyright remains with the author(s)

## Acknowledgment

* Thanks to Holger Förterer and Dr. Paul Modler

[Circuitry-Based Sound](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#circuitry-based-sound)
