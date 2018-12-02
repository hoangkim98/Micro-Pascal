# Generated from /home/bestjungvn/Desktop/PPL/assignment4/src/main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u023e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\2\7\2\u00b8\n")
        buf.write("\2\f\2\16\2\u00bb\13\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3\u00c3")
        buf.write("\n\3\f\3\16\3\u00c6\13\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00d0\n\4\f\4\16\4\u00d3\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\5,\u0194\n,\3-\3-\5-\u0198\n-\3-\3-\3-\6-\u019d\n-\r")
        buf.write("-\16-\u019e\5-\u01a1\n-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\3\67\5\67\u01b9\n\67\3\67\5\67\u01bc\n\67\5")
        buf.write("\67\u01be\n\67\3\67\5\67\u01c1\n\67\3\67\3\67\3\67\5\67")
        buf.write("\u01c6\n\67\5\67\u01c8\n\67\38\38\38\38\78\u01ce\n8\f")
        buf.write("8\168\u01d1\138\38\38\38\39\69\u01d7\n9\r9\169\u01d8\3")
        buf.write("9\39\3:\3:\3:\3:\7:\u01e1\n:\f:\16:\u01e4\13:\3:\3:\3")
        buf.write(":\5:\u01e9\n:\3:\3:\3;\3;\3;\3;\7;\u01f1\n;\f;\16;\u01f4")
        buf.write("\13;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3")
        buf.write("K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3")
        buf.write("T\3U\3U\3V\3V\3W\6W\u0230\nW\rW\16W\u0231\3X\6X\u0235")
        buf.write("\nX\rX\16X\u0236\3Y\3Y\5Y\u023b\nY\3Y\3Y\4\u00b9\u00c4")
        buf.write("\2Z\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\3\2$\4\2\f\f\17\17\n\2$$))^^ddhhppttvv\7\2\n\f\16\17")
        buf.write("$$))^^\5\2\13\f\16\17\"\"\7\2\n\13\16\16$$))^^\4\2CCc")
        buf.write("c\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2")
        buf.write("JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4")
        buf.write("\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWw")
        buf.write("w\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62;\4")
        buf.write("\2C\\c|\4\2--//\2\u023a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\3\u00b3\3\2\2\2\5\u00c0\3\2\2\2\7\u00cb\3")
        buf.write("\2\2\2\t\u00d6\3\2\2\2\13\u00db\3\2\2\2\r\u00e1\3\2\2")
        buf.write("\2\17\u00ea\3\2\2\2\21\u00ee\3\2\2\2\23\u00f1\3\2\2\2")
        buf.write("\25\u00f8\3\2\2\2\27\u00fb\3\2\2\2\31\u00fe\3\2\2\2\33")
        buf.write("\u0103\3\2\2\2\35\u0108\3\2\2\2\37\u010f\3\2\2\2!\u0115")
        buf.write("\3\2\2\2#\u011b\3\2\2\2%\u011f\3\2\2\2\'\u0128\3\2\2\2")
        buf.write(")\u0132\3\2\2\2+\u0136\3\2\2\2-\u013c\3\2\2\2/\u013f\3")
        buf.write("\2\2\2\61\u0144\3\2\2\2\63\u014c\3\2\2\2\65\u0154\3\2")
        buf.write("\2\2\67\u015b\3\2\2\29\u015f\3\2\2\2;\u0163\3\2\2\2=\u0166")
        buf.write("\3\2\2\2?\u016a\3\2\2\2A\u016e\3\2\2\2C\u0170\3\2\2\2")
        buf.write("E\u0172\3\2\2\2G\u0174\3\2\2\2I\u0176\3\2\2\2K\u0179\3")
        buf.write("\2\2\2M\u017b\3\2\2\2O\u017d\3\2\2\2Q\u017f\3\2\2\2S\u0182")
        buf.write("\3\2\2\2U\u0185\3\2\2\2W\u0193\3\2\2\2Y\u0197\3\2\2\2")
        buf.write("[\u01a2\3\2\2\2]\u01a4\3\2\2\2_\u01a6\3\2\2\2a\u01a8\3")
        buf.write("\2\2\2c\u01aa\3\2\2\2e\u01ac\3\2\2\2g\u01ae\3\2\2\2i\u01b1")
        buf.write("\3\2\2\2k\u01b3\3\2\2\2m\u01c7\3\2\2\2o\u01c9\3\2\2\2")
        buf.write("q\u01d6\3\2\2\2s\u01dc\3\2\2\2u\u01ec\3\2\2\2w\u01f7\3")
        buf.write("\2\2\2y\u01fa\3\2\2\2{\u01fc\3\2\2\2}\u01fe\3\2\2\2\177")
        buf.write("\u0200\3\2\2\2\u0081\u0202\3\2\2\2\u0083\u0204\3\2\2\2")
        buf.write("\u0085\u0206\3\2\2\2\u0087\u0208\3\2\2\2\u0089\u020a\3")
        buf.write("\2\2\2\u008b\u020c\3\2\2\2\u008d\u020e\3\2\2\2\u008f\u0210")
        buf.write("\3\2\2\2\u0091\u0212\3\2\2\2\u0093\u0214\3\2\2\2\u0095")
        buf.write("\u0216\3\2\2\2\u0097\u0218\3\2\2\2\u0099\u021a\3\2\2\2")
        buf.write("\u009b\u021c\3\2\2\2\u009d\u021e\3\2\2\2\u009f\u0220\3")
        buf.write("\2\2\2\u00a1\u0222\3\2\2\2\u00a3\u0224\3\2\2\2\u00a5\u0226")
        buf.write("\3\2\2\2\u00a7\u0228\3\2\2\2\u00a9\u022a\3\2\2\2\u00ab")
        buf.write("\u022c\3\2\2\2\u00ad\u022f\3\2\2\2\u00af\u0234\3\2\2\2")
        buf.write("\u00b1\u0238\3\2\2\2\u00b3\u00b4\7*\2\2\u00b4\u00b5\7")
        buf.write(",\2\2\u00b5\u00b9\3\2\2\2\u00b6\u00b8\13\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00bd\7+\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b")
        buf.write("\2\2\2\u00bf\4\3\2\2\2\u00c0\u00c4\7}\2\2\u00c1\u00c3")
        buf.write("\13\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c7\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7\177\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00ca\b\3\2\2\u00ca\6\3\2\2\2\u00cb\u00cc")
        buf.write("\7\61\2\2\u00cc\u00cd\7\61\2\2\u00cd\u00d1\3\2\2\2\u00ce")
        buf.write("\u00d0\n\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\b\4\2\2\u00d5\b")
        buf.write("\3\2\2\2\u00d6\u00d7\5\u00a5S\2\u00d7\u00d8\5\u0089E\2")
        buf.write("\u00d8\u00d9\5\u009fP\2\u00d9\u00da\5\u0087D\2\u00da\n")
        buf.write("\3\2\2\2\u00db\u00dc\5{>\2\u00dc\u00dd\5\u009bN\2\u00dd")
        buf.write("\u00de\5\u0081A\2\u00de\u00df\5y=\2\u00df\u00e0\5\u008d")
        buf.write("G\2\u00e0\f\3\2\2\2\u00e1\u00e2\5}?\2\u00e2\u00e3\5\u0095")
        buf.write("K\2\u00e3\u00e4\5\u0093J\2\u00e4\u00e5\5\u009fP\2\u00e5")
        buf.write("\u00e6\5\u0089E\2\u00e6\u00e7\5\u0093J\2\u00e7\u00e8\5")
        buf.write("\u00a1Q\2\u00e8\u00e9\5\u0081A\2\u00e9\16\3\2\2\2\u00ea")
        buf.write("\u00eb\5\u0083B\2\u00eb\u00ec\5\u0095K\2\u00ec\u00ed\5")
        buf.write("\u009bN\2\u00ed\20\3\2\2\2\u00ee\u00ef\5\u009fP\2\u00ef")
        buf.write("\u00f0\5\u0095K\2\u00f0\22\3\2\2\2\u00f1\u00f2\5\177@")
        buf.write("\2\u00f2\u00f3\5\u0095K\2\u00f3\u00f4\5\u00a5S\2\u00f4")
        buf.write("\u00f5\5\u0093J\2\u00f5\u00f6\5\u009fP\2\u00f6\u00f7\5")
        buf.write("\u0095K\2\u00f7\24\3\2\2\2\u00f8\u00f9\5\177@\2\u00f9")
        buf.write("\u00fa\5\u0095K\2\u00fa\26\3\2\2\2\u00fb\u00fc\5\u0089")
        buf.write("E\2\u00fc\u00fd\5\u0083B\2\u00fd\30\3\2\2\2\u00fe\u00ff")
        buf.write("\5\u009fP\2\u00ff\u0100\5\u0087D\2\u0100\u0101\5\u0081")
        buf.write("A\2\u0101\u0102\5\u0093J\2\u0102\32\3\2\2\2\u0103\u0104")
        buf.write("\5\u0081A\2\u0104\u0105\5\u008fH\2\u0105\u0106\5\u009d")
        buf.write("O\2\u0106\u0107\5\u0081A\2\u0107\34\3\2\2\2\u0108\u0109")
        buf.write("\5\u009bN\2\u0109\u010a\5\u0081A\2\u010a\u010b\5\u009f")
        buf.write("P\2\u010b\u010c\5\u00a1Q\2\u010c\u010d\5\u009bN\2\u010d")
        buf.write("\u010e\5\u0093J\2\u010e\36\3\2\2\2\u010f\u0110\5\u00a5")
        buf.write("S\2\u0110\u0111\5\u0087D\2\u0111\u0112\5\u0089E\2\u0112")
        buf.write("\u0113\5\u008fH\2\u0113\u0114\5\u0081A\2\u0114 \3\2\2")
        buf.write("\2\u0115\u0116\5{>\2\u0116\u0117\5\u0081A\2\u0117\u0118")
        buf.write("\5\u0085C\2\u0118\u0119\5\u0089E\2\u0119\u011a\5\u0093")
        buf.write("J\2\u011a\"\3\2\2\2\u011b\u011c\5\u0081A\2\u011c\u011d")
        buf.write("\5\u0093J\2\u011d\u011e\5\177@\2\u011e$\3\2\2\2\u011f")
        buf.write("\u0120\5\u0083B\2\u0120\u0121\5\u00a1Q\2\u0121\u0122\5")
        buf.write("\u0093J\2\u0122\u0123\5}?\2\u0123\u0124\5\u009fP\2\u0124")
        buf.write("\u0125\5\u0089E\2\u0125\u0126\5\u0095K\2\u0126\u0127\5")
        buf.write("\u0093J\2\u0127&\3\2\2\2\u0128\u0129\5\u0097L\2\u0129")
        buf.write("\u012a\5\u009bN\2\u012a\u012b\5\u0095K\2\u012b\u012c\5")
        buf.write("}?\2\u012c\u012d\5\u0081A\2\u012d\u012e\5\177@\2\u012e")
        buf.write("\u012f\5\u00a1Q\2\u012f\u0130\5\u009bN\2\u0130\u0131\5")
        buf.write("\u0081A\2\u0131(\3\2\2\2\u0132\u0133\5\u00a3R\2\u0133")
        buf.write("\u0134\5y=\2\u0134\u0135\5\u009bN\2\u0135*\3\2\2\2\u0136")
        buf.write("\u0137\5y=\2\u0137\u0138\5\u009bN\2\u0138\u0139\5\u009b")
        buf.write("N\2\u0139\u013a\5y=\2\u013a\u013b\5\u00a9U\2\u013b,\3")
        buf.write("\2\2\2\u013c\u013d\5\u0095K\2\u013d\u013e\5\u0083B\2\u013e")
        buf.write(".\3\2\2\2\u013f\u0140\5\u009bN\2\u0140\u0141\5\u0081A")
        buf.write("\2\u0141\u0142\5y=\2\u0142\u0143\5\u008fH\2\u0143\60\3")
        buf.write("\2\2\2\u0144\u0145\5{>\2\u0145\u0146\5\u0095K\2\u0146")
        buf.write("\u0147\5\u0095K\2\u0147\u0148\5\u008fH\2\u0148\u0149\5")
        buf.write("\u0081A\2\u0149\u014a\5y=\2\u014a\u014b\5\u0093J\2\u014b")
        buf.write("\62\3\2\2\2\u014c\u014d\5\u0089E\2\u014d\u014e\5\u0093")
        buf.write("J\2\u014e\u014f\5\u009fP\2\u014f\u0150\5\u0081A\2\u0150")
        buf.write("\u0151\5\u0085C\2\u0151\u0152\5\u0081A\2\u0152\u0153\5")
        buf.write("\u009bN\2\u0153\64\3\2\2\2\u0154\u0155\5\u009dO\2\u0155")
        buf.write("\u0156\5\u009fP\2\u0156\u0157\5\u009bN\2\u0157\u0158\5")
        buf.write("\u0089E\2\u0158\u0159\5\u0093J\2\u0159\u015a\5\u0085C")
        buf.write("\2\u015a\66\3\2\2\2\u015b\u015c\5\u0093J\2\u015c\u015d")
        buf.write("\5\u0095K\2\u015d\u015e\5\u009fP\2\u015e8\3\2\2\2\u015f")
        buf.write("\u0160\5y=\2\u0160\u0161\5\u0093J\2\u0161\u0162\5\177")
        buf.write("@\2\u0162:\3\2\2\2\u0163\u0164\5\u0095K\2\u0164\u0165")
        buf.write("\5\u009bN\2\u0165<\3\2\2\2\u0166\u0167\5\177@\2\u0167")
        buf.write("\u0168\5\u0089E\2\u0168\u0169\5\u00a3R\2\u0169>\3\2\2")
        buf.write("\2\u016a\u016b\5\u0091I\2\u016b\u016c\5\u0095K\2\u016c")
        buf.write("\u016d\5\177@\2\u016d@\3\2\2\2\u016e\u016f\7-\2\2\u016f")
        buf.write("B\3\2\2\2\u0170\u0171\7/\2\2\u0171D\3\2\2\2\u0172\u0173")
        buf.write("\7,\2\2\u0173F\3\2\2\2\u0174\u0175\7\61\2\2\u0175H\3\2")
        buf.write("\2\2\u0176\u0177\7>\2\2\u0177\u0178\7@\2\2\u0178J\3\2")
        buf.write("\2\2\u0179\u017a\7?\2\2\u017aL\3\2\2\2\u017b\u017c\7>")
        buf.write("\2\2\u017cN\3\2\2\2\u017d\u017e\7@\2\2\u017eP\3\2\2\2")
        buf.write("\u017f\u0180\7>\2\2\u0180\u0181\7?\2\2\u0181R\3\2\2\2")
        buf.write("\u0182\u0183\7@\2\2\u0183\u0184\7?\2\2\u0184T\3\2\2\2")
        buf.write("\u0185\u0186\7<\2\2\u0186\u0187\7?\2\2\u0187V\3\2\2\2")
        buf.write("\u0188\u0189\5\u009fP\2\u0189\u018a\5\u009bN\2\u018a\u018b")
        buf.write("\5\u00a1Q\2\u018b\u018c\5\u0081A\2\u018c\u0194\3\2\2\2")
        buf.write("\u018d\u018e\5\u0083B\2\u018e\u018f\5y=\2\u018f\u0190")
        buf.write("\5\u008fH\2\u0190\u0191\5\u009dO\2\u0191\u0192\5\u0081")
        buf.write("A\2\u0192\u0194\3\2\2\2\u0193\u0188\3\2\2\2\u0193\u018d")
        buf.write("\3\2\2\2\u0194X\3\2\2\2\u0195\u0198\7a\2\2\u0196\u0198")
        buf.write("\5\u00afX\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u01a0\3\2\2\2\u0199\u019d\7a\2\2\u019a\u019d\5\u00af")
        buf.write("X\2\u019b\u019d\5\u00adW\2\u019c\u0199\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019c\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1Z\3\2\2")
        buf.write("\2\u01a2\u01a3\7*\2\2\u01a3\\\3\2\2\2\u01a4\u01a5\7+\2")
        buf.write("\2\u01a5^\3\2\2\2\u01a6\u01a7\7]\2\2\u01a7`\3\2\2\2\u01a8")
        buf.write("\u01a9\7_\2\2\u01a9b\3\2\2\2\u01aa\u01ab\7<\2\2\u01ab")
        buf.write("d\3\2\2\2\u01ac\u01ad\7=\2\2\u01adf\3\2\2\2\u01ae\u01af")
        buf.write("\7\60\2\2\u01af\u01b0\7\60\2\2\u01b0h\3\2\2\2\u01b1\u01b2")
        buf.write("\7.\2\2\u01b2j\3\2\2\2\u01b3\u01b4\5\u00adW\2\u01b4l\3")
        buf.write("\2\2\2\u01b5\u01c0\5\u00adW\2\u01b6\u01b8\7\60\2\2\u01b7")
        buf.write("\u01b9\5\u00adW\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2")
        buf.write("\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01bc\5\u00b1Y\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2")
        buf.write("\u01bd\u01b6\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c1\3")
        buf.write("\2\2\2\u01bf\u01c1\5\u00b1Y\2\u01c0\u01bd\3\2\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c8\3\2\2\2\u01c2\u01c3\7\60\2")
        buf.write("\2\u01c3\u01c5\5\u00adW\2\u01c4\u01c6\5\u00b1Y\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write("\u01c7\u01b5\3\2\2\2\u01c7\u01c2\3\2\2\2\u01c8n\3\2\2")
        buf.write("\2\u01c9\u01cf\7$\2\2\u01ca\u01cb\7^\2\2\u01cb\u01ce\t")
        buf.write("\3\2\2\u01cc\u01ce\n\4\2\2\u01cd\u01ca\3\2\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d2\u01d3\7$\2\2\u01d3\u01d4\b8\3\2\u01d4p\3\2\2\2")
        buf.write("\u01d5\u01d7\t\5\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01db\b9\2\2\u01dbr\3\2\2\2\u01dc\u01e2")
        buf.write("\7$\2\2\u01dd\u01de\7^\2\2\u01de\u01e1\t\3\2\2\u01df\u01e1")
        buf.write("\n\4\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01df\3\2\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e8\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7")
        buf.write("^\2\2\u01e6\u01e9\n\3\2\2\u01e7\u01e9\t\6\2\2\u01e8\u01e5")
        buf.write("\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01eb\b:\4\2\u01ebt\3\2\2\2\u01ec\u01f2\7$\2\2\u01ed")
        buf.write("\u01ee\7^\2\2\u01ee\u01f1\t\3\2\2\u01ef\u01f1\n\4\2\2")
        buf.write("\u01f0\u01ed\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3")
        buf.write("\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\b;\5\2\u01f6")
        buf.write("v\3\2\2\2\u01f7\u01f8\13\2\2\2\u01f8\u01f9\b<\6\2\u01f9")
        buf.write("x\3\2\2\2\u01fa\u01fb\t\7\2\2\u01fbz\3\2\2\2\u01fc\u01fd")
        buf.write("\t\b\2\2\u01fd|\3\2\2\2\u01fe\u01ff\t\t\2\2\u01ff~\3\2")
        buf.write("\2\2\u0200\u0201\t\n\2\2\u0201\u0080\3\2\2\2\u0202\u0203")
        buf.write("\t\13\2\2\u0203\u0082\3\2\2\2\u0204\u0205\t\f\2\2\u0205")
        buf.write("\u0084\3\2\2\2\u0206\u0207\t\r\2\2\u0207\u0086\3\2\2\2")
        buf.write("\u0208\u0209\t\16\2\2\u0209\u0088\3\2\2\2\u020a\u020b")
        buf.write("\t\17\2\2\u020b\u008a\3\2\2\2\u020c\u020d\t\20\2\2\u020d")
        buf.write("\u008c\3\2\2\2\u020e\u020f\t\21\2\2\u020f\u008e\3\2\2")
        buf.write("\2\u0210\u0211\t\22\2\2\u0211\u0090\3\2\2\2\u0212\u0213")
        buf.write("\t\23\2\2\u0213\u0092\3\2\2\2\u0214\u0215\t\24\2\2\u0215")
        buf.write("\u0094\3\2\2\2\u0216\u0217\t\25\2\2\u0217\u0096\3\2\2")
        buf.write("\2\u0218\u0219\t\26\2\2\u0219\u0098\3\2\2\2\u021a\u021b")
        buf.write("\t\27\2\2\u021b\u009a\3\2\2\2\u021c\u021d\t\30\2\2\u021d")
        buf.write("\u009c\3\2\2\2\u021e\u021f\t\31\2\2\u021f\u009e\3\2\2")
        buf.write("\2\u0220\u0221\t\32\2\2\u0221\u00a0\3\2\2\2\u0222\u0223")
        buf.write("\t\33\2\2\u0223\u00a2\3\2\2\2\u0224\u0225\t\34\2\2\u0225")
        buf.write("\u00a4\3\2\2\2\u0226\u0227\t\35\2\2\u0227\u00a6\3\2\2")
        buf.write("\2\u0228\u0229\t\36\2\2\u0229\u00a8\3\2\2\2\u022a\u022b")
        buf.write("\t\37\2\2\u022b\u00aa\3\2\2\2\u022c\u022d\t \2\2\u022d")
        buf.write("\u00ac\3\2\2\2\u022e\u0230\t!\2\2\u022f\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3")
        buf.write("\2\2\2\u0232\u00ae\3\2\2\2\u0233\u0235\t\"\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0237\u00b0\3\2\2\2\u0238\u023a\t\13\2")
        buf.write("\2\u0239\u023b\t#\2\2\u023a\u0239\3\2\2\2\u023a\u023b")
        buf.write("\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\5\u00adW\2\u023d")
        buf.write("\u00b2\3\2\2\2\34\2\u00b9\u00c4\u00d1\u0193\u0197\u019c")
        buf.write("\u019e\u01a0\u01b8\u01bb\u01bd\u01c0\u01c5\u01c7\u01cd")
        buf.write("\u01cf\u01d8\u01e0\u01e2\u01e8\u01f0\u01f2\u0231\u0236")
        buf.write("\u023a\7\b\2\2\38\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_1 = 1
    COMMENT_2 = 2
    COMMENT_3 = 3
    WITH = 4
    BREAK = 5
    CONTINUE = 6
    FOR = 7
    TO = 8
    DOWNTO = 9
    DO = 10
    IF = 11
    THEN = 12
    ELSE = 13
    RETURN = 14
    WHILE = 15
    BEGIN = 16
    END = 17
    FUNCTION = 18
    PROCEDURE = 19
    VAR = 20
    ARRAY = 21
    OF = 22
    REAL = 23
    BOOLEAN = 24
    INTEGER = 25
    STRING = 26
    NOT = 27
    AND = 28
    OR = 29
    DIV = 30
    MOD = 31
    PLUS = 32
    SUBTRACTION = 33
    MULTIPLICATION = 34
    DIVISION = 35
    NOT_EQUAL = 36
    EQUAL = 37
    LESS = 38
    GREATER = 39
    LE = 40
    GE = 41
    ASSIGN = 42
    BOOLLIT = 43
    ID = 44
    LB = 45
    RB = 46
    LS = 47
    RS = 48
    COLON = 49
    SEMI = 50
    DOUBLE_DOT = 51
    COMMA = 52
    INTLIT = 53
    FLOATLIT = 54
    STRINGLIT = 55
    WS = 56
    ILLEGAL_ESCAPE = 57
    UNCLOSE_STRING = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'('", "')'", "'['", "']'", "':'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_1", "COMMENT_2", "COMMENT_3", "WITH", "BREAK", "CONTINUE", 
            "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
            "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "PLUS", "SUBTRACTION", "MULTIPLICATION", 
            "DIVISION", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LE", "GE", 
            "ASSIGN", "BOOLLIT", "ID", "LB", "RB", "LS", "RS", "COLON", 
            "SEMI", "DOUBLE_DOT", "COMMA", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT_1", "COMMENT_2", "COMMENT_3", "WITH", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "ARRAY", "OF", "REAL", "BOOLEAN", 
                  "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", "MOD", 
                  "PLUS", "SUBTRACTION", "MULTIPLICATION", "DIVISION", "NOT_EQUAL", 
                  "EQUAL", "LESS", "GREATER", "LE", "GE", "ASSIGN", "BOOLLIT", 
                  "ID", "LB", "RB", "LS", "RS", "COLON", "SEMI", "DOUBLE_DOT", 
                  "COMMA", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR", "A", "B", "C", "D", "E", 
                  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "DIGIT", 
                  "LETTER", "EXPONENT" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRINGLIT_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	    self.text = self.text[1:len(self.text)-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	    raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ErrorToken(self.text)
     


