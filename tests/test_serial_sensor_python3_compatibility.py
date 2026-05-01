#!/usr/bin/env python3
"""
Unit tests for Python 3 compatibility in serial_sensor.py.
"""

import pytest
from src.io_protocols.serial_sensor import SerialSensorReader


def test_serial_sensor_initialization():
    """Test SerialSensorReader initialization."""
    reader = SerialSensorReader("/dev/null")
    assert reader.port_path == "/dev/null"


def test_serial_sensor_exception_handling():
    """Test exception handling in SerialSensorReader."""
    reader = SerialSensorReader("/dev/null")

    # Mock exception handling (Python 3 compatible)
    with pytest.raises(Exception) as exc_info:
        reader.read_packet()

    assert "IOError" in str(exc_info.value) or "AttributeError" in str(exc_info.value)
