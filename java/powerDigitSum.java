
public class powerDigitSum {

	static int size = 1200;
	static int[] number = new int[size];
	
	public static void main(String[] args) {
		
		// Init number to 1:
		for (int i=0;i<size;i++) number[i] = 0;
		number[0] = 1;
		
		// Double 1000 times
		for (int i=0;i<1000;i++) doubleIt();
		
		int sum=0;
		System.out.print("Number: ");
		int start = size-1;
		while(number[start]==0) start--;
		for (int i=start;i>=0;i--){
			System.out.print(number[i]);
		}		
		
		for (int i=size-1;i>=0;i--){
			sum += number[i];
		}

		System.out.println("\nSum: " + sum);
	}
	
	static void doubleIt(){
		int carry=0;
		for (int i=0;i<size;i++){
			int temp = ((number[i]<<1)+carry)%10;		
			carry = ((number[i]<<1)+carry)/10;
			number[i] = temp;
		}
		
	}

}
