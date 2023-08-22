import os
from PIL import Image, ImageDraw, ImageFont

from engine import themeConfiguration

hourLines = [[125, 40, 125, 60],
             [125, 190, 125, 210],
             [190, 125, 210, 125],
             [40, 125, 60, 125],
             [166, 51, 156, 69],
             [166, 199, 156, 181],
             [84, 199, 94, 181],
             [84, 51, 94, 69],
             [198, 82, 180, 93],
             [198, 168, 180, 157],
             [52, 168, 70, 157],
             [52, 82, 70, 93]]

minLines = [[134, 40, 133, 50], [143, 42, 140, 51], [152, 44, 148, 53], [160, 47, 155, 56],
            [175, 56, 169, 64], [182, 62, 174, 69], [189, 68, 180, 75], [194, 75, 185, 81],
            [203, 90, 194, 95], [206, 99, 197, 101], [209, 108, 199, 109], [210, 116, 200, 117],

            [134, 210, 133, 200], [143, 208, 140, 199], [152, 206, 148, 197], [160, 203, 155, 194],
            [175, 194, 169, 186], [182, 188, 174, 181], [189, 182, 180, 175], [194, 175, 185, 169],
            [203, 160, 194, 155], [206, 151, 197, 149], [209, 142, 199, 141], [210, 134, 200, 133],

            [116, 210, 117, 200], [107, 208, 110, 199], [98, 206, 102, 197], [90, 203, 95, 194],
            [75, 194, 81, 186], [68, 188, 76, 181], [61, 182, 70, 175], [56, 175, 65, 169],
            [47, 160, 56, 155], [44, 151, 53, 149], [41, 142, 51, 141], [40, 134, 50, 133],

            [116, 40, 117, 50], [107, 42, 110, 51], [98, 44, 102, 53], [90, 47, 95, 56],
            [75, 56, 81, 64], [68, 62, 76, 69], [61, 68, 70, 75], [56, 75, 65, 81],
            [47, 90, 56, 95], [44, 99, 53, 101], [41, 108, 51, 109], [40, 116, 50, 117]]

nums = [[[118, 22], "12"],
        [[168, 34], "1"],
        [[204, 68], "2"],
        [[215, 116], "3"],
        [[202, 165], "4"],
        [[165, 200], "5"],
        [[122, 210], "6"],
        [[78, 200], "7"],
        [[42, 165], "8"],
        [[28, 116], "9"],
        [[36, 68], "10"],
        [[74, 34], "11"]]

numFont = ImageFont.truetype(font=os.path.join("font", "RifficFree.ttf"), size=15)

def draw_icon(theme: themeConfiguration.ThemeConfiguration, PATH: str):
    icon = Image.new("RGBA", (250, 250), (0, 0, 0, 0))

    iconDraw = ImageDraw.Draw(icon)

    iconDraw.ellipse([0, 0, 250, 250], fill=theme.bodyRGB, outline=theme.bodyRGB)
    iconDraw.ellipse([12, 12, 238, 238], outline=theme.borderRGB, width=10)

    for line in hourLines:
        iconDraw.line(line, fill=theme.hourLineRGB, width=5)
    for line in minLines:
        iconDraw.line(line, fill=theme.minLineRGB, width=3)

    for number in nums:
        iconDraw.text(xy=number[0], text=number[1], fill=theme.numberRGB, font=numFont)

    icon.save(PATH)
    return
