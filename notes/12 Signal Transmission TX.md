Signal Transmission Steps
1. Modulate
2. Tune
3. Filter

**Q1** There are several types of filters used in GNU Radio wiki for modulation and demodulation examples: FFT Root Raised Cosine filter OR Decimating FIR filter with taps defined to RRC taps. When do we use each of those? 

According to google FIR filter is doing the filtering in time domain, compared to FFT filter which is doing the filtering after transforming everything to frequency domain. Tap counts also play a role, FFT is used for large tap count and small to moderate tap counts are filtered using FIR filter.



4. Send