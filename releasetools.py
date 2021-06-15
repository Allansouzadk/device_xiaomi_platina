# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017 The LineageOS Project
# Copyright (c) 2021 The PixelExperience Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import common
import re

def FullOTA_Assertions(info):
  OTA_UpdateFirmware(info)
  return

def IncrementalOTA_Assertions(info):
  OTA_UpdateFirmware(info)
  return

def OTA_UpdateFirmware(info):
  info.script.AppendExtra('ui_print("Flashing MIUI V12.0.3.QDTMIXM firmware...");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hyp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/BTFM.bin", "/dev/block/bootdevice/by-name/bluetooth");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tz");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster64.mbn", "/dev/block/bootdevice/by-name/keymaster");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/logfs_ufs_8mb.bin", "/dev/block/bootdevice/by-name/logfs");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/pmic.elf", "/dev/block/bootdevice/by-name/pmic");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.elf", "/dev/block/bootdevice/by-name/abl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dspso.bin", "/dev/block/bootdevice/by-name/dsp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/storsec.mbn", "/dev/block/bootdevice/by-name/storsec");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xbl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64bak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlibbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hypbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tzbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster64.mbn", "/dev/block/bootdevice/by-name/keymasterbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/pmic.elf", "/dev/block/bootdevice/by-name/pmicbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.elf", "/dev/block/bootdevice/by-name/ablbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfgbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/storsec.mbn", "/dev/block/bootdevice/by-name/storsecbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xblbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpmbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/logo.img", "/dev/block/bootdevice/by-name/logo");')
