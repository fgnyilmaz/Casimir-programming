from email.policy import default
from typing import Dict
import numpy as np
from math import *
from qiskit_metal import draw
from re import sub

default_options = Dict(
    pocket_width='800um',
    pocket_height='900um',
)

def make(self):
    """Define the way the options are turned into QGeometry."""

    self.make_pocket()

def make_pocket(self):
    # self.p allows us to directly access parsed values (string -> numbers) form the user option
    p = self.p

# Draw the pocket
rect_pk = draw.rectangle(p.pocket_width, p.pocket_height)