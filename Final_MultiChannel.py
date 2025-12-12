#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Final_MultiChannel
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
import math
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from xmlrpc.server import SimpleXMLRPCServer
import threading
import sip



class Final_MultiChannel(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Final_MultiChannel", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Final_MultiChannel")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Final_MultiChannel")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 9000000
        self.fsk_deviation = fsk_deviation = 4800
        self.deviation = deviation = 4000
        self.channel_rate = channel_rate = 48000
        self.baud_rate = baud_rate = 9600
        self.audio_decim = audio_decim = 4
        self.NOAA_gain = NOAA_gain = 0
        self.NOAA = NOAA = 1
        self.CH16_gain = CH16_gain = 0
        self.CH16 = CH16 = 0
        self.CH13_gain = CH13_gain = 0
        self.CH13 = CH13 = 0
        self.AIS_samp_rate = AIS_samp_rate = 250000

        ##################################################
        # Blocks
        ##################################################

        self.xmlrpc_server_0 = SimpleXMLRPCServer(('localhost', 8081), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(165000000, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(9000000, 0)
        self.uhd_usrp_source_0.set_gain(70, 0)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=36,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=36,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_1_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0_1_0 = filter.rational_resampler_ccc(
                interpolation=8,
                decimation=375,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=8,
                decimation=375,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=8,
                decimation=375,
                taps=[],
                fractional_bw=0)
        self.qtgui_sink_x_0_1_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            AIS_samp_rate, #bw
            "Og", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_1_0_0_win)
        self.qtgui_sink_x_0_1_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            AIS_samp_rate, #bw
            "Og", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_1_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Og", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "DSC", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)



        labels = ['DSC', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Channel 13", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['Channel 13', 'Channel 16', 'Channel 13', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "dark blue", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "NOAA", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['NOAA', 'Channel 16', 'Channel 13', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "dark blue", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            5,
            firdes.low_pass(
                1,
                AIS_samp_rate,
                12500,
                2000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            5,
            firdes.low_pass(
                1,
                AIS_samp_rate,
                12500,
                2000,
                window.WIN_HAMMING,
                6.76))
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_ff(
            digital.TED_MUELLER_AND_MULLER,
            5,
            0.045,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(
            digital.TED_MUELLER_AND_MULLER,
            5,
            0.045,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_multiply_const_vxx_1_1_0 = blocks.multiply_const_ff(CH13_gain)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(CH16_gain)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(NOAA_gain)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(5, (1/5), 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(5, (1/5), 4000, 1)
        self.blocks_freqshift_cc_6 = blocks.rotator_cc(2.0*math.pi*8.35e6/samp_rate)
        self.blocks_freqshift_cc_5 = blocks.rotator_cc(2.0*math.pi*8.475e6/samp_rate)
        self.blocks_freqshift_cc_4 = blocks.rotator_cc(2.0*math.pi*2.475e6/samp_rate)
        self.blocks_freqshift_cc_3 = blocks.rotator_cc(2.0*math.pi*2.525e6/samp_rate)
        self.blocks_freqshift_cc_0_0 = blocks.rotator_cc(2.0*math.pi*8200000/samp_rate)
        self.blocks_freqshift_cc_0 = blocks.rotator_cc(2.0*math.pi*2400000/samp_rate)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.audio_sink_0_0_1_0 = audio.sink(48000, '', True)
        self.audio_sink_0_0 = audio.sink(48000, '', True)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0_0_1_0 = analog.wfm_rcv(
        	quad_rate=192000,
        	audio_decimation=4,
        )
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=192000,
        	audio_decimation=4,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=192000,
        	audio_decimation=4,
        )
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf((channel_rate/(2*math.pi*fsk_deviation)))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((channel_rate/(2*math.pi*fsk_deviation)))
        self._NOAA_range = qtgui.Range(0, 1, 1, 1, 200)
        self._NOAA_win = qtgui.RangeWidget(self._NOAA_range, self.set_NOAA, "NOAA", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._NOAA_win)
        self._CH16_range = qtgui.Range(0, 1, 1, 0, 200)
        self._CH16_win = qtgui.RangeWidget(self._CH16_range, self.set_CH16, "CH16", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._CH16_win)
        self._CH13_range = qtgui.Range(0, 1, 1, 0, 200)
        self._CH13_win = qtgui.RangeWidget(self._CH13_range, self.set_CH13, "CH13", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._CH13_win)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.qtgui_sink_x_0, 'freq'), (self.uhd_usrp_source_0, 'command'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.analog_wfm_rcv_0_0_1_0, 0), (self.blocks_multiply_const_vxx_1_1_0, 0))
        self.connect((self.analog_wfm_rcv_0_0_1_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_sink_x_0_1_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_freqshift_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_freqshift_cc_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_freqshift_cc_3, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_freqshift_cc_4, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_freqshift_cc_5, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_freqshift_cc_6, 0), (self.rational_resampler_xxx_0_0_1_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.audio_sink_0_0_1_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_1_0, 0), (self.analog_wfm_rcv_0_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0_1_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_3, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_4, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_5, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_freqshift_cc_6, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Final_MultiChannel")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

        self.blocks_freqshift_cc_0.set_phase_inc(2.0 * math.pi * 2400000 / self.samp_rate)
        self.blocks_freqshift_cc_0_0.set_phase_inc(2.0 * math.pi * 8200000 / self.samp_rate)
        self.blocks_freqshift_cc_3.set_phase_inc(2.0 * math.pi * 2.525e6 / self.samp_rate)
        self.blocks_freqshift_cc_4.set_phase_inc(2.0 * math.pi * 2.475e6 / self.samp_rate)
        self.blocks_freqshift_cc_5.set_phase_inc(2.0 * math.pi * 8.475e6 / self.samp_rate)
        self.blocks_freqshift_cc_6.set_phase_inc(2.0 * math.pi * 8.35e6 / self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_fsk_deviation(self):
        return self.fsk_deviation

    def set_fsk_deviation(self, fsk_deviation):
        self.fsk_deviation = fsk_deviation
        self.analog_quadrature_demod_cf_0.set_gain((self.channel_rate/(2*math.pi*self.fsk_deviation)))
        self.analog_quadrature_demod_cf_0_0.set_gain((self.channel_rate/(2*math.pi*self.fsk_deviation)))

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation

    def get_channel_rate(self):
        return self.channel_rate

    def set_channel_rate(self, channel_rate):
        self.channel_rate = channel_rate
        self.analog_quadrature_demod_cf_0.set_gain((self.channel_rate/(2*math.pi*self.fsk_deviation)))
        self.analog_quadrature_demod_cf_0_0.set_gain((self.channel_rate/(2*math.pi*self.fsk_deviation)))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim

    def get_NOAA_gain(self):
        return self.NOAA_gain

    def set_NOAA_gain(self, NOAA_gain):
        self.NOAA_gain = NOAA_gain
        self.blocks_multiply_const_vxx_0.set_k(self.NOAA_gain)

    def get_NOAA(self):
        return self.NOAA

    def set_NOAA(self, NOAA):
        self.NOAA = NOAA

    def get_CH16_gain(self):
        return self.CH16_gain

    def set_CH16_gain(self, CH16_gain):
        self.CH16_gain = CH16_gain
        self.blocks_multiply_const_vxx_1.set_k(self.CH16_gain)

    def get_CH16(self):
        return self.CH16

    def set_CH16(self, CH16):
        self.CH16 = CH16

    def get_CH13_gain(self):
        return self.CH13_gain

    def set_CH13_gain(self, CH13_gain):
        self.CH13_gain = CH13_gain
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.CH13_gain)

    def get_CH13(self):
        return self.CH13

    def set_CH13(self, CH13):
        self.CH13 = CH13

    def get_AIS_samp_rate(self):
        return self.AIS_samp_rate

    def set_AIS_samp_rate(self, AIS_samp_rate):
        self.AIS_samp_rate = AIS_samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.AIS_samp_rate, 12500, 2000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.AIS_samp_rate, 12500, 2000, window.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0_1_0.set_frequency_range(0, self.AIS_samp_rate)
        self.qtgui_sink_x_0_1_0_0.set_frequency_range(0, self.AIS_samp_rate)




def main(top_block_cls=Final_MultiChannel, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
