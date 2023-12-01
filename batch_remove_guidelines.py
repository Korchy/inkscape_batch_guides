#!/usr/bin/env python
# coding=utf-8

# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/inkscape_batch_guides

import sys
from inkex import EffectExtension


# for debug output
def eprint(*args, **kwargs):
    # print to stderr
    print(*args, file=sys.stderr, **kwargs)


class BatchRemoveGuidelines(EffectExtension):

    def effect(self):
        # main method for Effect action
        for guide in self.guides(direction=self.options.guide_direction):
            guide.delete()

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
            '--guide_direction',
            type=str,
            default='all',
            help='Guide Direction'
        )


if __name__ == '__main__':
    BatchRemoveGuidelines().run()
