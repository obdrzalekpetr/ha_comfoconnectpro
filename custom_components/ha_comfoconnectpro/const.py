"""Constants for the integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, Any

import sys

from homeassistant.components.climate import (
    ClimateEntityDescription,
    ClimateEntityFeature,
)
from homeassistant.components.sensor import *
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.components.number import (
    NumberEntity,
    NumberEntityDescription,
    NumberDeviceClass,
)
from homeassistant.const import (
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfEnergy,
    UnitOfPower,
    CONF_NAME,
    Platform,
)

from pymodbus.client import ModbusTcpClient

import logging

thismodule = sys.modules[__name__]
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
_LOGGER.info(f"{thismodule}.const loaded")



DOMAIN = "ha_comfoconnectpro"
DEFAULT_NAME = "ComfoConnect PRO"
DEFAULT_SCAN_INTERVAL = 15
DEFAULT_PORT = 502
DEFAULT_HOSTID = 1
CONF_HOSTID = "hostid"
CONF_HUB = "hacomfoconnectpro_hub"
ATTR_MANUFACTURER = "Zehnder"



# ------------------------------------------------------------
# 1) Error constants (C_<NAME> = "<error_num>")
#    >> These constants serve as keys in the ERROR_DICT.
# ------------------------------------------------------------
C_NO_ERR = 0
C_HRU_T_FIRE_ERR = 21
C_T_HRU_ERR = 22
C_T_11_ERR = 23
C_T_11_LIMIT_ERR = 24
C_T_12_ERR = 25
C_T_12_LIMIT_ERR = 26
C_T_20_ERR = 27
C_T_20_LIMIT_ERR = 28
C_T_21_ERR = 29
C_T_21_LIMIT_ERR = 30
C_T_22_ERR = 31
C_T_22_LIMIT_ERR = 32
C_HRU_INIT_ERR = 33
C_HRU_FRONT_OPEN_ERR = 34
C_H_21_RELEASE_ERR = 35
C_H_21_P_ERR = 37
C_H_21_P_RATIO_ERR = 38
C_PHI_11_ERR = 39
C_PHI_12_ERR = 41
C_PHI_20_ERR = 43
C_PHI_21_ERR = 45
C_PHI_22_ERR = 47
C_P_12_ERR = 49
C_P_22_ERR = 50
C_F_12_S_ERR = 51
C_F_22_S_ERR = 52
C_PTOT_12_S_ERR = 53
C_PTOT_22_S_ERR = 54
C_F_12_S_SET_ERR = 55
C_F_22_S_SET_ERR = 56
C_QM_12_SET_ERR = 57
C_QM_22_SET_ERR = 58
C_T_21_SET_ERR = 59
C_T_22_SET_ERR = 60
C_T_22_FROST_ERR = 61
C_UNBALANCE_ERR = 62
C_PRESENT_RF_ERR = 66
C_PRESENT_IO_ERR = 67
C_PRESENT_H_21_ERR = 68
C_PRESENT_H_23_ERR = 69
C_PRESENT_HOOD_ERR = 74
C_PRESENT_CCOOL_ERR = 75
C_PRESENT_G_ERR = 76
C_FILTER_ALARM_FLAG = 77
C_FILTER_EXT_ERR = 78
C_FILTER_WARNING_FLAG = 79
C_STANDBY_ERR = 80
C_H_21_COMM_ERR = 81
C_T_22_MANUAL_ERR = 89
C_CC_OVERHEAT_ERR = 90
C_CC_COMP_ERR = 91
C_CC_T_10_ERR = 92
C_CC_T_13_ERR = 93
C_CC_T_23_ERR = 94
C_T_HOOD_ERR = 95
C_IO_HOOD_DUTY_ERR = 96
C_QM_CONSTRAINT_MIN_ERR = 97
C_H_21_QM_MIN_ERR = 98
C_CONFIG_ERR = 99
C_ANALYSIS_BUSY_WARNING = 100
C_COMFONET_ERR = 101
C_CO2_SENS_COUNT_ERR = 102
C_CO2_SENS_TOO_MANY_ERR = 103
C_CO2_SENS_GENERAL_ERR = 104

# Dictionary with descriptions
ERROR_DICT: Dict[str, Any] = {
    C_NO_ERR: "Normal operation",
    C_HRU_T_FIRE_ERR: "Two or more temperature sensors are out of bounds",
    C_T_HRU_ERR: "Temperature too high for HRU",
    C_T_11_ERR: "Value of temperature sensor T11 has exceeded the limit too often",
    C_T_11_LIMIT_ERR: "Value of temperature sensor T11 is exceeding the limit",
    C_T_12_ERR: "Value of temperature sensor T12 has exceeded the limit too often",
    C_T_12_LIMIT_ERR: "Value of temperature sensor T12 is exceeding the limit",
    C_T_20_ERR: "Value of temperature sensor T20 has exceeded the limit too often",
    C_T_20_LIMIT_ERR: "Value of temperature sensor T20 is exceeding the limit",
    C_T_21_ERR: "Value of temperature sensor T21 has exceeded the limit too often",
    C_T_21_LIMIT_ERR: "Value of temperature sensor T21 is exceeding the limit",
    C_T_22_ERR: "Value of temperature sensor T22 has exceeded the limit too often",
    C_T_22_LIMIT_ERR: "Value of temperature sensor T22 is exceeding the limit",
    C_HRU_INIT_ERR: "HRU has not been initialized",
    C_HRU_FRONT_OPEN_ERR: "The front door is open",
    C_H_21_RELEASE_ERR: "Preheater is present, but its position (left/right) does not match the HRU orientation",
    C_H_21_P_ERR: "Preheater is not delivering the required power",
    C_H_21_P_RATIO_ERR: "Preheater is not delivering the required power in the required ratio",
    C_PHI_11_ERR: "Value of humidity sensor ϕ11 has exceeded the limit too often",
    C_PHI_12_ERR: "Value of humidity sensor ϕ12 has exceeded the limit too often",
    C_PHI_20_ERR: "Value of humidity sensor ϕ20 has exceeded the limit too often",
    C_PHI_21_ERR: "Value of humidity sensor ϕ21 has exceeded the limit too often",
    C_PHI_22_ERR: "Value of humidity sensor ϕ22 has exceeded the limit too often",
    C_P_12_ERR: "Value of pressure sensor P12 has exceeded the limit too often",
    C_P_22_ERR: "Value of pressure sensor P22 has exceeded the limit too often",
    C_F_12_S_ERR: "Speed of F12 fan has exceeded the limit too often",
    C_F_22_S_ERR: "Speed of F22 fan has exceeded the limit too often",
    C_PTOT_12_S_ERR: "Static pressure of sensor P12 has exceeded the limit too often",
    C_PTOT_22_S_ERR: "Static pressure of sensor P22 has exceeded the limit too often",
    C_F_12_S_SET_ERR: "Required F12 fan speed was not reached too often",
    C_F_22_S_SET_ERR: "Required F22 fan speed was not reached too often",
    C_QM_12_SET_ERR: "Required mass flow for F12 fan was not reached too often",
    C_QM_22_SET_ERR: "Required mass flow for F22 fan was not reached too often",
    C_T_21_SET_ERR: "Required temperature for the outdoor air after the preheater was not reached too often",
    C_T_22_SET_ERR: "Required temperature for the supply air was not reached too often",
    C_T_22_FROST_ERR: "Supply air temperature (sensor T22) is too low too often",
    C_UNBALANCE_ERR: "Imbalance was outside the tolerance values too often in the past period",
    C_PRESENT_RF_ERR: "RF communication hardware was present but is no longer detected",
    C_PRESENT_IO_ERR: "Option board was present but is no longer detected",
    C_PRESENT_H_21_ERR: "Preheater was present but is no longer detected",
    C_PRESENT_H_23_ERR: "Reheater was present but is no longer detected",
    C_PRESENT_HOOD_ERR: "Extractor hood was present but is no longer detected",
    C_PRESENT_CCOOL_ERR: "Comfo Cool was present but is no longer detected",
    C_PRESENT_G_ERR: "ComfoFond was present but is no longer detected",
    C_FILTER_ALARM_FLAG: "Filters must be replaced now",
    C_FILTER_EXT_ERR: "The external filter input is high",
    C_FILTER_WARNING_FLAG: "The filters must be ordered now as the remaining filter life is limited",
    C_STANDBY_ERR: "Standby is active",
    C_H_21_COMM_ERR: "Preheater is not communicating reliably",
    C_T_22_MANUAL_ERR: "Bypass is being used manually.",
    C_CC_OVERHEAT_ERR: "ComfoCool is overheated",
    C_CC_COMP_ERR: "ComfoCool compressor error",
    C_CC_T_10_ERR: "ComfoCool room temperature out of bounds",
    C_CC_T_13_ERR: "ComfoCool compressor temperature out of bounds",
    C_CC_T_23_ERR: "ComfoCool supply temperature out of bounds",
    C_T_HOOD_ERR: "Hood temperature is too high",
    C_IO_HOOD_DUTY_ERR: "Hood is activated",
    C_QM_CONSTRAINT_MIN_ERR: "STATUS-FLAG",
    C_H_21_QM_MIN_ERR: "Current too low for preheater",
    C_CONFIG_ERR: "Configuration error",
    C_ANALYSIS_BUSY_WARNING: "Warning that an error analysis is running",
    C_COMFONET_ERR: "Error on the ComfoNet bus",
    C_CO2_SENS_COUNT_ERR: "The number of CO2 sensors on a controller has decreased - one or more sensors are no longer detected",
    C_CO2_SENS_TOO_MANY_ERR: "More than 8 sensors are detected in one zone",
    C_CO2_SENS_GENERAL_ERR: "General CO2 sensor error",
}

# --- Constants ---

# Data type for coils or discrete_inputs
C_DT_BITS = ModbusTcpClient.DATATYPE.BITS  # "bit"     # 1 Bit

# Data types for input_registers or holding_registers
C_DT_INT16 = ModbusTcpClient.DATATYPE.INT16  # "INT16"     # 1 Register
C_DT_UINT16 = ModbusTcpClient.DATATYPE.UINT16  # "UINT16"   # 1 Register
C_DT_INT32 = ModbusTcpClient.DATATYPE.INT32  # "INT32"   # 2 Register
C_DT_UINT32 = ModbusTcpClient.DATATYPE.UINT32  # "UINT32"   # 2 Register

C_MIN_INPUT_REGISTER = sys.maxsize
C_MAX_INPUT_REGISTER = -1
C_MIN_HOLDING_REGISTER = sys.maxsize
C_MAX_HOLDING_REGISTER = -1
C_MIN_COILS = sys.maxsize
C_MAX_COILS = -1
C_MIN_DISCRETE_INPUTS = sys.maxsize
C_MAX_DISCRETE_INPUTS = -1

# Constants for defining the register type
C_REG_TYPE_UNKNOWN = 0
C_REG_TYPE_COILS = 1
C_REG_TYPE_DISCRETE_INPUTS = 2
C_REG_TYPE_HOLDING_REGISTERS = 3
C_REG_TYPE_INPUT_REGISTERS = 4

# ------------------------------------------------------------
# 2) Entity constants (C_<NAME> = "<entity_key>")
#    >> These constants serve as keys in the ENTITIES_DICT.
# ------------------------------------------------------------
C_CONNECTION_STATE = "connection_state"
C_ACTIVEERROR1 = "activeerror1"
C_ACTIVEERROR2 = "activeerror2"
C_ACTIVEERROR3 = "activeerror3"
C_ACTIVEERROR4 = "activeerror4"
C_ACTIVEERROR5 = "activeerror5"
C_AIRFLOW = "airflow"
C_ROOM_TEMPERATURE = "room_temperature"
C_EXTRACT_TEMPERATURE = "extract_temperature"
C_EXHAUST_TEMPERATURE = "exhaust_temperature"
C_OUTDOOR_TEMPERATURE = "outdoor_temperature"
C_SUPPLY_TEMPERATURE = "supply_temperature"
C_ROOM_HUMIDITY = "room_humidity"
C_EXTRACT_HUMIDITY = "extract_humidity"
C_EXHAUST_HUMIDITY = "exhaust_humidity"
C_OUTDOOR_HUMIDITY = "outdoor_humidity"
C_SUPPLY_HUMIDITY = "supply_humidity"
C_CO2_SENSOR_ZONE_1 = "co2_sensor_zone_1"
C_CO2_SENSOR_ZONE_2 = "co2_sensor_zone_2"
C_CO2_SENSOR_ZONE_3 = "co2_sensor_zone_3"
C_CO2_SENSOR_ZONE_4 = "co2_sensor_zone_4"
C_CO2_SENSOR_ZONE_5 = "co2_sensor_zone_5"
C_CO2_SENSOR_ZONE_6 = "co2_sensor_zone_6"
C_CO2_SENSOR_ZONE_7 = "co2_sensor_zone_7"
C_CO2_SENSOR_ZONE_8 = "co2_sensor_zone_8"
C_FILTER_DAYS_REMAINING = "filter_days_remaining"

C_ERROR_FLAG = "error_flag"
C_STANDBY = "standby"
C_COMFOHOOD = "comfohood"
C_FILTER_DIRTY = "filter_dirty"

C_VENTILATION_PRESET = "ventilation_preset"
C_TEMPERATURE_PROFILE = "temperature_profile"
C_TEMPERATURE_PROFILE_MODE = "temperature_profile_mode"
C_EXTERNAL_SETPOINT = "external_setpoint"
C_BOOST_TIME = "boost_time"

C_RESET_ERRORS = "reset_errors"
C_VENTILATION_PRESET_AWAY = "ventilation_preset_away"
C_VENTILATIONPRESET1 = "ventilationpreset1"
C_VENTILATIONPRESET2 = "ventilationpreset2"
C_VENTILATIONPRESET3 = "ventilationpreset3"
C_AUTO_MODE = "auto_mode"
C_BOOST = "boost"
C_AWAY_FUNCTION = "away_function"
C_COMFOCOOL = "comfocool"


# --------------------------------------------------------------------------------------------
# 2) ENTITIES_DICT DICT, new registers only need to be added here.
#    If additional registers do not require new logic, the rest of the code is already prepared for it
# --------------------------------------------------------------------------------------------
#    ENTITIES_DICT: Dict[str, Dict[str, Any]]
#    *Key = matching C_<...>-constant = HASS sensor_id
#    *NAME: Displayed name
#    *REG: Modbus register (Zero-Based)
#    *RT: Register Type (currently 1..4): Holding-Register, Coils (read-write) or Input-Register, Discrete-Inputs (read-only)
#    *DT: Data type (currently only BITS, INT16, UINT16), Note: BITS for Coils and Discrete-Inputs (optional). Switches always with 0 or 1
#    RW: Prevent Read/Write for Coils and Holding-Registers with "RW":0
#    FAKTOR: Multiplier for display in HA (currently: 1, 0.1)
#    UNIT: Unit of the entity (°C, W, kW, Wh, kWh, bar, ppm, m³/h...)
#    STEP: Controls the display in HA, step size of the setting (e.g. 5.0, 1.0, 0.5, 0.1)
#    MIN: Allowed minimum value of the entity
#    MAX: Allowed maximum value of the entity
#    VALUES: Valid selection values; dict[id,DisplayName] with optional component: "default":<defaultvalue>
#    INC: 1, if entity provides continuously increasing values.
#    SWITCH: Values for "off" and optionally for "on". If "on" is not specified, all other integer values are valid for "on"
#    PF: Override display variant in HA. "PF":Platform.NUMBER v=> Temperature value is treated as NUMBER instead of CLIMATE.
#
#    *: Mandatory value
# --------------------------------------------------------------------------------------------

# Modbus registers according to Zehnder_CSY_ComfoConnect-Pro_INM_EN-en.pdf from 24.09.2024
# Attention: Registers are numbered starting from 1 in the documentation and it is pointed out,
# that in the PDU, registers are addressed starting from zero (1-16 -> 0-15). Therefore, always reduce the value from the doc by one for the REG value.
# Tested with Zehnder ComfoConnect PRO  RCG 2.0.0.10

# --- ENTITIES_DICT ---
ENTITIES_DICT: Dict[str, Dict[str, Any]] = {
    # INPUT_REGISTERS
    C_CONNECTION_STATE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 0,
        "NAME": "Connection State",
        "VALUES": {
            0: "ok",
            30: "the detected ventilation unit is not a CAQ",
            40: "CAQ version not compatible",
            50: "no ventilation unit detected",
        },
        "DT": C_DT_UINT16,
    },
    C_ACTIVEERROR1: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 1,
        "NAME": "Error 1",
        "VALUES": ERROR_DICT,
        "DT": C_DT_UINT16,
    },
    C_ACTIVEERROR2: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 2,
        "NAME": "Error 2",
        "VALUES": ERROR_DICT,
        "DT": C_DT_UINT16,
    },
    C_ACTIVEERROR3: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 3,
        "NAME": "Error 3",
        "VALUES": ERROR_DICT,
        "DT": C_DT_UINT16,
    },
    C_ACTIVEERROR4: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 4,
        "NAME": "Error 4",
        "VALUES": ERROR_DICT,
        "DT": C_DT_UINT16,
    },
    C_ACTIVEERROR5: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 5,
        "NAME": "Error 5",
        "VALUES": ERROR_DICT,
        "DT": C_DT_UINT16,
    },
    C_AIRFLOW: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 6,
        "NAME": "Supply Air Fan Volume",
        "UNIT": "m³",
        "DT": C_DT_UINT16,
    },
    C_ROOM_TEMPERATURE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 7,
        "NAME": "Room Air Temperature",
        "FAKTOR": 0.1,
        "UNIT": "°C",
        "DT": C_DT_INT16,
    },
    C_EXTRACT_TEMPERATURE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 8,
        "NAME": "Extract Air Temperature",
        "FAKTOR": 0.1,
        "UNIT": "°C",
        "DT": C_DT_INT16,
    },
    C_EXHAUST_TEMPERATURE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 9,
        "NAME": "Exhaust Air Temperature",
        "FAKTOR": 0.1,
        "UNIT": "°C",
        "DT": C_DT_INT16,
    },
    C_OUTDOOR_TEMPERATURE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 10,
        "NAME": "Outdoor Air Temperature",
        "FAKTOR": 0.1,
        "UNIT": "°C",
        "DT": C_DT_INT16,
    },
    C_SUPPLY_TEMPERATURE: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 11,
        "NAME": "Supply Air Temperature",
        "FAKTOR": 0.1,
        "UNIT": "°C",
        "DT": C_DT_INT16,
    },
    C_ROOM_HUMIDITY: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 12,
        "NAME": "Room Air Humidity",
        "UNIT": "%",
        "DT": C_DT_UINT16,
    },
    C_EXTRACT_HUMIDITY: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 13,
        "NAME": "Extract Air Humidity",
        "UNIT": "%",
        "DT": C_DT_UINT16,
    },
    C_EXHAUST_HUMIDITY: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 14,
        "NAME": "Exhaust Air Humidity",
        "UNIT": "%",
        "DT": C_DT_UINT16,
    },
    C_OUTDOOR_HUMIDITY: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 15,
        "NAME": "Outdoor Air Humidity",
        "UNIT": "%",
        "DT": C_DT_UINT16,
    },
    C_SUPPLY_HUMIDITY: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 16,
        "NAME": "Supply Air Humidity",
        "UNIT": "%",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_1: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 17,
        "NAME": "CO2 Sensor Zone 1",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_2: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 18,
        "NAME": "CO2 Sensor Zone 2",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_3: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 19,
        "NAME": "CO2 Sensor Zone 3",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_4: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 20,
        "NAME": "CO2 Sensor Zone 4",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_5: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 21,
        "NAME": "CO2 Sensor Zone 5",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_6: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 22,
        "NAME": "CO2 Sensor Zone 6",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_7: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 23,
        "NAME": "CO2 Sensor Zone 7",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_CO2_SENSOR_ZONE_8: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 24,
        "NAME": "CO2 Sensor Zone 8",
        "UNIT": "ppm",
        "DT": C_DT_UINT16,
    },
    C_FILTER_DAYS_REMAINING: {
        "RT": C_REG_TYPE_INPUT_REGISTERS,
        "REG": 25,
        "NAME": "Filter replacement in",
        "UNIT": "d",
        "DT": C_DT_UINT16,
    },
    # DISCRETE_INPUTS
    C_ERROR_FLAG: {"RT": C_REG_TYPE_DISCRETE_INPUTS, "REG": 0, "NAME": "Error active?"},
    C_STANDBY: {"RT": C_REG_TYPE_DISCRETE_INPUTS, "REG": 1, "NAME": "Standby"},
    C_COMFOHOOD: {"RT": C_REG_TYPE_DISCRETE_INPUTS, "REG": 2, "NAME": "ComfoHood"},
    C_FILTER_DIRTY: {
        "RT": C_REG_TYPE_DISCRETE_INPUTS,
        "REG": 3,
        "NAME": "Change filter",
    },
    # HOLDING_REGISTERS
    C_VENTILATION_PRESET: {
        "RT": C_REG_TYPE_HOLDING_REGISTERS,
        "REG": 0,
        "NAME": "Ventilation Level",
        "DT": C_DT_UINT16,  # byte -> in 16 Bit Register
        "VALUES": {
            0: "Away",
            1: "Preset 1",
            2: "Preset 2",
            3: "Preset 3",
            "default": 2,
        },
    },
    C_TEMPERATURE_PROFILE: {
        "RT": C_REG_TYPE_HOLDING_REGISTERS,
        "REG": 1,
        "NAME": "Temperature Profile",
        "DT": C_DT_UINT16,  # byte -> in 16 Bit Register
        "VALUES": {0: "Comfort", 1: "Eco", 2: "Warm", "default": 0},
        # Note: only works in mode 0 or 1
    },
    C_TEMPERATURE_PROFILE_MODE: {
        "RT": C_REG_TYPE_HOLDING_REGISTERS,
        "REG": 2,
        "NAME": "Temperature Profile Mode",
        "DT": C_DT_UINT16,  # byte -> in 16 Bit Register
        "VALUES": {0: "Adaptive", 1: "Fixed", 2: "according to ext. setpoint", "default": 0},
    },
    C_EXTERNAL_SETPOINT: {
        "RT": C_REG_TYPE_HOLDING_REGISTERS,
        "REG": 3,
        "NAME": "External Setpoint",
        "FAKTOR": 0.1,
        "MIN": 5.0,
        "MAX": 35.0,
        "UNIT": "°C",
        "DT": C_DT_UINT16,
        # Note: only works in mode 2
    },
    C_BOOST_TIME: {
        "RT": C_REG_TYPE_HOLDING_REGISTERS,
        "REG": 4,
        "NAME": "Boost Time [min.]",
        "FAKTOR": 0.016666666667,  # Seconds: 1.0, register contains seconds, conversion to minutes
        "UNIT": "min",
        "STEP": 1,  # Seconds: 60,
        "MIN": 0,
        "MAX": 1092,  # Seconds: 65535,
        "DT": C_DT_UINT16,
        # Note: 65535 (18h12m15s) is considered as 24 hours
    },
    # COILS
    C_RESET_ERRORS: {
        "RT": C_REG_TYPE_COILS,
        "REG": 0,
        "NAME": "Acknowledge Errors",
        # self-resetting coil, the value False is ignored
    },
    # # Is already set via C_VENTILATION_PRESET
    # C_VENTILATION_PRESET_AWAY: {
    #     "RT": C_REG_TYPE_COILS, "REG": 1, "NAME": "Ventilation Preset Away"
    #     # the value False is ignored
    # },
    # C_VENTILATIONPRESET1: {
    #     "RT": C_REG_TYPE_COILS, "REG": 2, "NAME": "VentilationPreset1"
    #     # the value False is ignored
    # },
    # C_VENTILATIONPRESET2: {
    #     "RT": C_REG_TYPE_COILS, "REG": 3, "NAME": "VentilationPreset2"
    #     # the value False is ignored
    # },
    # C_VENTILATIONPRESET3: {
    #    "RT": C_REG_TYPE_COILS, "REG": 4, "NAME": "VentilationPreset3"
    #    # the value False is ignored
    # },
    C_AUTO_MODE: {"RT": C_REG_TYPE_COILS, "REG": 5, "NAME": "Auto Mode"},
    C_BOOST: {"RT": C_REG_TYPE_COILS, "REG": 6, "NAME": "Boost"},
    C_AWAY_FUNCTION: {"RT": C_REG_TYPE_COILS, "REG": 7, "NAME": "Away function"},
    C_COMFOCOOL: {"RT": C_REG_TYPE_COILS, "REG": 8, "NAME": "ComfoCool"},
}


# ------------------------------------------------------------
# Class definitions for the different entity types
# ------------------------------------------------------------


@dataclass
class MyBinarySensorEntityDescription(BinarySensorEntityDescription):
    """A class that describes Modbus binarysensor entities."""


@dataclass
class MySensorEntityDescription(SensorEntityDescription):
    """A class that describes Modbus sensor entities."""


@dataclass
class MyBinaryEntityDescription(BinarySensorEntityDescription):
    """A class that describes Modbus binary entities."""

    # Note: If real switch entities are used, use SwitchEntityDescription if necessary.


@dataclass
class MySelectEntityDescription(SensorEntityDescription):
    """A class that describes Modbus select sensor entities."""

    select_options: list[str] = None
    default_select_option: str = None
    setter_function = None


@dataclass
class MyClimateEntityDescription(ClimateEntityDescription):
    """A class that describes Modbus climate sensor entities."""

    min_value: float = None
    max_value: float = None
    step: float = None
    hvac_modes: list[str] = None
    temperature_unit: str = "°C"
    supported_features: ClimateEntityFeature = ClimateEntityFeature.TARGET_TEMPERATURE


@dataclass
class MyNumberEntityDescription(NumberEntityDescription):
    """A class that describes Modbus number entities."""

    mode: str = "slider"
    initial: float = None
    editable: bool = True


BINARYSENSOR_TYPES: dict[str, MyBinarySensorEntityDescription] = {}
SENSOR_TYPES: dict[str, MySensorEntityDescription] = {}
SELECT_TYPES: dict[str, MySelectEntityDescription] = {}
CLIMATE_TYPES: dict[str, MyClimateEntityDescription] = {}
NUMBER_TYPES: dict[str, MyNumberEntityDescription] = {}
BINARY_TYPES: dict[str, MyBinaryEntityDescription] = {}


# --------------------------------------------------------------------
# Helper functions for classifying the entities from ENTITIES_DICT
# --------------------------------------------------------------------

TEMP_UNITS = {"°C", "K"}


def is_entity_readonly(props: Dict[str, Any]) -> bool:
    """Input registers or discrete inputs or Read-Only: RW=0)"""
    reg_type = get_entity_type(props)
    return reg_type in [C_REG_TYPE_INPUT_REGISTERS, C_REG_TYPE_DISCRETE_INPUTS] or (props.get("RW") == 0)


def is_entity_readwrite(props: Dict[str, Any]) -> bool:
    """Writable, Read-Only: Writable (WR=None)"""
    reg_type = get_entity_type(props)
    return reg_type in [C_REG_TYPE_HOLDING_REGISTERS, C_REG_TYPE_COILS]


def is_entity_switch(props: Dict[str, Any]) -> bool:
    reg_type = get_entity_type(props)
    return (reg_type in [C_REG_TYPE_DISCRETE_INPUTS, C_REG_TYPE_COILS]) or (
        get_entity_switch(props) is not None
    )


def is_entity_select(props: Dict[str, Any]) -> bool:
    return props.get("VALUES") not in (None, {})


def is_entity_climate(props: Dict[str, Any]) -> bool:
    return get_entity_unit(props) in TEMP_UNITS and get_entity_platform(props) in {
        None,
        Platform.CLIMATE,
    }


def is_entity_number(props: Dict[str, Any]) -> bool:
    return get_entity_platform(props) == Platform.NUMBER or not (
        is_entity_switch(props) or is_entity_select(props) or is_entity_climate(props)
    )


# -------------------------------------------------
# Helper functions for reading the data of an entity
# -------------------------------------------------


def get_entity_type(props: Dict[str, Any]) -> int | None:
    return props.get("RT")


def get_entity_name(props: Dict[str, Any], default: str = None) -> str | None:
    return props.get("NAME", default)


def get_entity_unit(props: Dict[str, Any], default: str = None) -> str | None:
    return props.get("UNIT", default)


def get_entity_platform(props: Dict[str, Any], default: str = None) -> str | None:
    return props.get("PF", default)


def get_entity_min(props: Dict[str, Any]) -> float | None:
    return props.get("MIN", 0)


def get_entity_max(props: Dict[str, Any]) -> float | None:
    return props.get("MAX", 50.0)


def get_entity_step(props: Dict[str, Any]) -> float | None:
    return props.get("STEP", 0.1)


def get_entity_hvac_modes(
    props: Dict[str, Any], default: str = None
) -> list[str] | None:
    return props.get("HVAC_MODES") or default


def get_entity_switch(props: Dict[str, Any]) -> dict[str, int] | None:
    return props.get("SWITCH")


def get_entity_select(props: Dict[str, Any]) -> dict[Any, Any] | None:
    return props.get("VALUES")


def get_entity_select_values_and_default(
    props: dict[str, Any],
) -> tuple[list[str], str] | None:
    values = get_entity_select(props)
    default_index = values.get("default")
    select_map = {k: v for k, v in values.items() if k != "default"}
    return list(select_map.values()), select_map.get(default_index)


def get_entity_reg(
    props: Dict[str, Any],
) -> tuple[int | None, ModbusTcpClient.DATATYPE | None]:
    reg_type = get_entity_type(props)
    if reg_type in [C_REG_TYPE_COILS, C_REG_TYPE_DISCRETE_INPUTS]:
        dt = C_DT_BITS
    else:
        dt = props.get("DT")
    return props.get("REG"), dt


def get_entity_props(entity: str) -> dict:
    return ENTITIES_DICT[entity]


def get_entity_factor(props: Dict[str, Any]) -> float:
    return props.get("FAKTOR", 1.0)


# --------------------------------------------------------------------------------
# Helper functions for creating the data structures derived from ENTITIES_DICT
# --------------------------------------------------------------------------------


def _classify_register(props: Dict[str, Any]) -> int | None:
    global \
        C_MIN_INPUT_REGISTER, \
        C_MAX_INPUT_REGISTER, \
        C_MIN_HOLDING_REGISTER, \
        C_MAX_HOLDING_REGISTER, \
        C_MIN_COILS, \
        C_MAX_COILS, \
        C_MIN_DISCRETE_INPUTS, \
        C_MAX_DISCRETE_INPUTS

    reg_type = get_entity_type(props)
    reg_from, dt = get_entity_reg(props)
    if reg_from is None or dt is None:
        return None
    if dt == ModbusTcpClient.DATATYPE.BITS:
        sizeofdt = 1
    else:
        sizeofdt = dt.value[1]
    reg_to = reg_from + sizeofdt - 1

    match reg_type:
        case thismodule.C_REG_TYPE_DISCRETE_INPUTS:
            C_MIN_DISCRETE_INPUTS = min(reg_from, C_MIN_DISCRETE_INPUTS)
            C_MAX_DISCRETE_INPUTS = max(reg_to, C_MAX_DISCRETE_INPUTS)
        case thismodule.C_REG_TYPE_COILS:
            C_MIN_COILS = min(reg_from, C_MIN_COILS)
            C_MAX_COILS = max(reg_to, C_MAX_COILS)
        case thismodule.C_REG_TYPE_INPUT_REGISTERS:
            C_MIN_INPUT_REGISTER = min(reg_from, C_MIN_INPUT_REGISTER)
            C_MAX_INPUT_REGISTER = max(reg_to, C_MAX_INPUT_REGISTER)
        case thismodule.C_REG_TYPE_HOLDING_REGISTERS:
            C_MIN_HOLDING_REGISTER = min(reg_from, C_MIN_HOLDING_REGISTER)
            C_MAX_HOLDING_REGISTER = max(reg_to, C_MAX_HOLDING_REGISTER)

    if is_entity_readonly(props):
        if is_entity_switch(props):
            """Not writable, switch (SWITCH!=None)."""
            return MyBinarySensorEntityDescription  # C_REGISTERCLASS_BINARY_SENSOR
        elif is_entity_select(props):
            """Not writable, selection (VALUES contains at least one element)."""
            return MySensorEntityDescription  # C_REGISTERCLASS_SELECT_ENTITY
        else:
            """Not writable, no switch (SWITCH=None)."""
            return MySensorEntityDescription  # C_REGISTERCLASS_SENSOR
    else:
        if is_entity_switch(props):
            """Writable, switch (SWITCH!=None)."""
            return MyBinaryEntityDescription  # C_REGISTERCLASS_BINARY_ENTITY
        elif is_entity_select(props):
            """Writable, selection (VALUES contains at least one element)."""
            return MySelectEntityDescription  # C_REGISTERCLASS_SELECT_ENTITY
        elif is_entity_climate(props):
            """Writable, only allow temperature units (°C or K)"""
            return MyClimateEntityDescription  # C_REGISTERCLASS_CLIMATE_ENTITY
        else:
            """Writable, no switch (SWITCH=None), no selection (VALUES is None), unit optional, but not °C or K."""
            return MyNumberEntityDescription  # C_REGISTERCLASS_NUMBER_ENTITY


def _unit_mapping(
    unit: Optional[str],
) -> tuple[Optional[str], Optional[SensorDeviceClass], Optional[SensorStateClass]]:
    """
    Maps our unit (UNIT) to Home Assistant native_unit_of_measurement + device_class + state_class.
    For unknown units, classes remain empty.
    """
    if unit is None:
        return None, None, None

    u = unit.strip()
    # Temperature
    if u == "°C":
        return (
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
        )
    if u == "K":
        # Rarely as absolute temperature; here usually offsets -> not meaningful as °C.
        return (
            UnitOfTemperature.KELVIN,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
        )

    # Pressure
    if u.lower() in {"bar"}:
        return (
            UnitOfPressure.BAR,
            SensorDeviceClass.PRESSURE,
            SensorStateClass.MEASUREMENT,
        )

    # Energy & Power
    if u.lower() in {"kwh", "kW/h".lower()}:  # accept both spellings
        return (
            UnitOfEnergy.KILO_WATT_HOUR,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL_INCREASING,
        )
    if u.lower() in {"w"}:
        return UnitOfPower.WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    if u.lower() in {"kw"}:
        return (
            UnitOfPower.KILO_WATT,
            SensorDeviceClass.POWER,
            SensorStateClass.MEASUREMENT,
        )

    # Volume flow
    if u.lower() in {"l/min", "l/Min", "l pro min"}:
        return "l/min", None, SensorStateClass.MEASUREMENT
    if u.lower() in {"m³/h"}:
        return "m³/h", None, SensorStateClass.MEASUREMENT

    # Speed / Control level
    if u == "‰":
        return "‰", None, SensorStateClass.MEASUREMENT
    if u == "%":
        return "%", None, SensorStateClass.MEASUREMENT

    # PPM, Proportion
    if u == "ppm":
        return "ppm", None, SensorStateClass.MEASUREMENT

    # Time/Duration
    if u.lower() in {"h", "std"}:
        return "h", SensorDeviceClass.DURATION, SensorStateClass.TOTAL_INCREASING
    if u.lower() in {"min"}:
        return "min", SensorDeviceClass.DURATION, SensorStateClass.MEASUREMENT
    if u.lower() in {"s", "sek", "sec"}:
        return "s", SensorDeviceClass.DURATION, SensorStateClass.MEASUREMENT

    # Remaining duration
    if u.lower() in {"d", "days"}:
        return "d", SensorDeviceClass.DURATION, SensorStateClass.MEASUREMENT

    # Fallback: use raw unit without device class
    return u, None, SensorStateClass.MEASUREMENT


_initialized = False


def init():
    global \
        _initialized, \
        BINARYSENSOR_TYPES, \
        SENSOR_TYPES, \
        SELECT_TYPES, \
        CLIMATE_TYPES, \
        NUMBER_TYPES, \
        BINARY_TYPES
    if _initialized:
        return
    _LOGGER.info(
        "****************************************  initalizing ***************************************"
    )

    thismodule.BINARYSENSOR_TYPES = {}
    thismodule.SENSOR_TYPES = {}
    thismodule.SELECT_TYPES = {}
    thismodule.CLIMATE_TYPES = {}
    thismodule.NUMBER_TYPES = {}
    thismodule.BINARY_TYPES = {}

    for c_key, props in ENTITIES_DICT.items():
        entity_key: str = c_key
        name: str = get_entity_name(props, entity_key)
        registerclass = _classify_register(props)

        match registerclass:
            case thismodule.MySensorEntityDescription:
                unit, device_class, state_class = _unit_mapping(get_entity_unit(props))
                _LOGGER.debug(f"Sensor {entity_key}: {name}, Unit {unit}")
                SENSOR_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                    native_unit_of_measurement=unit,
                    device_class=device_class,
                    state_class=state_class,
                )

            case thismodule.MyBinarySensorEntityDescription:
                _LOGGER.debug(f"Binary Sensor {entity_key}: {name}")
                BINARYSENSOR_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                )

            case thismodule.MyClimateEntityDescription:
                # key = f"{C_PREFIX_CLIMATE}_{entity_key}"
                min_value = get_entity_min(props)
                max_value = get_entity_max(props)
                step = get_entity_step(props)
                hvac_modes = get_entity_hvac_modes(props)
                temperature_unit = get_entity_unit(props)
                _LOGGER.debug(
                    f"Temperature Setpoint {entity_key}: {name}, {min_value}-{max_value}{temperature_unit} in {step} steps"
                )
                CLIMATE_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                    min_value=min_value,
                    max_value=max_value,
                    step=step,
                    hvac_modes=hvac_modes,
                    temperature_unit=temperature_unit,
                    supported_features=props.get(
                        "FEATURES", ClimateEntityFeature.TARGET_TEMPERATURE
                    ),
                )

            case thismodule.MyNumberEntityDescription:
                # key = f"{C_PREFIX_NUMBER}_{entity_key}"
                min_value = get_entity_min(props)
                max_value = get_entity_max(props)
                step = get_entity_step(props)
                unit_of_measurement = get_entity_unit(props)
                _LOGGER.debug(
                    f"Numerical Setpoint {entity_key}: {name}, {min_value}-{max_value}{unit_of_measurement} in {step} steps"
                )
                NUMBER_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                    min_value=min_value,
                    max_value=max_value,
                    step=step,
                    unit_of_measurement=unit_of_measurement,
                    editable=is_entity_readwrite(props),
                    mode="box",
                )

            case thismodule.MyBinaryEntityDescription:
                # key = f"{C_PREFIX_SWITCH}_{entity_key}"
                _LOGGER.debug(f"Switch {entity_key}: {name}")
                BINARY_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                )

            case thismodule.MySelectEntityDescription:
                # key = f"{C_PREFIX_SELECT}_{entity_key}"
                values, default = get_entity_select_values_and_default(props)
                _LOGGER.debug(
                    f"Select Entity {entity_key}: {name}, Value range: {values}, Default: {default}"
                )
                SELECT_TYPES[entity_key] = registerclass(
                    name=name,
                    key=entity_key,
                    select_options=values,
                    default_select_option=default,
                )

            case _:
                _LOGGER.warning(f"Unknown entity type {entity_key}: {props}")
                print(f"Sensor could not be assigned: {entity_key}/{name}")

    _initialized = True
    _LOGGER.debug(
        f"Status registers (r/o) from {C_MIN_INPUT_REGISTER} to {C_MAX_INPUT_REGISTER}"
    )
    _LOGGER.debug(
        f"Discrete inputs registers (r/o) from {C_MIN_DISCRETE_INPUTS} to {C_MAX_DISCRETE_INPUTS}"
    )
    _LOGGER.debug(f"- {len(SENSOR_TYPES)} Sensors")
    _LOGGER.debug(f"- {len(BINARYSENSOR_TYPES)} Binary Sensors")
    _LOGGER.debug(
        f"Holding registers (r/w) from {C_MIN_HOLDING_REGISTER} to {C_MAX_HOLDING_REGISTER}"
    )
    _LOGGER.debug(f"Coils (r/w) from {C_MIN_COILS} to {C_MAX_COILS}")
    _LOGGER.debug(f"- {len(SELECT_TYPES)} Select Entities")
    _LOGGER.debug(f"- {len(BINARY_TYPES)} Switches")
    _LOGGER.debug(f"- {len(CLIMATE_TYPES)} Temperature Setpoints")
    _LOGGER.debug(f"- {len(NUMBER_TYPES)} Numerical Setpoints")
    _LOGGER.info(
        "****************************************  initalized ****************************************"
    )


init()