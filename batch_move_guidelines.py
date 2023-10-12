#!/usr/bin/env python
# coding=utf-8

# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/inkscape_batch_guides

import sys
import inkex
from inkex import EffectExtension


# for debug output
def eprint(*args, **kwargs):
    # print to stderr
    print(*args, file=sys.stderr, **kwargs)


class Guidelines(EffectExtension):

    def effect(self):
        # main method for Effect action
        for guide in self.guides(direction=self.options.guide_direction):
            if inkex.__version__[:3] == '1.2':
                # inkscape v 1.2
                guide.move_to(
                    pos_x=guide.point.x + (self.options.offset if guide.is_vertical else 0.0),
                    pos_y=guide.point.y - (self.options.offset if guide.is_horizontal else 0.0)
                )
            else:
                # inkscape v 1.3
                guide.set_position(
                    pos_x=guide.position.x + (self.options.offset if guide.is_vertical else 0.0),
                    pos_y=guide.position.y + (self.options.offset if guide.is_horizontal else 0.0)
                )

    def guides(self, direction: str = None):
        # get guides by direction ['vertical', 'horizontal', None]
        if direction == 'vertical':
            return (guide for guide in self.svg.namedview.get_guides() if guide.is_vertical)
        elif direction == 'horizontal':
            return (guide for guide in self.svg.namedview.get_guides() if guide.is_horizontal)
        else:
            return self.svg.namedview.get_guides()

    def add_arguments(self, pars):
        # parse arguments from the UI
        pars.add_argument(
            '--offset',
            type=float,
            default=0.0,
            help='Offset'
        )
        pars.add_argument(
            '--guide_direction',
            type=str,
            default='vertical',
            help='Guide Direction'
        )


if __name__ == '__main__':
    Guidelines().run()
