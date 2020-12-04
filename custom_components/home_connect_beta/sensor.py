"""Provides a sensor for Home Connect."""

from datetime import timedelta
import logging

from homeassistant.const import DEVICE_CLASS_TIMESTAMP
import homeassistant.util.dt as dt_util

from .const import DOMAIN
from .entity import HomeConnectEntity
from .enum import enum_list

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Home Connect sensor."""

    def get_entities():
        """Get a list of entities."""
        entities = []
        hc_api = hass.data[DOMAIN][config_entry.entry_id]
        for device_dict in hc_api.devices:
            entity_dicts = device_dict.get("entities", {}).get("sensor", [])
            for d in entity_dicts:
                if d['key'] == 'BSH.Common.Option.OperationState':
                    entities += [HomeConnectStatusSensor(**d)]
                else:
                    entities += [HomeConnectSensor(**d)]
        return entities

    async_add_entities(await hass.async_add_executor_job(get_entities), True)


class HomeConnectStatusSensor(HomeConnectEntity):
    """Sensor class for device Status entity in Home Connect."""

    def __init__(self, device, desc, key, unit, icon, device_class, sign=1):
        """Initialize the entity."""
        super().__init__(device, desc)
        self._state = None
        self._key = "BSH.Common.Status.OperationState"
        self._unit = None
        self._icon = "hass:power-plug"
        self._device_class = device_class
        self._sign = sign

    @property
    def state(self):
        """Return true if the sensor is on."""
        return self._state

    @property
    def available(self):
        """Return true if the sensor is available."""
        return self._state is not None

    async def async_update(self):
        """Update the sensor status."""
        status = self.device.appliance.status

        self._state = None
        attributes = {}
        """ DB: Due to specific solution in homeassistant module (HomeConnectAppliance.handle_event, line 251),
                all status keys ever used during current HA session, will be left in self.device.appliance.status
                until session restarts. With this behavior, it is necessary to use this sensor attributes with
                caution, as they may be outdated and/or obsolete.
                I don't see any way to change this behavior without extending the original homeassistant module.
        """

        """ TODO: It's necessary to check for "units" key """
        for k, v in status.items():
            v1 = v.get("value")
            kn = enum_list[k] if enum_list.get(k) else k
            vn = enum_list[v1] if enum_list.get(v1) else v1
            if self._key == k:
                self._state = vn
            else:
                if "unit" in v:
                    attributes[kn] = f"{vn} {v.get('unit')}"
                else:
                    attributes[kn] = vn

        self._attributes = attributes
        _LOGGER.debug("[DB] %s:%s updated, new state: %s", self.device.appliance.name, self._key, self._state)

    @property
    def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        return self._attributes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def icon(self):
        """Return the icon."""
        return self._icon

    @property
    def device_class(self):
        """Return the device class."""
        return self._device_class

class HomeConnectSensor(HomeConnectEntity):
    """Sensor class for Home Connect."""

    def __init__(self, device, desc, key, unit, icon, device_class, sign=1):
        """Initialize the entity."""
        super().__init__(device, desc)
        self._state = None
        self._key = key
        self._unit = unit
        self._icon = icon
        self._device_class = device_class
        self._sign = sign

    @property
    def state(self):
        """Return true if the binary sensor is on."""
        return self._state

    @property
    def available(self):
        """Return true if the sensor is available."""
        return self._state is not None

    async def async_update(self):
        """Update the sensor status."""
        status = self.device.appliance.status
        if self._key not in status:
            self._state = None
        else:
            if self.device_class == DEVICE_CLASS_TIMESTAMP:
                if "value" not in status[self._key]:
                    self._state = None
                elif (
                    self._state is not None
                    and self._sign == 1
                    and dt_util.parse_datetime(self._state) < dt_util.utcnow()
                ):
                    # if the date is supposed to be in the future but we're
                    # already past it, set state to None.
                    self._state = None
                else:
                    seconds = self._sign * float(status[self._key]["value"])
                    self._state = (
                        dt_util.utcnow() + timedelta(seconds=seconds)
                    ).isoformat()
            else:
                self._state = status[self._key].get("value")
        _LOGGER.debug("Updated, new state: %s", self._state)

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def icon(self):
        """Return the icon."""
        return self._icon

    @property
    def device_class(self):
        """Return the device class."""
        return self._device_class
