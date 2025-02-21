
# Circuitry-Based Sound


![Circuitry-Based Sound ZKM 2023](/Img/CBS2023_ZKM_Jihye-Jang_sm.jpg)
*Group live performance at the ZKM*

<br>
<br>

<!--
![Technical Setup with self built audio electronics, laboratory power supply, mixing desk, and loudspeaker](/Img/Circuitry_Based_Sound_Foto_Yunfei_Zhang.jpg)
*Photo: Yunfei Zhang*
<br>
<br>
-->




"Circuitry-Based Sound" is an artistic workshop at the intersection of electronic music, sound art, and performance, exploring the low-threshold use of analog sound technologies in structured improvisation, experimental music, and live electronics. The course provides hands-on skills for building custom musical circuits and modifying existing audio hardware, offering practical knowledge of electronics for sound creation and DIY instrument design.

The workshop covers basic electronics, soldering, and assembling circuits on breadboards and perfboards, as well as their applications in audio composition and installation art. A major focus is on hardware prototyping, including testing, fault finding, and designing electronic instruments, with an emphasis on musical interaction through experimental interfaces and haptic controllers.

Beyond the technical aspects, the project explores the performative and aesthetic potential of self-built audio circuits, enabling collaborative music-making in concert settings.

Below is a documentation of the workshop’s study materials and findings.

<br>
<br>
<br>
<br>

<div align="center">
 
[**TABLE OF CONTENTS**](/readme.md#table-of-contents)
</div>

---

[**INTRODUCTION**](/readme.md#introduction)
  - [Unconventional Electronic Sound](/readme.md#unconventional-electronic-sound)
  - [CMOS Chips for Sound Creation](/readme.md#cmos-chips-for-sound-creation)
  - [Basic Example](/readme.md#basic-example)
  - [Logic Control](/readme.md#logic-control)
  - [Building Circuits with Breadboards](/readme.md#building-circuits-with-breadboards)
  - [Identifying IC Pins
](/readme.md#identifying-ic-pins)
<br>
<br>

[**ELECTRONIC COMPONENTS**](/readme.md#electronic-components)
  - [Numerical Index](/readme.md#numerical-index)
<br>
<br>

[**BASIC PRINCIPLES AND APPLICATIONS**](/readme.md#basic-principles-and-applications)
  - [Signal Mixing](/readme.md#mixing)
  - [Passive Filters](/readme.md#passive-filters)
  - [Potentiometers](/readme.md#potentiometers)
  - [LDRs (light-dependent resistors)](/readme.md#ldrs-light-dependent-resistors)
  - [Pull-up and Pull-down Resistors](/readme.md#pull-up-and-pull-down-resistors)
<br>
<br>

[**EXPLORATORY SOUND CIRCUITS**](/readme.md#exploratory-sound-circuits)
  - [Linear Feedback Shift Register](/readme.md#linear-feedback-shift-register)
  - [Step Sequencer](/readme.md#step-sequencer-under-construction)
  - [Melody Generator](/readme.md#melody-generator)
  - [Voltage Starve](/readme.md#voltage-starve)
<br>
<br>

<!--
[**PHOTOS**](/readme.md#photos)
<br>
<br>
-->

[**MATERIALS**](/readme.md#Materials)
  - [Requirements](/readme.md#requirements)
  - [Bill of Materials](/readme.md#bill-of-materials)
  - [Artists](/readme.md#artists)
  - [Acknowledgment](/readme.md#acknowledgment)
  - [Literature](/readme.md#literature)
  - [Links](/readme.md#links)
  - [License](/readme.md#license)

---


<br>

# Disclaimer

The authors accept no responsibility for any damages arising from or in connection with the use of the information provided on this website. While we strive to ensure that all content is accurate and complete, unintended errors may occur. Users are encouraged to cross-check and verify the information before applying it.
<br>
<br>



# Introduction

![Technical Setup with self built audio electronics, laboratory power supply, mixing desk, and loudspeaker](/Img/Circuitry_Based_Sound_Foto_Yunfei_Zhang.jpg)
*Photo: Yunfei Zhang*
<br>
<br>


Aside from the conventional use of electronics in analog synthesizers to generate and process sound, there are also unconventional applications for creating experimental music and sound, which will be introduced below. Analog synthesizers typically employ techniques like [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis "subtractive synthesis"), where an oscillator’s output is filtered and dynamically shaped in volume. Variations of this concept are found in most synthesizers, both analog and digital. Hardware-based analog modular synthesizers are highly valued for their distinctive sound and, in particular, for their voltage-controlled compositional flexibility and immediate, tactile sound manipulation. However, achieving these functionalities, especially when building analog circuits for modular synthesizers, requires relatively complex circuits, a high component count, and precision parts.




### Unconventional Electronic Sound

Another approach to electronic sound creation emerges from hardware hacking and circuit bending techniques. In particular, the use of logic circuits beyond their conventional applications presents a compelling method for building customized instruments for artistic sound production and interactive music. These components are inexpensive, widely available, and require minimal external circuitry, making them highly accessible for DIY experimentation. Their ability to generate and process sound with minimal wiring and low cost makes them a powerful tool for unconventional electronic music.


### CMOS Chips for Sound Creation


![Various CMOS-chips in SMD and through-hole technology and with different foot prints](/Img/CMOS-chips.jpg)
*Various CMOS chips*
<br>
<br>

[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute Boolean functions. The development of electronic circuits capable of performing logical functions was a major milestone in the history of computers. Complementary metal–oxide–semiconductor (CMOS) technology utilizes p-type and n-type MOSFETs to construct logic gates, where voltage levels represent binary states (0 and 1). A Boolean function is a logical expression that maps one or more binary inputs (0 and 1) to a single binary output. Produced as integrated circuits, individual CMOS components implement basic logic functions such as [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter"), [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "Or gate"), [NAND](https://en.wikipedia.org/wiki/NAND_gate "NAND gate"), [XOR](https://en.wikipedia.org/wiki/XOR_gate "XOR gate"), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate "XNOR gate"). More complex chips provide functions like  [multiplexers](https://en.wikipedia.org/wiki/Multiplexer "multiplexer"), [counters](https://en.wikipedia.org/wiki/Counter_(digital) "counter"), dividers, [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop") and [registers](https://en.wikipedia.org/wiki/Shift_register "shift register").

A binary logic signal, which encodes 0 and 1 as two distinct voltage levels, can be represented as a square wave. A logic signal that continuously switches between these two voltage states can therefore be interpreted as a square wave—and thus as sound. 

The following diagram illustrates the waveform of a square wave and assigns the values 0 and 1 to its two voltage states.
<br>
<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Square_Wave_as_Binary_DARK.svg">
  <img alt="Demonstrating the relationship between a square wave and its equivalent binary representation (0s and 1s)." src="/Img/Square_Wave_as_Binary_LIGHT.svg">
</picture>



When the relationship between logic operations, voltage, and sound is understood, CMOS logic chips become an inexhaustible resource for unconventional electronic sound. These chips generate square waves that can be modified, shaped, gated, sequenced, and layered. By combining different logic functions, they enable the creation of a vast range of unique sounds and temporal musical structures, while still retaining the richness of analog sound. Additionally, these circuits often exhibit unpredictable behavior, producing rhythmic glitches, digital noise, and evolving textures, making them an essential tool for experimental sound design.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Switching_Circuit_DARK.svg">
  <img alt="Boolean logic as switching circuit." src="/Img/Switching_Circuit_LIGHT.svg">
</picture>

 

Logical operations can be implemented as switching circuits, where single-pole single-throw (SPST) switches represent inputs, and an LED indicates the output result. Both the switch and the LED have two distinct states: on and off.
- An open switch corresponds to logical 0, while a closed switch represents logical 1.
- A lit LED indicates 1, whereas an unlit LED represents 0.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Logic_Gates_DARK.svg">
  <img alt="Illustration of electronic logic gate symbols." src="/Img/Logic_Gates_LIGHT.svg">
</picture>



A truth table is used in Boolean algebra to display all possible input and output values of a logical expression.

Output comparison of 2-input logic gates:

<br>
<div align="center">

| INPUT A | INPUT B | AND | NAND | OR | NOR | XOR | XNOR |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `0` | 0 | 1 | 0 | 1 | 0 | 1 |
| `0` | `1` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `0` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `1` | 1 | 0 | 1 | 0 | 0 | 1 |
 
</div>
<br>
<br>

Due to their simplicity and accessibility, CMOS chips are widely used for artistic and educational purposes, as their technical operations are easy to understand and closely related to basic electronics concepts. This topic has been explored in various publications, most notably in [Nicolas Collins'](https://en.wikipedia.org/wiki/Nicolas_Collins "Collins") *Handmade Electronic Music: The Art of Hardware Hacking* (2006). American composer [David Tudor](https://de.wikipedia.org/wiki/David_Tudor "David Tudor") (1926–1996) is regarded as a pioneer of self-built electronic circuits and instruments, which he integrated into his compositions. Similarly, avant-garde composer and artist Stanley Lunetta (1937–2016) began incorporating digital electronics into his compositions and sound art sculptures in the 1970s, sharing his techniques with fellow artists. As a result, in the experimental music community, CMOS-based synthesizers are often referred to as “Lunettas”, honoring Lunetta’s contributions to DIY electronic music.





### Basic Example


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CMOS_Oscillator_Breadboard_DARK.svg">
  <img alt="Simplified depiction of a Schmitt trigger oscillator on a breadboard." src="/Img/CMOS_Oscillator_Breadboard_LIGHT.svg">
</picture>


The “Hello World” of CMOS synthesizers, illustrating how easily sound can be generated, is shown in the diagram above. It depicts a [square wave](https://en.wikipedia.org/wiki/Square_wave "square wave") sound generator that requires only three components, jumper wires, and a power supply:

- An inverting [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger "Schmitt trigger") IC (e.g., CD40106)
- A capacitor (C)
- A resistor (R)
  
An inverting Schmitt trigger is an active electronic component whose output state toggles complementarily in response to an input signal, with distinct positive and negative trigger thresholds—a property known as hysteresis. By feeding the output back to the input via a resistor (R) and connecting a capacitor (C) between the input and ground, a circuit known as an RC oscillator is formed. This configuration, commonly referred to as a relaxation oscillator or [astable multivibrator](https://en.wikipedia.org/wiki/Multivibrator#Astable_multivibrator "astable multivibrator"), generates a continuous square wave signal. The resistor limits the charging current, while the capacitor and resistor together determine the [RC time constant](https://en.wikipedia.org/wiki/RC_time_constant "RC time constant"), which sets the oscillator's frequency.

<!-- ANIMATED GIF -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Schmitt_Trigger_DARK.gif">
  <img alt="Animated iIllustration of a Schmitt trigger oscillator and its waveforms." src="/Img/Schmitt_Trigger_LIGHT.gif">
</picture>


<br>
<br>


### Calculating the Oscillation Frequency

The frequency can be roughly calculated with this formula


$$
f=\dfrac{1}{T}=\dfrac{1}{RC ln \left[\left(\dfrac{V_P}{V_N}\right)\left(\dfrac{V_{DD}-V_N}{V_{DD}-V_P}\right)\right]}
$$

where V<sub>P</sub> is the positive trigger threshold voltage and V<sub>N</sub> the negative trigger threshold voltage.


For a **10V power supply**, the typical threshold voltages, according to the datasheet, are $V_P \approx 5.9V$ and $V_N \approx 3.9V$.

<!--
Substituting **$V_{DD} = 10V$, $V_P = 5.9V$, and $V_N = 3.9V$**:  

$$
f = \frac{1}{RC \cdot \ln \left[\left(\frac{5.9}{3.9}\right) \left(\frac{10 - 3.9}{10 - 5.9}\right)\right]}
$$

$$
f = \frac{1}{RC \cdot \ln (2.2508)}
$$

Since:

$$
\ln (2.2508) \approx 0.8113
$$
-->

The final formula simplifies to:

$$
f \approx \frac{1}{RC \cdot 0.8113}
$$

<br>

Based on this formula, the following table provides an approximation:

| @10V   | **0.01µF** | **0.1µF** | **0.22µF** | **0.47µF** | **1µF** | **22µF** | **47µF** |
|--------|---------|--------|---------|---------|--------|-------|-------|
| 1k     | 120000 Hz  | 12000 Hz  | 5600 Hz  | 2600 Hz  | 1200 Hz  | 56 Hz  | 26 Hz  |
| 4.7k   | 26000 Hz   | 2600 Hz   | 1200 Hz  | 560 Hz   | 260 Hz   | 12 Hz  | 5.6 Hz   |
| 10k    | 12000 Hz   | 1200 Hz   | 560 Hz   | 260 Hz   | 120 Hz   | 5.6 Hz   | 2.6 Hz   |
| 47k    | 2600 Hz    | 260 Hz    | 120 Hz   | 56 Hz    | 26 Hz    | 1.2 Hz   | 0.56 Hz   |
| 82k    | 1500 Hz    | 150 Hz    | 68 Hz    | 32 Hz    | 15 Hz    | 0.68 Hz   | 0.32 Hz   |
| 100k   | 1200 Hz    | 120 Hz    | 56 Hz    | 26 Hz    | 12 Hz    | 0.56 Hz   | 0.26 Hz   |
| 470k   | 260 Hz     | 26 Hz     | 12 Hz    | 5.6 Hz     | 2.6 Hz     | 0.12 Hz   | 0.06 Hz   |




<br>
<br>

The values in the table should be used as a starting point, as actual frequencies may vary due to chip manufacturing tolerances, large capacitor tolerances, and the effects of parasitic capacitance and additional resistance introduced by wiring and jumper cables. Therefore it is difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa. The frequency is determined through the capacitor C and the resistor R. Therefore, a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer "potentiometer") instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting [photoresistors](https://en.wikipedia.org/wiki/Photoresistor "photoresistor"), [force-sensitive resistors](https://en.wikipedia.org/wiki/Force-sensing_resistor "FSR") (FSR) or [flex sensors](https://en.wikipedia.org/wiki/Flex_sensor "flex sensor"). Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


### Logic Control

In digital electronics, [binary code](https://en.wikipedia.org/wiki/Binary_code "binary code") is represented by two defined voltage levels that are specified by the used technology and circuit. Everything below a certain voltage threshold level is recognized as 0 and everything above a certain threshold level is recognized as 1. A voltage level in between the two thresholds is not defined or forbidden and will produce false output triggers. CMOS digital inputs have a high impedance and pick up thermal noise voltages if left floating. Unused inputs should be tied to a defined voltage. Other input configurations (e.g. taster, toggle switches,) require [pull-up or pull-down resistors](/readme.md#pull-up-and-pull-down-resistors "pull-up or pull-down"). The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF". 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Logic_Signal_DARK.svg">
  <img alt="Common CMOS input voltage levels without and with Schmitt trigger implementation." src="/Img/Logic_Signal_LIGHT.svg">
</picture>



V<sub>IH</sub> is the minimum input voltage that will be interpreted as a logical high, while V<sub>IL</sub> is the maximum input voltage that will be interpreted as a logical low. The region in between is undefined and may trigger unpredictable highs or lows (chattering). This problem is solved by implementing a Schmitt trigger with different thresholds for negative-going and positive-going input voltages, depending on whether the input signal is changing from high to low (V<sub>N</sub>) or low to high (V<sub>P</sub>). When the input is between the two thresholds the output retains its value.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Square_Wave_DARK.svg">
  <img alt="Analytical description of a square wave logic signal." src="/Img/Square_Wave_LIGHT.svg">
</picture>



A logic gate is a single input - output device, designed to carry out a specific [Boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), mapped to two voltage levels. Over time, the two alternating voltage levels may form a periodic rectangular waveform and the speed of switching between the two levels is perceived as pitch. Certain logic gates can be repurposed as oscillators in this way. In digital systems, this principle is used to generate clock signals, which are essential for synchronizing processes. Logic gates with two inputs compare the signals at their inputs and generate an output based on the corresponding logic function, enabling signal processing and modification. Other logic gates can count sequential square wave pulses, outputting a single pulse per cycle. Some function as frequency dividers, halving the input signal’s frequency. Additionally, various CMOS chips can act as binary-controlled switches. These and many other functions can be considered as modulation effects, which transform or modify the incoming audio signal. 

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Gated_Oscillator_DARK.svg">
  <img alt="Schematic of a gated square wave oscillator with the CD4093, showing input control and output waveform." src="/Img/Gated_Oscillator_LIGHT.svg">
</picture>


Aperiodic switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on- and off-states is by default close to 1:1, a 50% [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle "duty cycle"). Further circuitry is needed to change this ratio, which alters the ratio of the amplitudes of the harmonic components to the fundamental. The [square wave](https://en.wikipedia.org/wiki/Square_wave "Square wave") contains only overtones with odd numbered harmonics (⅓, ⅕, ⅐, etc). The relative amplitudes of the harmonics are equal to 1/harmonic number n.




### Building Circuits with Breadboards

Since assembling an electronic circuit on a breadboard does not require soldering (unlike working with printed circuit boards) it allows for quick prototyping and easy modifications. This makes breadboards particularly useful for testing and developing preliminary functional versions of circuit designs, which can then be used to verify circuit behavior and operating points. They serve as temporary platforms for functional verification and feasibility testing, while their flexibility and reusability make troubleshooting easier.

Typically, circuits built on breadboards are not suitable as permanent solutions, as the connections rely solely on spring contacts. These contacts can corrode over time or become loose, leading to unreliable connections. This is especially problematic during transport, as components may detach.

Nevertheless, breadboards are highly effective for DIY electronic music projects, as they allow for rapid prototyping and easy circuit adjustments to match sonic preferences. They can also be expanded with control elements, enabling intuitive sound manipulation and music interaction.


Breadboards are made of plastic and feature a standardized hole grid with metal spring contacts. The grid spacing is 2.54 mm (0.1 inch), making it compatible with most standard electronic components and allowing for easy insertion and interconnection.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Breadboard_DARK.svg">
  <img alt="How a Breadboard Works: Functional Sections and Internal Wiring" src="/Img/Breadboard_LIGHT.svg">
</picture>

<br>
<br>


A typical breadboard consists of three main sections:

- **Power Rails:**
 Located along the outer edges, these two continuous strips are internally connected and typically used to distribute power across the board (usually indicated with the     symbols + and - and/or the colors red and blue).
- **DIP Support:** A central gap that separates the two sides of the breadboard, designed to accommodate dual in-line package (DIP) components, such as integrated circuits (ICs).
- **Terminal Strips:** Arranged perpendicularly to the power rails, these rows of interconnected holes on either side of the centerline provide access to the pins of DIP components, enabling circuit connections.

In most circuits, the majority of connections go to ground or a supply voltage. For convenience, it’s best to connect the power rails on both sides of the breadboard so you can easily access ground or the supply at any point across the entire board.

### Identifying IC Pins

Manufacturers provide documentation for integrated circuits (ICs) and other electronic components in so-called datasheets, which describe the components' characteristics and functions. In an IC datasheet, the pinout diagram explains the function of each pin (or terminal) while also providing important information about operating conditions and supply voltage. When using ICs, it is important and highly recommended to have the datasheet readily available to ensure proper implementation of the component.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/IC_DARK.svg">
  <img alt="Illustration of an integrated circuit (IC) and a detailed view of one functional block from its internal circuitry" src="/Img/IC_LIGHT.svg">
</picture>

Illustration of an integrated circuit (IC) and a detailed view of one functional block from its internal circuitry


For Dual In-Line Packages (DIL or DIP ICs), the pins are numbered sequentially. When looking at a DIP IC from above, there is typically a marking or notch on one of the shorter sides of the package, which serves as an orientation guide.

To correctly identify the pin numbering:

- Align the IC so that the notch or marking is at the top.
- Start counting from the first pin on the left side of the notch (Pin 1).
- Continue numbering counterclockwise around the IC.

This standard numbering convention helps ensure correct connections when integrating the IC into a circuit.




<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/GH_IC_Pinout_DARK.svg">
  <img alt="A diagram illustrating how to identify the pinout of an IC and showing the typical power connections of a CMOS chip" src="/Img/GH_IC_Pinout_LIGHT.svg">
</picture>

Most CMOS chips have 14 or 16 pins.
With only few exceptions (e.g., CD4049UB and CD4050B), the bottom-left pin is typically connected to ground (GND or Vss), while the top-right pin (the last pin) is connected to the positive supply voltage (VDD).

### Practical Breadboarding Tips 
 
- **Use a color code for wires** – Standardizing wire colors (e.g., red for power, black or blue for ground, other colors for signals) helps with readability and troubleshooting.
- **Document your work** – Take notes and photos of your circuit at different stages to keep track of progress and troubleshoot issues later.
- **Update your schematic** when modifying a circuit—redraw it and clearly mark any changes.
- **Refer to datasheets** – Always check component pinouts and electrical characteristics online before connecting parts to ensure proper functionality.
- **Keep your workspace organized** – Remove unused cables and sort components properly to avoid mistakes and make debugging easier.
- **Dispose of burned chips** –  If a chip overheats or burns due to incorrect power supply connections or wiring faults, it is likely damaged and should be replaced rather than reused to prevent further issues.

## How to Read a Schematic

A schematic visually represents how components are connected by using lines to indicate electrical connections between their terminals. In more complex circuits, these lines, called nets, can branch, split, or form junctions. Junctions, where multiple wires connect electrically, are indicated with a dot. If wires cross without forming a connection, a small bridge should be used to clarify that they belong to separate nets.

Electronic components are represented using standardized symbols in a schematic, allowing anyone familiar with these symbols to identify components and understand their function within a circuit. Below is an overview of the most common symbols related to DIY electronics for music and sound creation.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Components_DARK.svg">
  <img alt="Common Electronic Schematic Symbols" src="/Img/Components_LIGHT.svg">
</picture>

Voltage supply lines (power nets) are often not drawn explicitly throughout the schematic but are instead represented by a symbol (e.g., Vcc, Vdd, or V+) that appears at multiple locations in the circuit. Similarly, ground (GND) connections are frequently represented by a ground symbol, avoiding the need to draw individual connections for every grounded component. This makes schematics easier to read.

Integrated circuits (ICs) have multiple pins, each serving a specific function. In a schematic, pin numbers are usually indicated next to the IC symbol to help identify which pin corresponds to which function.

In schematics, components are typically labeled with abbreviations, such as R for resistors, C for capacitors, D for diodes, and so on. Along with these labels, a numerical value is often provided to specify the exact component used in the circuit (e.g., "R1 10kΩ").


# Electronic Components

The following is a list of CMOS chips and other integrated circuits used for sound creation and processing. This list will be continuously expanded throughout the seminar. Each chip’s primary applications are outlined, along with a brief explanation. Pinouts, functional diagrams, truth tables, and basic example circuits are also provided. However, these examples do not represent a comprehensive guide. The main objective is to explore variations, modifications, and new creative combinations for experimental sound and music. For detailed specifications, please refer to the manufacturer’s datasheet.

## Numerical Index


- [CD40106](/readme.md#cd40106)
- [CD4093](/readme.md#cd4093)
- [CD4070](/readme.md#cd4070)
- [CD4015](/readme.md#cd4015)
- [CD4022](/readme.md#cd4022)
- [CD4040](/readme.md#cd4040)
- [CD4046](/readme.md#cd4046)
- [CD405x](/readme.md#cd405x)
  - [CD4051](/readme.md#cd4051)
  - [CD4052](/readme.md#cd4052)
  - [CD4053](/readme.md#cd4053)
- [CD4066](/readme.md#cd4066)
- [CD4060](/readme.md#cd4060)
- [CD4013](/readme.md#cd4013)
- [CD4018](/readme.md#cd4018-under-construction)
- [555 Timer](/readme.md#555-timer-under-construction)
- [LM386](/readme.md#lm386---power-operational-amplifier-under-construction)




### CD40106

The inverter is a fundamental component in digital electronics, performing the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub>, and vice versa. The CD40106 Hex Schmitt Trigger Inverter contains six independent inverters in a single chip. Unlike standard inverters, its Schmitt trigger action provides hysteresis, allowing for unrestricted rise and fall times on the input, which makes it especially robust against noise. This chip can be externally wired to function as one or more square-wave oscillators (see illustration).

When using a potentiometer for frequency control, always include a series resistor to prevent an excessively low-resistance path between the output and input. Without it, lowering the potentiometer to its minimum value can disrupt proper operation, pushing the oscillator to extremely high frequencies, potentially beyond the audible range. A reliable setup consists of a **100kΩ potentiometer** in series with a **1kΩ resistor** and a **100nF capacitor**, allowing frequency tuning from approximately **100 Hz to several kilohertz**. For lower frequencies, increasing the capacitance expands the range. Using a **1µF** capacitor enables oscillations between **10 Hz and several hundred Hertz**, while even lower frequencies can be achieved with larger capacitance values.

*Applications:*
* Square Wave Generator
* Inverting Buffer



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD40106_DARK.svg">
  <img alt="Pinout of the CD40106 IC and a schematic of a CMOS oscillator built with CD40106 hex Schmitt trigger inverter." src="/Img/CD40106_LIGHT.svg">
</picture>



Truth table for NOT
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

"1" = High Level  
"0" = Low Level


[CD40106 Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")
<br>
<br>

### CD4093

The CD4093 contains four NAND Schmitt triggers, each with two inputs and one output. When configured as an inverter, it can function as a square wave oscillator. The last two rows of the truth table show that one input must be set to a logical high for the gate to act as an inverter, allowing the second input to control the output. By wiring one input like the CD40106 oscillator in the previous example and keeping the other input high, the CD4093 can also generate square waves.

*Applications:*
* Square Wave Generator
* Gated Oscillator


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4093_Button_DARK.svg">
  <img alt="Pinout of the CD4093 IC and a schematic of an oscillator built with a CD4093 CMOS chip and controllable by a push button." src="/Img/CD4093_Button_LIGHT.svg">
</picture>


Oscillators built with 2-input NAND Schmitt triggers can be manually switched on and off using a push button. When the push button is not pressed (normally open), the logical low at the second input forces the output high, regardless of the state of the first input (see NAND truth table). The image above illustrates how to configure a normally open push button as an ON switch to control the sound. A [pull down resistor](/readme.md#pull-up-and-pull-down-resistors) ensures the input remains at a defined logic low when the push button is open. When the push button is closed, the power supply applies a logical high, allowing the NAND gate to oscillate. In this setup, the second input serves as a control input for gating the oscillator. Instead of a manually operated push button, a logic signal can be applied to the second input for automated control.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4093_Gated_DARK.svg">
  <img alt="Pinout of the CD4093 IC and a schematic of an oscillator built with a CD4093 CMOS chip which in turn is controlled by a second oscillator configuration of the same chip. This is called a gated oscillator." src="/Img/CD4093_Gated_LIGHT.svg">
</picture>



Truth table for NAND

|A|B|J=A NAND B|
|----|----|:----:|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|





[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")
<br>
<br>



### CD4070


The CD4070 contains four Exclusive-OR (XOR) logic gates, each with two inputs and one output. The output is high (1) when only one of the inputs is high, and low (0) when both inputs are either high or low. When two square wave signals are applied to the inputs, the XOR gate acts as a frequency mixer, producing an output that represents the difference between the input signals. This creates a rich, harmonically altered waveform useful in sound synthesis. The CD4070 can also be used for frequency doubling by applying a single square wave directly to one input and feeding it to the second input through a resistor, with a capacitor to ground. In this configuration, the output is driven high on both the rising and falling edges of the input waveform, effectively doubling the frequency. The pulse width of the output depends on the resistor-capacitor (RC) time constant and is shorter than the original square wave cycle. However, when shifting a tone up by an octave using this method, the perceived effect may only be musically satisfying within a limited range of component values.

CD4077 is the Exclusive-NOR version.

*Applications:*
* Digital Frequency Mixer
* Frequency Doubler


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4070_DARK.svg">
  <img alt="Pinout of the CD4070 IC and a schematic that shows sigital frequency mixing with the said chip." src="/Img/CD4070_LIGHT.svg">
</picture>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/XOR_DARK.svg">
  <img alt="Timing diagram of the CD4070 XOR gate with two suqare waves as inputs, showing the resulting output waveform" src="/Img/XOR_LIGHT.svg">
</picture>

Truth table for XOR (CD4070)

|A|B|Y = A XOR B|
|----|----|:----:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

<!-- 
Truth table for XNOR (CD4077)

|A|B|Y = A XNOR B|
|----|----|:----:|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|
-->

[CD4070 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4077b.pdf?ts=1606308007892&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4070")
<br>
<br>


### CD4015

CD4015 IC consists of two four stage shift registers.

The CD4015 is an integrated circuit containing two independent 4-stage shift registers. A shift register is a series of interconnected [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop"), which are bistable multivibrators capable of storing binary states (0 or 1). Each flip-flop stores one bit of data, and its state is controlled by a clock signal. On each clock pulse, the stored data shifts from one flip-flop to the next. In the CD4015, serial input data (D) is shifted through the register stages and appears at the parallel outputs (Qn), synchronized with the rising edge of the clock signal (CL). When a bit is stored in the first flip-flop, it moves sequentially through the register stages with each clock cycle. A logical high at the reset pin clears all stored values, setting the outputs to zero. To enable continuous operation, the reset pin should be kept low.

*Applications:*
* Sequencer
* Noise Generator
* Linear-feedback Shift Register ([LFSR](/readme.md#linear-feedback-shift-register "LFSR"))

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4015_DARK.svg">
  <img alt="Pinout of the CD4015 IC and a schematic symbol describing the functions of the two 4-stage shift registers included in one chip." src="/Img/CD4015_LIGHT.svg">
</picture>



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





[CD4015 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4015b.pdf?ts=1607676770686&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4015")
<br>
<br>


### CD4022

The CD4022 and CD4017 are counter/divider ICs, with the CD4022 providing 8 outputs and the CD4017 providing 10 outputs. These chips increment their output sequentially on the rising edge of an incoming clock signal. The "carry out" pin generates a pulse once every 8 clock cycles (CD4022) or 10 clock cycles (CD4017), making it useful for cascading multiple counters. A logical high at the "clock inhibit" pin pauses the counting process, preventing further increments. Similarly, a logical high at the "reset" pin resets the counter, setting it back to the first output stage.


*Applications:*
* Sequencer
* Staircase Wave Form Generator
* Wave Shaper

<!-- IMAGE -->


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4022_DARK.svg">
  <img alt="Pinout of the CD4022 IC and a schematic symbol describing the functions of the counter/divider." src="/Img/CD4022_LIGHT.svg">
</picture>



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4022_Outputs_DARK.svg">
  <img alt="CD4022 timing diagram." src="/Img/CD4022_Outputs_LIGHT.svg">
</picture>




[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")
<br>
<br>

### CD4040

The CD4040, CD4020, and CD4024 are binary counter/divider ICs that perform frequency division. The CD4040 and CD4020 provide 12 outputs, while the CD4024 has 7 outputs. The CD4020 is a 14-stage counter, but its divide-by-4 and divide-by-8 outputs (stages 2 and 3) are not accessible. The CD4024 also has three pins with no internal connection (pins 8, 10, and 13).

When a square wave clock signal is applied to the input, each output generates a square wave at half the frequency of the preceding stage. The first output (Q1) oscillates at half the input frequency, Q2 at one-quarter, Q3 at one-eighth, Q4 at one-sixteenth, and so on. This makes these ICs useful for octave division, subharmonic generation, and frequency scaling. Multiple counters can be cascaded for extended division.

The "reset" pin sets all outputs low (0) when activated. For continuous frequency division, it should be kept at a logical low state.

*Applications:*
* Frequency Divider
* Sub Octave Generator
* Representation of Binary Numbers

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4040_DARK.svg">
  <img alt="Pinout of the CD4040 IC and a schematic symbol describing the functions of the frequency divider." src="/Img/CD4040_LIGHT.svg">
</picture>




For sound generation with square waves, each output produces a frequency one octave lower than the previous stage, with the input serving as the highest frequency reference.

The timing diagram below illustrates the voltage relationships between all outputs of the CD4024, the 7-stage version of this counter/divider IC:

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4040_Outputs_DARK.svg">
  <img alt="CD4040 timing diagram." src="/Img/CD4040_Outputs_LIGHT.svg">
</picture>



[CD4040 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4040b.pdf?ts=1600261370155&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4040B "CD4040")
<br>
<br>

### CD4046


Phase locked loop

*Applications:*
* Tone Distortion
* Pitch Tracking
* Frequency Multiplication
* Voltage Controlled Square Wave Generator


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4046_DARK.svg">
  <img alt="Pinout of the CD4046 IC and a schematic of the phase locked loop circuit built with the CD4046." src="/Img/CD4046_LIGHT.svg">
</picture>



[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")

<br>
<br>

### CD405x

The CD405x series consists of CMOS analog switches available in a 16-pin DIP package, commonly used for switching and routing both analog and digital signals.

The on-resistance (R<sub>ON</sub>) of these switches depends on the input voltage, power supply voltage, and temperature. For CD405x devices, this resistance typically ranges from 120Ω to over 200Ω, which may cause some signal distortion in certain applications. However, for the purposes of this project, this resistance is generally low enough to be negligible.

Key Functional Notes:
- Unused control pins must be connected to either GND or V<sub>DD</sub> to prevent floating inputs.
- Inhibit input (active low): When set high, all channels are switched off.
- V<sub>EE</sub> (Pin 7) is used for dual-supply operation. In single-supply mode, it should be tied to ground.



*Applications:*
* Wave Shaper
* Digitally-controlled Analog Switching
* Signal Routing
* controlling LEDs

#### CD4051

The CD4051 is an analog switch configured as a single-pole, 8-throw (SP8T) multiplexer with three binary control inputs for selecting the active channel.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4051_DARK.svg">
  <img alt="Pinout of the CD4051 IC and a schematic symbol representing the digitally controlled single pole octal throw function." src="/Img/CD4051_LIGHT.svg">
</picture>


<!--
<img src=/Img/CD4051_animated.gif>
-->


Truth table for the CD4051  

|INHIBIT|C|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|:---:|
|0|0|0|0|0|
|0|0|0|1|1|
|0|0|1|0|2|
|0|0|1|1|3|
|0|1|0|0|4|
|0|1|0|1|5|
|0|1|1|0|6|
|0|1|1|1|7|
|1|X|X|X|None|  

X = Don't Care

#### CD4052

The CD4052 is an analog switch configured as a double-pole, 4-throw (DP4T) multiplexer, allowing for the selection of one of four differential signal pairs. It has two binary control inputs for channel selection.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4052_DARK.svg">
  <img alt="Pinout of the CD4052 IC and a schematic symbol representing the digitally controlled double-pole quad-throw function." src="/Img/CD4052_LIGHT.svg">
</picture>


Truth table for the CD4052  

|INHIBIT|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|
|0|0|0|X0, Y0|
|0|0|1|X1, Y1|
|0|1|0|X2, Y2|
|0|1|1|X3, Y3|
|1|X|X|None|

X = Don't Care

#### CD4053

The CD4053 is a triple single-pole, double-throw (SPDT) analog switch, with each of its three channels individually controlled by an independent binary input.

<!--
When the control signal is less than 1/3 V<sub>DD</sub>, z is connected to x0. When the control signal is more than 2/3 V<sub>DD</sub>, z is connected to y1.
 -->


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4053_DARK.svg">
  <img alt="Pinout of the CD4053 IC and a schematic symbol representing the digitally controlled CMOS chip, containing three single-pole double-throw CMOS switches." src="/Img/CD4053_LIGHT.svg">
</picture>

Truth table for the CD4053  

|INHIBIT|C|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|:---:|
|0|X|X|0|ax|
|0|X|X|1|ay|
|0|X|0|X|bx|
|0|X|1|X|by|
|0|0|X|X|cx|
|0|1|X|X|cy|
|1|X|X|X|None|

X = Don't Care

[CD405x Data Sheet](https://www.ti.com/lit/ds/symlink/cd4051b.pdf?ts=1599079621658&ref_url=https%253A%252F%252Fwww.google.com%252F "CD405xB")

<br>
<br>

### CD4066

Quad Bilateral Single Pole Single Throw Switch

The CD4066 is an integrated circuit containing four identical, independently controlled single-pole, single-throw (SPST) analog switches, suitable for both analog and digital signals.

- Inputs and outputs are interchangeable, similar to conventional mechanical switches.
- Each switch is controlled by a dedicated binary control input.
- On-state resistance (R<sub>ON</sub>) ranges from a few hundred ohms to over one thousand ohms, depending on V<sub>DD</sub>.
- The absolute maximum input current per pin is 10mA.

Control Logic:

- Logic 1 (High) → Switch ON
- Logic 0 (Low) → Switch OFF


*Applications:*
* Signal Gating
* Signal Routing
* Transmission Gate Inverter



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4066_DARK.svg">
  <img alt="Pinout of the CD4066 IC and a schematic symbol representing the digitally controlled CMOS chip, containing four single-pole single-throw switches." src="/Img/CD4066_LIGHT.svg">
</picture>



<!--
The following example shows a single pole double throw (SPDT) configuration built with two bilateral switches of the CD4066 (lower section, SW2 and SW3). SW1 is set up to do logic and acts as an inverter: A high at the control input makes a connection to ground and "pulls" the output node down, while a logical low opens the switch and the pull-up resistor ensures a high at the same node. The non-inverted and the inverted control signals are then connected to the respective control inputs of the remaining switches SW2 and SW3. If one switch is open, the other is closed and vice versa. A common signal will be routed to either one of the outputs. This setup can be used for ping-pong stereo effects. Interchanging the input and output in this SPDT example makes a signal selector. The CD4053 contains already three SPDT switches.
-->

<!--
<img src=/Img/CD4066_Ping-pong_Stereo.jpg>
-->

[CD4066 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4066b.pdf?ts=1608449210166&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4066")

<br>
<br>

### CD4060

14 stage ripple-carry binary counter/divider and oscillator. Q1, Q2, Q3 and Q11 are not connected to the outside of the package. A high level on input pin 12 resets the counter and disables the oscillator.



*Applications:*
* Frequency Divider
* Square Wave Generator




<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4060_DARK.svg">
  <img alt="Pinout of the CD4060 IC (on the left) and a schematic symbol representing the individual gates of the frequency divider (middle section). On the right is a circuit schematic of the RC oscillator circuit built with the CD4060." src="/Img/CD4060_LIGHT.svg">
</picture>


[CD4060 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4060b.pdf "CD4060")

<br>
<br>


### CD4013
 
The CD4013 IC flip-flop is called a D flip-flop type to characterize its behavior, while D stands for "data" or "delay". It contains two identical D flip-flop arrangements. The device stores a digital state 0 or 1, which is accessible at the output **Q**. The second output **/Q** presents the inverse of **Q**. The control input **Clock** transfers the input state **D** to the output **Q** respectively **/Q**. The CD4013 is positive-edge-triggered, which means that the positive-going transition of a clock impulse triggers the device to hold the state that is present at the input and provides it at the output until the next positive-going clock signal. The additional control inputs **Set** and **Reset** have priority over the clock. With a high level on the **Set** input, the output follows its state and goes low with a high level on the **Reset** input, ignoring **D** and **Clock**.



*Applications:*
* Frequency Divider
* Counter
* Toggle Switch


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4013_DARK.svg">
  <img alt="Pinout of the CD4013 IC (on the left) and a schematic symbol representing the individual gates of the CD4013 IC flip-flop (right side)." src="/Img/CD4013_LIGHT.svg">
</picture>


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

<br>
<br>


### CD4018 (under construction)

Divide-By-'N' Counter

By feeding the output stages back into the Data input, the CD4018 can divide a clock signal by 10, 8, 6, 4, or 2. For odd division factors (9, 7, 5, 3), an additional NAND gate (CD4011 or CD4093) can be used. Simply NAND two appropriate output stages and feed the inverted result back into the Data input to achieve the desired division. By cascading multiple CD4018 chips, higher divide-by-N ratios can be implemented for more complex rhythmic patterns or frequency modulation techniques.

Control Functions
- **Preset Enable:** Transfers the data from the Jam input to its corresponding /Q (inverted) output.
- **Reset:** A logical HIGH on the Reset input forces all /Q outputs HIGH, resetting the counter.


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
* Rhythm/Chord Generator



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4018_DARK.svg">
  <img alt="On the left: Pinout of the CD4018 IC. In the middle: a schematic symbol representing the individual gates of the divide-by-'N' counter. On the right: Circuit configuration for building a divide-by-3 counter." src="/Img/CD4018_LIGHT.svg">
</picture>



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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Divide_by_odd_DARK.svg">
  <img alt="Timing diagram of the CD4018 CMOS counter/divider demonstrating odd division ratios (÷3, ÷5, ÷7)." src="/Img/Divide_by_odd_LIGHT.svg">
</picture>

[CD4018 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4018b.pdf?ts=1610571153497&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4018B "CD4018")
<br>
<br>

### 555 Timer

Note: The bipolar version (NE555) and the CMOS version (TLC555, LMC555) have the same pinout and are exchangeable. The CMOS version consumes significantly less power. Its name derives from the three 5kΩ resistors that form a voltage divider network. This IC generates output pulses for precision timing or works as an oscillator with adjustable duty cycle. The timing function can be configured with just a few external components.

*Applications:*
* Frequency Divider
* Timer
* Pulse Delay
* Square Wave Generator
* Pulse Width Modulator

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Timer_DARK.svg">
  <img alt="On the left: Pinout of the 555 timer. On the right: Functional diagram of the internal circuit of the 555 timer." src="/Img/555_Timer_LIGHT.svg">
</picture>


|Pin|Function|
|----|----|
|1|Ground.|
|2|Start of timing input. TRIG < ½ CONT sets output high and discharge open.|
|3|High current timer output signal.|
|4|Active low reset input forces output and discharge low.|
|5|Controls comparator thresholds, Outputs 2/3 VCC, allows bypass capacitor connection.|
|6|End of timing input. THRES > CONT sets output low and discharge low.|
|7|Open collector output to discharge timing capacitor.|
|8|Input supply voltage, 4.5 V to 16 V.|




<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Astable_DARK.svg">
  <img alt="Schematic of the 555 timer IC connected as an astable multivibrator." src="/Img/555_Astable_LIGHT.svg">
</picture>

In the astable configuration or multivibrator mode, the circuit generates a string of pulses by retriggering itself. Different values for $R_A$ and $R_B$ allow for changing the ratio of the high time and the low time. A low at reset pin 4 stops the oscillation.
The time to complete one cycle (high and low) can be calculated with $T=  ln(2) \cdot (R_A + 2R_B)C$ and the frequency with $f=\frac{1}{T}$.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Mono_Timing_DARK.svg">
  <img alt="Schematic of the 555 timer IC for monostable operation including timing diagram." src="/Img/555_Mono_Timing_LIGHT.svg">
</picture>




For mono stable operation, a negative going pulse at the trigger input causes the output to go high for a defined amount of time (one shot). A second pulse within that time period has no effect on the output pulse and will be ignored. This circuit can be used for debouncing switches. The time the output stays high is set through the RC circuit and can be calculated with $T_H = ln(3) \cdot R_1C_1  \approx 1.1 \cdot R_1 C_1$.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Stepped-Tone_Generator_DARK.svg">
  <img alt="Schematic of the 'Stepped-Tone Generator' (also known as Atari Punk Console) by Forrest M. Mims III." src="/Img/Stepped-Tone_Generator_LIGHT.svg">
</picture>

The stepped-tone generator is built using two 555 timer chips. By varying the resistor-capacitor (RC) values, this circuit can produce a wide range of interesting sounds.


| Designator  | Description   | Value   |
| ----------- | ------------- | ------- |
| VR1, VR2    | Potentiometer | 500k    |
| U1, U2      | 555 Timer     |         |
| R1          | Resistor      | 1k      |
| C1          | Capacitor     | 0,01uF  |
| C2          | Capacitor     | 0,1uF   |

[LMC555 Data Sheet](https://www.ti.com/lit/ds/symlink/lmc555.pdf?ts=1609974121158&ref_url=https%253A%252F%252Fwww.google.com%252F "LMC555")  
[TLC555 Data Sheet](https://www.ti.com/lit/ds/symlink/tlc555.pdf "TLC555")
<br>
<br>

<!-- 

this link shows a circuit for an edge triggered monostable multivibrator by Jim Keith  
the duration of the output pulse is independent of the duration of the trigger pulse  
https://www.electroschematics.com/edge-triggered-555-monostable-multivibrator/ 

-->

### LM386 - Power Operational Amplifier (under construction)

Although not part of the CMOS logic family this ubiquitous power op amp is a very versatile component when it comes to amplification or driving small speakers.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/LM386_DARK.svg">
  <img alt="On the left: Pinout of the LM386 - Power Operational Amplifier IC. On the right: Circuit diagram showing the external configuration of the LM386 with a amplification factor of 200" src="/Img/LM386_LIGHT.svg">
</picture>



[LM386 Data Sheet](https://www.ti.com/lit/ds/symlink/lm386.pdf?ts=1613028335418&ref_url=https%253A%252F%252Fwww.google.com%252F "LM386")
<br>
<br>
|Pin|Function|
|----|----|
|1|Gain setting|
|2|Inverting input|
|3|Noninverting input|
|4|Ground reference|
|5|Output|
|6|Power supply voltage|
|7|Bypass decoupling path|
|8|Gain setting pin|

|  |min Voltage|max Voltage|
|----|----|----|
|Supply Voltage|4V|12V|
|Analog input voltage|-0.4V|0.4V|






# Basic Principles and Applications

## Electronic-hydraulic analogy

The electronic-hydraulic analogy compares the flow of electrical current to water moving through pipes. In this model, voltage corresponds to water pressure, while current is analogous to the rate of water flow. Resistance is similar to the narrowing of a pipe, limiting the flow. Capacitors can be thought of as storage tanks or buckets that temporarily hold and release water.

## Mixing

There are various ways of mixing signals together. Using CMOS chips like the XOR CD4070 works for digital signals. If more than two signals should be mixed or merged, several logic gates can be chained together. Even though the resulting signal is not the sum of the source signals but some modulated result, the output signal is still compatible with digital electronics. This is not the case with active and passive mixing, which alters the amplitude of the output. Active mixing involves components, such as operational amplifiers, that need a power supply. Passive mixing works without an additional power supply, but introduces a voltage drop.

### Passive Mixing

Passive mixing is a very simple method that can be accomplished by using resistors for each source. The mixing resistors work as a voltage divider network and lower the amplitude of each signal. Therefore, the passive mixer doesn't give the sum of all input signals but the [average](https://en.wikipedia.org/wiki/Millman%27s_theorem "Millman's theorem"). Small resistance values will drain more current and create distortion. Good values are between 10kΩ - 50kΩ. The advantage of this method is its low part count. To avoid attenuation and interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/passive_mixing_DARK.svg">
  <img alt="On the left: Schematic diagram of a passive mixer with resistors. On the right: The formula to calculate the output voltage according to Millman's theorem." src="/Img/passive_mixing_LIGHT.svg">
</picture>


### Active Mixing

For most audio applications it is desired to control the portion of each input signal in the sum of the output mix. For this, another class of active electronic components can be used, the [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier "op amp") (op amp). The basic wiring is shown below. 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Active_Mixing_DARK.svg">
  <img alt="On the left: Pinout of the LM 358 operational amplifier. On the right: Schematic for a single supply active mixer." src="/Img/Active_Mixing_LIGHT.svg">
</picture>


By adding voltage dividers or potentiometers, it allows for gain control over every individual input. Besides its function as a mixer, it can also be used to achieve the desired output gain by modifying the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inverted. To undo inversion, a second stage following the shown circuit can be used.

$V_{OUT} = - [ \frac{R_F} {R_{IN1}} V_{IN1} + \frac{R_F} {R_{IN2}} V_{IN2} + \frac{R_F} {R_{IN3}} V_{IN3} + etc.]$  
$- V_{OUT} = \frac{R_F} {R_{IN}} [V_{IN1} + V_{IN2} + V_{IN3} + etc.]$ if all $R_{IN}$ are the same.


It should be underlined that the example shown is a single supply based circuit, which is uncommon for audio mixing where usually symmetrical dual supply voltages are used. It is important therefore to create a reference voltage of 1/2 V<sub>CC</sub> at the non-inverting input. When working with logic circuits, the signals are almost at the supply levels. Even with rail-to-rail op amps caution is required to keep the summed signals below the working range of the op amp.




## Passive Filters

Tone control, modifying the frequency spectrum of a signal or creative equalization are very important processes when working with audio. A filter is frequency-selective and passes only a desired range of frequencies, which is called the pass band. Outside of this pass band, frequencies are attenuated or ideally completely reduced. The boundary between pass and stop band is called cutoff frequency. The simplest way to shape an electronic signal is the use of a combination of resistor and capacitor, an RC element. This forms a first order filter. The circuit can be considered as a frequency dependent potential divider. A band-pass filter can be built with two RC elements, as a combination of a high-pass and a low-pass configuration. Since no amplifying components are involved, the amplitude of the output is lower than the input amplitude. When a filter is designed with two passive components, the transition from pass to stop band is rather smooth. For instance, a first order low-pass filter will have a 6dB/octave roll-off with increasing frequency. Unfortunately, the properties of passive filters are not sufficient to achieve a higher steepness or musical effects like resonance, which requires active filter designs. However, the simplicity and the low part count make this method very attractive for subtle tone control.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Passive_Filter_DARK.svg">
  <img alt="On the upper left side: schematic of a passive low-pass filter. On the upper right side: Diagram showing the frequency response of an analog, passive low-pass filter. On the bottom left side: schematic of a passive high-pass filter. On the bottom right side: Diagram showing the frequency response of an analog, passive hight-pass filter" src="/Img/Passive_Filter_LIGHT.svg">
</picture>


## Potentiometers
A potentiometer is a passive, mechanical component enclosed in a housing. It consists of a resistive track and a movable contact called the wiper. The wiper’s position along the resistive track can be adjusted using an actuator.

The three terminals of a potentiometer provide access to:

- The two ends of the resistive element (fixed resistance between them)
- The wiper, which moves along the resistive track to divide the total resistance into two separate resistance values
  
Potentiometer Structure

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Potentiometer_DARK.svg">
  <img alt=" Diagram of a potentiometer and a slider, labeling key components: (a) Housing, (b) Terminals, (c) Actuator, (d) Resistive track, and (e) Wiper." src="/Img/Potentiometer_LIGHT.svg">
</picture>


a) Housing, b) Terminals, c) Actuator, d) Resistive track, e) Wiper


**Potentiometer as a Variable Resistor:**<br>
If only one end terminal and the wiper are used, the potentiometer functions as a variable resistor, where the resistance varies based on the wiper’s position.

**Potentiometer as a Voltage Divider:**<br>
By connecting a voltage source (e.g., supply voltage or signal) to one of the outer terminals and ground (GND) to the other outer terminal, the potentiometer acts as a variable voltage divider. The output voltage can be tapped from the middle (wiper) terminal and adjusted by turning the actuator.

For example, as the wiper moves from one end to the other, the output voltage scales continuously from minimum to maximum—making this configuration ideal for applications such as volume control.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Volume_Control_DARK.svg">
  <img alt=" Simplified schematic illustrating how to use a potentiometer as both a variable resistor (left) and a voltage divider (right)." src="/Img/Volume_Control_LIGHT.svg">
</picture>

Simplified schematic illustrating how to use a potentiometer as both a variable resistor (left) and a voltage divider (right).

<!--
## Touch Circuits

Most approaches for touch-sensitive circuits make use of the resistance or conductivity of the human skin to alter the voltage of one section within a circuit compared to a defined voltage reference. A simple touch switch is based on a NAND logic gate with one of the inputs connected to V<sub>DD</sub> and the other connected in a pull-up configuration via a high value resistor (several MΩ) to V<sub>DD</sub> . A layout for a touch point consists of two conductive areas, electrically separated but close together, where one part is connected to the pulled-up input and the second part is connected to ground. Without touching the conductive area, both logic inputs are high. When a finger is shorting the touch point, the finger's resistance forms a voltage divider together with the pull-up resistor. The resistance of the human skin varies greatly depending on conditions like humidity. Values from several thousands to more than 100kΩ can be assumed. The resulting voltage at the respective input is fairly low and equates a logical 0. In a NAND gate, this condition forces the output to go high, as long as both inputs are different.


<img src="/Img/Resistive_Touch.jpg">



The piezo electric effect describes that a voltage is generated when a mechanical strain is applied to specific crystalline or ceramic materials. They are commercially manufactured as small discs for various shock/impact sensing applications and loudspeakers, since the inverse piezo electric effect is causing the material to vibrate when an electrical audio signal is applied. A comparator can compare the voltage of the piezo with a reference threshold voltage level. If the voltage level generated by the piezo disc exceeds or falls below the reference threshold, the comparator circuit outputs either a high or a low. 

<img src="/Img/Piezo_Trigger_Comparator.jpg">

Most voltage comparators use open-collector output stages. If the inverting input has a higher potential than the non-inverting input, the output transistor is open and together with the pull-up resistor, a dedicated trigger impulse is generated.


For many applications, the rather short voltage spike of a piezo element needs to be transformed into a pulse with a determined on-time period. This can be done with a  mono stable multivibrator. It remains in this state for a time determined by the circuitry, then it flips back to its initial state. In this case, the comparator circuit of the 555 Timer can be used instead of a regular comparator. 



Another approach for sensing a touch or the proximity of human fingers or hands is based on capacitance. In CMOS circuits it can be used for controlling pitch. This method of touch control uses the parasitic capacitance between two conductive areas (electrodes) within a circuit. When a high frequency is applied to the two conductive areas, they create an electric field that stores opposite electric charges and act like plates of a capacitor. The electrodes are placed in parallel to a capacitor that forms an RC network together with a resistor. The RC network in turn defines the time constant of an astable multivibrator. When a finger or stylus is brought in close proximity to the electric field, it changes the capacitance and therefore the frequency of the multivibrator. When the electrodes are touched, the finger or stylus changes the dielectric constant. The dielectric is the material between the electrodes. The alterations of capacitance is linear to the force of the touch. The electrodes should be insulated with conformal coating or a thin adhesive strip.

<img src="/Img/Capacitive_Touch_02_edit.JPG">


The [CD4060](/readme.md#cd4060 "CD4060") has a built-in oscillator configuration that can be used to generate such a high frequency that is applied to, for example, two copper areas. The output is then fed into the binary counter function for frequency division to generate an audio signal. Various forms of electrodes had been tested using thin copper strips using a cutting plotter.

<img src="/Img/Touch-Sensing_Diagram.jpg">

-->
### LDRs (light-dependent resistors)

A photoresistor (also known as a light-dependent resistor, LDR) is a two-terminal electronic component whose resistance varies based on the amount of light hitting it (photoconductivity). The brighter the light, the lower its resistance, and vice versa. This makes it an effective light sensor that can be used to control sound. For example, if you place a photoresistor in the feedback loop of a CMOS oscillator, moving your hand over it to cast a shadow changes its resistance, which in turn alters the oscillator’s frequency (pitch). In this scenario, lower light levels produce a deeper pitch, while brighter light raises the pitch.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/LDR_Examples_DARK.svg">
  <img alt=" Two circuits using an LDR: a voltage divider adjusting output voltage based on light levels (left) and a Schmitt-trigger oscillator where light controls the pitch (right)." src="/Img/LDR_Examples_LIGHT.svg">
</picture>

Two circuits using an LDR: a voltage divider adjusting output voltage based on light levels (left) and a Schmitt-trigger oscillator where light controls the pitch (right).


## Pull-up and Pull-down Resistors


When connecting external circuits or devices to a logic gate, it's important to ensure that the inputs remain in a defined state. Floating inputs (inputs that are left unconnected) can behave unpredictably due to their high impedance, making them highly susceptible to electromagnetic noise. For example, when a normally open push button is in its default position (not pressed), it effectively disconnects the input. In this state, the logic input may pick up random interference, causing the circuit to behave erratically by generating unintended high or low signals. This phenomenon is known as "floating", leading to unreliable circuit operation.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/pull-up_pull-down_DARK.svg">
  <img alt="Schematic of pull-up and pull-down resistors with logic gate inputs. Left: Pull-up configuration. Right: Pull-down configuration." src="/Img/pull-up_pull-down_LIGHT.svg">
</picture>



To prevent unpredictable behavior, a pull-up or pull-down resistor should be connected to either V<sub>CC</sub> (high voltage) or GND (ground). This ensures that the input remains in a defined state even when no active signal is applied, such as when a switch is open. When the switch is closed, the input can still receive a valid signal.
- A connection to V<sub>CC</sub> is called a pull-up resistor, keeping the input high (logic 1) by default.
- A connection to GND is called a pull-down resistor, keeping the input low (logic 0) by default.
- For CMOS logic, typical resistor values range from several kilo-ohms (e.g., 10kΩ – 100kΩ).

Even unused logic gates can cause issues, as they may pick up interference, leading to false triggering or increased power consumption. To ensure stable operation, all unused inputs should be tied to either GND or V<sub>CC</sub> instead of being left floating.

# Exploratory Sound Circuits

This section features a selection of DIY sound circuits that explore the creative possibilities of CMOS chips. They serve as a starting point for hands-on experimentation and modification. These circuits can be combined with the basic circuitry examples above or extended using them, allowing for even more complex and dynamic sound generation

## Linear Feedback Shift Register

A linear feedback shift register (LFSR) can be used for generating deterministic pseudorandomness. In terms of electronic sound production it can be used to build a noise source. An LFSR consists of n numbers of flip-flops which are connected in series to form a shift register as described for the [CD4015](/readme.md#cd4015). This shift register is controlled by a clock that triggers the shift process. Two junctions at a specific position within that chain of flip-flops are directed into an XOR logic gate. The resulting value is fed back into the first register. The number of stages can be extended by connecting multiple devices. The produced values are determined by the shift register's current states and total length. Since the states are finite it will repeat after a certain number of steps. The goal is to choose those taps that form the longest possible sequence of zeros and ones before they repeat. Other implementations of an LFSR exist and work similarly. To activate an LFSR each stage needs to be loaded with an initial value. This is called the seed. By using an XOR function for the feedback, having the value 0 in all flip-flops is forbidden. By using an XNOR function it is forbidden to set all flip-flops to 1. A maximum-length sequence is therefore 2<sup>n</sup> - 1. No matter if XOR or XNOR functions are used, the sequences will have the same length. The duration of one cycle is determined by the clock frequency. When looked at a shift register from the viewpoint of a musician, the long LFSR arrangements will create white and pink noise when controlled with a high frequency (several ten thousands of hertz). Shorter cycles produce grainy tones, stuttering textures or short noise loops.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/basic_LFSR_DARK.svg">
  <img alt="Simplified schematic of an LFSR." src="/Img/basic_LFSR_LIGHT.svg">
</picture>




The Xilinx application note [XAPP210](https://www.xilinx.com/support/documentation/application_notes/xapp210.pdf "Xilinx application note XAPP210") (V1.3) and the Maxim Integrated (now Analog Devices) application note [APP4400](https://pdfserv.maximintegrated.com/en/an/AN4400.pdf "application note APP4400") (Jun 30, 2010) show tables for maximum length sequences, which are presented here for up to 32 bits:

|n|taps from|length| |n|taps from|length| |n|taps from|length|
|:---|:---|---:|-|:---|:---|---:|-|:---|:---|---:|
|3|3,2|7||13|13,4,3,1|8,191||23|23,18|8,388,607|
|4|4,3|15||14|14,5,3,1|16,383||24|24,23,22,17|16,777,215|
|5|5,3|31||15|15,14|32,767||25|25,22|33,554,431|
|6|6,5|63||16|16,15,13,4|65,535||26|26,6,2,1|67,108,863|
|7|7,6|127||17|17,14|131,071||27|27,5,2,1|134,217,727|
|8|8,6,5,4|255||18|18,11|262,143||28|28,25|268,435,455|
|9|9,5|511||19|19,6,2,1|524,287||29|29,27|536,870,911|
|10|10,7|1,023||20|20,17|1,048,575||30|30,6,4,1|1,073,741,823|
|11|11,9|2,047||21|21,19|2,097,151||31|31,28|2,147,483,647|
|12|12,6,4,1|4,095||22|22,21|4,194,303||32|32,22,2,1|4,294,967,295|







Depending on the desired operation, other applicable devices may be CD4094, CD4014, CD4021 which are all 8-stage shift registers.
 

This video displays an excerpt of a maximum sequence length of 2147483647 bits, generated with a 31 bit long shift register and the 28th tap. The clock rate is 5 Hz. 



https://github.com/SCLW/Circuitry-Based-Sound/assets/51890764/fa4ba6e8-b892-4d65-845a-6749760b0387




## Step Sequencer (under construction)

This circuit for a step sequencer is shown in N. Collins book 'Handmade Electronic Music'. It makes use of the built-in voltage controlled oscillator (VCO) of the [CD4046](/readme.md#cd4046 "CD4046") Phase-Locked Loop. The voltage levels of the output pulses of the [CD4022](/readme.md#cd4022 "CD4022") counter can be scaled down by the potentiometer voltage dividers and are mixed together via the [diodes](https://en.wikipedia.org/wiki/Diode "Diode") D1-D8 (1N4148). The CD4046’s voltage controlled oscillator is then generating a frequency according to the input voltage level. Therefore, each step Q0-Q7 of the CD4022 can be used to produce a single tone.



![Step_Sequencer Waveform](/Img/Step_Sequencer_Waveform_DSO.jpg)
*Input voltage (blue graph) and VCO frequency (yellow graph) of the CD4046.*
<br>
<br>




A logical high on the 'Clock Inhibit' of the CD4022 stops the counter advancement and hence the sequence. A manual push button switch with a pull down resistor to GND or a control logic circuit can be used to pause the sequence for rhythmic effects. A logical high on the 'Reset' input restarts the counter. Connecting one of the outputs of the counter to the 'Reset' pin shortens the length of the sequence by one in regard to the number of the used output. (Step length = Qx-1, if Qx is connected to 'Reset'). More complex patterns can be created when the reset and the inhibit functionality is dynamically controlled by logic circuits.

A clock source is needed for triggering the CD4022. When the clock is set to an audio frequency, the step sequencer works as a wave shaper.
Pin 5 (Inhibit) of the CD4046 must be set to a logical low for operation. The frequency range of the CD4046 VCO can be set via the two resistors connected between pin 12 and ground and pin 11 and ground. According to the schematic below, a rough approximation can be calculated with the following formula:

$$
f_{min} =  \dfrac{1} {{R_5}(C_1 + 32 pF)}
$$  

$$
f_{max} =  \dfrac{1} {({R_4}+VR)(C_1 + 32 pF)} + f_{min}
$$  

The output of the VCO can be gated with the clock source through a CMOS switch, e.g. CD4066. 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Step-Sequencer_DARK.svg">
  <img alt="Schematic of a CMOS step sequencer after N. Collins." src="/Img/Step-Sequencer_LIGHT.svg">
</picture>



Bill of Material:  

| Designator  | Description | Value |
| ------------- | ------------- | ------------- |
| D1, D2, ... (for each step)| Diode | 1N4148  |
| VR | Potentiometer $f_{max}$ | 100K |
| VR1, VR2, ... (for each step)| Potentiometer | 100K |
| R1*, R2* | Resistor |1K - 10K |
| R3 | Resistor  | 100K |
| R4 | Resistor $f_{max}$  |10K |
| R5 | Resistor $f_{min}$ | |
| C1 | Capacitor | 100nF |
| SW1, SW2 (optional) |push button or toggle switch| on - off |
| CD4022 | Counter | |
| CD4046 | PLL | |
| Clock |  Clock Generator (eg. CD40106) | |

## Melody Generator


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Melody_Generator_DARK.svg">
  <img alt="Schematic of Slacker's Melody Generator—a CMOS sound generator using a CD4017 counter and a CD4051 multiplexer to produce evolving, semi-random melodic sequences." src="/Img/Melody_Generator_LIGHT.svg">
</picture>

Schematic of Slacker's Melody Generator—a CMOS sound generator using a CD4017 counter (left) and a CD4051 multiplexer (right) to produce evolving, semi-random melodic sequences.

<!--
https://electro-music.com/forum/viewtopic.php?t=27239&postorder=asc&start=50
-->

## Voltage Starve


“Voltage starve” or “voltage sag” can be used as an unconventional modulation technique in experimental music, describing the effect of a low supply voltage and limited current on a circuit’s behavior. In particular, battery-powered guitar pedals can exhibit unique dynamic distortion when the battery’s voltage and current delivery capacity deteriorates over time.

Changing the supply voltage has different effects depending on the circuit topology and component choices. Bypass capacitors help stabilize the power rail, but for instance, the hysteresis thresholds in Schmitt trigger elements vary with supply voltage. Consequently, lowering the supply voltage alters both the frequency and amplitude of Schmitt trigger oscillators.

When using an adjustable power supply or a custom-built circuit, you can explore how limited current and reduced voltage—especially near or below an IC’s minimum requirements—impact performance. A similar effect can be reproduced simply by placing a series resistor in the power rail. Experimenting with potentiometers ranging from 500 Ω to 10 kΩ can yield a variety of unusual modulation effects.


<!-- the content of this sections needs to be edited-->

<!--
# Photos

The artistic range of applications for electronic projects in the fields of experimental sound, interactive music and sound art is quite large. This section gives some impressions of the works made in the context of this seminar.


<br>

![Circuitry-Based Sound Langa 2024](/Img/Workshop_Langa_2024.jpg)
*Workshop preparations at Langa, Cape Town (ZA) 2024*



<br>

![Circuitry-Based Sound !Khwa ttu 2024 2024](/Img/!Khwa_ttu_2024.jpg)
*Hybrid electronic group performance, integrating traditional African instruments at !Khwa ttu (ZA) 2024*

<br>

![Live electronics with DIY synthesizer at ZKM 2024](/Img/Yunfei_ZKM_2024.jpg)
*Live electronics with DIY synthesizer at ZKM 2024 (Photo: Jihye Jang)*

<br>

![Self-built CMOS synthesizer](/Img/Yunfei_Setup_Kinemathek_2022.jpg)
*Self-built CMOS synthesizer at Kinemathek Karlsruhe 2022 (Photo: Jihye Jang)*

<br>
-->

<!--
![Circuitry-Based Sound](/Img/CBS.jpg)
*Photo: Yunfei Zhang*
-->


# Materials

Instructions, parts, tools, shopping lists, components, assemblies, and other materials required to create electronic projects in this field.

## Requirements

Helpful tools and useful materials:

- Worktables.
- Good lighting conditions.
- Small audio mixing desk (for signal routing and monitoring).
- Active loudspeakers (e.g., powered monitor Behringer B205D).
- Pen and paper for drawing schematics.
- Screwdrivers (flathead & Phillips).
- Precision knife (e.g., scalpel).
- Electronic Components & Connections
- Stranded wire (various gauges).
- Crocodile clips.
- Jumper wires (male-to-male).
- Battery clips.
- 9V batteries.
- Laboratory power supply & connectors (preferably 4mm banana laboratory connectors).
- Digital multimeter (DVM).
- Digital storage oscilloscope (DSO).
- Breadboards.
- Temperature-controlled soldering station.
- ESD electronic diagonal cutter.

## Bill of Materials (BoM)

This [BOM](/BOM/Readme.md#bill-of-material "Bill of Material") helps to source necessary components for electronic art projects and self-built instruments.




## Artists

Circuitry-Based Sound are:

Marc Bendt<br>
Bent van den Berg<br>
Fangchao Bi<br>
Zhen Bian<br>
Yinxuan Chen<br>
Hangyan Chen<br>
Siting Chen<br>
Haram Choi<br>
Mark Damian<br>
Thabisa Dinga<br>
Kurt Diedericks<br>
Tobias Ehrhardt<br>
Jung Eun Lee<br>
Damiana Facen<br>
Bi Fangchao<br>
Qianqian Feng<br>
Zufilkar Filandra<br>
Hongyu Guo<br>
Jeongmin Han<br>
Juhee Han<br>
Anna-Lina Helsen<br>
Keita Hori<br>
Jihye Jang<br>
Hoin Ji<br>
Minsu Kim<br>
Florian Knöbl<br>
László Kőrösi<br>
Sangyi Lee<br>
Xingchen Liu<br>
Su Lu<br>
Daniel Lythgoe<br>
Ziyang Ma<br>
Mqhorhana Magqaza<br>
Simphiwe Matole<br>
Jason Mendiola<br>
Victoria Mikhaylova<br>
Lakheni Ntsodo<br>
Jiun-You Ou<br>
Isabella Panigada<br>
Azile Plaatjies<br>
Ukwanda Plaatjies<br>
Pavel Polenz<br>
Max Pospiech<br>
Ruoyi Qiu<br>
Bob Reinert<br>
Vivian Reuter<br>
Arno Schlipf<br>
Dario Schmid<br>
Florian Schwarz<br>
Yifan Su<br>
Anna Szilágyi<br>
Eveline Vervliet<br>
Christina Vinke<br>
Julian Vollmert<br>
Aaron Wagner<br>
Niklas Wallbaum<br>
Dakang Wang<br>
Yudong Wang<br>
Lutz Ben Wesch<br>
Eunchae Won<br>
Le Yang<br>
Sayuki Yoneda <br>
Jiahui Yong<br>
Huiyeon Yun<br>
Rui Zhang<br>
Yunfei Zhang<br>
Xinyi Zhao<br>
Yange Zheng<br>
Pei Zhou<br>




**Lorenz Schwarz** - *lecturer*
<br>
<br>
<br>





## Acknowledgment

Thanks to Dr. Paul Modler, Dizu Plaatjies, Dr. John Richards, Theo Herbst, Dr. Paul Rommelaere, and Holger Förterer.
<br>
<br>
<br>

## Literature

Anderton, Craig. *Electronic Projects for Musicians.* Amsco, 1980.

Barlow, Klarenz. *On Musiquantics.* Bereich Musikinformatik, Musikwissenschaftliches Institut, Johannes Gutenberg-Universität Mainz, 2012.   

Brindley, Keith. *Starting Electronics.* Newnes, 2011.

Collins, Nicolas. *Handmade Electronic Music: The Art of Hardware Hacking.* Taylor & Francis, 2009.

Horowitz, Paul and Winfield Hill. *The art of electronics.* Cambridge University Press, 2021.

Lancaster, Don. *Das CMOS-Kochbuch.* IWT-Verlag, 1980.

Maxfield, Clive. *Bebop to the Boolean Boogie: An Unconventional Guide to Electronics.* Newnes, 2003.

Roads, Curtis. *Computer Music Tutorial.* The MIT Press, 1996.

Self, Douglas. *Small Signal Audio Design.* Focal Press, 2020.

Tate, Timothy, et al. „Hand Turned Synthesis: A One Chip Exploration of CMOS Electronics“. Proceedings of the International Conference on New Interfaces for Musical Expression, Zenodo, 2024, S. 612--621, doi:10.5281/zenodo.13904971.



## Links

Below are links to various online resources related to audio electronics and Synth DIY, as well as inspiring websites from artists and researchers:

**Nicolas Collins** - Sound artist, composer and performer of electronic music.  
https://www.nicolascollins.com  

**John Richards** - British musician and artist. Self-made instruments, installations and sound projects with electronics.  
https://www.dirtyelectronics.org/about.html  

**Handmade Electronic Music** - Hands-on guide to DIY electronic instruments by Nicolas Collins.  
www.HandmadeElectronicMusic.com  

**Klarenz Barlow** -  Pioneer and celebrated composer in the field of computer music and influential teacher.   
http://clarlow.org/texts   

**Eberhard Sengpiel** - Sound engineer, musician, lecturer. Sound studio and audio calculations, audio and acoustics conversions.  
http://www.sengpielaudio.com  

**audiodiwhy** - DIY music technology, programming.  
https://audiodiwhy.blogspot.com  

**Electric Druid** - About audio electronics and analogue synthesizers.  
https://electricdruid.net  

**Synthesizer DIY website of René Schmitz**  
https://www.schmitzbits.de  

**Elliott Sound Products** - Professional results for the Do-It-Yourself enthusiast.  
https://sound-au.com  

**The Institute of Sonology** - Informational website from the Royal Conservatoire in Den Haag about electronics for art and education.  
https://electronics.koncon.nl  

**Adrian Freed** - Former Research Director of UC Berkeley's Center for New Music and Audio Technologies (CNMAT).  
Ideas, projects, examples regarding creative and artistic use of electronics in sound and music.  
http://www.adrianfreed.com  

**diyaudio forum** - DIY audio community forum for learning and sharing knowledge about music technology and audio electronics.  
https://www.diyaudio.com  

**electro-music forum** - Dedicated to experimental electro-acoustic and electronic music.  
https://electro-music.com  

**modwiggler forum** - Source of information about modular synthesizers and DIY analog circuits.  
https://www.modwiggler.com  
<br>
<br>

## License

The content of this documentation is licensed under the [Creative Commons Attribution 3.0 Unported license](https://creativecommons.org/licenses/by/3.0/ "CC BY 3.0"), software is licensed under the MIT License - see the [LICENSE.md](/MIT%20License.md) file for details. Copyright remains with the author(s)
<br>
<br>
<br>

