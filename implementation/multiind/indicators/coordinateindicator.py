import re

from multiind.indicators import Indicator


class CoordinateIndicator(Indicator):
    """
    Indicator for users with coordinates in their location field.
    """

    regex = r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)[\s,]+[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d)‌​)(\.\d+)?)$"

    def __init__(self, config):
        self.prog = re.compile(CoordinateIndicator.regex)
        self.weight = config.getfloat("mi_weights", "COD")

    def get_loc(self, string):
        if not string:
            return []

        # see if the string matches the coordinate
        if self.prog.match(string):
            split = re.split('[\s,]+', string)
            poly = self.point_to_poly((float(split[0]), float(split[1])), 1) # 1 belief
            return [poly]
        return []
