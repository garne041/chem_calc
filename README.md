# chem_calc
The module chem_calc calculates chemical and physical properties based on the stoichometry of a chemical compound.

# Available properties
The 20 available properties (or features) used in this package are elemental properties from the CRC Handbook of Chemistry and Physics as well as the NIST X-ray Mass Attenuation Coefficients Database.


CRC Handbook of Chemistry and Physics
|Property / Feature|Tag|
|-----|-----|
|Number of 4f electrons| '4f'|
|Number of 5d electrons|'5d'|
|Combined number of 4f and 5d electrons |'add4f5d'|
|Absolute value of the difference of number of 4f and 5d electrons | 'sub4f5dabs'|
|Number of electrons| 'allelectrons'|
|Number of valence outer shell electrons| 'val_e'|
|Atomic number | 'atomicnumber'|
|Atomic weight |'atomicweight'|
|First ionization energy | 'ionenergy'|
|Pauling electronegativity of most common oxidation state | 'el_neg_chi'|
|van der Waals radius |'R_vdw_element'|
|Covalent radius | 'R_cov_element'| 
|Atomic number to mass number ratio | 'zaratio'|
|Excitation energy| 'ex_energy'|
|Period| 'period'|
|Elemental density | 'density'|

Features from the CRC Handbook of Chemistry and Physics that are currently available are number of 4f electrons ('4f'), number of 5d electrons ('5d'), combined number of 4f and 5d electrons ('add4f5d'), absolute value of the difference of number of 4f and 5d electrons ('sub4f5dabs'), number of electrons('allelectrons'), number of valence outer shell electrons ('val_e'), atomic number ('atomicnumber'), atomic weight ('atomicweight'), first ionization energy ('ionenergy'), Pauling electronegativity of most common oxidation state ('el_neg_chi'), van der Waals radius ('R_vdw_element'), covalent radius ('R_cov_element'), atomic number to mass number ratio ('zaratio'), excitation energy ('ex_energy'), period ('period'), and elemental density ('density').

NIST X-ray Mass Attenuation Coefficients Database for features at 662 keV and include the following:
|Property / Feature| Tag|
|-----|-----|
|Coherent scattering coefficient |'co_scatt'|
|Incoherent scattering coefficient |'inco_scatt'|
|Photoelectric absorption |'pe_abs'|
|Coherent attenutation coefficient |'atten_co'|
|Incoherent attenutation coefficient |'atten_inco'|

NIST X-ray Mass Attenuation Coefficients Database for features at 662 keV. They include the following: coherent scattering coefficient ('co_scatt'), incoherent scattering coefficient ('inco_scatt'), photoelectric absorption ('pe_abs'), coherent attenutation coefficient ('atten_co'), and the incoherent attenutation coefficient ('atten_inco')."""


# Methods
* how_many -- Returns the number of atoms in a given chemical formula.
* total --  Returns the feature total for a given chemical formula.
* min_feature -- Returns the feature minimum for a given chemical formula.
* max_feature -- Returns the feature maximum for a given chemical formula.
* avg_feature -- Returns the feature average for a given chemical formula.


