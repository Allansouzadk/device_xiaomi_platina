#
# Copyright (C) 2020 The LineageOS Project
# Copyright (C) 2020 Paranoid Android
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sdm660-common
include device/xiaomi/sdm660-common/BoardConfigCommon.mk

# Device Path
DEVICE_PATH := device/xiaomi/platina

# Assert
TARGET_OTA_ASSERT_DEVICE := platina

# Hild
DEVICE_MANIFEST_FILE += $(DEVICE_PATH)/manifest.xml

# Kernel
TARGET_KERNEL_SOURCE := kernel/xiaomi/platina
TARGET_KERNEL_CONFIG := platina_defconfig

# Platform
BOARD_VENDOR_PLATFORM := xiaomi-sdm660

# Inherit from the proprietary version
-include vendor/xiaomi/platina/BoardConfigVendor.mk
