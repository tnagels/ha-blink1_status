"""Blink(1) Status Light integration."""
import logging

from blink1.blink1 import Blink1
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
import homeassistant.util.color as color_util

# Import the device class from the component that you want to support
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_HS_COLOR,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    PLATFORM_SCHEMA,
    LightEntity,
)

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    # Add devices
    b1 = Blink1()
    add_entities([blinkOneLight(b1)])


class blink1(LightEntity):
    """Representation of a BlinkLight Light."""

    def __init__(self, light):
        """Initialize an AwesomeLight."""
        self._light = light
        self._name = "Blink1"
        self._state = None
        self._hs_color = [0, 0]
        self._brightness = 0

    @property
    def brightness(self):
        """Read back the brightness of the light."""
        return self._brightness

    @property
    def supported_features(self):
        """Flag supported features."""
        return SUPPORT_BRIGHTNESS | SUPPORT_COLOR

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def hs_color(self):
        """Return the color of this light."""
        return self._hs_color

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        if ATTR_HS_COLOR in kwargs:
            self._hs_color = kwargs[ATTR_HS_COLOR]
        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
        self._state = True
        rgb_color = color_util.color_hsv_to_RGB(
            self._hs_color[0], self._hs_color[1], self._brightness / 255 * 100
        )
        self._light.fade_to_color(100, rgb_color)

    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        self._state = False
        self._light.fade_to_rgb(100, 0, 0, 0)

    def update(self):
        """There is not data to get as we use an assumed state."""
