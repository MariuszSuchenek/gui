#!/usr/bin/python3
from PyQt5 import QtWidgets, uic
import sys

class Monitor(QtWidgets.QWidget):
    def __init__(self, *args):
        """
        Initialize the Monitor widget.

        Grabs child widgets.
        """
        super(Monitor, self).__init__(*args)
        uic.loadUi("monitor/monitor.ui", self)
        self.label_name = self.findChild(QtWidgets.QLabel, "label_name")
        self.label_value = self.findChild(QtWidgets.QLabel, "label_value")
        self.label_min = self.findChild(QtWidgets.QLabel, "label_min")
        self.label_max = self.findChild(QtWidgets.QLabel, "label_max")
        self.label_units = self.findChild(QtWidgets.QLabel, "label_units")
        self.label_statnames = [];
        self.label_statnames.append(self.findChild(QtWidgets.QLabel, "label_statname1"))
        self.label_statnames.append(self.findChild(QtWidgets.QLabel, "label_statname2"))
        self.label_statvalues = [];
        self.label_statvalues.append(self.findChild(QtWidgets.QLabel, "label_statvalue1"))
        self.label_statvalues.append(self.findChild(QtWidgets.QLabel, "label_statvalue2"))

        self.show()
    def setup(self, name, setrange=(0,50,100), units=None, stats=None):
        """
        Sets up main values for the Monitor widget, including the name and the values for the
        range as (minimum, initial, maximum). Also optionally set the units and statistical values
        of the monitored field.

        name: The name to be displayed.
        setrange: Tuple (min, current, max) specifying the allowed min/max values and current value.
        units: String value for the units to be displayed.
        """
        self.label_name.setText(name)

        # unpack and assign min, current, and max
        (low, val, high) = setrange
        self.label_min.setText(str(low))
        self.label_max.setText(str(high))
        self.value = val
        self.minimum = low
        self.maximum = high

        # Handle optional units
        if units is not None:
            self.label_units.setText(str(units))
        else:
            self.label_units.setText("")
        self.update(val)

        # Handle optional stats
        # TODO: determine is stats are useful/necessary

    def update(self, value):
        """
        Updates the value in the monitored field

        value: The value that the monitor will display.
        """
        self.value = value;
        self.label_value.setText(str(value))

    def is_alarm(self):
        """
        Returns true if the monitored value is beyond the min or max threshold (i.e ALARM!).
        """
        return self.value <= self.minimum or self.value >= self.maximum
