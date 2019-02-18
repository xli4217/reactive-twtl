# $ANTLR 3.4 twtl.g 2019-02-18 14:18:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

                       
license_text='''
    Lexer for TWTL formulae.
    Copyright (C) 2015-2016  Cristian Ioan Vasile <cvasile@bu.edu>
    Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab,
    Boston University

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__21=21
T__22=22
T__23=23
T__24=24
T__25=25
T__26=26
AND=4
CONCAT=5
DIGIT=6
FALSE=7
HGLETTER=8
HGLETTERALL=9
HOLD=10
INT=11
LETTER=12
LINECMT=13
LWLETTER=14
NOT=15
OR=16
PROP=17
TRUE=18
WITHIN=19
WS=20


class twtlLexer(Lexer):

    grammarFileName = "twtl.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(twtlLexer, self).__init__(input, state)

        self.delegates = []




                             
    def getAlphabet(self):
        return self.alphabet

    def setAlphabet(self, alphabet):
        self.alphabet = alphabet



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # twtl.g:36:5: ( '&' )
            # twtl.g:36:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "CONCAT"
    def mCONCAT(self, ):
        try:
            _type = CONCAT
            _channel = DEFAULT_CHANNEL

            # twtl.g:37:8: ( '*' )
            # twtl.g:37:10: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONCAT"



    # $ANTLR start "HOLD"
    def mHOLD(self, ):
        try:
            _type = HOLD
            _channel = DEFAULT_CHANNEL

            # twtl.g:38:6: ( 'H' )
            # twtl.g:38:8: 'H'
            pass 
            self.match(72)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "HOLD"



    # $ANTLR start "NOT"
    def mNOT(self, ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # twtl.g:39:5: ( '!' )
            # twtl.g:39:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # twtl.g:40:4: ( '|' )
            # twtl.g:40:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "WITHIN"
    def mWITHIN(self, ):
        try:
            _type = WITHIN
            _channel = DEFAULT_CHANNEL

            # twtl.g:41:8: ( 'W' )
            # twtl.g:41:10: 'W'
            pass 
            self.match(87)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WITHIN"



    # $ANTLR start "T__21"
    def mT__21(self, ):
        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # twtl.g:42:7: ( '(' )
            # twtl.g:42:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):
        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # twtl.g:43:7: ( ')' )
            # twtl.g:43:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):
        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # twtl.g:44:7: ( ',' )
            # twtl.g:44:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):
        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # twtl.g:45:7: ( '[' )
            # twtl.g:45:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):
        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # twtl.g:46:7: ( ']' )
            # twtl.g:46:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):
        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # twtl.g:47:7: ( '^' )
            # twtl.g:47:9: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__26"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):
        try:
            # twtl.g:133:13: ( ( '0' .. '9' ) )
            # twtl.g:
            pass 
            if (48 <= self.input.LA(1) <= 57):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LWLETTER"
    def mLWLETTER(self, ):
        try:
            # twtl.g:135:13: ( ( 'a' .. 'z' ) )
            # twtl.g:
            pass 
            if (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LWLETTER"



    # $ANTLR start "HGLETTER"
    def mHGLETTER(self, ):
        try:
            # twtl.g:137:13: ( ( 'A' .. 'Z' ) )
            # twtl.g:
            pass 
            if (65 <= self.input.LA(1) <= 90):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HGLETTER"



    # $ANTLR start "HGLETTERALL"
    def mHGLETTERALL(self, ):
        try:
            # twtl.g:139:13: ( ( 'A' .. 'G' ) | ( 'I' .. 'V' ) | ( 'X' .. 'Z' ) )
            # twtl.g:
            pass 
            if (65 <= self.input.LA(1) <= 71) or (73 <= self.input.LA(1) <= 86) or (88 <= self.input.LA(1) <= 90):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HGLETTERALL"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):
        try:
            # twtl.g:141:13: ( LWLETTER | HGLETTER )
            # twtl.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # twtl.g:144:5: ( ( '0' | ( ( '1' .. '9' ) ( DIGIT )* ) ) )
            # twtl.g:144:7: ( '0' | ( ( '1' .. '9' ) ( DIGIT )* ) )
            pass 
            # twtl.g:144:7: ( '0' | ( ( '1' .. '9' ) ( DIGIT )* ) )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 48) :
                alt2 = 1
            elif ((49 <= LA2_0 <= 57)) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # twtl.g:144:8: '0'
                pass 
                self.match(48)


            elif alt2 == 2:
                # twtl.g:144:14: ( ( '1' .. '9' ) ( DIGIT )* )
                pass 
                # twtl.g:144:14: ( ( '1' .. '9' ) ( DIGIT )* )
                # twtl.g:144:15: ( '1' .. '9' ) ( DIGIT )*
                pass 
                if (49 <= self.input.LA(1) <= 57):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                # twtl.g:144:25: ( DIGIT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((48 <= LA1_0 <= 57)) :
                        alt1 = 1


                    if alt1 == 1:
                        # twtl.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop1










            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # twtl.g:148:6: ( 'True' | 'true' )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 84) :
                alt3 = 1
            elif (LA3_0 == 116) :
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae


            if alt3 == 1:
                # twtl.g:148:8: 'True'
                pass 
                self.match("True")



            elif alt3 == 2:
                # twtl.g:148:17: 'true'
                pass 
                self.match("true")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):
        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # twtl.g:149:7: ( 'False' | 'false' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 70) :
                alt4 = 1
            elif (LA4_0 == 102) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # twtl.g:149:9: 'False'
                pass 
                self.match("False")



            elif alt4 == 2:
                # twtl.g:149:19: 'false'
                pass 
                self.match("false")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "PROP"
    def mPROP(self, ):
        try:
            _type = PROP
            _channel = DEFAULT_CHANNEL

            # twtl.g:152:7: ( ( ( LWLETTER | HGLETTERALL ) ( '_' | LETTER | DIGIT )* ) )
            # twtl.g:152:9: ( ( LWLETTER | HGLETTERALL ) ( '_' | LETTER | DIGIT )* )
            pass 
            # twtl.g:152:9: ( ( LWLETTER | HGLETTERALL ) ( '_' | LETTER | DIGIT )* )
            # twtl.g:152:10: ( LWLETTER | HGLETTERALL ) ( '_' | LETTER | DIGIT )*
            pass 
            if (65 <= self.input.LA(1) <= 71) or (73 <= self.input.LA(1) <= 86) or (88 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # twtl.g:152:34: ( '_' | LETTER | DIGIT )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or LA5_0 == 95 or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # twtl.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5





            #action start
                
            if str(self.text).lower() not in ('true', 'false'):
                self.alphabet.add(str(self.text));
                
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROP"



    # $ANTLR start "LINECMT"
    def mLINECMT(self, ):
        try:
            _type = LINECMT
            _channel = DEFAULT_CHANNEL

            # twtl.g:160:9: ( ( '//' ) (~ ( '\\n' | '\\r' ) )* )
            # twtl.g:160:11: ( '//' ) (~ ( '\\n' | '\\r' ) )*
            pass 
            # twtl.g:160:11: ( '//' )
            # twtl.g:160:12: '//'
            pass 
            self.match("//")





            # twtl.g:160:17: (~ ( '\\n' | '\\r' ) )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 9) or (11 <= LA6_0 <= 12) or (14 <= LA6_0 <= 65535)) :
                    alt6 = 1


                if alt6 == 1:
                    # twtl.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop6


            #action start
            self.skip()
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINECMT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # twtl.g:165:5: ( ( ( '\\n' | '\\r' | '\\f' | '\\t' | ' ' )+ ) )
            # twtl.g:165:7: ( ( '\\n' | '\\r' | '\\f' | '\\t' | ' ' )+ )
            pass 
            # twtl.g:165:7: ( ( '\\n' | '\\r' | '\\f' | '\\t' | ' ' )+ )
            # twtl.g:165:8: ( '\\n' | '\\r' | '\\f' | '\\t' | ' ' )+
            pass 
            # twtl.g:165:8: ( '\\n' | '\\r' | '\\f' | '\\t' | ' ' )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((9 <= LA7_0 <= 10) or (12 <= LA7_0 <= 13) or LA7_0 == 32) :
                    alt7 = 1


                if alt7 == 1:
                    # twtl.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1





            #action start
            self.skip()
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # twtl.g:1:8: ( AND | CONCAT | HOLD | NOT | OR | WITHIN | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | INT | TRUE | FALSE | PROP | LINECMT | WS )
        alt8 = 18
        LA8 = self.input.LA(1)
        if LA8 == 38:
            alt8 = 1
        elif LA8 == 42:
            alt8 = 2
        elif LA8 == 72:
            alt8 = 3
        elif LA8 == 33:
            alt8 = 4
        elif LA8 == 124:
            alt8 = 5
        elif LA8 == 87:
            alt8 = 6
        elif LA8 == 40:
            alt8 = 7
        elif LA8 == 41:
            alt8 = 8
        elif LA8 == 44:
            alt8 = 9
        elif LA8 == 91:
            alt8 = 10
        elif LA8 == 93:
            alt8 = 11
        elif LA8 == 94:
            alt8 = 12
        elif LA8 == 48 or LA8 == 49 or LA8 == 50 or LA8 == 51 or LA8 == 52 or LA8 == 53 or LA8 == 54 or LA8 == 55 or LA8 == 56 or LA8 == 57:
            alt8 = 13
        elif LA8 == 84:
            LA8_14 = self.input.LA(2)

            if (LA8_14 == 114) :
                LA8_21 = self.input.LA(3)

                if (LA8_21 == 117) :
                    LA8_25 = self.input.LA(4)

                    if (LA8_25 == 101) :
                        LA8_29 = self.input.LA(5)

                        if ((48 <= LA8_29 <= 57) or (65 <= LA8_29 <= 90) or LA8_29 == 95 or (97 <= LA8_29 <= 122)) :
                            alt8 = 16
                        else:
                            alt8 = 14

                    else:
                        alt8 = 16

                else:
                    alt8 = 16

            else:
                alt8 = 16

        elif LA8 == 116:
            LA8_15 = self.input.LA(2)

            if (LA8_15 == 114) :
                LA8_22 = self.input.LA(3)

                if (LA8_22 == 117) :
                    LA8_26 = self.input.LA(4)

                    if (LA8_26 == 101) :
                        LA8_30 = self.input.LA(5)

                        if ((48 <= LA8_30 <= 57) or (65 <= LA8_30 <= 90) or LA8_30 == 95 or (97 <= LA8_30 <= 122)) :
                            alt8 = 16
                        else:
                            alt8 = 14

                    else:
                        alt8 = 16

                else:
                    alt8 = 16

            else:
                alt8 = 16

        elif LA8 == 70:
            LA8_16 = self.input.LA(2)

            if (LA8_16 == 97) :
                LA8_23 = self.input.LA(3)

                if (LA8_23 == 108) :
                    LA8_27 = self.input.LA(4)

                    if (LA8_27 == 115) :
                        LA8_31 = self.input.LA(5)

                        if (LA8_31 == 101) :
                            LA8_34 = self.input.LA(6)

                            if ((48 <= LA8_34 <= 57) or (65 <= LA8_34 <= 90) or LA8_34 == 95 or (97 <= LA8_34 <= 122)) :
                                alt8 = 16
                            else:
                                alt8 = 15

                        else:
                            alt8 = 16

                    else:
                        alt8 = 16

                else:
                    alt8 = 16

            else:
                alt8 = 16

        elif LA8 == 102:
            LA8_17 = self.input.LA(2)

            if (LA8_17 == 97) :
                LA8_24 = self.input.LA(3)

                if (LA8_24 == 108) :
                    LA8_28 = self.input.LA(4)

                    if (LA8_28 == 115) :
                        LA8_32 = self.input.LA(5)

                        if (LA8_32 == 101) :
                            LA8_35 = self.input.LA(6)

                            if ((48 <= LA8_35 <= 57) or (65 <= LA8_35 <= 90) or LA8_35 == 95 or (97 <= LA8_35 <= 122)) :
                                alt8 = 16
                            else:
                                alt8 = 15

                        else:
                            alt8 = 16

                    else:
                        alt8 = 16

                else:
                    alt8 = 16

            else:
                alt8 = 16

        elif LA8 == 65 or LA8 == 66 or LA8 == 67 or LA8 == 68 or LA8 == 69 or LA8 == 71 or LA8 == 73 or LA8 == 74 or LA8 == 75 or LA8 == 76 or LA8 == 77 or LA8 == 78 or LA8 == 79 or LA8 == 80 or LA8 == 81 or LA8 == 82 or LA8 == 83 or LA8 == 85 or LA8 == 86 or LA8 == 88 or LA8 == 89 or LA8 == 90 or LA8 == 97 or LA8 == 98 or LA8 == 99 or LA8 == 100 or LA8 == 101 or LA8 == 103 or LA8 == 104 or LA8 == 105 or LA8 == 106 or LA8 == 107 or LA8 == 108 or LA8 == 109 or LA8 == 110 or LA8 == 111 or LA8 == 112 or LA8 == 113 or LA8 == 114 or LA8 == 115 or LA8 == 117 or LA8 == 118 or LA8 == 119 or LA8 == 120 or LA8 == 121 or LA8 == 122:
            alt8 = 16
        elif LA8 == 47:
            alt8 = 17
        elif LA8 == 9 or LA8 == 10 or LA8 == 12 or LA8 == 13 or LA8 == 32:
            alt8 = 18
        else:
            nvae = NoViableAltException("", 8, 0, self.input)

            raise nvae


        if alt8 == 1:
            # twtl.g:1:10: AND
            pass 
            self.mAND()



        elif alt8 == 2:
            # twtl.g:1:14: CONCAT
            pass 
            self.mCONCAT()



        elif alt8 == 3:
            # twtl.g:1:21: HOLD
            pass 
            self.mHOLD()



        elif alt8 == 4:
            # twtl.g:1:26: NOT
            pass 
            self.mNOT()



        elif alt8 == 5:
            # twtl.g:1:30: OR
            pass 
            self.mOR()



        elif alt8 == 6:
            # twtl.g:1:33: WITHIN
            pass 
            self.mWITHIN()



        elif alt8 == 7:
            # twtl.g:1:40: T__21
            pass 
            self.mT__21()



        elif alt8 == 8:
            # twtl.g:1:46: T__22
            pass 
            self.mT__22()



        elif alt8 == 9:
            # twtl.g:1:52: T__23
            pass 
            self.mT__23()



        elif alt8 == 10:
            # twtl.g:1:58: T__24
            pass 
            self.mT__24()



        elif alt8 == 11:
            # twtl.g:1:64: T__25
            pass 
            self.mT__25()



        elif alt8 == 12:
            # twtl.g:1:70: T__26
            pass 
            self.mT__26()



        elif alt8 == 13:
            # twtl.g:1:76: INT
            pass 
            self.mINT()



        elif alt8 == 14:
            # twtl.g:1:80: TRUE
            pass 
            self.mTRUE()



        elif alt8 == 15:
            # twtl.g:1:85: FALSE
            pass 
            self.mFALSE()



        elif alt8 == 16:
            # twtl.g:1:91: PROP
            pass 
            self.mPROP()



        elif alt8 == 17:
            # twtl.g:1:96: LINECMT
            pass 
            self.mLINECMT()



        elif alt8 == 18:
            # twtl.g:1:104: WS
            pass 
            self.mWS()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(twtlLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
