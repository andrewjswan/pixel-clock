## Integration in Home Assistant

To control your display, it has to be integrated in Home Assistant. Then it provides several services, all prefixed with the configured `devicename` e.g. `pixel_clock`.

### Services

All communication with Home Assistant use the homeasistant-api. The services can be provided by default or also defined additionally in the YAML. To define the additional services, you need the ID of the ehmtx-component e.g. `id(rgb8x32)`.

### Use in Home Assistant automations

#### Icon names as trigger ID

The easiest way to use Pixel Clock as a status display is to use the icon names as trigger ID. In my example, I have an icon named `wind` when the `sensor.wind_speed` has a new state, this automation sends the new data to the screen with the icon named `wind` and so on.

!!! example "Icon names as trigger ID"

    ``` yaml
    alias: EHMTX Pixel Clock 
    trigger:
      - platform: numeric_state
        entity_id: sensor.wind_speed
        id: wind
      - platform: state
        entity_id: sensor.outside_temperature
        id: temp
      - platform: state
        entity_id: sensor.cover_device
        id: cover
    action:
      - service: esphome.pixel_clock_icon_screen
        data:
          icon_name: '{{trigger.id}}'
          text: >-
            {{trigger.to_state.state}}{{trigger.to_state.attributes.unit_of_measurement}}
    mode: queued
    max: 10
    ```

#### Specific icons per state

Sample automation to show the weather with local temperature

!!! example "Weather with icon per condition"

    ``` yaml
    alias: EHMTX Pixel Clock Weather
    trigger:
      - platform: state
        entity_id: weather.current
    action:
      - service: esphome.pixel_clock_del_screen
        data:
          icon_name: weather_*
          mode: 5
      - service: esphome.pixel_clock_icon_screen
        data:
          icon_name: weather_{{ trigger.to_state.state }}
          text: >-
            {{ states("sensor.outside_temperature") }}°C
    ```

Sample automation for the trashcan type

!!! example "Trashcan type"

    ``` yaml
    alias: "EHMTX Müllanzeige"
    description: Anzeige welche Tonne raus muss. iconnamen gekürzt
    trigger:
      - platform: time
        at:
          - "06:30"
          - "08:30"
          - "10:30"
          - "15:00"
          - "17:00"
          - "19:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.mulltrigger
        below: "3"
    action:
      - service: esphome.ulanzi_del_screen
        data:
          icon_name: trash_*
          mode: 5
      - service: esphome.ulanzi_icon_screen
        data:
          icon_name: >-
            trash_{{ states("sensor.mulldetails") | replace("Biotonne",   "brow")|
            replace("Papiertonne","blue")| replace("Restmüll",   "grey")|
            replace("gelbe Tonne","yell|") | truncate(4,true,"")  }}     
          text: >-
            {{ states("sensor.mulldetails") }}
          lifetime: 120
    ```

#### Tips

!!! tip "Display sensor precision after Home Assistant 2023.3"

    See [templating](https://www.home-assistant.io/docs/configuration/templating/#states) for possibilities to optimize the output e.g. `{{ states(sensor.solarpower, rounded=True) }} kWh`
