
public class largestPalindromeProd {

	public static void main(String[] args) {

		int largestPalindrome = 0;
		
		int temp;
		
		for (int i=999;i>=100;i--){
			for (int j=999;j>=100;j--){
				temp = i*j;
				if (temp == flip(temp)){
					if (temp>largestPalindrome)	largestPalindrome = temp;
				}
			}
		}
		
		System.out.println(largestPalindrome);
		
	}

	static int flip(int orig){
		int flipped = 0;
		while (orig != 0){
			flipped = flipped*10 + orig%10;
			orig /= 10;
		}
		return flipped;
	}
	
}
