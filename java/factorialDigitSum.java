// Find the sum of the digits in the number 100!
public class factorialDigitSum {

	static int[] number = new int[200];
	
	public static void main(String[] args) {

		number[0] = 1;
		for (int i=100;i>1;i--) multiplyBy(i);
		
		int sum=0;
		
		for (int i=0;i<200;i++) sum += number[i];
		
		System.out.println("Sum: " + sum);
	}
	
	static void multiplyBy(int n){
		int carry = 0;
		
		for (int i=0;i<200;i++){
			number[i] = carry + (number[i]*n);
			carry = number[i] / 10;
			number[i] = number[i] % 10;
		}
	}

}
