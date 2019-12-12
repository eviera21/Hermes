
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEleftEXPONENTCLIENT CONNECT DIVIDE EQUALS EXIT EXPONENT FLOAT GET INT MINUS MULTIPLY NAME PLUS POST SERVER START STOP STRING\n    calc : expression\n        | var_assign\n        | empty\n    \n    var_assign : NAME EQUALS expression\n    \n    empty :\n    \n    expression : START CLIENT NAME\n                | STOP NAME\n    \n    expression : START SERVER NAME\n    expression : NAME CONNECT NAMEexpression : EXIT\n    expression : NAME POST NAME STRING\n               | NAME POST NAME NAME\n    expression : GET NAME\n    expression : expression EXPONENT expression\n                | expression MULTIPLY expression\n                | expression DIVIDE expression\n                | expression PLUS expression\n                | expression MINUS expression\n    \n    expression : INT\n                | FLOAT\n                | STRING\n    \n    expression : NAME\n    '
    
_lr_action_items = {'START':([0,13,14,15,16,17,22,],[5,5,5,5,5,5,5,]),'STOP':([0,13,14,15,16,17,22,],[7,7,7,7,7,7,7,]),'NAME':([0,7,10,13,14,15,16,17,18,19,20,21,22,34,],[6,23,24,26,26,26,26,26,31,32,33,34,26,36,]),'EXIT':([0,13,14,15,16,17,22,],[8,8,8,8,8,8,8,]),'GET':([0,13,14,15,16,17,22,],[10,10,10,10,10,10,10,]),'INT':([0,13,14,15,16,17,22,],[11,11,11,11,11,11,11,]),'FLOAT':([0,13,14,15,16,17,22,],[12,12,12,12,12,12,12,]),'STRING':([0,13,14,15,16,17,22,34,],[9,9,9,9,9,9,9,37,]),'$end':([0,1,2,3,4,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[-5,0,-1,-2,-3,-22,-10,-21,-19,-20,-7,-13,-14,-22,-15,-16,-17,-18,-6,-8,-9,-4,-12,-11,]),'EXPONENT':([2,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[13,-22,-10,-21,-19,-20,-7,-13,-14,-22,13,13,13,13,-6,-8,-9,13,-12,-11,]),'MULTIPLY':([2,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[14,-22,-10,-21,-19,-20,-7,-13,-14,-22,-15,-16,14,14,-6,-8,-9,14,-12,-11,]),'DIVIDE':([2,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[15,-22,-10,-21,-19,-20,-7,-13,-14,-22,-15,-16,15,15,-6,-8,-9,15,-12,-11,]),'PLUS':([2,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[16,-22,-10,-21,-19,-20,-7,-13,-14,-22,-15,-16,-17,-18,-6,-8,-9,16,-12,-11,]),'MINUS':([2,6,8,9,11,12,23,24,25,26,27,28,29,30,31,32,33,35,36,37,],[17,-22,-10,-21,-19,-20,-7,-13,-14,-22,-15,-16,-17,-18,-6,-8,-9,17,-12,-11,]),'CLIENT':([5,],[18,]),'SERVER':([5,],[19,]),'CONNECT':([6,26,],[20,20,]),'POST':([6,26,],[21,21,]),'EQUALS':([6,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,13,14,15,16,17,22,],[2,25,27,28,29,30,35,]),'var_assign':([0,],[3,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','language.py',81),
  ('calc -> var_assign','calc',1,'p_calc','language.py',82),
  ('calc -> empty','calc',1,'p_calc','language.py',83),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','language.py',89),
  ('empty -> <empty>','empty',0,'p_empty','language.py',95),
  ('expression -> START CLIENT NAME','expression',3,'p_expression_start_stop_client','language.py',101),
  ('expression -> STOP NAME','expression',2,'p_expression_start_stop_client','language.py',102),
  ('expression -> START SERVER NAME','expression',3,'p_expression_start_server','language.py',116),
  ('expression -> NAME CONNECT NAME','expression',3,'p_expression_connect','language.py',130),
  ('expression -> EXIT','expression',1,'p_expression_exit','language.py',140),
  ('expression -> NAME POST NAME STRING','expression',4,'p_expression_post','language.py',146),
  ('expression -> NAME POST NAME NAME','expression',4,'p_expression_post','language.py',147),
  ('expression -> GET NAME','expression',2,'p_expression_get','language.py',155),
  ('expression -> expression EXPONENT expression','expression',3,'p_expression','language.py',163),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','language.py',164),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','language.py',165),
  ('expression -> expression PLUS expression','expression',3,'p_expression','language.py',166),
  ('expression -> expression MINUS expression','expression',3,'p_expression','language.py',167),
  ('expression -> INT','expression',1,'p_expression_int_float_str','language.py',173),
  ('expression -> FLOAT','expression',1,'p_expression_int_float_str','language.py',174),
  ('expression -> STRING','expression',1,'p_expression_int_float_str','language.py',175),
  ('expression -> NAME','expression',1,'p_expression_var','language.py',182),
]
