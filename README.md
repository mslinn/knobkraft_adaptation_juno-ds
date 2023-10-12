# KnobKraft Adaptation For Roland Juno-ds

The KnobKraft Orm is a F/OSS MIDI sysex librarian.
In other words, it is a MIDI patch manager.

This git project is a plugin (an *extension*) for KnobKraft-Orm that provides support for the Roland Juno-DS synthsizer.
It is a work in progress.

See:

- https://github.com/christofmuc/KnobKraft-orm
- https://github.com/christofmuc/KnobKraft-orm/blob/master/adaptations/Adaptation%20Programming%20Guide.md
- https://github.com/christofmuc/KnobKraft-orm/blob/master/adaptations/Adaptation%20Testing%20Guide.md
- https://github.com/christofmuc/KnobKraft-orm/discussions/274


## Testing

The program must be restarted after each change to this Python program.


## Axial Patch Libraries

[Axial / Roland Synthesizer Patch Libraries](https://axial.roland.com/category/juno-ds61_juno-ds76_juno-ds88_xps-30/) provides free `jxl` format patch libraries.

[JUNO-DS_XV_Patch_Collection_Bank_A.jxl](JUNO-DS_XV_Patch_Collection_Bank_A.jxl) is enclosed.

The JUNO-DS Librarian can read `jxl` format files, but cannot convert them to any other format.


## Roland Tone Manager

> [JUNO-DS Tone Manager](https://www.roland.com/global/support/by_product/juno-ds61/owners_manuals/8de9a4d7-443b-4e18-b8f1-004200b366f2/) is an application that lets you use your computer to manage JUNO-DS patches, drum kits, performances, and samples
in a library, and to edit their parameters. Using your computer, you’ll be able to efficiently manage and edit large numbers of tones.

The JUNO-DS Tone Manager manual is provided [here](roland_juno-ds_tone_manager.pdf) in PDF format.
