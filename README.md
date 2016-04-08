
 Tejas Patil
---------------------

* BUG 1


	- **In bool ConnectX::inBounds(int w, int h)**
	<pre>
	bool ConnectX::inBounds(int w, int h)
	{
	bool inside;
	if( w>=width || w<0 )  
		inside = false;
	else                          	   
		inside = true;
	if( h<0 || h>=height )                      
		inside = false;
	else                           
		inside = true;
	return inside;
	}
	</pre>

	This function checks for given location
	if it inside board returns 'inside' = true else returns false

	but if input 'w' is out side board it sets value of 'inside' (w>=width || w<0) to false and it
	checks for input 'h' if its inside board then it sets value of 'inside'=false, but practically
	given location is out of board. So this function doesn't work properly.



* BUG 2

	- **In ConnectX::ConnectX(int wide, int high, int x)**

	If values of wide hign and x are less than or equal to zero then
	these values are set to Default values

	**LINE NO 9:**
	This doesn't consider the case when high with and x are equal to 1
	if it accepts 1 then following problems will occure

		- If dimention is det to 1x1 then  only one player can play
		- First player will always win because value of towin is 1
		- second player will never get chance to play.


* BUG 3

	- **In function  void ConnectX::placePiece(int column)**

	for bad input value of column -1 it gives codedump
	*** Error in `./ConnectXTest': free(): invalid next size (fast): 0x000000000181a5f0 ***
	Aborted (core dumped)


* BUG 4

	- **ConnectX::ConnectX(8,8,100)**

		* this function accepts value of 'towin' greater than the size of board
		* length of 'towin'  must be less than or equal to Diagonal length of board
