## Time Zones

!!! example "Time Zones"

    ``` { .yaml .copy }
    substitutions:
    ...
      time_zone: AST4ADT,M3.2.0,M11.1.0

    esphome:
    ...
      on_boot:
        - priority: -100
          then:
            - script.execute: set_timezone

    time:
      - platform: sntp
        id: my_time
        timezone: "${time_zone}"
        update_interval: 8h
        on_time_sync:
          then:
            - ds1307.write_time:
      - platform: ds1307
        update_interval: never
        id: ehmtx_time

    text:
      - platform: template
        name: "Time Zone POSIX"
        id: timezone_text
        optimistic: true
        min_length: 0
        max_length: 45
        mode: text
        restore_value: true
        initial_value: "${time_zone}"
        icon: mdi:airplane-time
        entity_category: config
        disabled_by_default: true
        on_value:
          then:
            - script.execute: set_timezone

    script:
      - id: set_timezone
        mode: restart
        then:
          - wait_until:
              condition: wifi.connected
          - lambda: |-
              if (id(timezone_text).state != "" && id(timezone_text).state.c_str() != "${time_zone}") {
                id(my_time)->set_timezone(id(timezone_text).state.c_str());
                id(ehmtx_time)->set_timezone(id(timezone_text).state.c_str());
                // id(my_time)->call_setup();
                ESP_LOGI("main", "Alt Time Zone Set");
              } else {
                id(my_time)->set_timezone("${time_zone}");
                id(ehmtx_time)->set_timezone("${time_zone}");
                // id(my_time)->call_setup();
                ESP_LOGI("main", "Default Time Zone");
                id(timezone_text).state="${time_zone}";
              }

    preferences:
      flash_write_interval: 15s # 0 does immediate write to memory with no mem buffer (not recommended) (only saves when persistent variables have changed)
    ```

!!! note
    The first `set_timezone` changes the ESP's time, the second changes the RTC's time. The `call_setup` calls internal code to restart the time module (which will also trigger a sync).

!!! note
    Thanks @trip5 https://github.com/andrewjswan/pixel-clock/issues/56
