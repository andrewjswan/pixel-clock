<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="../js/installer.js"></script>

<style>
  .md-typeset h1 {
    display: none;
  }
</style>

[![Made for ESPHome](img/made-for-esphome.svg){ align=right loading=lazy style="width:30%" }](https://esphome.io/guides/made_for_esphome.html)

!!! info "ESP Web Tools"
    User friendly tools to manage `ESP8266` and `ESP32` devices in the browser:

    * Install &amp; update firmware.
    * Connect device to the `Wi-Fi` network.
    * Visit the device's hosted `web interface`.
    * Access logs and send terminal commands.
    * Add devices to [Home Assistant](https://www.home-assistant.io).

## Install PixelClock (TRAM) <b><span id="version"></span></b>

<div class="esp-installer-page">
<div class="radios">
  <label>
    <input
      type="radio"
      name="pixel-clock-device"
      class="device"
      id=""
      value="pixel-clock"
      checked
    />
    <img src="../img/ulanzi-ua.png" alt="Ulanzi TC001" />
    <span></span>
  </label>
  <label>
    <input
      type="radio"
      name="pixel-clock-device"
      class="device"
      id="en"
      value="pixel-clock"
    />
    <img src="../img/ulanzi-en.png" alt="Ulanzi TC001 (EN)" />
    <span></span>
  </label>
  <label>
    <input
      type="radio"
      name="pixel-clock-device"
      class="device"
      id="ru"
      value="pixel-clock"
    />
    <img src="../img/ulanzi-ru.png" alt="Ulanzi TC001 (RU)" />
    <span></span>
  </label>
</div>

<div class="button-row">
  <esp-web-install-button manifest="../pixel-clock-manifest.json"></esp-web-install-button>
</div>

</div>

---

[PixelClock](https://github.com/andrewjswan/pixel-clock) — Installer powered by [ESP Web Tools](https://esphome.github.io/esp-web-tools/).
