from dpr_calculator import *

if __name__ == '__main__':
    redbrand_shortsword = attack(4, '1d6', 2)
    print_ac_dc_range(12, 18, [redbrand_shortsword, redbrand_shortsword], "Redbrand")

    manticore_bite = attack(5, '1d8', 3)
    manticore_claw = attack(5, '1d6', 3)
    manticore_tail_spike = attack(5, '1d8', 3)
    print_ac_dc_range(12, 18, [manticore_bite, manticore_claw, manticore_claw], "Manticore melee")
    print_ac_dc_range(12, 18, [manticore_tail_spike, manticore_tail_spike, manticore_tail_spike], "Manticore ranged")

    test_dc_attack = dc_attack(10, '1d10', False)
    print_ac_dc_range(0, 3, [test_dc_attack], "Test")

    acid_spray = dc_attack(13, '3d6', True)
    print_ac_dc_range(0, 7, [acid_spray], "Ankheg")

