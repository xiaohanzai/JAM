#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : JAM/utils/util_fig.py
# Author            : Hongyu Li <lhy88562189@gmail.com>
# Date              : 29.09.2017
# Last Modified Date: 29.09.2017
# Last Modified By  : Hongyu Li <lhy88562189@gmail.com>
import matplotlib as mpl
from matplotlib import colors, colorbar
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
# from matplotlib import rc
# rc('mathtext', fontset='stix')
JAMPATH = os.environ.get('JAMPATH')
if JAMPATH is None:
    raise RuntimeError('Enviroment variable JAMPAHT must be set')
# from matplotlib.ticker import MaxNLocator
_cdict = {'red': ((0.000,   0.01,   0.01),
                  (0.170,   0.0,    0.0),
                  (0.336,   0.4,    0.4),
                  (0.414,   0.5,    0.5),
                  (0.463,   0.3,    0.3),
                  (0.502,   0.0,    0.0),
                  (0.541,   0.7,    0.7),
                  (0.590,   1.0,    1.0),
                  (0.668,   1.0,    1.0),
                  (0.834,   1.0,    1.0),
                  (1.000,   0.9,    0.9)),
          'green': ((0.000,   0.01,   0.01),
                    (0.170,   0.0,    0.0),
                    (0.336,   0.85,   0.85),
                    (0.414,   1.0,    1.0),
                    (0.463,   1.0,    1.0),
                    (0.502,   0.9,    0.9),
                    (0.541,   1.0,    1.0),
                    (0.590,   1.0,    1.0),
                    (0.668,   0.85,   0.85),
                    (0.834,   0.0,    0.0),
                    (1.000,   0.9,    0.9)),
          'blue': ((0.000,   0.01,   0.01),
                   (0.170,   1.0,    1.0),
                   (0.336,   1.0,    1.0),
                   (0.414,   1.0,    1.0),
                   (0.463,   0.7,    0.7),
                   (0.502,   0.0,    0.0),
                   (0.541,   0.0,    0.0),
                   (0.590,   0.0,    0.0),
                   (0.668,   0.0,    0.0),
                   (0.834,   0.0,    0.0),
                   (1.000,   0.9,    0.9))
          }

sauron = colors.LinearSegmentedColormap('sauron', _cdict)

ticks_font =\
    mpl.font_manager.FontProperties(fname='{}/utils/TimesNewRomanBold.ttf'
                                    .format(JAMPATH), size='small')

text_font =\
    mpl.font_manager.FontProperties(fname='{}/utils/TimesNewRomanBold.ttf'
                                    .format(JAMPATH), size='large')

ticks_font1 =\
    mpl.font_manager.FontProperties(fname='{}/utils/TimesNewRomanBold.ttf'
                                    .format(JAMPATH), size='x-small')

label_font =\
    mpl.font_manager.FontProperties(fname='{}/utils/TimesNewRomanBold.ttf'
                                    .format(JAMPATH), size='large')


nticks_font =\
    mpl.font_manager.FontProperties(size='small')

ntext_font =\
    mpl.font_manager.FontProperties(size='large')

nticks_font1 =\
    mpl.font_manager.FontProperties(size='x-small')

nlabel_font =\
    mpl.font_manager.FontProperties(size='large')


def set_labels(ax, x=True, y=True, xrotate=False,
               yrotate=False, font=ticks_font, xmax=None,
               ymax=None):
    for l in ax.get_xticklabels():
        if xrotate:
            l.set_rotation(xrotate)
        l.set_fontproperties(font)
    for l in ax.get_yticklabels():
        if yrotate:
            l.set_rotation(yrotate)
        l.set_fontproperties(font)
    if xmax is not None:
        ax.xaxis.set_major_locator(MaxNLocator(xmax))
    if ymax is not None:
        ax.yaxis.set_major_locator(MaxNLocator(ymax))


def equal_limits1(ax, lim=None):
    if lim is None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        lim = [min(xlim+ylim), max(xlim+ylim)]
    ax.set_aspect(1, adjustable='box', anchor='C')
    ax.set_xlim(lim[::-1])
    ax.set_ylim(lim)


def equal_limits(ax, lim=None, xreverse=True):
    if lim is None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        lim = [min(xlim+ylim), max(xlim+ylim)]
    if xreverse:
        ax.set_xlim(lim[::-1])
    else:
        ax.set_xlim(lim)
    ax.set_ylim(lim)
    fig = plt.gcf()
    pos = ax.get_position()
    # print pos.x0,pos.x1,pos.y0,pos.y1,pos.height,pos.width
    figsize = fig.get_size_inches()
    pysicalLength = min(pos.width*figsize[0], pos.height*figsize[1])
    width = pysicalLength/figsize[0]
    height = pysicalLength/figsize[1]
    npos = [pos.x0, pos.y0, width, height]
    ax.set_position(npos)


def add_colorbar(ax, cmap, norm, width=0.02, position='right',
                 barlabel='', fig=None, cmax=None, **kwargs):
    if fig is None:
        fig = plt.gcf()

    pos = ax.get_position()
    if position == 'right':
        axc = fig.add_axes([pos.x1, pos.y0, width, pos.height])
        colorbar.ColorbarBase(axc, orientation='vertical',
                              norm=norm, cmap=cmap)
        if cmax is not None:
            axc.yaxis.set_major_locator(MaxNLocator(cmax))
    elif position == 'left':
        axc = fig.add_axes([pos.x0-width, pos.y0, width, pos.height])
        colorbar.ColorbarBase(axc, orientation='vertical',
                              norm=norm, cmap=cmap)
        if cmax is not None:
            axc.yaxis.set_major_locator(MaxNLocator(cmax))
    elif position == 'top':
        axc = fig.add_axes([pos.x0, pos.y1, pos.width, width])
        colorbar.ColorbarBase(axc, orientation='horizontal',
                              norm=norm, cmap=cmap)
        for tick in axc.xaxis.get_major_ticks():
            tick.label1On = False
            tick.label2On = True
        if cmax is not None:
            axc.xaxis.set_major_locator(MaxNLocator(cmax))
    elif position == 'bottom':
        axc = fig.add_axes([pos.x0, pos.y0-width, pos.width, width])
        colorbar.ColorbarBase(axc, orientation='horizontal',
                              norm=norm, cmap=cmap)
        if cmax is not None:
            axc.xaxis.set_major_locator(MaxNLocator(cmax))
    set_labels(axc, font=ticks_font1)
    barlabelSize = kwargs.get('barlabelSize', 'x-small')
    axc.set_ylabel(barlabel, fontsize=barlabelSize)
