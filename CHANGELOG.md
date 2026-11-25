# Changelog

## [v1.5.0.1](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.37/compare/v1.5.0...v1.5.0.1) - 2026-11-25

### What's Changed

### 🚀 Features

- Optimize `rainbow text` rendering to O(N) and streamline `GetTextWidth` @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/120)
- Refactor: Send `new_screen` event only when API is connected @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/119)
- Optimize rainbow text rendering, reduce prognosis buffer size, and clean up string ops @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/118)
- Deduplicate icon drawing, fix bitmap leak on expiration, and clean up warnings @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/117)
- Align trigger template types in `__init__.py` with C++ definitions, align `trigger` templates, fix `icon size` check, and standardize logging @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/116)
- Сlean up remaining `night-mode` loops, unused declarations, and `bitmap_stack` parsing @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/115)
- Replace `std::regex` with lightweight parsing helpers @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/114)
- Consolidate queue filtering and screen helper logic @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/113)
- Pass `std::string` parameters by const reference to avoid unnecessary copies @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/112)
- Extract `find_icon_checked_` helper to deduplicate icon fallback handling @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/111)
- Refactor `draw_day_of_week` and fix Sunday accent alignment on Monday-first week @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/110)
- Optimize and group status log output @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/109)
- Add `color_correct` option to preserve RGB balance during brightness scaling @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/108)
- Common: Add `OTA` page @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/107)
- AAB Light: Implement non-linear brightness curve and fixed hysteresis @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/106)
- AAB Tiny: Implement non-linear brightness curve and fixed hysteresis @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/105)

### 🚋 Pixel Clock aka Tram

- Refactor: Send `new_screen` event only when API is connected @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/119)
- Common: Add `OTA` page @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/107)
- AAB Light: Implement non-linear brightness curve and fixed hysteresis @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/106)
- AAB Tiny: Implement non-linear brightness curve and fixed hysteresis @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/105)

### 🧩 Pixel Clock Component

- Optimize `rainbow text` rendering to O(N) and streamline `GetTextWidth` @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/120)
- Optimize rainbow text rendering, reduce prognosis buffer size, and clean up string ops @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/118)
- Deduplicate icon drawing, fix bitmap leak on expiration, and clean up warnings @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/117)
- Align trigger template types in `__init__.py` with C++ definitions, align `trigger` templates, fix `icon size` check, and standardize logging @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/116)
- Сlean up remaining `night-mode` loops, unused declarations, and `bitmap_stack` parsing @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/115)
- Replace `std::regex` with lightweight parsing helpers @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/114)
- Consolidate queue filtering and screen helper logic @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/113)
- Pass `std::string` parameters by const reference to avoid unnecessary copies @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/112)
- Extract `find_icon_checked_` helper to deduplicate icon fallback handling @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/111)
- Refactor `draw_day_of_week` and fix Sunday accent alignment on Monday-first week @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/110)
- Optimize and group status log output @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/109)
- Add `color_correct` option to preserve RGB balance during brightness scaling @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/108)

#### ⚡ Performance & Memory Optimization

* **Reduced firmware size by ~206.6 KB (15.4%) and static RAM by ~5.0 KB:**
  * **Binary image:** `1,374,691 B` → `1,163,163 B` (`-211,528 B`, Flash usage `74.9%` → `63.4%`, free OTA space `+12%`)
  * **Flash Code (`.text`):** `1,006,244 B` → `812,696 B` (`-193,548 B` / `-19.2%`)
  * **Flash Data (`.rodata`):** `272,804 B` → `255,496 B` (`-17,308 B` / `-6.3%`)
  * **Static DRAM (`.bss` + `.data`):** `58,572 B` → `53,436 B` (`-5,136 B` / `-8.8%`, RAM usage `32.4%` → `29.6%`)


### 🤝 Support

If you like the project, you can support it with a star ⭐ on GitHub.

### ✨ Changelog

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.5.0...v1.5.0.1

## [v1.5.0](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.37/compare/v1.1.5.39...v1.5.0) - 2026-11-19

### 🧩 Component Migration (`ehmtxv2` → `pixel_clock`)

Starting from version **`2026.11.1`**, the core ESPHome custom component has been migrated from the archived `EspHoMaTriXv2` repository into this repository and renamed to **`pixel_clock`**.

#### ⚠️ Breaking Changes & Migration Steps

- **External Component:** Update `external_components` in your YAML to point to `andrewjswan/pixel-clock` with `components: [pixel_clock]`.
- **YAML Configuration:** Rename the top-level `ehmtxv2:` key to `pixel_clock:`.
- **Home Assistant Services:** Default service prefixes changed from `esphome.ulanzi_*` / `esphome.ehmtxv2_*` to `esphome.pixel_clock_*`.

### What's Changed

### ❗️ Breaking Changes

- Migrate from `ehmtxv2` to `pixel-clock` component @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/102)

### 🚀 Features

- Migrate from `ehmtxv2` to `pixel-clock` component @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/102)

### 🧰 Maintenance

- Migrate from `ehmtxv2` to `pixel-clock` component @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/102)
- Add `mkdocs-git-revision-date-localized-plugin` @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/101)
- Add `MODE_ICON_SCREEN` @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/100)
- Add `MODE_ICON_CLOCK` @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/99)
- ESP: Bump actions/setup-python from 6 to 7 @[dependabot[bot]](https://github.com/apps/dependabot) (https://github.com/andrewjswan/pixel-clock/pull/98)

### 🤝 Support

If you like the project, you can support it with a star ⭐ on GitHub.

### ✨ Changelog

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.39...v1.5.0

## [v1.1.5.39](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.37/compare/v1.1.5.37...v1.1.5.39) - 2026-07-17

### What's Changed

### 🐛 Bug Fixes

- 2026.7.1: Compatibility with ESPHome 2026.7.0 @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/96)

### 🧰 Maintenance

- 2026.7.1: Compatibility with ESPHome 2026.7.0 @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/96)
- ESP: Bump actions/checkout from 6 to 7 @[dependabot[bot]](https://github.com/apps/dependabot) (https://github.com/andrewjswan/pixel-clock/pull/95)
- Add `Changelog` to Doc @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/94)
- ESP: Bump strumwolf/delete-deployment-environment from 3 to 4 @[dependabot[bot]](https://github.com/apps/dependabot) (https://github.com/andrewjswan/pixel-clock/pull/93)

### 🤝 Support

If you like the project, you can support it with a star ⭐ on GitHub.

### ✨ Changelog

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.37...v1.1.5.39

## [v1.1.5.37](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.37) - 2026-05-07

### What's Changed

* ESPHome **2026.4.5**
* Add `bitmap_converter` to Doc by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/83)
* Add `bitmap-editor` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/84)
* Migrate `bitmap-editor` to JS by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/85)
* Add `16x16` mode to `Bitmap editor` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/86)
* Add `bitmap-array` to `Converter` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/87)
* Add `BITMAP_SCREEN` to Doc by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/88)
* Fix `bitmap-editor` for mobile by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/89)
* Fix `temperature_hot_down` icon by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/90)
* Add `icons` to docs by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/91)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.35...v1.1.5.37

## [v1.1.5.35](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.35) - 2026-04-28

### What's Changed

* ESPHome **2026.4.3**
* 2026.4.1: Version bump by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/79)
* Add Icons to Doc by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/80)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.33...v1.1.5.35

## [v1.1.5.33](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.33) - 2026-04-21

### What's Changed

* ESPHome **2026.4.1**
* Bump `EHMTX` to `2026.4.0` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/75)
* ESP: Bump actions/upload-pages-artifact from 4 to 5 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/77)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.31...v1.1.5.33

## [v1.1.5.31](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.31) - 2026-04-17

### What's Changed

* ESPHome **2026.4.0**
* ESP: Bump actions/configure-pages from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/71)
* ESP: Bump actions/deploy-pages from 4 to 5 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/70)
* Add `Social` background by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/72)
* ESP: Bump softprops/action-gh-release from 2 to 3 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/73)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.29...v1.1.5.31

## [v1.1.5.29](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.29) - 2026-03-25

### What's Changed

* Add `social` cards to documentation by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/63)
* Switch `esp32` from `board` to `variant` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/66)
* Bump `EHMTX` to `2026.3.0` by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/68)

### Dependencies

* ESP: Bump actions/upload-artifact from 6 to 7 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/65)
* ESP: Bump actions/download-artifact from 7 to 8 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/64)
* ESP: Bump geekyeggo/delete-artifact from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/67)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.27...v1.1.5.29

## [v1.1.5.27](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.27) - 2026-02-20

### What's Changed

* Update EspHoMaTriX to 2025.12.0 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/53)
* Add TZ example by @trip5 (https://github.com/andrewjswan/pixel-clock/pull/57)
* Add permition to Validate action by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/58)
* Comment `id(my_time)->call_setup();` look like not needed by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/59)
* Rework `ESPHome Version` sensor by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/60)
* Rework `firmware` page by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/61)
* ESP: Bump actions/checkout from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/52)
* ESP: Bump actions/download-artifact from 6 to 7 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/55)
* ESP: Bump actions/upload-artifact from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/54)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.25...v1.1.5.27

## [v1.1.5.25](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.25) - 2025-11-13

### What's Changed

* ESP: Bump actions/download-artifact from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/47)
* ESP: Bump actions/upload-artifact from 4 to 5 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/48)
* expose Display as light and make AAB bounds configurable by @nschimme (https://github.com/andrewjswan/pixel-clock/pull/50)

### New Contributors

* @nschimme made their first contribution in https://github.com/andrewjswan/pixel-clock/pull/50

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.23...v1.1.5.25

## [v1.1.5.23](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.23) - 2025-10-15

### What's Changed

* Switch to ESPHoMatrix 2025.10.1 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/44)
* Switch to ESPHoMatrix 2025.10.3 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/45)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.21...v1.1.5.23

## [v1.1.5.21](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.21) - 2025-09-18

### What's Changed

* Documentation: Add HA TZ Tip by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/40)
* Add esp-idf package and test by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/41)

### In Pre-Release

* 2025.9: Remove TZ package from configuration by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/38)
* ESP: Bump actions/setup-python from 5 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/37)

### Breaking changes

* Configuration changed, changes in packages.

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.19...v1.1.5.21

## [v1.1.5.17](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.17) - 2025-09-06

### What's Changed

* Documentation: Big update by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/28)
* Failed to download manifest fix by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/30)
* Adoption dashboard broken fix by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/33)

Thanks @nschimme

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.15...v1.1.5.17

## [v1.1.5.15](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.15) - 2025-08-29

### What's Changed

* ESP: Bump actions/download-artifact from 4 to 5 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/16)
* ESP: Bump actions/checkout from 4 to 5 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/17)
* ESP: Bump actions/upload-pages-artifact from 3 to 4 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/18)
* Documentation by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/19)
* Updated EspHoMaTriX: 2025.8.1 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/25)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.13...v1.1.5.15

## [v1.1.5.13](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.13) - 2025-08-10

### What's Changed

* Flip local font to trip5 Matrix-Fonts repo by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/12)
* Fix for Boot-Loop issue when WiFi is not connected when calling set timezone by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/14)
* Updated EspHoMaTriX: 2025.7.1

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.11...v1.1.5.13

## [v1.1.5.11](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.11) - 2025-07-18

### What's Changed

* EspHoMaTriX: 2025.7.1 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/10)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.9...v1.1.5.11

## [v1.1.5.9](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.9) - 2025-07-12

### What's Changed

* Update pixel_clock.yaml add pullup to left and right button by @d4g (https://github.com/andrewjswan/pixel-clock/pull/8)

### New Contributors

* @d4g made their first contribution in https://github.com/andrewjswan/pixel-clock/pull/8

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.7...v1.1.5.9

## [v1.1.5.7](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.7) - 2025-07-01

### What's Changed

* Switch to EspHoMaTriX 2025.6.3 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/5)

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.5...v1.1.5.7

## [v1.1.5.5](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.5) - 2025-06-15

### What's Changed

* Switch to EspHoMaTriX 2025.5.3 by @andrewjswan
* ESP: Bump esphome/build-action from 6 to 7 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/3)
* Switch to EspHoMaTriX 2025.6.1 by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/4)

### Changelog

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5.1..v1.1.5.5

## [v1.1.5.1](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5.1) - 2025-02-20

### What's Changed

* ESP: Bump esphome/build-action from 4 to 6 by @dependabot (https://github.com/andrewjswan/pixel-clock/pull/2)

### New Contributors

* @dependabot made their first contribution in https://github.com/andrewjswan/pixel-clock/pull/2

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/compare/v1.1.5...v1.1.5.1

## [v1.1.5](https://github.com/andrewjswan/pixel-clock/releases/tag/v1.1.5) - 2024-12-20

### What's Changed

* Add TimeZone support by @andrewjswan (https://github.com/andrewjswan/pixel-clock/pull/1)

### New Contributors

* @andrewjswan made their first contribution in https://github.com/andrewjswan/pixel-clock/pull/1

**Full Changelog**: https://github.com/andrewjswan/pixel-clock/commits/v1.1.5
