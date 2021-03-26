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

# DT2W
TARGET_TAP_TO_WAKE_NODE := "/proc/touchpanel/wake_gesture"

# Assert
TARGET_OTA_ASSERT_DEVICE := platina

# WLAN MAC
WLAN_MAC_SYMLINK := true

# Hild
DEVICE_MANIFEST_FILE += $(DEVICE_PATH)/manifest.xml

# Display
TARGET_SCREEN_DENSITY := 440

# Security patch level
VENDOR_SECURITY_PATCH := 2019-11-01

# Kernel
TARGET_KERNEL_SOURCE := kernel/xiaomi/platina
TARGET_KERNEL_CONFIG := platina_defconfig

# Platform
BOARD_VENDOR_PLATFORM := xiaomi-sdm660

# SELinux
BOARD_VENDOR_SEPOLICY_DIRS += $(DEVICE_PATH)/sepolicy/vendor

# Inherit the proprietary files
include vendor/xiaomi/platina/BoardConfigVendor.mk

