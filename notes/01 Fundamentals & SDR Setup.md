 

### QPSK and BPSK

A raised cosine pulse is given by the following formula:
$$p(t) = \frac{\sin(\frac{\pi t}{T_s})}{\pi t/T_s} \ \frac{\cos t(\frac{\pi \alpha t}{T_s})}{1 - \alpha^2t^2/T_s^2}$$Here $\alpha$ is the Roll-off Factor which controls the excess BW, $\alpha \in [0,1]$. When $\alpha = 0$ yields the narrowest bandwidth, and $\alpha = 1$ yields to wider bandwidth.

For a raised-cosine spectrum, the occupied bandwidth is approximately $$B = \frac{1 + \alpha}{2T_s}$$
ISI (inter-symbol interference)

**Q1** From my understanding we use this pulse shaping techniques to reduce out of band emissions and not interfere with adjacent channels. Rectangular signals used for PSK have sinc-shaped spectrum. So, we use the root raised cosine filter at each node (TX RX) to reduce the spectrum. I imagine wed need to agree on some parameters for both nodes for this to work properly. How does the synchronization happen here?