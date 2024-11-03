import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/llagoeiro/Desktop/FEI/8_semestre/RoboticaProbFolder/proj3/TurtleBot3/install/navigation_pkg'
