#ifdef ___LINKER_INFO
; File: "main.c", produced by Gambit v4.9.3
(
409003
(C)
"main"
(("main"))
(
"main"
)
(
)
(
"arr"
"f-scheme"
"good"
"input"
"len"
"main#"
"main#0"
)
(
)
(
"+"
"<"
"="
"bitwise-and"
"bitwise-xor"
"char->integer"
"display"
"list-ref"
"not"
"read-line"
"string-length"
"string-ref"
)
 ()
)
#else
#define ___VERSION 409003
#define ___MODULE_NAME "main"
#define ___LINKER_ID ___LNK_main
#define ___MH_PROC ___H_main
#define ___SCRIPT_LINE 0
#define ___SYMCOUNT 1
#define ___GLOCOUNT 19
#define ___SUPCOUNT 7
#define ___CNSCOUNT 40
#define ___SUBCOUNT 4
#define ___LBLCOUNT 29
#define ___MODDESCR ___REF_SUB(3)
#include "gambit.h"

___NEED_SYM(___S_main)

___NEED_GLO(___G__2b_)
___NEED_GLO(___G__3c_)
___NEED_GLO(___G__3d_)
___NEED_GLO(___G_arr)
___NEED_GLO(___G_bitwise_2d_and)
___NEED_GLO(___G_bitwise_2d_xor)
___NEED_GLO(___G_char_2d__3e_integer)
___NEED_GLO(___G_display)
___NEED_GLO(___G_f_2d_scheme)
___NEED_GLO(___G_good)
___NEED_GLO(___G_input)
___NEED_GLO(___G_len)
___NEED_GLO(___G_list_2d_ref)
___NEED_GLO(___G_main_23_)
___NEED_GLO(___G_main_23_0)
___NEED_GLO(___G_not)
___NEED_GLO(___G_read_2d_line)
___NEED_GLO(___G_string_2d_length)
___NEED_GLO(___G_string_2d_ref)

___BEGIN_SYM
___DEF_SYM(0,___S_main,"main")
___END_SYM

#define ___SYM_main ___SYM(0,___S_main)

___BEGIN_GLO
___DEF_GLO(0,"arr")
___DEF_GLO(1,"f-scheme")
___DEF_GLO(2,"good")
___DEF_GLO(3,"input")
___DEF_GLO(4,"len")
___DEF_GLO(5,"main#")
___DEF_GLO(6,"main#0")
___DEF_GLO(7,"+")
___DEF_GLO(8,"<")
___DEF_GLO(9,"=")
___DEF_GLO(10,"bitwise-and")
___DEF_GLO(11,"bitwise-xor")
___DEF_GLO(12,"char->integer")
___DEF_GLO(13,"display")
___DEF_GLO(14,"list-ref")
___DEF_GLO(15,"not")
___DEF_GLO(16,"read-line")
___DEF_GLO(17,"string-length")
___DEF_GLO(18,"string-ref")
___END_GLO

#define ___GLO_arr ___GLO(0,___G_arr)
#define ___PRM_arr ___PRM(0,___G_arr)
#define ___GLO_f_2d_scheme ___GLO(1,___G_f_2d_scheme)
#define ___PRM_f_2d_scheme ___PRM(1,___G_f_2d_scheme)
#define ___GLO_good ___GLO(2,___G_good)
#define ___PRM_good ___PRM(2,___G_good)
#define ___GLO_input ___GLO(3,___G_input)
#define ___PRM_input ___PRM(3,___G_input)
#define ___GLO_len ___GLO(4,___G_len)
#define ___PRM_len ___PRM(4,___G_len)
#define ___GLO_main_23_ ___GLO(5,___G_main_23_)
#define ___PRM_main_23_ ___PRM(5,___G_main_23_)
#define ___GLO_main_23_0 ___GLO(6,___G_main_23_0)
#define ___PRM_main_23_0 ___PRM(6,___G_main_23_0)
#define ___GLO__2b_ ___GLO(7,___G__2b_)
#define ___PRM__2b_ ___PRM(7,___G__2b_)
#define ___GLO__3c_ ___GLO(8,___G__3c_)
#define ___PRM__3c_ ___PRM(8,___G__3c_)
#define ___GLO__3d_ ___GLO(9,___G__3d_)
#define ___PRM__3d_ ___PRM(9,___G__3d_)
#define ___GLO_bitwise_2d_and ___GLO(10,___G_bitwise_2d_and)
#define ___PRM_bitwise_2d_and ___PRM(10,___G_bitwise_2d_and)
#define ___GLO_bitwise_2d_xor ___GLO(11,___G_bitwise_2d_xor)
#define ___PRM_bitwise_2d_xor ___PRM(11,___G_bitwise_2d_xor)
#define ___GLO_char_2d__3e_integer ___GLO(12,___G_char_2d__3e_integer)
#define ___PRM_char_2d__3e_integer ___PRM(12,___G_char_2d__3e_integer)
#define ___GLO_display ___GLO(13,___G_display)
#define ___PRM_display ___PRM(13,___G_display)
#define ___GLO_list_2d_ref ___GLO(14,___G_list_2d_ref)
#define ___PRM_list_2d_ref ___PRM(14,___G_list_2d_ref)
#define ___GLO_not ___GLO(15,___G_not)
#define ___PRM_not ___PRM(15,___G_not)
#define ___GLO_read_2d_line ___GLO(16,___G_read_2d_line)
#define ___PRM_read_2d_line ___PRM(16,___G_read_2d_line)
#define ___GLO_string_2d_length ___GLO(17,___G_string_2d_length)
#define ___PRM_string_2d_length ___PRM(17,___G_string_2d_length)
#define ___GLO_string_2d_ref ___GLO(18,___G_string_2d_ref)
#define ___PRM_string_2d_ref ___PRM(18,___G_string_2d_ref)

___BEGIN_CNS
 ___DEF_CNS(___REF_FIX(106),___REF_CNS(1))
,___DEF_CNS(___REF_FIX(117),___REF_CNS(2))
,___DEF_CNS(___REF_FIX(84),___REF_CNS(3))
,___DEF_CNS(___REF_FIX(121),___REF_CNS(4))
,___DEF_CNS(___REF_FIX(119),___REF_CNS(5))
,___DEF_CNS(___REF_FIX(83),___REF_CNS(6))
,___DEF_CNS(___REF_FIX(90),___REF_CNS(7))
,___DEF_CNS(___REF_FIX(52),___REF_CNS(8))
,___DEF_CNS(___REF_FIX(54),___REF_CNS(9))
,___DEF_CNS(___REF_FIX(20),___REF_CNS(10))
,___DEF_CNS(___REF_FIX(15),___REF_CNS(11))
,___DEF_CNS(___REF_FIX(205),___REF_CNS(12))
,___DEF_CNS(___REF_FIX(201),___REF_CNS(13))
,___DEF_CNS(___REF_FIX(163),___REF_CNS(14))
,___DEF_CNS(___REF_FIX(151),___REF_CNS(15))
,___DEF_CNS(___REF_FIX(118),___REF_CNS(16))
,___DEF_CNS(___REF_FIX(70),___REF_CNS(17))
,___DEF_CNS(___REF_FIX(52),___REF_CNS(18))
,___DEF_CNS(___REF_FIX(52),___REF_CNS(19))
,___DEF_CNS(___REF_FIX(230),___REF_CNS(20))
,___DEF_CNS(___REF_FIX(211),___REF_CNS(21))
,___DEF_CNS(___REF_FIX(135),___REF_CNS(22))
,___DEF_CNS(___REF_FIX(125),___REF_CNS(23))
,___DEF_CNS(___REF_FIX(29),___REF_CNS(24))
,___DEF_CNS(___REF_FIX(0),___REF_CNS(25))
,___DEF_CNS(___REF_FIX(206),___REF_CNS(26))
,___DEF_CNS(___REF_FIX(178),___REF_CNS(27))
,___DEF_CNS(___REF_FIX(124),___REF_CNS(28))
,___DEF_CNS(___REF_FIX(20),___REF_CNS(29))
,___DEF_CNS(___REF_FIX(242),___REF_CNS(30))
,___DEF_CNS(___REF_FIX(162),___REF_CNS(31))
,___DEF_CNS(___REF_FIX(103),___REF_CNS(32))
,___DEF_CNS(___REF_FIX(28),___REF_CNS(33))
,___DEF_CNS(___REF_FIX(255),___REF_CNS(34))
,___DEF_CNS(___REF_FIX(164),___REF_CNS(35))
,___DEF_CNS(___REF_FIX(124),___REF_CNS(36))
,___DEF_CNS(___REF_FIX(60),___REF_CNS(37))
,___DEF_CNS(___REF_FIX(153),___REF_CNS(38))
,___DEF_CNS(___REF_FIX(204),___REF_CNS(39))
,___DEF_CNS(___REF_FIX(125),___REF_NUL)
___END_CNS

___DEF_SUB_STR(___X0,10UL)
               ___STR8(80,97,115,115,119,111,114,100)
               ___STR2(58,32)
___DEF_SUB_STR(___X1,9UL)
               ___STR8(67,111,114,114,101,99,116,33)
               ___STR1(10)
___DEF_SUB_STR(___X2,7UL)
               ___STR7(87,114,111,110,103,33,10)
___DEF_SUB_VEC(___X3,5UL)
               ___VEC1(___REF_SYM(0,___S_main))
               ___VEC1(___REF_PRC(1))
               ___VEC1(___REF_FIX(1))
               ___VEC1(___REF_NUL)
               ___VEC1(___REF_FAL)
               ___VEC0

___BEGIN_SUB
 ___DEF_SUB(___X0)
,___DEF_SUB(___X1)
,___DEF_SUB(___X2)
,___DEF_SUB(___X3)
___END_SUB



  int f(int n) {
      return n * n + 2 * n + 3;
  }

#undef ___MD_ALL
#define ___MD_ALL ___D_FP ___D_R0 ___D_R1 ___D_R2 ___D_R4 ___D_F64(___F64V1) ___D_F64(___F64V2)
#undef ___MR_ALL
#define ___MR_ALL ___R_FP ___R_R0 ___R_R1 ___R_R2 ___R_R4
#undef ___MW_ALL
#define ___MW_ALL ___W_FP ___W_R0 ___W_R1 ___W_R2 ___W_R4
___BEGIN_M_COD
___BEGIN_M_HLBL
___DEF_M_HLBL_INTRO
___DEF_M_HLBL(___L0_main_23_)
___DEF_M_HLBL(___L1_main_23_)
___DEF_M_HLBL(___L2_main_23_)
___DEF_M_HLBL(___L3_main_23_)
___DEF_M_HLBL(___L4_main_23_)
___DEF_M_HLBL(___L5_main_23_)
___DEF_M_HLBL(___L6_main_23_)
___DEF_M_HLBL(___L7_main_23_)
___DEF_M_HLBL(___L8_main_23_)
___DEF_M_HLBL(___L9_main_23_)
___DEF_M_HLBL(___L10_main_23_)
___DEF_M_HLBL(___L11_main_23_)
___DEF_M_HLBL(___L12_main_23_)
___DEF_M_HLBL(___L13_main_23_)
___DEF_M_HLBL(___L14_main_23_)
___DEF_M_HLBL(___L15_main_23_)
___DEF_M_HLBL(___L16_main_23_)
___DEF_M_HLBL(___L17_main_23_)
___DEF_M_HLBL(___L18_main_23_)
___DEF_M_HLBL(___L19_main_23_)
___DEF_M_HLBL(___L20_main_23_)
___DEF_M_HLBL(___L21_main_23_)
___DEF_M_HLBL(___L22_main_23_)
___DEF_M_HLBL(___L23_main_23_)
___DEF_M_HLBL(___L24_main_23_)
___DEF_M_HLBL_INTRO
___DEF_M_HLBL(___L0_main_23_0)
___DEF_M_HLBL(___L1_main_23_0)
___END_M_HLBL

___BEGIN_M_SW

#undef ___PH_PROC
#define ___PH_PROC ___H_main_23_
#undef ___PH_LBL0
#define ___PH_LBL0 1
#undef ___PD_ALL
#define ___PD_ALL ___D_FP ___D_R0 ___D_R1 ___D_R2 ___D_R4 ___D_F64(___F64V1) ___D_F64(___F64V2)
#undef ___PR_ALL
#define ___PR_ALL ___R_FP ___R_R0 ___R_R1 ___R_R2 ___R_R4
#undef ___PW_ALL
#define ___PW_ALL ___W_FP ___W_R0 ___W_R1 ___W_R2 ___W_R4
___BEGIN_P_COD
___BEGIN_P_HLBL
___DEF_P_HLBL_INTRO
___DEF_P_HLBL(___L0_main_23_)
___DEF_P_HLBL(___L1_main_23_)
___DEF_P_HLBL(___L2_main_23_)
___DEF_P_HLBL(___L3_main_23_)
___DEF_P_HLBL(___L4_main_23_)
___DEF_P_HLBL(___L5_main_23_)
___DEF_P_HLBL(___L6_main_23_)
___DEF_P_HLBL(___L7_main_23_)
___DEF_P_HLBL(___L8_main_23_)
___DEF_P_HLBL(___L9_main_23_)
___DEF_P_HLBL(___L10_main_23_)
___DEF_P_HLBL(___L11_main_23_)
___DEF_P_HLBL(___L12_main_23_)
___DEF_P_HLBL(___L13_main_23_)
___DEF_P_HLBL(___L14_main_23_)
___DEF_P_HLBL(___L15_main_23_)
___DEF_P_HLBL(___L16_main_23_)
___DEF_P_HLBL(___L17_main_23_)
___DEF_P_HLBL(___L18_main_23_)
___DEF_P_HLBL(___L19_main_23_)
___DEF_P_HLBL(___L20_main_23_)
___DEF_P_HLBL(___L21_main_23_)
___DEF_P_HLBL(___L22_main_23_)
___DEF_P_HLBL(___L23_main_23_)
___DEF_P_HLBL(___L24_main_23_)
___END_P_HLBL
___BEGIN_P_SW
___DEF_SLBL(0,___L0_main_23_)
   ___IF_NARGS_EQ(0,___NOTHING)
   ___WRONG_NARGS(0,0,0,0)
___DEF_GLBL(___L_main_23_)
   ___SET_GLO(1,___G_f_2d_scheme,___PRC(27))
   ___SET_GLO(0,___G_arr,___CNS(0))
   ___SET_STK(1,___R0)
   ___SET_R1(___SUB(0))
   ___ADJFP(4)
   ___POLL(1)
___DEF_SLBL(1,___L1_main_23_)
   ___SET_R0(___LBL(2))
   ___JUMPGLOSAFE(___SET_NARGS(1),13,___G_display)
___DEF_SLBL(2,___L2_main_23_)
   ___SET_R0(___LBL(3))
   ___JUMPGLOSAFE(___SET_NARGS(0),16,___G_read_2d_line)
___DEF_SLBL(3,___L3_main_23_)
   ___SET_GLO(3,___G_input,___R1)
   ___SET_GLO(2,___G_good,___FIX(1L))
   ___SET_STK(-2,___GLO_input)
   ___IF(___NOT(___EQP(___GLO_string_2d_length,___PRM_string_2d_length)))
   ___GOTO(___L57_main_23_)
   ___END_IF
   ___IF(___NOT(___STRINGP(___STK(-2))))
   ___GOTO(___L57_main_23_)
   ___END_IF
   ___SET_R1(___STRINGLENGTH(___STK(-2)))
   ___GOTO(___L25_main_23_)
___DEF_SLBL(4,___L4_main_23_)
___DEF_GLBL(___L25_main_23_)
   ___SET_GLO(4,___G_len,___R1)
   ___SET_STK(-2,___GLO_len)
   ___IF(___NOT(___EQP(___GLO__3d_,___PRM__3d_)))
   ___GOTO(___L56_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-2))))
   ___GOTO(___L56_main_23_)
   ___END_IF
   ___SET_R1(___BOOLEAN(___FIXEQ(___STK(-2),___FIX(40L))))
   ___IF(___NOT(___EQP(___GLO_not,___PRM_not)))
   ___GOTO(___L55_main_23_)
   ___END_IF
___DEF_GLBL(___L26_main_23_)
   ___IF(___NOT(___NOTFALSEP(___R1)))
   ___GOTO(___L54_main_23_)
   ___END_IF
___DEF_GLBL(___L27_main_23_)
   ___SET_R1(___FIX(0L))
   ___SET_R0(___LBL(19))
___DEF_GLBL(___L28_main_23_)
   ___SET_STK(1,___GLO_len)
   ___ADJFP(1)
   ___IF(___NOT(___EQP(___GLO__3c_,___PRM__3c_)))
   ___GOTO(___L49_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(0))))
   ___GOTO(___L48_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___R1)))
   ___GOTO(___L48_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXLT(___R1,___STK(0))))
   ___GOTO(___L46_main_23_)
   ___END_IF
___DEF_GLBL(___L29_main_23_)
   ___SET_STK(0,___R0)
   ___SET_STK(1,___R1)
   ___SET_R2(___R1)
   ___SET_R1(___GLO_arr)
   ___ADJFP(7)
   ___POLL(5)
___DEF_SLBL(5,___L5_main_23_)
   ___SET_R0(___LBL(6))
   ___JUMPGLOSAFE(___SET_NARGS(2),14,___G_list_2d_ref)
___DEF_SLBL(6,___L6_main_23_)
   ___SET_STK(-5,___R1)
   ___SET_R1(___STK(-6))
   ___SET_R0(___LBL(7))
   ___JUMPGLOSAFE(___SET_NARGS(1),1,___G_f_2d_scheme)
___DEF_SLBL(7,___L7_main_23_)
   ___IF(___NOT(___EQP(___GLO_bitwise_2d_and,___PRM_bitwise_2d_and)))
   ___GOTO(___L45_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___R1)))
   ___GOTO(___L45_main_23_)
   ___END_IF
   ___SET_R1(___FIXAND(___R1,___FIX(255L)))
   ___GOTO(___L30_main_23_)
___DEF_SLBL(8,___L8_main_23_)
___DEF_GLBL(___L30_main_23_)
   ___SET_STK(-4,___R1)
   ___SET_STK(-3,___GLO_input)
   ___IF(___NOT(___EQP(___GLO_string_2d_ref,___PRM_string_2d_ref)))
   ___GOTO(___L44_main_23_)
   ___END_IF
   ___IF(___NOT(___STRINGP(___STK(-3))))
   ___GOTO(___L44_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-6))))
   ___GOTO(___L44_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXLE(___FIX(0L),___STK(-6))))
   ___GOTO(___L44_main_23_)
   ___END_IF
   ___SET_R1(___STRINGLENGTH(___STK(-3)))
   ___IF(___NOT(___FIXLT(___STK(-6),___R1)))
   ___GOTO(___L44_main_23_)
   ___END_IF
   ___SET_R1(___STRINGREF(___STK(-3),___STK(-6)))
   ___SET_R0(___LBL(9))
   ___JUMPGLOSAFE(___SET_NARGS(1),12,___G_char_2d__3e_integer)
___DEF_SLBL(9,___L9_main_23_)
   ___IF(___NOT(___EQP(___GLO_bitwise_2d_xor,___PRM_bitwise_2d_xor)))
   ___GOTO(___L43_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___R1)))
   ___GOTO(___L43_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-4))))
   ___GOTO(___L43_main_23_)
   ___END_IF
   ___SET_R1(___FIXXOR(___STK(-4),___R1))
   ___IF(___EQP(___GLO__3d_,___PRM__3d_))
   ___GOTO(___L31_main_23_)
   ___END_IF
   ___GOTO(___L42_main_23_)
___DEF_SLBL(10,___L10_main_23_)
   ___IF(___NOT(___EQP(___GLO__3d_,___PRM__3d_)))
   ___GOTO(___L42_main_23_)
   ___END_IF
___DEF_GLBL(___L31_main_23_)
   ___IF(___NOT(___FIXNUMP(___R1)))
   ___GOTO(___L40_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-5))))
   ___GOTO(___L40_main_23_)
   ___END_IF
   ___SET_R1(___BOOLEAN(___FIXEQ(___STK(-5),___R1)))
   ___IF(___NOT(___EQP(___GLO_not,___PRM_not)))
   ___GOTO(___L41_main_23_)
   ___END_IF
___DEF_GLBL(___L32_main_23_)
   ___IF(___NOT(___NOTFALSEP(___R1)))
   ___GOTO(___L39_main_23_)
   ___END_IF
___DEF_GLBL(___L33_main_23_)
   ___SET_STK(-5,___GLO_good)
   ___IF(___NOT(___EQP(___GLO__3d_,___PRM__3d_)))
   ___GOTO(___L38_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-5))))
   ___GOTO(___L38_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXEQ(___STK(-5),___FIX(1L))))
   ___GOTO(___L37_main_23_)
   ___END_IF
___DEF_GLBL(___L34_main_23_)
   ___IF(___NOT(___EQP(___GLO__2b_,___PRM__2b_)))
   ___GOTO(___L36_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-6))))
   ___GOTO(___L36_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXADDP_NOTFALSEP(___R1,___STK(-6),___FIX(1L))))
   ___SET_R1(___FAL)
   ___GOTO(___L36_main_23_)
   ___END_IF
   ___ADJFP(-4)
___DEF_GLBL(___L35_main_23_)
   ___SET_R0(___STK(-3))
   ___ADJFP(-4)
   ___POLL(11)
___DEF_SLBL(11,___L11_main_23_)
   ___GOTO(___L28_main_23_)
___DEF_GLBL(___L36_main_23_)
   ___SET_R1(___STK(-6))
   ___SET_R2(___FIX(1L))
   ___SET_R0(___LBL(12))
   ___ADJFP(-4)
   ___JUMPGLOSAFE(___SET_NARGS(2),7,___G__2b_)
___DEF_SLBL(12,___L12_main_23_)
   ___GOTO(___L35_main_23_)
___DEF_SLBL(13,___L13_main_23_)
   ___IF(___NOTFALSEP(___R1))
   ___GOTO(___L34_main_23_)
   ___END_IF
___DEF_GLBL(___L37_main_23_)
   ___SET_R1(___VOID)
   ___ADJFP(-8)
   ___JUMPPRM(___NOTHING,___STK(1))
___DEF_GLBL(___L38_main_23_)
   ___SET_R1(___STK(-5))
   ___SET_R2(___FIX(1L))
   ___SET_R0(___LBL(13))
   ___JUMPGLOSAFE(___SET_NARGS(2),9,___G__3d_)
___DEF_SLBL(14,___L14_main_23_)
   ___IF(___NOT(___NOTFALSEP(___R1)))
   ___GOTO(___L33_main_23_)
   ___END_IF
___DEF_GLBL(___L39_main_23_)
   ___SET_GLO(2,___G_good,___FIX(0L))
   ___GOTO(___L33_main_23_)
___DEF_GLBL(___L40_main_23_)
   ___IF(___NOT(___FLONUMP(___R1)))
   ___GOTO(___L42_main_23_)
   ___END_IF
   ___IF(___NOT(___FLONUMP(___STK(-5))))
   ___GOTO(___L42_main_23_)
   ___END_IF
   ___SET_F64(___F64V1,___F64UNBOX(___STK(-5)))
   ___SET_F64(___F64V2,___F64UNBOX(___R1))
   ___SET_R1(___BOOLEAN(___F64EQ(___F64V1,___F64V2)))
   ___IF(___EQP(___GLO_not,___PRM_not))
   ___GOTO(___L32_main_23_)
   ___END_IF
___DEF_GLBL(___L41_main_23_)
   ___SET_R0(___LBL(14))
   ___JUMPGLOSAFE(___SET_NARGS(1),15,___G_not)
___DEF_GLBL(___L42_main_23_)
   ___SET_R2(___R1)
   ___SET_R1(___STK(-5))
   ___SET_R0(___LBL(15))
   ___JUMPGLOSAFE(___SET_NARGS(2),9,___G__3d_)
___DEF_SLBL(15,___L15_main_23_)
   ___IF(___EQP(___GLO_not,___PRM_not))
   ___GOTO(___L32_main_23_)
   ___END_IF
   ___GOTO(___L41_main_23_)
___DEF_GLBL(___L43_main_23_)
   ___SET_R2(___R1)
   ___SET_R1(___STK(-4))
   ___SET_R0(___LBL(10))
   ___JUMPGLOSAFE(___SET_NARGS(2),11,___G_bitwise_2d_xor)
___DEF_GLBL(___L44_main_23_)
   ___SET_R2(___STK(-6))
   ___SET_R1(___STK(-3))
   ___SET_R0(___LBL(16))
   ___JUMPGLOSAFE(___SET_NARGS(2),18,___G_string_2d_ref)
___DEF_SLBL(16,___L16_main_23_)
   ___SET_R0(___LBL(9))
   ___JUMPGLOSAFE(___SET_NARGS(1),12,___G_char_2d__3e_integer)
___DEF_GLBL(___L45_main_23_)
   ___SET_R2(___FIX(255L))
   ___SET_R0(___LBL(8))
   ___JUMPGLOSAFE(___SET_NARGS(2),10,___G_bitwise_2d_and)
___DEF_SLBL(17,___L17_main_23_)
   ___IF(___NOTFALSEP(___R1))
   ___GOTO(___L47_main_23_)
   ___END_IF
   ___SET_R0(___STK(-6))
   ___ADJFP(-7)
___DEF_GLBL(___L46_main_23_)
   ___SET_R1(___TRU)
   ___ADJFP(-1)
   ___JUMPPRM(___NOTHING,___R0)
___DEF_GLBL(___L47_main_23_)
   ___SET_R1(___STK(-5))
   ___SET_R0(___STK(-6))
   ___ADJFP(-7)
   ___GOTO(___L29_main_23_)
___DEF_GLBL(___L48_main_23_)
   ___IF(___NOT(___FLONUMP(___STK(0))))
   ___GOTO(___L49_main_23_)
   ___END_IF
   ___IF(___NOT(___FLONUMP(___R1)))
   ___GOTO(___L49_main_23_)
   ___END_IF
   ___SET_F64(___F64V1,___F64UNBOX(___R1))
   ___SET_F64(___F64V2,___F64UNBOX(___STK(0)))
   ___IF(___F64LT(___F64V1,___F64V2))
   ___GOTO(___L29_main_23_)
   ___END_IF
   ___GOTO(___L46_main_23_)
___DEF_GLBL(___L49_main_23_)
   ___SET_STK(1,___R0)
   ___SET_STK(2,___R1)
   ___SET_R2(___STK(0))
   ___ADJFP(7)
   ___POLL(18)
___DEF_SLBL(18,___L18_main_23_)
   ___SET_R0(___LBL(17))
   ___JUMPGLOSAFE(___SET_NARGS(2),8,___G__3c_)
___DEF_SLBL(19,___L19_main_23_)
   ___SET_STK(-2,___GLO_good)
   ___IF(___NOT(___EQP(___GLO__3d_,___PRM__3d_)))
   ___GOTO(___L53_main_23_)
   ___END_IF
   ___IF(___NOT(___FIXNUMP(___STK(-2))))
   ___GOTO(___L53_main_23_)
   ___END_IF
   ___IF(___FIXEQ(___STK(-2),___FIX(1L)))
   ___GOTO(___L50_main_23_)
   ___END_IF
   ___GOTO(___L52_main_23_)
___DEF_SLBL(20,___L20_main_23_)
   ___IF(___NOT(___NOTFALSEP(___R1)))
   ___GOTO(___L52_main_23_)
   ___END_IF
___DEF_GLBL(___L50_main_23_)
   ___SET_R1(___SUB(1))
   ___SET_R0(___STK(-3))
   ___POLL(21)
___DEF_SLBL(21,___L21_main_23_)
___DEF_GLBL(___L51_main_23_)
   ___ADJFP(-4)
   ___JUMPGLOSAFE(___SET_NARGS(1),13,___G_display)
___DEF_GLBL(___L52_main_23_)
   ___SET_R1(___SUB(2))
   ___SET_R0(___STK(-3))
   ___POLL(22)
___DEF_SLBL(22,___L22_main_23_)
   ___GOTO(___L51_main_23_)
___DEF_GLBL(___L53_main_23_)
   ___SET_R1(___STK(-2))
   ___SET_R2(___FIX(1L))
   ___SET_R0(___LBL(20))
   ___JUMPGLOSAFE(___SET_NARGS(2),9,___G__3d_)
___DEF_SLBL(23,___L23_main_23_)
   ___IF(___NOT(___NOTFALSEP(___R1)))
   ___GOTO(___L27_main_23_)
   ___END_IF
___DEF_GLBL(___L54_main_23_)
   ___SET_GLO(2,___G_good,___FIX(0L))
   ___GOTO(___L27_main_23_)
___DEF_SLBL(24,___L24_main_23_)
   ___IF(___EQP(___GLO_not,___PRM_not))
   ___GOTO(___L26_main_23_)
   ___END_IF
___DEF_GLBL(___L55_main_23_)
   ___SET_R0(___LBL(23))
   ___JUMPGLOSAFE(___SET_NARGS(1),15,___G_not)
___DEF_GLBL(___L56_main_23_)
   ___SET_R1(___STK(-2))
   ___SET_R2(___FIX(40L))
   ___SET_R0(___LBL(24))
   ___JUMPGLOSAFE(___SET_NARGS(2),9,___G__3d_)
___DEF_GLBL(___L57_main_23_)
   ___SET_R1(___STK(-2))
   ___SET_R0(___LBL(4))
   ___JUMPGLOSAFE(___SET_NARGS(1),17,___G_string_2d_length)
___END_P_SW
___END_P_COD

#undef ___PH_PROC
#define ___PH_PROC ___H_main_23_0
#undef ___PH_LBL0
#define ___PH_LBL0 27
#undef ___PD_ALL
#define ___PD_ALL ___D_FP ___D_R0 ___D_R1 ___D_F64(___F64V1) ___D_F64(___F64V2)
#undef ___PR_ALL
#define ___PR_ALL ___R_FP ___R_R0 ___R_R1
#undef ___PW_ALL
#define ___PW_ALL ___W_FP ___W_R0
___BEGIN_P_COD
___BEGIN_P_HLBL
___DEF_P_HLBL_INTRO
___DEF_P_HLBL(___L0_main_23_0)
___DEF_P_HLBL(___L1_main_23_0)
___END_P_HLBL
___BEGIN_P_SW
___DEF_SLBL(0,___L0_main_23_0)
   ___IF_NARGS_EQ(1,___NOTHING)
   ___WRONG_NARGS(0,1,0,0)
___DEF_GLBL(___L_main_23_0)
   ___SET_STK(1,___R1)
   ___SET_STK(2,___R0)
   ___SET_R0(___LBL(1))
   ___ADJFP(8)
#define ___NARGS 1
___BEGIN_CFUN(int ___result)
#define ___ARG1 ___CFUN_ARG(1)
___BEGIN_CFUN_ARG(1,int ___arg1)
___BEGIN_CFUN_SCMOBJ_TO_INT(___ARG1,___arg1,1)
___BEGIN_CFUN_BODY
#undef ___AT_END
___CFUN_ASSIGN(___result,f(___arg1))
#ifndef ___AT_END
#define ___AT_END
#endif
___BEGIN_CFUN_INT_TO_SCMOBJ(___result,___CFUN_RESULT)
___CFUN_SET_RESULT
___END_CFUN_INT_TO_SCMOBJ(___result,___CFUN_RESULT)
___END_CFUN_BODY
___END_CFUN_SCMOBJ_TO_INT(___ARG1,___arg1,1)
___END_CFUN_ARG(1)
#undef ___ARG1
___CFUN_ERROR
___END_CFUN
#undef ___NARGS
   ___JUMPPRM(___NOTHING,___R0)
___DEF_SLBL(1,___L1_main_23_0)
   ___ADJFP(-8)
   ___JUMPPRM(___NOTHING,___STK(2))
___END_P_SW
___END_P_COD

___END_M_SW
___END_M_COD

___BEGIN_LBL
 ___DEF_LBL_INTRO(___H_main_23_,"main#",___REF_FAL,25,0)
,___DEF_LBL_PROC(___H_main_23_,0,-1)
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,4,0,0x3f1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,8,0,0x3f03L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x3L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x7L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x7L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0xfL))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x7L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,0,0,0x3fL))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x3L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x3L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0x3L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,0,0xfL))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,5,1,0x6L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,8,1,0x3f06L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,4,4,0x3f0L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETI,4,4,0x3f0L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_RET(___H_main_23_,___IFD(___RETN,1,0,0x1L))
,___DEF_LBL_INTRO(___H_main_23_0,"main#0",___REF_FAL,2,0)
,___DEF_LBL_PROC(___H_main_23_0,1,-1)
,___DEF_LBL_RET(___H_main_23_0,___IFD(___RETN,2,1,0x3L))
___END_LBL

___BEGIN_MOD_PRM
___DEF_MOD_PRM(5,___G_main_23_,1)
___DEF_MOD_PRM(6,___G_main_23_0,27)
___END_MOD_PRM

___BEGIN_MOD_C_INIT
___END_MOD_C_INIT

___BEGIN_MOD_GLO
___DEF_MOD_GLO(5,___G_main_23_,1)
___DEF_MOD_GLO(6,___G_main_23_0,27)
___END_MOD_GLO

___BEGIN_MOD_SYM_KEY
___DEF_MOD_SYM(0,___S_main,"main")
___END_MOD_SYM_KEY

#endif
