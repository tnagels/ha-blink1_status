# Blink(1) Integration

This integration sets up and uses a Blink(1) usb status led for use within Home Assistant.


### Installation

Copy this folder to `<config_dir>/custom_components/blink1/`. Thanks to the work of Qu3uk you can now also add this repo to HACS for easy installation.


Add the following entry in your `configuration.yaml`:

```yaml
light:
  - platform: blink1_status 
```

### Remarks
- Use at your own risk. This is far from complete, but for me it works.
- Feel free to do anything with the code, for my work there is no license attached.
