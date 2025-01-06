import pyqtgraph as pg
from PySide6 import QtCore

N_X_DIVS = 15  # Number of divisions in the x axis
N_Y_DIVS = 10  # Number of divisions in the y axis
X_AX_PAD = 0.3  # Padding for the x axis


class SignalPlotter(pg.PlotWidget):
    timescale_changed = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set y range to 10 divisions, from -5 to 5, and dynamic x range, no auto range
        self.setRange(yRange=(-N_Y_DIVS // 2, N_Y_DIVS // 2), disableAutoRange=True)

        # Set the time scales
        self.time_scales = self.get_valid_time_scales()
        self.len_time_scales = len(self.time_scales)
        self.init_t_scale = self.time_scales[self.len_time_scales // 2]  # 1 ms/div
        self.setRange(xRange=(0, N_X_DIVS * self.init_t_scale + X_AX_PAD * self.init_t_scale), disableAutoRange=True,
                      padding=0)

        # Add a label in the top right corner to indicate the current time scale
        self.time_label = pg.LabelItem(justify='right',
                                       size='12pt',
                                       bold=True,
                                       font='Arial',
                                       angle=0)
        self.getPlotItem().scene().addItem(self.time_label)
        self.time_label.setParentItem(self.getPlotItem().vb)
        self.time_label.anchor((1, 0), (1, 0))  # Top-right corner
        self.update_time_label_and_ticks(self.init_t_scale)

        # Disable dragging
        self.setMouseEnabled(x=False, y=False)

        # Set up the grid
        self.showGrid(x=True, y=True)

    @staticmethod
    def get_valid_time_scales():
        multiplyers = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        units = [1, 1_000, 1_000_000]  # us, ms, s
        units = sorted(set([mult * unit for mult in multiplyers for unit in units]))
        # Remove the last 5 units, as they are too large (maximum value is 10 s/div)
        return units[:-5]

    def wheelEvent(self, event):
        """
        Zoom in or out the x axis based on the mouse wheel event
        :return: None
        """
        current_range = self.getViewBox().viewRange()
        old_range = current_range[0]
        try:
            current_scale = (old_range[1] - old_range[0]) // (N_X_DIVS + X_AX_PAD) + 1
            current_index = self.time_scales.index(current_scale)
        except ValueError:
            # Find the nearest timescale
            current_scale = min(self.time_scales,
                                key=lambda x: abs(x - (old_range[1] - old_range[0]) // (N_X_DIVS + X_AX_PAD) + 1))
            current_index = self.time_scales.index(current_scale)

        # Zoom in or out
        delta = event.angleDelta().y()
        new_index = current_index + (1 if delta < 0 else -1)
        new_index = max(0, min(new_index, self.len_time_scales - 1))
        new_scale = self.time_scales[new_index]
        new_x_range = (0, new_scale * (N_X_DIVS + X_AX_PAD))

        # Update range, and set the label
        self.setRange(xRange=new_x_range, padding=0)
        self.update_time_label_and_ticks(new_scale)
        self.timescale_changed.emit()
        event.accept()

    def update_time_label_and_ticks(self, current_scale):
        """
        Update the time label and ticks based on the current time scale
        :param current_scale: Current time scale in microseconds
        :return:
        """
        if current_scale >= 1_000_000:
            tick_multiplier = 1_000_000
            mult_str = ''

        elif current_scale >= 1_000:
            tick_multiplier = 1_000
            mult_str = 'm'
        else:
            tick_multiplier = 1
            mult_str = '\u03BC'

        self.time_label.setText(f"{current_scale // tick_multiplier} {mult_str}s/div")

        # Set the ticks
        x_axis = self.getAxis('bottom')
        x_ticks_pos = [i * current_scale for i in range(N_X_DIVS + 1)]
        x_ticks_labels = [f"{i * current_scale // tick_multiplier}" for i in range(N_X_DIVS + 1)]
        x_ticks_labels[-1] = f"[{mult_str}s]"
        x_axis.setTicks([list(zip(x_ticks_pos, x_ticks_labels))])
