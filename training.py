from ase.build import molecule, fcc111, add_adsorbate
from ase.visualize import view
import ase.dft.kpoints
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.constraints import FixAtoms

# kpts = ase.dft.kpoints.monkhorst_pack([4, 4, 1]) + [0.2, 0.15, 0.12]

molecules = molecule('CO')
molecules.set_calculator(EMT())
dyn = QuasiNewton(molecules)
dyn.run(fmax = 0.05)

E_gas = molecules.get_potential_energy()
slab = fcc111('Pt', size = (2, 2, 4), vacuum = 10)
c = FixAtoms(indices = [molecule.index for molecule in slab if molecule.index > 7])
slab.set_constraint(c)
slab.set_calculator(EMT())
dyn = QuasiNewton(slab)
dyn.run(fmax = 0.05)
E_slab = slab.get_potential_energy()

add_adsorbate(slab, molecules, 2.3,'hcp')
slab.set_calculator(EMT())
dyn = QuasiNewton(slab)
dyn.run(fmax=0.05)
E_slab_ads = slab.get_potential_energy()
view(slab)

E_ads = E_slab_ads - E_slab - E_gas
print(E_ads)
