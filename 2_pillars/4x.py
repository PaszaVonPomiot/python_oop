"""
Create Image abstract class with instance attributes as parameters: width, length, bit_depth
Image class defines abstract method export()
Create Jpeg and Png derived classes that implement export() method
export() returns string like "Fantastic jpeg 800x600x24"
"""


class Image:
    ...


class Jpeg:
    ...


class Png:
    ...


jpeg = Jpeg(width=1080, length=960, bit_depth=24)
jpeg.export()
