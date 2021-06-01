from .ElevatorConstants import *
from toontown.toonbase import ToontownGlobals

try:
    config = base.config
except:
    config = simbase.config
    
SUIT_PLANNER_CFO = 15

SuitBuildingInfo = (((1, 1),
  (1, 3),
  (4, 4),
  (10, 10),
  (1,)),
 ((1, 2),
  (2, 5),
  (6, 6),
  (13, 13),
  (1, 1.2)),
 ((1, 3),
  (3, 7),
  (8, 8),
  (16, 16),
  (1, 1.3, 1.6)),
 ((2, 3),
  (4, 9),
  (10, 10),
  (19, 19),
  (1, 1.4, 1.8)),
 ((2, 4),
  (5, 11),
  (12, 12),
  (22, 22),
  (1,
   1.6,
   1.8,
   2)),
 ((3, 4),
  (6, 13),
  (14, 14),
  (25, 25),
  (1,
   1.6,
   2,
   2.4)),
 ((3, 5),
  (7, 15),
  (16, 16),
  (29, 29),
  (1,
   1.6,
   1.8,
   2.2,
   2.4)),
 ((4, 5),
  (8, 17),
  (18, 18),
  (33, 33),
  (1,
   1.8,
   2.4,
   3,
   3.2)),
 ((5, 5),
  (9, 19),
  (20, 20),
  (55, 55),
  (1.4,
   1.8,
   2.6,
   3.4,
   4)),
 ((1, 1),
  (10, 14),
  (14, 14),
  (175, 175),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (10, 19),
  (30, 30),
  (150, 150),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (10, 16),
  (16, 16),
  (200, 200),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (10, 20),
  (35, 35),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (10, 18),
  (40, 40),
  (250, 250),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (10, 20),
  (20, 20),
  (275, 275),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (1, 5),
  (5, 5),
  (33, 33),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (4, 5),
  (5, 5),
  (50, 50),
  (1,
   1,
   1,
   1,
   1)))
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
SUIT_BLDG_INFO_IMMUNE = 6
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
