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
	/*  Disclaimer: This solution is not complete, and just happens to work for this input. The correct solution requires
            accounting for prime factors > sqrt of the target which I haven't implemented yet. It isn't obvious at all unless
            you're great at math, and required me to search around quite a bit on the internet to learn about prime factors.
            Here is a good explanation: https://math.stackexchange.com/a/883184/1225364
            What's remaining is to find the one possible prime factor > sqrt(target), and there can only be one. This one
            is calculated by starting with the target, and repeatedly dividing by all other prime factors that evenly divide
            it, or something of the sort. */

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
