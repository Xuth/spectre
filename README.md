# spectre
python script to generate "strictly chiral aperiodic monotiles"

Summary

Over the years many sets of shapes have been found that will tile a surface only in an aperiodic manner.  The most well known set of shapes to do this are "Penrose Tiles".  However they all required multiple shapes to perform the tiling.  This "einstein" tile (play on the German words "ein" "stein" or "one stone") was something of a holy grail.  Earlier this year (2023) several researchers discovered one of these, an individual shape that could tile a surface in an aperiodic manner and over several months discovered many of them and satisfied various annoyances until they refined the shape to this one dubbed a "spectre" for its shape.  https://arxiv.org/abs/2305.17743

While I found several sources where people had traced shapes from various articles and research papers, I couldn't find a source for a computationally created vector file (ideally tiled) so that I could laser cut a bunch of them so that I could play with them.  So I wrote a python script to write an SVG file for me.  The python script in this project generates an SVG file is of 32 spectre tiles at 10mm per edge of the shape that will fit in a 200mm x 200mm (8" x 8") square.


To run this just call run "python spectre.py".

The other two python files are two library files that I've written over the years, one implements a two dimensional interval tree (designed to allow me to efficiently find intersecting rectangles but it works here to help find overlapping line segments) and the other implements a simplified turtle without actually creating any graphics.  The SVG image is just "hand written" in spectre.py without any additional tools since it's just a simple xml file with only one type of line segment repeated hundreds of times.
