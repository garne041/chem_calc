# chem_calc
The module chem_calc calculates chemical and physical properties based on the stoichometry of a chemical compound.

# Available properties
The 20 available properties (or features) used in this package are elemental properties from the CRC Handbook of Chemistry and Physics as well as the NIST X-ray Mass Attenuation Coefficients Database.


CRC Handbook of Chemistry and Physics

| Property / Feature | Tag |
|-----------------|-----------------------|
| Number of 4f electrons  | '4f'|
| Number of 5d electrons  | '5d'|
| Combined number of 4f and 5d electrons | 'add4f5d'|
| Absolute value of the difference of number of 4f and 5d electrons | 'sub4f5dabs'|
| Number of electrons  | 'allelectrons' |
| Number of valence outer shell electrons  | 'val_e' |
| Atomic number | 'atomicnumber' |
| Atomic weight | 'atomicweight' |
| First ionization energy | 'ionenergy' |
| Pauling electronegativity of most common oxidation state | 'el_neg_chi' |
| van der Waals radius | 'R_vdw_element' |
| Covalent radius | 'R_cov_element' | 
| Atomic number to mass number ratio | 'zaratio' |
| Excitation energy  | 'ex_energy' |
| Period  | 'period' |
| Elemental density | 'density' |


NIST X-ray Mass Attenuation Coefficients Database for features at 662 keV and include the following:

|Property / Feature| Tag|
|----------|----------|
|Coherent scattering coefficient |'co_scatt'|
|Incoherent scattering coefficient |'inco_scatt'|
|Photoelectric absorption |'pe_abs'|
|Coherent attenutation coefficient |'atten_co'|
|Incoherent attenutation coefficient |'atten_inco'|

# Methods
* how_many -- Returns the number of atoms in a given chemical formula.
```{
>>> import chem_calc
>>> chem_calc.chem_calc('H2O').howmany
3.0
}
```
* total --  Returns the feature total for a given chemical formula.
```{
>>> import chem_calc
>>> chem_calc.chem_calc('H2O',feature='atomicweight').total
18.014710000000001
}
```

* avg_feature -- Returns the average value of a property for a given chemical formula.
```{
>>> import chem_calc
>>> chem_calc.chem_calc('H2O',feature='atomicweight').avg_feature
6.0049033333333339
}
```

# Installation

Use 'pip' to install from pypi:

```{
pip install chem_calc
}
```

or 'pip' to install from github:

```{
pip install git+https://github.com/garne041/chem_calc.git
}
```
or clone the package using git:

```{
git clone https://github.com/garne041/chem_calc.git
}
```

# Requirements
Requires numpy, pickle, and pandas

# License
The original code that this project is based on https://repl.it/@Supakri2680/Molecular-Mass-Calculator2. In keeping with this mentality, all code is released under the MIT.

