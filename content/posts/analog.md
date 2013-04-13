Title: Roll Your Own Analog Input
tags: analog, input
date: 17-04-2013


Modern computers are inherently digital devices. However, we live in a decidedly analog world, so many systems (including systems on a chip) have methods to generate and read different analog quantities.
Modern computers are inherently digital devices. They work with ones and zeros (although that hasn't always been the case). However, we live in a decidedly analog world, so many systems (including systems on a chip) have methods to generate and read different analog quantities.

I've mentioned it before, but these conversions usually take some form of my old algebra teacher's maxim: Take what you know and use it to figure out what you don't know. Granted, these days you typically buy analog inputs and outputs ready-made, possibly as part of your CPU, even. It can still be useful to understand how they work. In addition to theory, I'll show you a few simple Arduino-based demonstrations you can try.

There are many ways to coax a variable voltage output from a digital device. The classic method is to use an R2R network (see image below). The idea is that each bit contributes to the total output voltage (in this case, four bits)
