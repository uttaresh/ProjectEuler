
public class HighlyDivisibleTriangleNumber {

	public static void main(String[] args) {

		long n=1;
		long curr=0;
		int numDivs=0;		
		
		while (numDivs<=500){
			curr = (n*(n+1))>>1;
			numDivs = numDivisors(curr);
			n++;
		}
		System.out.println(curr + "    " + numDivs);

		
	}
	
	static int numDivisors(long n){
		int ret=0;
		long sqrt = (long) Math.sqrt(n);
		for (long i=1;i<=sqrt;i++){
			if ((n%i)==0) ret+=2;
		}
		return ret;
	}

}
