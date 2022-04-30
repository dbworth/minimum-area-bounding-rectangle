#!/usr/bin/python

# Test program to find minimum-area bounding rectangle
#
# Un-comment one of the arrays to test with a rectangle or 5-point polygon
# Some solutions to this problem will fail with simple shapes!
#
# Tested with Python 2.6.5 on Ubuntu 10.04.4
# Results verified using Matlab

# Copyright (c) 2013, David Butterworth, University of Queensland
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Willow Garage, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from numpy import *

from qhull_2d import *
from min_bounding_rect import *

if __name__ == "__main__":
    #
    # Un-comment one of these shapes below:
    #

    # Square
    # xy_points = 10*array([(x,y) for x in arange(10) for y in arange(10)])

    # Random points
    # xy_points = 100*random.random((32,2))

    # A rectangle
    # xy_points = array([ [0,0], [1,0], [1,2], [0,2], [0,0] ])

    # A rectangle, with 5th outlier
    v = [
        [282.15683092396523, 223.11512640953208],
        [282.6740563777786, 200.61399296154428],
        [248.98051148730354, 199.7099293962484],
        [248.46328600395807, 217.4898437932211],
        [229.3259436222214, 273.2403900872115],
        [261.3200334037592, 284.18959062917554],
        [282.15683092396523, 223.11512640953208],
    ]

    xy_points = array(v)

    # --------------------------------------------------------------------------#

    # Find convex hull
    hull_points = qhull2D(xy_points)

    # Reverse order of points, to match output from other qhull implementations
    hull_points = hull_points[::-1]

    print("Convex hull points: \n", hull_points, "\n")

    # Find minimum area bounding rectangle
    (rot_angle, area, width, height, center_point, corner_points) = minBoundingRect(
        hull_points
    )

    print("Minimum area bounding box:")
    print("Rotation angle:", rot_angle, "rad  (", rot_angle * (180 / math.pi), "deg )")
    print("Width:", width, " Height:", height, "  Area:", area)
    print("Center point: \n", center_point)  # numpy array
    print("Corner points: \n", corner_points, "\n")  # numpy array
