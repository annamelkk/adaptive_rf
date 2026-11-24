/*
 * This code connects to Pluto, locates the on board
 * chip phy and streaming devices, and sets the RX local oscillator
 * frequency
*/

#include <iio.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  // basically set device communication context orinak ip, usb address idk 
  struct iio_context *ctx = iio_create_context_from_uri("ip:192.168.2.1");
  if (!ctx)
  {
    fprintf(stderr, "Error, unable to create context. \n");
    return EXIT_FAILURE;
  }

  // after succ setting context parse the control deivce ie phy
  struct iio_device *phy = iio_context_find_device(ctx, "ad9361-phy");
  if (!phy)
  {
    fprintf(stderr, "phy device not found. \n");
    iio_context_destroy(ctx);
    return EXIT_FAILURE;
  }

  // - take what struct to search for deivce
  // - altvoltage0 for RF or clock signals, contorls oscillators
  //   voltage0 is for discrete ADC/DAC that carry IQ data samples
  // - true for out channels, false for input channels
  struct iio_channel *rx_lo = iio_device_find_channel(phy, "altvoltage0", true);
  if (rx_lo)
  {
    iio_channel_attr_write_longlong(rx_lo, "frequency", 2440000000LL); // 2.44 GHz as in simulations in GNU Radio
    long long current_freq = 0;
    iio_channel_attr_read_longlong(rx_lo, "frequency", &current_freq);
    printf("RX LO freq set to: %lld Hz \n", current_freq);
  }

  struct iio_device *rx_dev = iio_context_find_device(ctx, "cf-ad9361-lpc");
  if (rx_dev) printf("located RX streaming device : %s\n", iio_device_get_name(rx_dev));

  iio_context_destroy(ctx);
  return EXIT_SUCCESS;
}

// tasks for after
// Build a Python baseline link at 1–2 MSPS (e.g., QPSK burst framing with preamble + SNR estimator) so you have a working baseline before introducing adaptation.
// Port the TX/RX loop and adaptive controller to C once switching thresholds (SNR/PER triggers for modulation fallback or frequency hopping) are proven.
