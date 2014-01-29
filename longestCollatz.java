
public class longestCollatz {

	public static void main(String[] args) {

			int longestLength = 0;
			int start=0;
			
			for (int i=1;i<1000000;i++){
				int temp = CollatzLength((long)i);
				if ( temp > longestLength){
					longestLength = temp; 
					start = i;
				}
			}
			
			System.out.println(start);
		
		
	}
	
	static int CollatzLength(long n){

		int length=1;
		while (n != 1 ){
			if ((n & 1) == 0){
				// n is even
				n = n >> 1;
			}else
			{
				// n is odd
				n = 3*n + 1;
			}
			length++;
		}
		return length;
		
	}

}
