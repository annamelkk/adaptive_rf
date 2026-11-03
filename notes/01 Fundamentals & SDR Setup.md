
The system consists of a transmitter and receiver. There needs to be some kind of communication ingrained for decision making. 
Decision making process takes into account a set of pre-defined parameters, which can be the same for both modems or a characteristic of a single modem, and adapts to this set.

### QAM

- [ ] BPSK
	- [File transfer using BPSK](https://wiki.gnuradio.org/index.php?title=File_transfer_using_Packet_and_BPSK)
- [ ] QPSK
- [ ] 16QAM
- [ ] 64QAM

### List of parameters considered for decision making

- Distance
- Frequency offset
- Phase offset

### Forward Error Correction

- Hamming 4/3 Bell Labs
- Reed - Solomon
- Turbo Codes

### To Do

- [ ] Implement modulation schemes on hardware
- [ ] Separate different channel qualities by their parameters, eg bad channel means large distance, large offsets
- [ ] Research FEC
- [ ] Initial system archiecture
