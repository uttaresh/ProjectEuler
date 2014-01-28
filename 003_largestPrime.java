import java.util.Stack;

/**
 * Problem 3
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 * 
 */

public class largestPrime {

	static long target = 600851475143L;
	
	static boolean[] isPrime;
	
	
	public static void main(String[] args) {
		
		Stack<Integer> primes = new Stack<Integer>();
		
		long start = System.nanoTime();
		int sqrt = (int) Math.sqrt(target);
		
		isPrime = new boolean[sqrt+1];
		
		// Initialize all numbers as prime
		for (int i=0;i<=sqrt;i++){
			isPrime[i] = true;
		}
		
		// Mark all non-primes up to the square root
		for (int i=2;i<=sqrt;i++){
			
			// Has number already been marked as not prime? Then skip
			if (isPrime[i]==false){
				continue;
			}
			
			// If the number has not been marked as prime so far, then
			// clearly it is prime. Mark out all its multiples as not
			// prime. 
			// Also add it to the stack of prime numbers
			for (int j=i*2;j<=sqrt;j+=i){
				isPrime[j] = false;
			}			
			primes.add(i);
		}
		
		// Pop from stack till you find the first prime that is a factor of
		// the target
		int largestPrimeFactor = 1;
		int top=0;
		while (primes.empty()==false){
			top = primes.pop();
			if (target%top==0){
				largestPrimeFactor = top;
				break;
			}
		}
		
		long end = System.nanoTime();
		
		System.out.println("time taken: "+((double)(end-start)/1000000));
		System.out.println("Largest prime factor: "+largestPrimeFactor);
		
	}

}
