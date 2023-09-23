import java.util.Stack;

/**
 * Problem 3
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 * 
 */

public class tenThousandthPrime {
	
	static boolean[] isPrime;
	
	
	public static void main(String[] args) {
		
		Stack<Integer> primes = new Stack<Integer>();
		
		long start = System.nanoTime();
		int tenThousandthPrime = 0;
		
		int max = 20000000;
		isPrime = new boolean[max+1];
		
		// Initialize all numbers as prime
		for (int i=0;i<=max;i++){
			isPrime[i] = true;
		}
		
		// Mark all non-primes up to the square root
		for (int i=2;i<=max;i++){
			
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
			primes.add(i);
			
			// Stop if there are 10,001 elements in the stack
			if (primes.size()==10001){
				tenThousandthPrime = primes.pop();
				break;
			}
		}
		
		long end = System.nanoTime();
		
		System.out.println("time taken: "+((double)(end-start)/1000000));
		System.out.println("10,001st prime factor: "+tenThousandthPrime);
		
	}

}
