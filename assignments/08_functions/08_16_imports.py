# import the entire module
import printing_functions

# import specific functions
from printing_functions import print_models, show_completed_models

# import with aliases
import printing_functions as pf
from printing_functions import print_models as pm

# examples
unprinted_designs = ['keychain', 'bracelet', 'bottle opener']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
