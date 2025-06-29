"""
Tools package for the reasoning script.
Contains mathematical and string analysis tools.
"""

from .math_tools import MATH_TOOLS
from .string_tools import STRING_TOOLS

# Combined tool registry
ALL_TOOLS = {**MATH_TOOLS, **STRING_TOOLS} 