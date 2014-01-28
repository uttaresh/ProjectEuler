/*
 * If the numbers 1 to 5 are written out in words: one, two, three, four, 
 * five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * 
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written 
 * out in words, how many letters would be used?
 * 
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
 * forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
 * 20 letters. The use of "and" when writing out numbers is in compliance 
 * with British usage.
 * 
 */
public class numberLettersCount {

	
	
	
	public static void main(String[] args) {

		long sum=0;
		for (int i=1;i<=1000;i++){
			sum += letterCount(i);
		}
		
		System.out.println("letter count: " + sum);

	}

	static int letterCount(int n){
		
		int ret=0;
		
		// "One thousand"
		if (n==1000) return 11;
		
		// "X hundred"
		if (n>=100){
			ret += letterCount(n/100) + 7;		
			
			// "and"
			if (n%100 != 0) ret += 3;
			
		}
		
		// Whatever's in the ten's
		n = n%100;
		
		// Is there anything above twenty??
		if (n>=20){
			// Which ten's position?
			int tens = n/10;

			switch (tens){
			case 2:	ret += 6;
			break;
			case 3: ret += 6;
			break;
			case 4: ret += 5;
			break;
			case 5: ret += 5;
			break;
			case 6: ret += 5;
			break;
			case 7: ret += 7;
			break;
			case 8: ret += 6;
			break;
			case 9: ret += 6;
			}
			ret += letterCount(n%10);
			
		}else{
			switch (n){
			case 0: break;
			case 1: ret += 3;
			break;
			case 2: ret += 3;
			break;
			case 3: ret += 5;
			break;
			case 4: ret += 4;
			break;
			case 5: ret += 4;
			break;
			case 6: ret += 3;
			break;
			case 7: ret += 5;
			break;
			case 8: ret += 5;
			break;
			case 9: ret += 4;
			break;
			case 10: ret += 3;
			break;
			case 11: ret += 6;
			break;
			case 12: ret += 6;
			break;
			case 13: ret += 8;
			break;
			case 14: ret += 8;
			break;
			case 15: ret += 7;
			break;
			case 16: ret += 7;
			break;
			case 17: ret += 9;
			break;
			case 18: ret += 8;
			break;
			case 19: ret += 8;
			}
		}
		
		return ret;
	}
	
	
}
