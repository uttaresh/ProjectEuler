
public class thousandFib {

	static int[] f = new int[1000];
	static int[] fmin1 = new int[1000];
	static int[] fmin2 = new int[1000];
	
	static int[] temp = new int[1000];
	
	public static void main(String[] args) {

		// init F(2) and F(1):
		fmin2[0] = 1;
		fmin1[0] = 2;
		f[0] = 3;
		
		int i=4;
		while (f[999] == 0){			
			i++;
			computeCurrent();
			
			for (int j=3;j>=0;j--){
				while(f[j]==0 && j>0) j--;
			}
		}
		
		System.out.println("term number: "+i);
	}
	
	static void computeCurrent(){
		
		int carry = 0;
		temp = fmin2;
		fmin2 = fmin1;
		fmin1 = f;
		
		for (int i=0;i<1000;i++){
			temp[i] = carry + fmin1[i] + fmin2[i];
			carry = temp[i]/10;
			temp[i] = temp[i]%10;
		}
		f = temp;
		
		if (carry != 0) System.out.println("FAIL");

		
	}
}
