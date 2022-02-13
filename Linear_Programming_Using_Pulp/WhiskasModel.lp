\* The_Whiskas_Problem *\
Minimize
OBJ: __dummy
Subject To
FatRequirement: 0.1 BeefPercent + 0.08 ChickenPercent >= 6
FibreRequirement: 0.005 BeefPercent + 0.001 ChickenPercent <= 2
PercentagesSum: BeefPercent + ChickenPercent = 100
ProteinRequirement: 0.2 BeefPercent + 0.1 ChickenPercent >= 8
SaltRequirement: 0.005 BeefPercent + 0.002 ChickenPercent <= 0.4
Bounds
 0 <= BeefPercent
 0 <= ChickenPercent
 __dummy = 0
Generals
BeefPercent
ChickenPercent
End
