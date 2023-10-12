#
#   Copyright (c) 2022-2023 Christof Ruch. All rights reserved.
#
#   Dual licensed: Distributed under Affero GPL license by default, an MIT license is available for purchase
#

# See https://github.com/christofmuc/KnobKraft-orm/discussions/274

import sys
from typing import List

import testing.test_data
from roland import DataBlock, RolandData, GenericRoland

this_module = sys.modules[__name__]

_juno_ds_patch_data = [DataBlock((0x00, 0x00, 0x00, 0x00), 0x50, "Patch common"),
                      DataBlock((0x00, 0x00, 0x02, 0x00), (0x01, 0x11), "Patch common MFX"),
                      DataBlock((0x00, 0x00, 0x04, 0x00), 0x54, "Patch common Chorus"),
                      DataBlock((0x00, 0x00, 0x06, 0x00), 0x53, "Patch common Reverb"),
                      DataBlock((0x00, 0x00, 0x10, 0x00), 0x29, "Patch common Tone Mix Table"),
                      DataBlock((0x00, 0x00, 0x20, 0x00), (0x01, 0x1a), "Tone 1"),
                      DataBlock((0x00, 0x00, 0x22, 0x00), (0x01, 0x1a), "Tone 2"),
                      DataBlock((0x00, 0x00, 0x24, 0x00), (0x01, 0x1a), "Tone 3"),
                      DataBlock((0x00, 0x00, 0x26, 0x00), (0x01, 0x1a), "Tone 4")]
_juno_ds_edit_buffer_addresses = RolandData("Juno-DS Temporary Patch/Drum (patch mode part 1)", 1, 4, 4,
                                           (0x1f, 0x00, 0x00, 0x00),
                                           _juno_ds_patch_data)

'''There is an address calculation problem with the Juno-DS having 256 patches.
Temporarily limit the number of patches to 128 in line 29.
256 is correct, but it seems the address calculation does not handle the address overflow correctly.
We calculate invalid sysex messages which cause the download to stall.

See https://github.com/christofmuc/KnobKraft-orm/discussions/274#discussioncomment-7263645 '''
_juno_ds_program_buffer_addresses = RolandData("Juno-DS User Patches", 128, 4, 4,
                                              (0x30, 0x00, 0x00, 0x00),
                                              _juno_ds_patch_data)

juno_ds = GenericRoland("Roland Juno-DS",
                        model_id=[0x00, 0x00, 0x3a],
                        address_size=4,
                        edit_buffer=_juno_ds_edit_buffer_addresses,
                        program_dump=_juno_ds_program_buffer_addresses,
                        category_index=0x0c,
                        device_family=[0x3a, 0x02, 0x02])
juno_ds.install(this_module)


# Test data picked up by test_adaptation.py
def make_test_data():
    def programs(data: testing.TestData) -> List[testing.ProgramTestData]:
        patch = []
        names = ["RedPowerBass", "Sinus QSB", "Super W Bass"]
        i = 0
        # Extract the first 3 programs from the sysex dump loaded, and yield them with name and number to the test code
        for message in data.all_messages:
            if juno_ds.isPartOfSingleProgramDump(message):
                patch.extend(message)
                if juno_ds.isSingleProgramDump(patch):
                    yield testing.ProgramTestData(message=patch, name=names[i], number=i)
                    patch = []
                    i += 1
                    if i >= len(names):
                        break

    return testing.TestData(sysex="testData/jv1080_AGSOUND1.SYX",
                            program_generator=programs,
                            program_dump_request="f0 41 10 00 10 11 30 00 00 00 00 00 00 4f 01 f7",
                            device_detect_call="f0 7e 00 06 01 f7",
                            device_detect_reply=("f0 7e 10 06 02 41 10 01 00 00 00 00 00 00 f7", 0))
