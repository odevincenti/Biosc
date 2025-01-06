from PySide6 import QtWidgets


class ScaleSpinBox(QtWidgets.QSpinBox):
    """
    Custom spin box for the vertical scale
    The effect of this scale is to define a multiplyer that resizes the signal
    The plot's y scale is fixed to 10 divisions, from -5 to 5. The signal is then multiplied by the scale
    """
    def __init__(self, parent=None):
        super(ScaleSpinBox, self).__init__(parent)
        self.units = [1, 2, 5, 10]
        self.scales = [1, 10, 100, 1000]
        self.current_scale_index = 0
        self.valid_values = self.get_valid_values()

        self.setRange(1, 10000)
        self.setSingleStep(1)

        # Initialize value at 500 mV/div
        self.setValue(500)

    def get_valid_values(self):
        # Generate the possible values based on units and scales
        valid_values = [mult * scale for scale in self.scales for mult in self.units]
        return sorted(set(valid_values))

    def stepBy(self, steps):
        current_value = self.value()

        # Find the nearest valid step
        if current_value in self.valid_values:
            current_index = self.valid_values.index(current_value)
        else:
            current_index = min(range(len(self.valid_values)), key=lambda i: abs(self.valid_values[i] - current_value))

        # Compute new index within valid ranges
        new_index = current_index + steps
        new_index = max(0, min(new_index, len(self.valid_values) - 1))

        # Set new value
        self.setValue(self.valid_values[new_index])

    def textFromValue(self, value):
        # Customize text display for "mV/div" or "V/div"
        if value >= 1000:
            return f"{value // 1000} V/div"
        else:
            return f"{value} mV/div"

    def valueFromText(self, text):
        # Extract numerical value from text
        text = text.replace(" V/div", "").replace(" mV/div", "")
        return float(text)

    # Invert the direction of the wheel event
    def wheelEvent(self, event):
        inverted_delta = -event.angleDelta().y()
        new_event = event.clone()
        new_event.angleDelta().setY(inverted_delta)
        super().wheelEvent(new_event)


def main():
    pass


if __name__ == '__main__':
    main()
