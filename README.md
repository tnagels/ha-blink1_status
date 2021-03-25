# Blink(1) Integration

This integration sets up and uses a Blink(1) usb status led for use within Home Assistant.


### Installation

Copy this folder to `<config_dir>/custom_components/blink1/` or use HACS to install.

Add the following entry in your `configuration.yaml`:

```yaml
light:
  - platform: blink1_status 
```
