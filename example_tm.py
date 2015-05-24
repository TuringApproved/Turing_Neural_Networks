import NDA
import NeuralTM as nTM
import matplotlib.pyplot as plt
from plot_tm_symbologram import plot_symbologram

tape_symbols = ["\sqcup", "1"]
states = ["q_{acc}", "q_{rej}", "q_{even}", "q_{odd}"]
tm_descr = {("q_{even}", "1"): ("q_{odd}", "1", "R"),
            ("q_{even}", "\sqcup"): ("q_{acc}", "\sqcup", "L"),
            ("q_{odd}", "1"): ("q_{even}", "1", "R"),
            ("q_{odd}", "\sqcup"): ("q_{rej}", "\sqcup", "L"),
            ("q_{acc}", "1"): ("q_{acc}", "1", "S"),
            ("q_{acc}", "\sqcup"): ("q_{acc}", "\sqcup", "S"),
            ("q_{rej}", "1"): ("q_{rej}", "1", "S"),
            ("q_{rej}", "\sqcup"): ("q_{rej}", "\sqcup", "S")}

ge_q = NDA.GodelEncoder(states)
ge_n = NDA.GodelEncoder(tape_symbols)

ge_alpha = NDA.alphaGodelEncoder(ge_q, ge_n)
ge_beta = ge_n

init_state = ge_alpha.encode_string(["q_{even}", "\sqcup"])
init_tape = ge_n.encode_string(list("111"))

tm_gs = NDA.TMGeneralizedShift(states, tape_symbols, tm_descr)
nda = NDA.NonlinearDynamicalAutomaton(tm_gs, ge_alpha, ge_beta)
tm_nn = nTM.NeuralTM(nda.flow_params_x, nda.flow_params_y)

nda_states = nda.iterate(init_state, init_tape, 10)
tm_nn_states = tm_nn.run_net(init_x=init_state, init_y=init_tape,
                           n_iterations=10)

plt.ion()
fig = plt.figure(figsize=[5,5])
ax2 = plt.axes(aspect="equal")
ax2.axis([0, 1, 0, 1])

plot_symbologram(ax2, states, tape_symbols, ge_alpha)

x_states, y_states = zip(*tm_nn_states)
ax2.plot(x_states, y_states, linestyle="", marker=".", ms=10)

states_old = None
for i, tm_nn_state in enumerate(tm_nn_states):y

    if tm_nn_state == states_old:
        break

    ax2.annotate("{}".format(i+1),
                 xy = tm_nn_state, 
                 xytext= (tm_nn_state[0]-0.03, 
                          tm_nn_state[1]+0.01), 
                 size=15)

    states_old = tm_nn_state

ax2.set_xlabel("$c_x$ activation", size=15)
ax2.set_ylabel("$c_y$ activation", size=15)
plt.tight_layout()
plt.savefig("string_rej.pdf")

print "total number of neurons: {}".format(tm_nn.LTL.n_units +
                                           tm_nn.BSLbx.n_units +
                                           tm_nn.BSLby.n_units +
                                           tm_nn.MCLx.n_units +
                                           tm_nn.MCLy.n_units + 
                                           1)

