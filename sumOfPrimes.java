import java.util.Stack;


public class sumOfPrimes {

	static boolean[] isPrime;
	
	public static void main(String[] args) {
		
		int tenThousandthPrime = 0;
		long sum=0;
		
		int max = 2000000;
		isPrime = new boolean[max+1];
		
		// Initialize all numbers as prime
		for (int i=0;i<=max;i++){
			isPrime[i] = true;
		}
		
		// Mark all non-primes up to the square root
		for (int i=2;i<max;i++){
			
			// Has number already been marked as not prime? Then skip
			if (isPrime[i]==false){
				continue;
			}
			
			// If the number has not been marked as prime so far, then
			// clearly it is prime. Mark out all its multiples as not
			// prime. 
			// Also add it to the stack of prime numbers
			for (int j=i*2;j<=max;j+=i){
				isPrime[j] = false;
			}			
			sum += i;
			
		}
		System.out.println("sum of first 2 mill primes: " + sum);
		
	}

}
