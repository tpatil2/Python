# Python

BUGS FOUND
==============


**This will be Bold**

## In ConnectX::ConnectX(int wide, int high, int x)

If values of wide hign and x are less than or equal to zero then
these values are set to Default values
but This doesn't consider the case when high with and x are equal to 1
if it accepts 1 then following problems will occure

- If dimention is det to 1x1 then  only one player can play
- First player will always win because value of towin is 1
- second player will never get chance to play.
