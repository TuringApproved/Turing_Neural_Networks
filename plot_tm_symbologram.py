import matplotlib.pyplot
import itertools as itt

def plot_symbologram(ax, states, tape_symbols, ge_alpha):
    ge_n = ge_alpha.ge_n
    ge_q = ge_alpha.ge_q
    state_ticks_xpos = [ge_q.encode_string(state) for state in states]
    state_labels_xpos = [x + state_ticks_xpos[1]/2.0 for x in state_ticks_xpos]
    ax.set_xticks(sorted(state_ticks_xpos+state_labels_xpos))
    state_labels = [""]*len(ax.xaxis.get_major_ticks())
    state_labels[1::2] = ['$' + x + '$' for x in states]

    sym_ticks_xpos = [ge_alpha.encode_string([x[0],x[1]])
                      for x in itt.product(states, tape_symbols)]
    sym_labels_xpos = [x + sym_ticks_xpos[1]/2.0 for x in sym_ticks_xpos]
    ax.set_xticks(sorted(sym_ticks_xpos+sym_labels_xpos), minor=True)
    sym_labels_x = [""] * len(ax.xaxis.get_minor_ticks())
    sym_labels_x[1::2] = ['$' + x + '$'for x in tape_symbols*len(states)]

    ax.set_xticklabels(state_labels, size=20)
    ax.xaxis.set_tick_params(pad=20, length=10)
    ax.set_xticklabels(sym_labels_x, minor=True)

    for i, x in enumerate(ax.xaxis.get_major_ticks()):
        if i%2 == 1:
            x.tick1On = False
            x.tick2On = False

    for i, x in enumerate(ax.xaxis.get_minor_ticks()):
        if i%2 == 1:
            x.tick1On = False
            x.tick2On = False

    for xmaj in ax.xaxis.get_majorticklocs()[2::2]:
        ax.axvline(x=xmaj, ls="dotted", lw=1.5, c='black')
    for xmin in ax.xaxis.get_minorticklocs()[2::4]:
        ax.axvline(x=xmin, ls="dotted", lw=1, c='grey')

    sym_ticks_ypos = [ge_n.encode_string(x) for x in tape_symbols]
    sym_labels_ypos = [x + sym_ticks_ypos[1]/2.0 for x in sym_ticks_ypos]
    ax.set_yticks(sorted(sym_ticks_ypos+sym_labels_ypos))
    sym_labels_y = [""] * len(ax.yaxis.get_major_ticks())
    sym_labels_y[1::2] = ['$' + x + '$'for x in tape_symbols]

    ax.set_yticklabels(sym_labels_y, size=20)
    ax.yaxis.set_tick_params(pad=20, length=10)

    for i, x in enumerate(ax.yaxis.get_major_ticks()):
        if i%2 == 1:
            x.tick1On = False
            x.tick2On = False

    for ymaj in ax.yaxis.get_majorticklocs()[2::2]:
        ax.axhline(y=ymaj, ls="dotted", lw=1.5, c='black')

    return ax
