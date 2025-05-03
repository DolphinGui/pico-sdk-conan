#!/usr/bin/sh

openocd -s debugscripts -f interface/cmsis-dap.cfg -f interface/rp2350.cfg -c "adapter speed 5000"
