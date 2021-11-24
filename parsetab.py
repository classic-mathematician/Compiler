
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALSleftLTLTEGTGTEleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENAND BLOCKEND BLOCKSTART COLON COMMA COMMENT DIVIDE DOUBLEEQUAL DO_K ELSE_K EQUALS FLOAT FLOAT_K FOR_K FUNCTION_K GT GTE ID IF_K INT INT_K LBRACE LPAREN LT LTE MAIN_K MINUS OR PLUS PROGRAM_K RBRACE READ_K RETURN_K RPAREN SEMICOLON STRING STRING_K TIMES TO_K VARS_K VOID_K WHILE_K WRITE_KPROGRAM : PROGRAM_K ID neural_program_id SEMICOLON BLOCKneural_program_id : EMPTYBLOCK : VAR_BLOCK PROC_BLOCK PRINCIPAL_BLOCKVAR_BLOCK : VARS_K BLOCKSTART VAR_DECL BLOCKENDVAR_DECL : TYPE COLON VAR_LIST SEMICOLON VAR_DECL_RVAR_DECL_R : VAR_DECL\n                  | EMPTYVAR_LIST : VAR VAR_LIST2VAR_LIST2 : COMMA VAR VAR_LIST2\n                 | EMPTYTYPE : INT_K NEURAL_TYPE\n            | FLOAT_K NEURAL_TYPE\n            | STRING_K NEURAL_TYPENEURAL_TYPE : EMPTYPROC_BLOCK : PROC_DECLPROC_DECL : PROC_DECL_RETURN\n                 | PROC_DECL_VOID\n                 | EMPTYPROC_DECL_VOID : FUNCTION_K VOID_K ID neural_proc_void_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY BLOCKEND POST_FUNC PROC_DECLneural_proc_void_id : EMPTYPROC_DECL_RETURN : FUNCTION_K TYPE ID neural_proc_return_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY RETURN BLOCKEND POST_FUNC PROC_DECLPOST_FUNC : EMPTYneural_proc_return_id : EMPTYneural_param_decl : EMPTYPARAM_DECL : TYPE VAR neuro PARAM_DECL_R\n                  | EMPTYneuro : EMPTYPARAM_DECL_R : COMMA PARAM_DECL\n                    | EMPTYPROC_BODY : STATEMENT PROC_BODY_RFN_VARBLOCK : VARS_K BLOCKSTART LS_VARDECL BLOCKENDLS_VARDECL : TYPE COLON FNVAR_LS SEMICOLON LS_VARDECL_RLS_VARDECL_R : LS_VARDECL\n                    | EMPTYFNVAR_LS : VAR FNVAR_LS2FNVAR_LS2 : COMMA FNVAR_LS\n                 | EMPTYPROC_BODY_R : PROC_BODY\n                   | EMPTYSTATEMENT : ASSIGN SEMICOLON\n                 | ASSIGN1 SEMICOLON\n                 | FUNC_CALL SEMICOLON\n                 | READ SEMICOLON\n                 | WRITE SEMICOLON\n                 | FLOW\n                STATEMENT_R : STATEMENT STATEMENT_R\n                   | EMPTYFLOW : DECISION\n            | LOOPLOOP : WHILE_LOOP\n            | DO_WHILE_LOOP SEMICOLON\n            | FOR_LOOPDO_WHILE_LOOP : DO_K DW_PREV_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_K LPAREN H_EXPRESSION RPAREN DW_END_NEURALDW_PREV_NEURAL : EMPTYDW_END_NEURAL : EMPTYWHILE_LOOP : WHILE_K WHILE_PREV_NEURAL LPAREN H_EXPRESSION RPAREN WHILE_POST_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_END_NEURALWHILE_PREV_NEURAL : EMPTYWHILE_POST_NEURAL : EMPTYWHILE_END_NEURAL : EMPTYFOR_LOOP : FOR_K ID EQUALS INT TO_K INT DO_K BLOCKSTART STATEMENT_R BLOCKENDDECISION : IF_K LPAREN H_EXPRESSION RPAREN EXP_RESULT_NEURAL BLOCKSTART STATEMENT_R BLOCKEND DECISION_ALT DECISION_END_NEURALEXP_RESULT_NEURAL : EMPTYDECISION_END_NEURAL : EMPTYDECISION_ALT : ELSE\n                    | EMPTYELSE : ELSE_NEURAL ELSE_K BLOCKSTART STATEMENT_R BLOCKENDELSE_NEURAL : EMPTYRIGHT_ASSIGN : H_EXPRESSION\n                    | FUNC_CALLASSIGN : VAR ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURALASSIGN1 : ARR_AC ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURALN : EMPTYASSI_H_EXP_NEURAL : EMPTYEQUALS_NEURAL : EMPTYASSIGN_VAR_N : EMPTYARR_AC : ID ARR_ID_NP1 DIM_ACARR_ID_NP1 : EMPTYDIM_AC : LBRACE H_EXPRESSION DIM_AC_PREV RBRACE DIM_AC_RDIM_AC_PREV : EMPTYDIM_AC_R : DIM_AC\n                | EMPTYVAR : ID\n           | ARRAYARRAY : ID ARR_ID_NP DIMARR_ID_NP : EMPTYDIM : LBRACE INT LIM_NP RBRACE DIM_RLIM_NP : EMPTYDIM_R : DIM\n             | EMPTYFUNC_CALL : ID PRE_VERIFY LPAREN EXP_LIST POST_VERIFY RPARENPOST_VERIFY : EMPTYPRE_VERIFY : EMPTYEXP_LIST : H_EXPRESSION EXP_NEURAL EXP_LIST_2EXP_NEURAL : EMPTYEXP_LIST_2 : COMMA EXP_LIST\n                  | EMPTYCONSTANT : INT\n                | FLOAT\n                | STRINGREAD : READ_K LPAREN ID_LIST RPARENID_LIST : ID READ_NEURAL ID_LIST_RREAD_NEURAL : EMPTYID_LIST_R : COMMA ID_LIST\n                 | EMPTYWRITE : WRITE_K LPAREN WRITE_LIST RPARENWRITE_LIST : RIGHT_ASSIGN WRITE_LIST_R\n                  | CONSTANT CONSTANT_WRITE_N WRITE_LIST_RCONSTANT_WRITE_N : EMPTYWRITE_LIST_R : WRITE_NEURAL COMMA WRITE_LIST\n                    | WRITE_NEURAL EMPTYWRITE_NEURAL : EMPTYRETURN : RETURN_K LPAREN H_EXPRESSION RPAREN SEMICOLONEXPRESSION : TERM NEURAL_EXPRESSION EXPRESSION_RNEURAL_EXPRESSION : EMPTYEXPRESSION_R : PLUS NEURAL_PLUS EXPRESSION\n                    | MINUS NEURAL_MINUS EXPRESSION\n                    | EMPTYNEURAL_PLUS : EMPTYNEURAL_MINUS : EMPTYTERM : FACTOR NEURAL_TERM TERM_RNEURAL_TERM : EMPTYTERM_R : TIMES NEURAL_TIMES TERM\n              | DIVIDE NEURAL_DIVIDE TERM\n              | EMPTYNEURAL_TIMES : EMPTYNEURAL_DIVIDE : EMPTYFACTOR : ID NEURAL_ID_FAC\n              | CONSTANT NEURAL_CNT_FACT\n              | LPAREN H_EXPRESSION RPARENNEURAL_ID_FAC : EMPTYNEURAL_CNT_FACT : EMPTYS_EXPRESSION : EXPRESSION S_EXPRESSION_RNEURAL_EXP : EMPTYS_EXPRESSION_R : CONDI NEURAL_CONDI EXPRESSION NEURAL_EXP\n                      | EMPTYNEURAL_CONDI : EMPTYCONDI : GT\n             | LT\n             | LTE\n             | GTE\n             | DOUBLEEQUAL\n             | AND\n             | ORH_EXPRESSION : S_EXPRESSION H_EXPRESSION_RH_EXPRESSION_R : OR H_EXPRESSION\n                      | AND H_EXPRESSION\n                      | EMPTYPRINCIPAL_BLOCK : MAIN_K MAIN_NEURAL LPAREN RPAREN BLOCKSTART PRINCIPAL_BODY BLOCKENDMAIN_NEURAL : EMPTYPRINCIPAL_BODY : STATEMENT PRINCIPAL_BODY_R\n                      | EMPTYPRINCIPAL_BODY_R : PRINCIPAL_BODYEMPTY : '
    
_lr_action_items = {'PROGRAM_K':([0,],[2,]),'$end':([1,7,17,93,],[0,-1,-3,-148,]),'ID':([2,19,20,21,22,23,30,31,32,33,35,50,54,55,66,73,79,80,82,84,87,96,97,98,99,100,107,108,109,110,123,124,125,127,130,147,148,156,157,158,174,175,180,182,183,184,185,186,187,188,198,202,204,217,220,225,226,228,229,232,233,242,250,256,257,258,259,260,261,262,263,264,288,289,292,293,294,297,300,306,307,308,310,317,319,320,322,323,326,332,334,],[3,28,29,-153,-153,-153,-11,-14,-12,-13,43,43,76,43,76,-45,-48,-49,-50,-52,115,-40,-41,-42,-43,-44,129,140,145,-51,-153,-153,145,145,145,145,76,140,-74,140,145,145,-153,-137,-138,-139,-140,-141,-142,-143,76,76,76,129,140,145,-136,-153,-153,-153,-153,76,145,145,-118,145,-119,145,-125,145,-126,76,76,145,145,-31,43,-153,76,-153,-64,-65,-153,43,-61,-63,-56,-59,-60,76,-66,]),'SEMICOLON':([3,4,5,41,42,43,44,49,51,62,63,68,69,70,71,72,83,91,134,135,136,137,138,139,140,141,142,143,145,146,155,162,166,171,173,176,177,178,179,181,189,190,191,192,194,195,205,206,207,208,209,219,223,224,227,230,231,234,245,246,247,248,255,281,282,283,284,285,286,303,304,311,314,316,318,324,325,331,],[-153,6,-2,48,-153,-82,-83,-8,-10,-153,-84,96,97,98,99,100,110,-9,-68,-69,-97,-98,-99,-153,-153,-153,-153,-153,-153,-153,-153,-100,-105,-128,-144,-147,-127,-130,-132,-135,-153,-114,-153,-121,-130,-131,-86,-88,-89,-153,-153,-129,-145,-146,-113,-117,-120,-124,-70,-73,-71,-90,-153,-134,-133,-115,-116,-122,-123,315,-153,-153,327,-35,-37,-53,-55,-36,]),'VARS_K':([6,153,154,],[9,203,203,]),'FUNCTION_K':([8,34,276,291,295,296,301,],[15,-4,-153,-153,15,-22,15,]),'MAIN_K':([8,10,11,12,13,14,34,276,291,295,296,301,305,313,],[-153,18,-15,-16,-17,-18,-4,-153,-153,-153,-22,-153,-19,-21,]),'BLOCKSTART':([9,45,86,89,90,113,114,118,119,120,193,203,235,236,237,265,266,290,321,],[16,54,-153,-153,-153,148,-54,153,-24,154,-153,243,264,-62,-153,288,-58,300,332,]),'VOID_K':([15,],[20,]),'INT_K':([15,16,46,47,48,151,243,315,],[21,21,21,21,21,21,21,21,]),'FLOAT_K':([15,16,46,47,48,151,243,315,],[22,22,22,22,22,22,22,22,]),'STRING_K':([15,16,46,47,48,151,243,315,],[23,23,23,23,23,23,23,23,]),'LPAREN':([18,26,27,28,29,37,38,39,40,76,77,78,81,85,104,106,108,109,111,112,123,124,125,127,130,140,147,156,157,158,174,175,178,180,182,183,184,185,186,187,188,220,225,226,228,229,232,233,250,256,257,258,259,260,261,262,263,267,270,289,292,],[-153,36,-149,-153,-153,46,-23,47,-20,-153,107,108,109,-153,125,-92,130,130,147,-57,-153,-153,130,130,130,-153,130,130,-74,130,130,130,-92,-153,-137,-138,-139,-140,-141,-142,-143,130,130,-136,-153,-153,-153,-153,130,130,-118,130,-119,130,-125,130,-126,289,292,130,130,]),'COLON':([21,22,23,25,30,31,32,33,275,],[-153,-153,-153,35,-11,-14,-12,-13,294,]),'BLOCKEND':([24,48,54,59,60,61,65,66,67,73,79,80,82,84,94,95,96,97,98,99,100,110,148,197,198,199,239,242,244,264,269,271,272,273,274,287,288,297,298,300,306,307,308,310,312,315,319,320,322,323,326,327,328,329,330,332,333,334,],[34,-153,-153,-5,-6,-7,93,-153,-151,-45,-48,-49,-50,-52,-150,-152,-40,-41,-42,-43,-44,-51,-153,238,-153,-47,-46,-153,276,-153,291,-30,-38,-39,293,297,-153,-153,310,-153,-153,-64,-65,-153,326,-153,-61,-63,-56,-59,-60,-112,-32,-33,-34,-153,334,-66,]),'RPAREN':([36,43,44,46,47,56,57,58,63,88,116,117,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,150,151,152,155,159,160,163,164,165,167,168,169,170,171,172,173,176,177,178,179,181,189,190,191,192,194,195,196,201,205,206,207,210,211,212,213,216,218,219,221,222,223,224,227,230,231,234,248,249,251,253,254,255,277,281,282,283,284,285,286,299,302,],[45,-82,-83,-153,-153,89,-26,90,-84,-153,-153,-27,162,-153,166,-153,-153,-68,-69,-97,-98,-99,-153,-153,-153,-153,-153,193,-153,-153,-25,-153,-29,-153,-153,-153,-153,-102,219,-106,-153,-111,-153,-128,-108,-144,-147,-127,-130,-132,-135,-153,-114,-153,-121,-130,-131,237,-28,-86,-88,-89,248,-91,-153,-94,-101,-104,-129,-110,-107,-145,-146,-113,-117,-120,-124,-90,-93,-96,-103,-109,-153,-95,-134,-133,-115,-116,-122,-123,311,314,]),'COMMA':([42,43,44,62,63,88,116,117,129,132,133,134,135,136,137,138,139,140,141,142,143,145,146,155,160,163,164,168,169,170,171,172,173,176,177,178,179,181,189,190,191,192,194,195,205,206,207,212,213,219,223,224,227,230,231,234,248,255,281,282,283,284,285,286,304,],[50,-82,-83,50,-84,-153,151,-27,-153,-153,-153,-68,-69,-97,-98,-99,-153,-153,-153,-153,-153,-153,-153,-153,-153,217,-102,220,-111,-153,-128,-108,-144,-147,-127,-130,-132,-135,-153,-114,-153,-121,-130,-131,-86,-88,-89,250,-94,-129,-145,-146,-113,-117,-120,-124,-90,-153,-134,-133,-115,-116,-122,-123,317,]),'LBRACE':([43,52,53,76,105,106,155,252,],[-153,64,-85,-153,127,-77,64,127,]),'EQUALS':([44,63,74,75,76,101,102,103,115,126,155,205,206,207,252,278,279,280,],[-83,-84,-153,-153,-82,123,-75,124,149,-76,-153,-86,-88,-89,-153,-78,-80,-81,]),'READ_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,242,264,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[77,77,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,77,77,77,77,77,77,77,-31,-153,77,-153,-64,-65,-153,-61,-63,-56,-59,-60,77,-66,]),'WRITE_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,242,264,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[78,78,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,78,78,78,78,78,78,78,-31,-153,78,-153,-64,-65,-153,-61,-63,-56,-59,-60,78,-66,]),'IF_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,242,264,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[81,81,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,81,81,81,81,81,81,81,-31,-153,81,-153,-64,-65,-153,-61,-63,-56,-59,-60,81,-66,]),'WHILE_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,238,242,264,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[85,85,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,85,85,85,85,267,85,85,85,-31,-153,85,-153,-64,-65,-153,-61,-63,-56,-59,-60,85,-66,]),'DO_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,242,264,268,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[86,86,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,86,86,86,86,86,86,290,86,-31,-153,86,-153,-64,-65,-153,-61,-63,-56,-59,-60,86,-66,]),'FOR_K':([54,66,73,79,80,82,84,96,97,98,99,100,110,148,198,202,204,242,264,288,293,297,300,306,307,308,310,319,320,322,323,326,332,334,],[87,87,-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,87,87,87,87,87,87,87,-31,-153,87,-153,-64,-65,-153,-61,-63,-56,-59,-60,87,-66,]),'INT':([64,108,109,123,124,125,127,130,147,149,156,157,158,174,175,180,182,183,184,185,186,187,188,220,225,226,228,229,232,233,240,250,256,257,258,259,260,261,262,263,289,292,],[92,136,136,-153,-153,136,136,136,136,200,136,-74,136,136,136,-153,-137,-138,-139,-140,-141,-142,-143,136,136,-136,-153,-153,-153,-153,268,136,136,-118,136,-119,136,-125,136,-126,136,136,]),'RETURN_K':([73,79,80,82,84,96,97,98,99,100,110,241,242,271,272,273,297,306,307,308,310,319,320,322,323,326,334,],[-45,-48,-49,-50,-52,-40,-41,-42,-43,-44,-51,270,-153,-30,-38,-39,-153,-153,-64,-65,-153,-61,-63,-56,-59,-60,-66,]),'RBRACE':([92,121,122,136,137,138,139,141,142,143,145,146,161,171,173,176,177,179,181,189,190,191,192,194,195,214,215,219,223,224,227,230,231,234,255,281,282,283,284,285,286,],[-153,155,-87,-97,-98,-99,-153,-153,-153,-153,-153,-153,-153,-128,-144,-147,-127,-132,-135,-153,-114,-153,-121,-130,-131,252,-79,-129,-145,-146,-113,-117,-120,-124,-153,-134,-133,-115,-116,-122,-123,]),'FLOAT':([108,109,123,124,125,127,130,147,156,157,158,174,175,180,182,183,184,185,186,187,188,220,225,226,228,229,232,233,250,256,257,258,259,260,261,262,263,289,292,],[137,137,-153,-153,137,137,137,137,137,-74,137,137,137,-153,-137,-138,-139,-140,-141,-142,-143,137,137,-136,-153,-153,-153,-153,137,137,-118,137,-119,137,-125,137,-126,137,137,]),'STRING':([108,109,123,124,125,127,130,147,156,157,158,174,175,180,182,183,184,185,186,187,188,220,225,226,228,229,232,233,250,256,257,258,259,260,261,262,263,289,292,],[138,138,-153,-153,138,138,138,138,138,-74,138,138,138,-153,-137,-138,-139,-140,-141,-142,-143,138,138,-136,-153,-153,-153,-153,138,138,-118,138,-119,138,-125,138,-126,138,138,]),'TIMES':([133,136,137,138,140,143,145,146,171,172,177,178,191,192,194,195,219,],[-153,-97,-98,-99,-153,-153,-153,-153,-128,-131,-127,-130,232,-121,-130,-131,-129,]),'DIVIDE':([133,136,137,138,140,143,145,146,171,172,177,178,191,192,194,195,219,],[-153,-97,-98,-99,-153,-153,-153,-153,-128,-131,-127,-130,233,-121,-130,-131,-129,]),'PLUS':([133,136,137,138,140,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,231,234,285,286,],[-153,-97,-98,-99,-153,-153,-153,-153,-153,-128,-131,-127,-130,228,-114,-153,-121,-130,-131,-129,-120,-124,-122,-123,]),'MINUS':([133,136,137,138,140,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,231,234,285,286,],[-153,-97,-98,-99,-153,-153,-153,-153,-153,-128,-131,-127,-130,229,-114,-153,-121,-130,-131,-129,-120,-124,-122,-123,]),'GT':([133,136,137,138,140,141,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,227,230,231,234,283,284,285,286,],[-153,-97,-98,-99,-153,182,-153,-153,-153,-153,-128,-131,-127,-130,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-115,-116,-122,-123,]),'LT':([133,136,137,138,140,141,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,227,230,231,234,283,284,285,286,],[-153,-97,-98,-99,-153,183,-153,-153,-153,-153,-128,-131,-127,-130,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-115,-116,-122,-123,]),'LTE':([133,136,137,138,140,141,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,227,230,231,234,283,284,285,286,],[-153,-97,-98,-99,-153,184,-153,-153,-153,-153,-128,-131,-127,-130,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-115,-116,-122,-123,]),'GTE':([133,136,137,138,140,141,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,227,230,231,234,283,284,285,286,],[-153,-97,-98,-99,-153,185,-153,-153,-153,-153,-128,-131,-127,-130,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-115,-116,-122,-123,]),'DOUBLEEQUAL':([133,136,137,138,140,141,142,143,145,146,171,172,177,178,189,190,191,192,194,195,219,227,230,231,234,283,284,285,286,],[-153,-97,-98,-99,-153,186,-153,-153,-153,-153,-128,-131,-127,-130,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-115,-116,-122,-123,]),'AND':([133,136,137,138,139,140,141,142,143,145,146,171,172,177,178,179,181,189,190,191,192,194,195,219,227,230,231,234,255,281,282,283,284,285,286,],[-153,-97,-98,-99,175,-153,187,-153,-153,-153,-153,-128,-131,-127,-130,-132,-135,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-153,-134,-133,-115,-116,-122,-123,]),'OR':([133,136,137,138,139,140,141,142,143,145,146,171,172,177,178,179,181,189,190,191,192,194,195,219,227,230,231,234,255,281,282,283,284,285,286,],[-153,-97,-98,-99,174,-153,188,-153,-153,-153,-153,-128,-131,-127,-130,-132,-135,-153,-114,-153,-121,-130,-131,-129,-113,-117,-120,-124,-153,-134,-133,-115,-116,-122,-123,]),'TO_K':([200,],[240,]),'ELSE_K':([297,308,309,],[-153,-67,321,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'neural_program_id':([3,],[4,]),'EMPTY':([3,8,18,21,22,23,28,29,42,43,46,47,48,54,62,66,74,75,76,85,86,88,89,90,92,116,123,124,129,132,133,139,140,141,142,143,145,146,148,151,155,159,160,161,163,168,170,180,189,191,193,198,208,209,212,228,229,232,233,237,242,252,255,264,276,288,291,295,297,300,301,304,306,310,311,315,332,],[5,14,27,31,31,31,38,40,51,53,57,57,61,67,51,67,102,102,106,112,114,117,119,119,122,152,157,157,164,169,172,176,178,181,190,192,194,195,199,57,207,211,213,215,218,221,169,226,230,234,236,199,246,246,251,257,259,261,263,266,273,280,282,199,296,199,296,14,308,199,14,318,320,323,325,330,199,]),'BLOCK':([6,],[7,]),'VAR_BLOCK':([6,],[8,]),'PROC_BLOCK':([8,],[10,]),'PROC_DECL':([8,295,301,],[11,305,313,]),'PROC_DECL_RETURN':([8,295,301,],[12,12,12,]),'PROC_DECL_VOID':([8,295,301,],[13,13,13,]),'PRINCIPAL_BLOCK':([10,],[17,]),'TYPE':([15,16,46,47,48,151,243,315,],[19,25,55,55,25,55,275,275,]),'VAR_DECL':([16,48,],[24,60,]),'MAIN_NEURAL':([18,],[26,]),'NEURAL_TYPE':([21,22,23,],[30,32,33,]),'neural_proc_return_id':([28,],[37,]),'neural_proc_void_id':([29,],[39,]),'VAR_LIST':([35,],[41,]),'VAR':([35,50,54,55,66,148,198,202,204,242,264,288,294,300,317,332,],[42,62,74,88,74,74,74,74,74,74,74,74,304,74,304,74,]),'ARRAY':([35,50,54,55,66,148,198,202,204,242,264,288,294,300,317,332,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'VAR_LIST2':([42,62,],[49,91,]),'ARR_ID_NP':([43,76,],[52,52,]),'PARAM_DECL':([46,47,151,],[56,58,201,]),'VAR_DECL_R':([48,],[59,]),'DIM':([52,155,],[63,206,]),'PRINCIPAL_BODY':([54,66,],[65,95,]),'STATEMENT':([54,66,148,198,202,204,242,264,288,300,332,],[66,66,198,198,242,242,242,198,198,198,198,]),'ASSIGN':([54,66,148,198,202,204,242,264,288,300,332,],[68,68,68,68,68,68,68,68,68,68,68,]),'ASSIGN1':([54,66,148,198,202,204,242,264,288,300,332,],[69,69,69,69,69,69,69,69,69,69,69,]),'FUNC_CALL':([54,66,108,148,156,158,198,202,204,220,242,264,288,300,332,],[70,70,135,70,135,135,70,70,70,135,70,70,70,70,70,]),'READ':([54,66,148,198,202,204,242,264,288,300,332,],[71,71,71,71,71,71,71,71,71,71,71,]),'WRITE':([54,66,148,198,202,204,242,264,288,300,332,],[72,72,72,72,72,72,72,72,72,72,72,]),'FLOW':([54,66,148,198,202,204,242,264,288,300,332,],[73,73,73,73,73,73,73,73,73,73,73,]),'ARR_AC':([54,66,148,198,202,204,242,264,288,300,332,],[75,75,75,75,75,75,75,75,75,75,75,]),'DECISION':([54,66,148,198,202,204,242,264,288,300,332,],[79,79,79,79,79,79,79,79,79,79,79,]),'LOOP':([54,66,148,198,202,204,242,264,288,300,332,],[80,80,80,80,80,80,80,80,80,80,80,]),'WHILE_LOOP':([54,66,148,198,202,204,242,264,288,300,332,],[82,82,82,82,82,82,82,82,82,82,82,]),'DO_WHILE_LOOP':([54,66,148,198,202,204,242,264,288,300,332,],[83,83,83,83,83,83,83,83,83,83,83,]),'FOR_LOOP':([54,66,148,198,202,204,242,264,288,300,332,],[84,84,84,84,84,84,84,84,84,84,84,]),'PRINCIPAL_BODY_R':([66,],[94,]),'ASSIGN_VAR_N':([74,75,],[101,103,]),'PRE_VERIFY':([76,140,],[104,104,]),'ARR_ID_NP1':([76,],[105,]),'WHILE_PREV_NEURAL':([85,],[111,]),'DW_PREV_NEURAL':([86,],[113,]),'neuro':([88,],[116,]),'neural_param_decl':([89,90,],[118,120,]),'LIM_NP':([92,],[121,]),'DIM_AC':([105,252,],[126,279,]),'ID_LIST':([107,217,],[128,253,]),'WRITE_LIST':([108,220,],[131,254,]),'RIGHT_ASSIGN':([108,156,158,220,],[132,208,209,132,]),'CONSTANT':([108,109,125,127,130,147,156,158,174,175,220,225,250,256,258,260,262,289,292,],[133,146,146,146,146,146,146,146,146,146,133,146,146,146,146,146,146,146,146,]),'H_EXPRESSION':([108,109,125,127,130,147,156,158,174,175,220,250,289,292,],[134,144,160,161,165,196,134,134,223,224,134,160,299,302,]),'S_EXPRESSION':([108,109,125,127,130,147,156,158,174,175,220,250,289,292,],[139,139,139,139,139,139,139,139,139,139,139,139,139,139,]),'EXPRESSION':([108,109,125,127,130,147,156,158,174,175,220,225,250,256,258,289,292,],[141,141,141,141,141,141,141,141,141,141,141,255,141,283,284,141,141,]),'TERM':([108,109,125,127,130,147,156,158,174,175,220,225,250,256,258,260,262,289,292,],[142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,285,286,142,142,]),'FACTOR':([108,109,125,127,130,147,156,158,174,175,220,225,250,256,258,260,262,289,292,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,]),'PARAM_DECL_R':([116,],[150,]),'EQUALS_NEURAL':([123,124,],[156,158,]),'EXP_LIST':([125,250,],[159,277,]),'READ_NEURAL':([129,],[163,]),'WRITE_LIST_R':([132,170,],[167,222,]),'WRITE_NEURAL':([132,170,],[168,168,]),'CONSTANT_WRITE_N':([133,],[170,]),'NEURAL_CNT_FACT':([133,146,],[171,171,]),'H_EXPRESSION_R':([139,],[173,]),'NEURAL_ID_FAC':([140,145,],[177,177,]),'S_EXPRESSION_R':([141,],[179,]),'CONDI':([141,],[180,]),'NEURAL_EXPRESSION':([142,],[189,]),'NEURAL_TERM':([143,],[191,]),'STATEMENT_R':([148,198,264,288,300,332,],[197,239,287,298,312,333,]),'FN_VARBLOCK':([153,154,],[202,204,]),'DIM_R':([155,],[205,]),'POST_VERIFY':([159,],[210,]),'EXP_NEURAL':([160,],[212,]),'DIM_AC_PREV':([161,],[214,]),'ID_LIST_R':([163,],[216,]),'NEURAL_CONDI':([180,],[225,]),'EXPRESSION_R':([189,],[227,]),'TERM_R':([191,],[231,]),'EXP_RESULT_NEURAL':([193,],[235,]),'PROC_BODY':([202,204,242,],[241,244,272,]),'ASSI_H_EXP_NEURAL':([208,209,],[245,247,]),'EXP_LIST_2':([212,],[249,]),'NEURAL_PLUS':([228,],[256,]),'NEURAL_MINUS':([229,],[258,]),'NEURAL_TIMES':([232,],[260,]),'NEURAL_DIVIDE':([233,],[262,]),'WHILE_POST_NEURAL':([237,],[265,]),'RETURN':([241,],[269,]),'PROC_BODY_R':([242,],[271,]),'LS_VARDECL':([243,315,],[274,329,]),'DIM_AC_R':([252,],[278,]),'NEURAL_EXP':([255,],[281,]),'POST_FUNC':([276,291,],[295,301,]),'FNVAR_LS':([294,317,],[303,331,]),'DECISION_ALT':([297,],[306,]),'ELSE':([297,],[307,]),'ELSE_NEURAL':([297,],[309,]),'FNVAR_LS2':([304,],[316,]),'DECISION_END_NEURAL':([306,],[319,]),'WHILE_END_NEURAL':([310,],[322,]),'DW_END_NEURAL':([311,],[324,]),'LS_VARDECL_R':([315,],[328,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> PROGRAM_K ID neural_program_id SEMICOLON BLOCK','PROGRAM',5,'p_program','new.py',183),
  ('neural_program_id -> EMPTY','neural_program_id',1,'p_neural_program_id','new.py',188),
  ('BLOCK -> VAR_BLOCK PROC_BLOCK PRINCIPAL_BLOCK','BLOCK',3,'p_block','new.py',202),
  ('VAR_BLOCK -> VARS_K BLOCKSTART VAR_DECL BLOCKEND','VAR_BLOCK',4,'p_var_block','new.py',205),
  ('VAR_DECL -> TYPE COLON VAR_LIST SEMICOLON VAR_DECL_R','VAR_DECL',5,'p_var_decl','new.py',208),
  ('VAR_DECL_R -> VAR_DECL','VAR_DECL_R',1,'p_var_decl_r','new.py',211),
  ('VAR_DECL_R -> EMPTY','VAR_DECL_R',1,'p_var_decl_r','new.py',212),
  ('VAR_LIST -> VAR VAR_LIST2','VAR_LIST',2,'p_var_list','new.py',215),
  ('VAR_LIST2 -> COMMA VAR VAR_LIST2','VAR_LIST2',3,'p_var_list2','new.py',219),
  ('VAR_LIST2 -> EMPTY','VAR_LIST2',1,'p_var_list2','new.py',220),
  ('TYPE -> INT_K NEURAL_TYPE','TYPE',2,'p_type','new.py',249),
  ('TYPE -> FLOAT_K NEURAL_TYPE','TYPE',2,'p_type','new.py',250),
  ('TYPE -> STRING_K NEURAL_TYPE','TYPE',2,'p_type','new.py',251),
  ('NEURAL_TYPE -> EMPTY','NEURAL_TYPE',1,'p_neural_type','new.py',259),
  ('PROC_BLOCK -> PROC_DECL','PROC_BLOCK',1,'p_proc_block','new.py',262),
  ('PROC_DECL -> PROC_DECL_RETURN','PROC_DECL',1,'p_proc_decl','new.py',265),
  ('PROC_DECL -> PROC_DECL_VOID','PROC_DECL',1,'p_proc_decl','new.py',266),
  ('PROC_DECL -> EMPTY','PROC_DECL',1,'p_proc_decl','new.py',267),
  ('PROC_DECL_VOID -> FUNCTION_K VOID_K ID neural_proc_void_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY BLOCKEND POST_FUNC PROC_DECL','PROC_DECL_VOID',14,'p_proc_decl_void','new.py',271),
  ('neural_proc_void_id -> EMPTY','neural_proc_void_id',1,'p_neural_proc_void_id','new.py',276),
  ('PROC_DECL_RETURN -> FUNCTION_K TYPE ID neural_proc_return_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY RETURN BLOCKEND POST_FUNC PROC_DECL','PROC_DECL_RETURN',15,'p_proc_decl_return','new.py',290),
  ('POST_FUNC -> EMPTY','POST_FUNC',1,'p_post_func','new.py',295),
  ('neural_proc_return_id -> EMPTY','neural_proc_return_id',1,'p_neural_proc_return_id','new.py',302),
  ('neural_param_decl -> EMPTY','neural_param_decl',1,'p_neural_param_decl','new.py',319),
  ('PARAM_DECL -> TYPE VAR neuro PARAM_DECL_R','PARAM_DECL',4,'p_param_decl','new.py',322),
  ('PARAM_DECL -> EMPTY','PARAM_DECL',1,'p_param_decl','new.py',323),
  ('neuro -> EMPTY','neuro',1,'p_neuro','new.py',328),
  ('PARAM_DECL_R -> COMMA PARAM_DECL','PARAM_DECL_R',2,'p_param_decl_r','new.py',345),
  ('PARAM_DECL_R -> EMPTY','PARAM_DECL_R',1,'p_param_decl_r','new.py',346),
  ('PROC_BODY -> STATEMENT PROC_BODY_R','PROC_BODY',2,'p_proc_body','new.py',349),
  ('FN_VARBLOCK -> VARS_K BLOCKSTART LS_VARDECL BLOCKEND','FN_VARBLOCK',4,'p_fn_varblock','new.py',352),
  ('LS_VARDECL -> TYPE COLON FNVAR_LS SEMICOLON LS_VARDECL_R','LS_VARDECL',5,'p_ls_vardecl','new.py',362),
  ('LS_VARDECL_R -> LS_VARDECL','LS_VARDECL_R',1,'p_ls_vardecl_r','new.py',366),
  ('LS_VARDECL_R -> EMPTY','LS_VARDECL_R',1,'p_ls_vardecl_r','new.py',367),
  ('FNVAR_LS -> VAR FNVAR_LS2','FNVAR_LS',2,'p_fnvar_ls','new.py',371),
  ('FNVAR_LS2 -> COMMA FNVAR_LS','FNVAR_LS2',2,'p_fnvar_ls2','new.py',376),
  ('FNVAR_LS2 -> EMPTY','FNVAR_LS2',1,'p_fnvar_ls2','new.py',377),
  ('PROC_BODY_R -> PROC_BODY','PROC_BODY_R',1,'p_proc_body_r','new.py',397),
  ('PROC_BODY_R -> EMPTY','PROC_BODY_R',1,'p_proc_body_r','new.py',398),
  ('STATEMENT -> ASSIGN SEMICOLON','STATEMENT',2,'p_statement','new.py',402),
  ('STATEMENT -> ASSIGN1 SEMICOLON','STATEMENT',2,'p_statement','new.py',403),
  ('STATEMENT -> FUNC_CALL SEMICOLON','STATEMENT',2,'p_statement','new.py',404),
  ('STATEMENT -> READ SEMICOLON','STATEMENT',2,'p_statement','new.py',405),
  ('STATEMENT -> WRITE SEMICOLON','STATEMENT',2,'p_statement','new.py',406),
  ('STATEMENT -> FLOW','STATEMENT',1,'p_statement','new.py',407),
  ('STATEMENT_R -> STATEMENT STATEMENT_R','STATEMENT_R',2,'p_statement_r','new.py',412),
  ('STATEMENT_R -> EMPTY','STATEMENT_R',1,'p_statement_r','new.py',413),
  ('FLOW -> DECISION','FLOW',1,'p_flow','new.py',417),
  ('FLOW -> LOOP','FLOW',1,'p_flow','new.py',418),
  ('LOOP -> WHILE_LOOP','LOOP',1,'p_loop','new.py',422),
  ('LOOP -> DO_WHILE_LOOP SEMICOLON','LOOP',2,'p_loop','new.py',423),
  ('LOOP -> FOR_LOOP','LOOP',1,'p_loop','new.py',424),
  ('DO_WHILE_LOOP -> DO_K DW_PREV_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_K LPAREN H_EXPRESSION RPAREN DW_END_NEURAL','DO_WHILE_LOOP',10,'p_do_while_loop','new.py',428),
  ('DW_PREV_NEURAL -> EMPTY','DW_PREV_NEURAL',1,'p_dw_prev_neural','new.py',432),
  ('DW_END_NEURAL -> EMPTY','DW_END_NEURAL',1,'p_dw_end_neural','new.py',437),
  ('WHILE_LOOP -> WHILE_K WHILE_PREV_NEURAL LPAREN H_EXPRESSION RPAREN WHILE_POST_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_END_NEURAL','WHILE_LOOP',10,'p_while_loop','new.py',448),
  ('WHILE_PREV_NEURAL -> EMPTY','WHILE_PREV_NEURAL',1,'p_while_prev_neural','new.py',452),
  ('WHILE_POST_NEURAL -> EMPTY','WHILE_POST_NEURAL',1,'p_while_post_neural','new.py',457),
  ('WHILE_END_NEURAL -> EMPTY','WHILE_END_NEURAL',1,'p_while_end_neural','new.py',469),
  ('FOR_LOOP -> FOR_K ID EQUALS INT TO_K INT DO_K BLOCKSTART STATEMENT_R BLOCKEND','FOR_LOOP',10,'p_for_loop','new.py',479),
  ('DECISION -> IF_K LPAREN H_EXPRESSION RPAREN EXP_RESULT_NEURAL BLOCKSTART STATEMENT_R BLOCKEND DECISION_ALT DECISION_END_NEURAL','DECISION',10,'p_decision','new.py',482),
  ('EXP_RESULT_NEURAL -> EMPTY','EXP_RESULT_NEURAL',1,'p_exp_result_neural','new.py',485),
  ('DECISION_END_NEURAL -> EMPTY','DECISION_END_NEURAL',1,'p_decision_end_neural','new.py',497),
  ('DECISION_ALT -> ELSE','DECISION_ALT',1,'p_decision_alt','new.py',502),
  ('DECISION_ALT -> EMPTY','DECISION_ALT',1,'p_decision_alt','new.py',503),
  ('ELSE -> ELSE_NEURAL ELSE_K BLOCKSTART STATEMENT_R BLOCKEND','ELSE',5,'p_else','new.py',506),
  ('ELSE_NEURAL -> EMPTY','ELSE_NEURAL',1,'p_else_neural','new.py',510),
  ('RIGHT_ASSIGN -> H_EXPRESSION','RIGHT_ASSIGN',1,'p_right_assign','new.py',519),
  ('RIGHT_ASSIGN -> FUNC_CALL','RIGHT_ASSIGN',1,'p_right_assign','new.py',520),
  ('ASSIGN -> VAR ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURAL','ASSIGN',6,'p_assign','new.py',524),
  ('ASSIGN1 -> ARR_AC ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURAL','ASSIGN1',6,'p_assign1','new.py',527),
  ('N -> EMPTY','N',1,'p_n','new.py',532),
  ('ASSI_H_EXP_NEURAL -> EMPTY','ASSI_H_EXP_NEURAL',1,'p_assi_h_exp_neural','new.py',536),
  ('EQUALS_NEURAL -> EMPTY','EQUALS_NEURAL',1,'p_equals_neural','new.py',566),
  ('ASSIGN_VAR_N -> EMPTY','ASSIGN_VAR_N',1,'p_assing_var_n','new.py',570),
  ('ARR_AC -> ID ARR_ID_NP1 DIM_AC','ARR_AC',3,'p_arr_ac','new.py',594),
  ('ARR_ID_NP1 -> EMPTY','ARR_ID_NP1',1,'p_arr_id_np1','new.py',669),
  ('DIM_AC -> LBRACE H_EXPRESSION DIM_AC_PREV RBRACE DIM_AC_R','DIM_AC',5,'p_dim_ac','new.py',703),
  ('DIM_AC_PREV -> EMPTY','DIM_AC_PREV',1,'p_dim_ac_prev','new.py',709),
  ('DIM_AC_R -> DIM_AC','DIM_AC_R',1,'p_dim_ac_r','new.py',719),
  ('DIM_AC_R -> EMPTY','DIM_AC_R',1,'p_dim_ac_r','new.py',720),
  ('VAR -> ID','VAR',1,'p_var','new.py',723),
  ('VAR -> ARRAY','VAR',1,'p_var','new.py',724),
  ('ARRAY -> ID ARR_ID_NP DIM','ARRAY',3,'p_array','new.py',732),
  ('ARR_ID_NP -> EMPTY','ARR_ID_NP',1,'p_arr_id_np','new.py',771),
  ('DIM -> LBRACE INT LIM_NP RBRACE DIM_R','DIM',5,'p_dim','new.py',781),
  ('LIM_NP -> EMPTY','LIM_NP',1,'p_lim_np','new.py',788),
  ('DIM_R -> DIM','DIM_R',1,'p_dim_r','new.py',798),
  ('DIM_R -> EMPTY','DIM_R',1,'p_dim_r','new.py',799),
  ('FUNC_CALL -> ID PRE_VERIFY LPAREN EXP_LIST POST_VERIFY RPAREN','FUNC_CALL',6,'p_func_call','new.py',805),
  ('POST_VERIFY -> EMPTY','POST_VERIFY',1,'p_post_verify','new.py',809),
  ('PRE_VERIFY -> EMPTY','PRE_VERIFY',1,'p_pre_verify','new.py',832),
  ('EXP_LIST -> H_EXPRESSION EXP_NEURAL EXP_LIST_2','EXP_LIST',3,'p_exp_list','new.py',852),
  ('EXP_NEURAL -> EMPTY','EXP_NEURAL',1,'p_exp_neural','new.py',856),
  ('EXP_LIST_2 -> COMMA EXP_LIST','EXP_LIST_2',2,'p_exp_list_2','new.py',871),
  ('EXP_LIST_2 -> EMPTY','EXP_LIST_2',1,'p_exp_list_2','new.py',872),
  ('CONSTANT -> INT','CONSTANT',1,'p_constant','new.py',876),
  ('CONSTANT -> FLOAT','CONSTANT',1,'p_constant','new.py',877),
  ('CONSTANT -> STRING','CONSTANT',1,'p_constant','new.py',878),
  ('READ -> READ_K LPAREN ID_LIST RPAREN','READ',4,'p_read','new.py',883),
  ('ID_LIST -> ID READ_NEURAL ID_LIST_R','ID_LIST',3,'p_id_list','new.py',886),
  ('READ_NEURAL -> EMPTY','READ_NEURAL',1,'p_read_neural','new.py',889),
  ('ID_LIST_R -> COMMA ID_LIST','ID_LIST_R',2,'p_id_list_r','new.py',894),
  ('ID_LIST_R -> EMPTY','ID_LIST_R',1,'p_id_list_r','new.py',895),
  ('WRITE -> WRITE_K LPAREN WRITE_LIST RPAREN','WRITE',4,'p_write','new.py',898),
  ('WRITE_LIST -> RIGHT_ASSIGN WRITE_LIST_R','WRITE_LIST',2,'p_write_list','new.py',901),
  ('WRITE_LIST -> CONSTANT CONSTANT_WRITE_N WRITE_LIST_R','WRITE_LIST',3,'p_write_list','new.py',902),
  ('CONSTANT_WRITE_N -> EMPTY','CONSTANT_WRITE_N',1,'p_constant_write_n','new.py',905),
  ('WRITE_LIST_R -> WRITE_NEURAL COMMA WRITE_LIST','WRITE_LIST_R',3,'p_write_list_r','new.py',912),
  ('WRITE_LIST_R -> WRITE_NEURAL EMPTY','WRITE_LIST_R',2,'p_write_list_r','new.py',913),
  ('WRITE_NEURAL -> EMPTY','WRITE_NEURAL',1,'p_write_neural','new.py',916),
  ('RETURN -> RETURN_K LPAREN H_EXPRESSION RPAREN SEMICOLON','RETURN',5,'p_return','new.py',923),
  ('EXPRESSION -> TERM NEURAL_EXPRESSION EXPRESSION_R','EXPRESSION',3,'p_expression','new.py',928),
  ('NEURAL_EXPRESSION -> EMPTY','NEURAL_EXPRESSION',1,'p_neural_expression','new.py',933),
  ('EXPRESSION_R -> PLUS NEURAL_PLUS EXPRESSION','EXPRESSION_R',3,'p_expression_r','new.py',962),
  ('EXPRESSION_R -> MINUS NEURAL_MINUS EXPRESSION','EXPRESSION_R',3,'p_expression_r','new.py',963),
  ('EXPRESSION_R -> EMPTY','EXPRESSION_R',1,'p_expression_r','new.py',964),
  ('NEURAL_PLUS -> EMPTY','NEURAL_PLUS',1,'p_neural_plus','new.py',968),
  ('NEURAL_MINUS -> EMPTY','NEURAL_MINUS',1,'p_neural_minus','new.py',974),
  ('TERM -> FACTOR NEURAL_TERM TERM_R','TERM',3,'p_term','new.py',979),
  ('NEURAL_TERM -> EMPTY','NEURAL_TERM',1,'p_neural_term','new.py',983),
  ('TERM_R -> TIMES NEURAL_TIMES TERM','TERM_R',3,'p_term_r','new.py',1011),
  ('TERM_R -> DIVIDE NEURAL_DIVIDE TERM','TERM_R',3,'p_term_r','new.py',1012),
  ('TERM_R -> EMPTY','TERM_R',1,'p_term_r','new.py',1013),
  ('NEURAL_TIMES -> EMPTY','NEURAL_TIMES',1,'p_neural_times','new.py',1017),
  ('NEURAL_DIVIDE -> EMPTY','NEURAL_DIVIDE',1,'p_neural_divide','new.py',1022),
  ('FACTOR -> ID NEURAL_ID_FAC','FACTOR',2,'p_factor_','new.py',1027),
  ('FACTOR -> CONSTANT NEURAL_CNT_FACT','FACTOR',2,'p_factor_','new.py',1028),
  ('FACTOR -> LPAREN H_EXPRESSION RPAREN','FACTOR',3,'p_factor_','new.py',1029),
  ('NEURAL_ID_FAC -> EMPTY','NEURAL_ID_FAC',1,'p_neural_id_fac','new.py',1033),
  ('NEURAL_CNT_FACT -> EMPTY','NEURAL_CNT_FACT',1,'p_neural_cnt_fact','new.py',1057),
  ('S_EXPRESSION -> EXPRESSION S_EXPRESSION_R','S_EXPRESSION',2,'p_s_expression','new.py',1083),
  ('NEURAL_EXP -> EMPTY','NEURAL_EXP',1,'p_neural_exp','new.py',1087),
  ('S_EXPRESSION_R -> CONDI NEURAL_CONDI EXPRESSION NEURAL_EXP','S_EXPRESSION_R',4,'p_s_expression_r','new.py',1113),
  ('S_EXPRESSION_R -> EMPTY','S_EXPRESSION_R',1,'p_s_expression_r','new.py',1114),
  ('NEURAL_CONDI -> EMPTY','NEURAL_CONDI',1,'p_neural_condi','new.py',1118),
  ('CONDI -> GT','CONDI',1,'p_condi','new.py',1125),
  ('CONDI -> LT','CONDI',1,'p_condi','new.py',1126),
  ('CONDI -> LTE','CONDI',1,'p_condi','new.py',1127),
  ('CONDI -> GTE','CONDI',1,'p_condi','new.py',1128),
  ('CONDI -> DOUBLEEQUAL','CONDI',1,'p_condi','new.py',1129),
  ('CONDI -> AND','CONDI',1,'p_condi','new.py',1130),
  ('CONDI -> OR','CONDI',1,'p_condi','new.py',1131),
  ('H_EXPRESSION -> S_EXPRESSION H_EXPRESSION_R','H_EXPRESSION',2,'p_h_expression','new.py',1140),
  ('H_EXPRESSION_R -> OR H_EXPRESSION','H_EXPRESSION_R',2,'p_h_expression_r','new.py',1144),
  ('H_EXPRESSION_R -> AND H_EXPRESSION','H_EXPRESSION_R',2,'p_h_expression_r','new.py',1145),
  ('H_EXPRESSION_R -> EMPTY','H_EXPRESSION_R',1,'p_h_expression_r','new.py',1146),
  ('PRINCIPAL_BLOCK -> MAIN_K MAIN_NEURAL LPAREN RPAREN BLOCKSTART PRINCIPAL_BODY BLOCKEND','PRINCIPAL_BLOCK',7,'p_principal_block','new.py',1150),
  ('MAIN_NEURAL -> EMPTY','MAIN_NEURAL',1,'p_main_neural','new.py',1154),
  ('PRINCIPAL_BODY -> STATEMENT PRINCIPAL_BODY_R','PRINCIPAL_BODY',2,'p_principal_body','new.py',1164),
  ('PRINCIPAL_BODY -> EMPTY','PRINCIPAL_BODY',1,'p_principal_body','new.py',1165),
  ('PRINCIPAL_BODY_R -> PRINCIPAL_BODY','PRINCIPAL_BODY_R',1,'p_principal_body_r','new.py',1169),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','new.py',1172),
]
