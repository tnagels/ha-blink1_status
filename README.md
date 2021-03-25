# Blink(1) Integration

This integration sets up and uses a Blink(1) usb status led for use within Home Assistant.


### Installation

Copy this folder to `<config_dir>/custom_components/blink1/`.


Add the following entry in your `configuration.yaml`:

```yaml
light:
  - platform: blink1_status 
```

### Remarks
- Use at your own risk. This is far from complete, but for me it works.
- No HACS install because I could not get it to work right away and don't want to invest time in it.
- Feel free to do anything with the code, for my work there is no license attached.
