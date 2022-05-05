from app import proceed
from constant import TEST_FUNCTIONS

for fx in TEST_FUNCTIONS:
    proceed(fx["function"], fx["x_min"], fx["x_max"])
