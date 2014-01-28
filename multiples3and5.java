import java.io.*;

public class multiples3and5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		long start = System.nanoTime();
		int sum=0;
		
		// Add multiples of 3
		for (int i=3;i<1000;i+=3) sum+=i;
		
		int bythree=0;
		
		//Add multiples of 5
		for (int i=5;i<1000;i+=5){
			bythree = (bythree+1)%3;
			
			if (bythree != 0) sum+=i;
		}
		System.out.println(sum);
		System.out.println("time: " + (System.nanoTime()-start));
	}

}
