import pandas as pd
import pickle
import re
import os
from numpy import *

""" The 20 features used in this package are elemental properties from the CRC Handbook of Chemistry and Physics
as well as the NIST X-ray Mass Attenuation Coefficients Database.


CRC Handbook of Chemistry and Physics
Features that are currently available are the number of 4f electrons ('4f'),
number of 5d electrons ('5d'), combined number of 4f and 5d electrons ('add4f5d'),
absolute value of the difference of number of 4f and 5d electrons ('sub4f5dabs'),
number of electrons('allelectrons'), number of valence outer shell electrons ('val_e'),
atomic number ('atomicnumber'), atomic weight ('atomicweight'), first ionization energy ('ionenergy'),
Pauling electronegativity of most common oxidation state ('el_neg_chi'), van der Waals radius ('R_vdw_element'),
covalent radius ('R_cov_element'), atomic number to mass number ratio ('zaratio'),
excitation energy ('ex_energy'), period ('period'), and elemental density ('density').

NIST X-ray Mass Attenuation Coefficients Database for features at 662 keV
Gamma ray features are also included at 662 keV. They include the following:
coherent scattering coefficient ('co_scatt'), incoherent scattering coefficient ('inco_scatt'),
photoelectric absorption ('pe_abs'), coherent attenutation coefficient ('atten_co'), and the
incoherent attenutation coefficient ('atten_inco')."""

#Setting up the pickle import.
my_dir=os.path.dirname(__file__)
elementalfeature=['4f','5d', 'add4f5d', 'sub4f5dabs', 'allelectrons', 'val_e','atomicnumber', 'atomicweight', 'ionenergy','el_neg_chi', 'R_vdw_element', 'R_cov_element', 'co_scatt', 'inco_scatt', 'pe_abs', 'atten_co', 'atten_inco', 'zaratio', 'ex_energy', 'density','period']
d={}
for inputdict in elementalfeature:
    pickle_file_path=os.path.join(my_dir, inputdict + '.p')
    d[inputdict]=pickle.load(open(pickle_file_path, 'rb'))
keys, values=d.keys(), d.values()


#From the molecular weight python example and AtomicAverage code
def find_closing_paren(tokens):
    count = 0
    for index, tok in enumerate(tokens):
        if tok == ')':
            count -= 1
            if count == 0:
                return index
        elif tok == '(':
            count += 1
    raise ValueError('unmatched parentheses')

def howmany(tokens, stack):
    """Returns the number of atoms in a given chemical formula."""
    if len(tokens) == 0:
        return sum(stack)
    tok = tokens[0]
    if tok == '(':
        end = find_closing_paren(tokens)
        stack.append(howmany(tokens[1:end], []))
        return howmany(tokens[end + 1:], stack)
    elif not tok.isalpha():
        stack[-1] *= float(tok)
    else:
        stack.append(1)
    return howmany(tokens[1:], stack)

def total(tokens, stack, feature):
    """Returns the feature total for a given chemical formula."""
    if len(tokens) == 0:
        return sum(stack)
    tok = tokens[0]
    if tok == '(':
        end = find_closing_paren(tokens)
        stack.append(total(tokens[1:end], [],feature))
        return total(tokens[end + 1:], stack,feature)
    elif not tok.isalpha():
        stack[-1] *= float(tok)
    else:
        stack.append(d[feature][tok])
    return total(tokens[1:], stack, feature)



class chem_calc:
    def __init__(self, formula, feature = '4f'):
        self.formula=formula
        self.tokens=re.findall(r'[A-Z][a-z]*|\d+\.*\d*|\(|\)', formula)
        self.feature=feature
        self.total=total(self.tokens,[],self.feature)
        self.howmany=howmany(self.tokens,[])
        self.avg_feature=total(self.tokens,[],self.feature)/howmany(self.tokens,[])
