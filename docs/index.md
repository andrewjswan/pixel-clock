# ESPHome Pixel Clock aka TRAM
[![esphome_badge](https://img.shields.io/badge/ESPHome-Based-blue.svg)](https://esphome.io/)
[![pixel-clock_badge](https://img.shields.io/badge/Pixel-Clock-orange.svg)](https://github.com/andrewjswan/pixel-clock/)
[![esp32_arduino](https://img.shields.io/badge/ESP32-Arduino-darkcyan.svg)](https://esphome.io/)
[![Build](https://github.com/andrewjswan/pixel-clock/actions/workflows/build.yaml/badge.svg)](https://github.com/andrewjswan/pixel-clock/actions/workflows/build.yaml)
[![GitHub](https://img.shields.io/github/license/andrewjswan/pixel-clock?color=blue)](https://github.com/andrewjswan/pixel-clock/blob/main/LICENSE)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/andrewjswan/pixel-clock?include_prereleases)](https://github.com/andrewjswan/pixel-clock/releases)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/downloads-pre/andrewjswan/pixel-clock/latest/total?label=release@downloads)](https://github.com/andrewjswan/pixel-clock/releases)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

## Description

**Pixel Clock** provides a complete ESPHome-based solution for **Ulanzi TC001** and custom `8×32` RGB LED matrix displays:

- **Core Component (`pixel-clock`):** The underlying [ESPHome Custom component](pixel-clock.md) that powers the display. It is the actively maintained successor to [**EspHoMaTriXv2**](https://github.com/lubeda/EspHoMaTriXv2), originally created by [@lubeda](https://github.com/lubeda). Following the official end of development of the original project at version `2026.9.1`, this repository continues its maintenance, bug fixes, and compatibility updates for modern ESPHome releases.
- **Ready-to-Use Configurations:** Modular YAML configurations tailored specifically for the **Ulanzi TC001** hardware.
- **Pre-built Firmware:** Ready-to-flash binaries for quick installation via Web browser or [**ESPHome**](https://esphome.io/).

![Ulanzi TC001](img/ulanzi-tc001.png)

## Firmware
You can install the firmware using [ESPHome](https://esphome.io/) using one of the ready-made configuration files or use [**PixelClock - ESP Web Tools**](firmware.md) - a convenient tool for installing and updating the firmware of ESP32 devices in the browser.
