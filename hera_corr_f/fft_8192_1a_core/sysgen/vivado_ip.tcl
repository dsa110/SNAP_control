#-----------------------------------------------------------------
# System Generator version 2016.4 IP Tcl source file.
#
# Copyright(C) 2013 by Xilinx, Inc.  All rights reserved.  This
# text/file contains proprietary, confidential information of Xilinx,
# Inc., is distributed under license from Xilinx, Inc., and may be used,
# copied and/or disclosed only pursuant to the terms of a valid license
# agreement with Xilinx, Inc.  Xilinx hereby grants you a license to use
# this text/file solely for design, simulation, implementation and
# creation of design files limited to Xilinx devices or technologies.
# Use with non-Xilinx devices or technologies is expressly prohibited
# and immediately terminates your license unless covered by a separate
# agreement.
#
# Xilinx is providing this design, code, or information "as is" solely
# for use in developing programs and solutions for Xilinx devices.  By
# providing this design, code, or information as one possible
# implementation of this feature, application or standard, Xilinx is
# making no representation that this implementation is free from any
# claims of infringement.  You are responsible for obtaining any rights
# you may require for your implementation.  Xilinx expressly disclaims
# any warranty whatsoever with respect to the adequacy of the
# implementation, including but not limited to warranties of
# merchantability or fitness for a particular purpose.
#
# Xilinx products are not intended for use in life support appliances,
# devices, or systems.  Use in such applications is expressly prohibited.
#
# Any modifications that are made to the source code are done at the user's
# sole risk and will be unsupported.
#
# This copyright and support notice must be retained as part of this
# text at all times.  (c) Copyright 1995-2013 Xilinx, Inc.  All rights
# reserved.
#-----------------------------------------------------------------

set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i0] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i0
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i0}
lappend params_list CONFIG.algorithm {Minimum_Area}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_RAM}
lappend params_list CONFIG.operating_mode_a {READ_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {8kx2}
lappend params_list CONFIG.read_width_a {144}
lappend params_list CONFIG.read_width_b {144}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {144}
lappend params_list CONFIG.write_width_b {144}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i0_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i0]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i0] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i0
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i0}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {19}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {19}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {19}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i0]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i1] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i1
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i1}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {21}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {21}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {21}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i1]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i2] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i2
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i2}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {19}
lappend params_list CONFIG.Add_Mode {Subtract}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {19}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {19}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i2]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i1] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i1
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i1}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {9}
lappend params_list CONFIG.read_width_b {9}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {9}
lappend params_list CONFIG.write_width_b {9}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i1_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i1]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i2] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i2
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i2}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_RAM}
lappend params_list CONFIG.operating_mode_a {READ_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {36}
lappend params_list CONFIG.read_width_b {36}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {36}
lappend params_list CONFIG.write_width_b {36}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i2_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i2]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i0] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i0
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i0}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {10}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i0]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i3] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i3
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i3}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {9}
lappend params_list CONFIG.read_width_b {9}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {9}
lappend params_list CONFIG.write_width_b {9}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i3_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i3]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i4] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i4
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i4}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {9}
lappend params_list CONFIG.read_width_b {9}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {9}
lappend params_list CONFIG.write_width_b {9}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i4_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i4]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i3] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i3
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i3}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {15}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {15}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {15}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i3]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i4] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i4
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i4}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {23}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {23}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {23}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i4]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i5] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i5
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i5}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {22}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {22}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {false}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {0}
lappend params_list CONFIG.Out_Width {22}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i5]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i6] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i6
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i6}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {39}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {39}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {39}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i6]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i5] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i5
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i5}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {36}
lappend params_list CONFIG.read_width_b {36}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {512}
lappend params_list CONFIG.write_width_a {36}
lappend params_list CONFIG.write_width_b {36}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i5_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i5]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i7] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i7
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i7}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Unsigned}
lappend params_list CONFIG.A_Width {3}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Unsigned}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {3}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {false}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {0}
lappend params_list CONFIG.Out_Width {3}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i7]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i1] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i1
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i1}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {2}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i1]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i8] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i8
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i8}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {16}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {16}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {16}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i8]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i2] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i2
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i2}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {9}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i2]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i9] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i9
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i9}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {18}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {18}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {18}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i9]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i10] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i10
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i10}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {35}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {35}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {35}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i10]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i0] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i0
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i0}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {18}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {16}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {dual_port_ram}
lappend params_list CONFIG.output_options {non_registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {false}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i0_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i0]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i3] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i3
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i3}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {8}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i3]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i11] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i11
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i11}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {36}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {36}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {36}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i11]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i1] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i1
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i1}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {18}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {16}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {dual_port_ram}
lappend params_list CONFIG.output_options {non_registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {false}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i1_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i1]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i4] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i4
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i4}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {7}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i4]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i12] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i12
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i12}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {20}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {20}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {20}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i12]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i13] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i13
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i13}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {37}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {37}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {37}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i13]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i2] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i2
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i2}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {18}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {16}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {dual_port_ram}
lappend params_list CONFIG.output_options {non_registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {false}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i2_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i2]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i5] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i5
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i5}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {6}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i5]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_addsub_v12_0_i14] < 0} {
create_ip -name c_addsub -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_addsub_v12_0_i14
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_addsub_v12_0_i14}
lappend params_list CONFIG.AINIT_Value {0}
lappend params_list CONFIG.A_Type {Signed}
lappend params_list CONFIG.A_Width {38}
lappend params_list CONFIG.Add_Mode {Add}
lappend params_list CONFIG.B_Constant {false}
lappend params_list CONFIG.B_Type {Signed}
lappend params_list CONFIG.B_Value {0}
lappend params_list CONFIG.B_Width {38}
lappend params_list CONFIG.Borrow_Sense {Active_Low}
lappend params_list CONFIG.Bypass {false}
lappend params_list CONFIG.Bypass_CE_Priority {Bypass_Overrides_CE}
lappend params_list CONFIG.Bypass_Sense {Active_Low}
lappend params_list CONFIG.CE {true}
lappend params_list CONFIG.C_In {false}
lappend params_list CONFIG.C_Out {false}
lappend params_list CONFIG.Implementation {Fabric}
lappend params_list CONFIG.Latency {1}
lappend params_list CONFIG.Out_Width {38}
lappend params_list CONFIG.SCLR {false}
lappend params_list CONFIG.SINIT {false}
lappend params_list CONFIG.SINIT_Value {0}
lappend params_list CONFIG.SSET {false}
lappend params_list CONFIG.Sync_CE_Priority {Sync_Overrides_CE}
lappend params_list CONFIG.Sync_Ctrl_Priority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_addsub_v12_0_i14]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i3] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i3
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i3}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {18}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {dual_port_ram}
lappend params_list CONFIG.output_options {non_registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {false}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i3_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i3]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i6] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i6
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i6}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {5}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i6]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i6] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i6
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i6}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {36}
lappend params_list CONFIG.read_width_b {36}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {64}
lappend params_list CONFIG.write_width_a {36}
lappend params_list CONFIG.write_width_b {36}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i6_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i6]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i7] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i7
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i7}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {4}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i7]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i7] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i7
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i7}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {36}
lappend params_list CONFIG.read_width_b {36}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {128}
lappend params_list CONFIG.write_width_a {36}
lappend params_list CONFIG.write_width_b {36}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i7_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i7]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i8] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i8
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i8}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {true}
lappend params_list CONFIG.output_width {3}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i8]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_blk_mem_gen_v8_3_i8] < 0} {
create_ip -name blk_mem_gen -version 8.3 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_blk_mem_gen_v8_3_i8
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_blk_mem_gen_v8_3_i8}
lappend params_list CONFIG.algorithm {Fixed_Primitives}
lappend params_list CONFIG.assume_synchronous_clk {false}
lappend params_list CONFIG.byte_size {9}
lappend params_list CONFIG.collision_warnings {ALL}
lappend params_list CONFIG.disable_collision_warnings {false}
lappend params_list CONFIG.ecc {false}
lappend params_list CONFIG.enable_a {Use_ENA_Pin}
lappend params_list CONFIG.enable_b {Always_Enabled}
lappend params_list CONFIG.error_injection_type {Single_Bit_Error_Injection}
lappend params_list CONFIG.fill_remaining_memory_locations {false}
lappend params_list CONFIG.load_init_file {TRUE}
lappend params_list CONFIG.memory_type {Single_Port_ROM}
lappend params_list CONFIG.operating_mode_a {WRITE_FIRST}
lappend params_list CONFIG.operating_mode_b {WRITE_FIRST}
lappend params_list CONFIG.output_reset_value_a {0}
lappend params_list CONFIG.output_reset_value_b {0}
lappend params_list CONFIG.pipeline_stages {0}
lappend params_list CONFIG.primitive {512x36}
lappend params_list CONFIG.read_width_a {36}
lappend params_list CONFIG.read_width_b {36}
lappend params_list CONFIG.register_porta_output_of_memory_core {false}
lappend params_list CONFIG.register_porta_output_of_memory_primitives {true}
lappend params_list CONFIG.register_portb_output_of_memory_core {false}
lappend params_list CONFIG.register_portb_output_of_memory_primitives {false}
lappend params_list CONFIG.remaining_memory_locations {0}
lappend params_list CONFIG.reset_type {SYNC}
lappend params_list CONFIG.use_byte_write_enable {false}
lappend params_list CONFIG.use_error_injection_pins {false}
lappend params_list CONFIG.use_regcea_pin {false}
lappend params_list CONFIG.use_regceb_pin {false}
lappend params_list CONFIG.use_rsta_pin {false}
lappend params_list CONFIG.use_rstb_pin {false}
lappend params_list CONFIG.write_depth_a {256}
lappend params_list CONFIG.write_width_a {36}
lappend params_list CONFIG.write_width_b {36}
lappend params_list CONFIG.coe_file {../fft_8192_1a_core_blk_mem_gen_v8_3_i8_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_blk_mem_gen_v8_3_i8]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i4] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i4
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i4}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i4_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i4]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i5] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i5
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i5}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {16}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {dual_port_ram}
lappend params_list CONFIG.output_options {non_registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {false}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i5_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i5]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i6] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i6
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i6}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i6_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i6]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i7] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i7
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i7}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i7_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i7]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i8] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i8
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i8}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i8_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i8]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i9] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i9
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i9}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i9_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i9]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i10] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i10
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i10}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i10_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i10]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i11] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i11
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i11}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i11_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i11]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i12] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i12
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i12}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i12_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i12]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i13] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i13
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i13}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i13_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i13]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i14] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i14
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i14}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i14_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i14]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i15] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i15
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i15}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i15_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i15]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i16] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i16
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i16}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i16_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i16]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i17] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i17
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i17}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i17_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i17]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i18] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i18
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i18}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i18_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i18]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_dist_mem_gen_v8_0_i19] < 0} {
create_ip -name dist_mem_gen -version 8.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_dist_mem_gen_v8_0_i19
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_dist_mem_gen_v8_0_i19}
lappend params_list CONFIG.ce_overrides {sync_controls_overrides_ce}
lappend params_list CONFIG.common_output_ce {false}
lappend params_list CONFIG.common_output_clk {false}
lappend params_list CONFIG.data_width {36}
lappend params_list CONFIG.default_data {0}
lappend params_list CONFIG.default_data_radix {16}
lappend params_list CONFIG.depth {32}
lappend params_list CONFIG.dual_port_address {non_registered}
lappend params_list CONFIG.dual_port_output_clock_enable {false}
lappend params_list CONFIG.input_clock_enable {false}
lappend params_list CONFIG.input_options {non_registered}
lappend params_list CONFIG.memory_type {rom}
lappend params_list CONFIG.output_options {registered}
lappend params_list CONFIG.qualify_we_with_i_ce {false}
lappend params_list CONFIG.reset_qdpo {false}
lappend params_list CONFIG.reset_qspo {false}
lappend params_list CONFIG.single_port_output_clock_enable {true}
lappend params_list CONFIG.sync_reset_qdpo {false}
lappend params_list CONFIG.sync_reset_qspo {false}
lappend params_list CONFIG.coefficient_file {../fft_8192_1a_core_dist_mem_gen_v8_0_i19_vivado.coe}

set_property -dict $params_list [get_ips fft_8192_1a_core_dist_mem_gen_v8_0_i19]
}


set existingipslist [get_ips]
if {[lsearch $existingipslist fft_8192_1a_core_c_counter_binary_v12_0_i9] < 0} {
create_ip -name c_counter_binary -version 12.0 -vendor xilinx.com -library ip -module_name fft_8192_1a_core_c_counter_binary_v12_0_i9
set params_list [list]
lappend params_list CONFIG.Component_Name {fft_8192_1a_core_c_counter_binary_v12_0_i9}
lappend params_list CONFIG.ainit_value {0}
lappend params_list CONFIG.ce {true}
lappend params_list CONFIG.count_mode {DOWN}
lappend params_list CONFIG.fb_latency {0}
lappend params_list CONFIG.final_count_value {1}
lappend params_list CONFIG.implementation {Fabric}
lappend params_list CONFIG.increment_value {1}
lappend params_list CONFIG.latency {1}
lappend params_list CONFIG.load {false}
lappend params_list CONFIG.output_width {3}
lappend params_list CONFIG.restrict_count {false}
lappend params_list CONFIG.sclr {false}
lappend params_list CONFIG.sinit {true}
lappend params_list CONFIG.sinit_value {0}
lappend params_list CONFIG.sset {false}
lappend params_list CONFIG.sync_ce_priority {Sync_Overrides_CE}
lappend params_list CONFIG.sync_threshold_output {false}
lappend params_list CONFIG.syncctrlpriority {Reset_Overrides_Set}

set_property -dict $params_list [get_ips fft_8192_1a_core_c_counter_binary_v12_0_i9]
}


validate_ip [get_ips]
