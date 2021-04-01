import pandas as pd
from IPython.display import display
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pprint
import re


general_ledger = pd.read_csv('31-01-2021-Balancete-Miniera_CSV.csv')

general_ledger.style
display(general_ledger)
