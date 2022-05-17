import fontforge
import json

BASE_FONTS_MAP = {
    './Times New Roman/times new roman.ttf': 'TimesNewScrambled',
    # './Times New Roman/times new roman italic.ttf': 'TimesNewScrambledItalic',
    # './Times New Roman/times new roman bold.ttf': 'TimesNewScrambledBold',
    # './Times New Roman/times new roman bold italic.ttf': 'TimesNewScrambledBoldItalic',
}

DEST_FONT_SUBDIR = 'Times New Scrambled'

# import random
# a = list(reversed(string.ascii_uppercase+string.ascii_lowercase))
# random.shuffle(a)
# SCRAMBLE_MAP = dict(zip(string.ascii_uppercase+string.ascii_lowercase, a))
with open('scramble_map.json') as scramble_map_file:
    SCRAMBLE_MAP = json.load(scramble_map_file)


if __name__=='__main__':
    for base_font_path, dest_font_name in BASE_FONTS_MAP.items():
        base_font = fontforge.open(base_font_path)
        dest_font = fontforge.font()

        for src_glyph, dest_glyph in SCRAMBLE_MAP.items():
            base_font.selection.select(src_glyph)
            base_font.copy()
            dest_font.selection.select(dest_glyph)
            dest_font.paste()

        for src_glyph, _ in SCRAMBLE_MAP.items():
            dest_font.selection.select(src_glyph)
            dest_font.copy()
            base_font.selection.select(src_glyph)
            base_font.paste()

        base_font.fontname = dest_font_name
        base_font.fullname = dest_font_name
        base_font.sfnt_names = (('English (US)', 'Copyright', f'{dest_font_name} © The Monotype Cprporation plc. Data © The Monotype Corporation plc/Type Solutions Inc 1990 - 1992. All Rights Reserved.'), ('English (US)', 'Family', f'{dest_font_name}'), ('English (US)', 'SubFamily', 'Regular'), ('English (US)', 'UniqueID', f'Monotype: {dest_font_name}:version1(Microsoft)'), ('English (US)', 'Fullname', 'TimesNewScrambled'), ('English (US)', 'Version', 'Version 1.0 - November 1992'), ('English (US)', 'PostScriptName', 'TimesNewScrambled'), ('English (US)', 'Trademark', f'{dest_font_name} ® Trademark of The Monotype Corporation plc registered in the US Pat & TM Off. and elsewhere.'), ('Czech', 'SubFamily', 'obyčejné'), ('Czech', 'Fullname', f'{dest_font_name}'), ('German German', 'SubFamily', 'Standard'), ('German German', 'Fullname', f'{dest_font_name}'), ('Hungarian', 'SubFamily', 'Normál'), ('Hungarian', 'Fullname', f'{dest_font_name}'), ('Polish', 'SubFamily', 'Normalny'), ('Polish', 'Fullname', f'{dest_font_name}'))
        # breakpoint()
        base_font.generate(dest_font_name + '.ttf')
