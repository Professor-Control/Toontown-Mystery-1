from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattlePlace1 = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 16,
  'battleCell': BattleCellId,
  'pos': Point3(-8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 17,
  'battleCell': BattleCellId,
  'pos': Point3(-3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 15,
  'battleCell': BattleCellId,
  'pos': Point3(3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 16,
  'battleCell': BattleCellId,
  'pos': Point3(8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = []
