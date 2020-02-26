
from helperfun import *




'''
    parse pdb with only nanotube atoms/conects

'''

# open pdb file
empty_tube_file = open(input_file, 'r')
# seperate empty tube pdb file by header, atoms, conect
header, tube_atoms, tube_conect = seperate_empty_tube(empty_tube_file)
# close it
empty_tube_file.close()


'''
    compute pdb atoms/conects for water molecules
    
'''
# get x,y coordinants representing the center of the Nano Tube  
tube_center = get_tube_center(tube_atoms)
print(tube_center)

# move tube to center of box
# moveTube(tube_atoms, tube_center)

# centerCoordsInBox(tube_atoms, tube_center)



startn = len(tube_atoms)+1
oxygen_quantity = calculate_water_molecules_inside_nanotube(rho)
oxygens = assign_positions_to_oxygens_list_pdb_new(oxygen_quantity, tube_center, startn)
hydro1 = adding_H1(len(oxygens), angle, bond_length)
hydro2 = adding_H2(hydro1, angle, bond_length)
h1_final = final_position_for_H(oxygens, hydro1) #move the water atoms from the origin to the random positions generated in oxygens
h2_final = final_position_for_H(oxygens, hydro2)
water_positions = water_class_pdb(oxygens, 4, h1_final, h2_final, 3, startn)
oxygens_to_print = water_positions.oxy_processed()
hydro1_to_print = water_positions.hydro_processed1()
hydro2_to_print = water_positions.hydro_processed2()
water_atoms = oxygens_to_print + hydro1_to_print + hydro2_to_print
water_atoms = sorted(water_atoms)
water_conect = water_conections(oxygen_quantity, startn)


'''
    output pdb of water-filled nanotube

'''

centerAtoms(tube_atoms, tube_center)
centerAtoms(water_atoms, tube_center)

print("new tube center: ", get_tube_center(tube_atoms))


final_out = open("output.pdb", 'w')
final_out.write(header)

for atom in tube_atoms:
	line = formatPdbRow(atom, True)
	final_out.write(line)
for atom in water_atoms:
    line = formatPdbRow(atom, False)
    final_out.write(line)
for conect in tube_conect+water_conect:
    final_out.write(conect)

final_out.write("END\n")
final_out.close()




'''

    Things to do:

        - normalize coordinates?
        - check assign_positions_to_oxygens_list_pdb_new


    Extra:

        - make code nicer via some oop?


'''
