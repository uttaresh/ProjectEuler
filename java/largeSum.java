import java.io.*;


public class largeSum {

	static int numbers[][] = new int[100][50];
	
	
	public static void main(String[] args) {

		RandomAccessFile file = null;
		
		int temp;
		int i=0,j=49;
		
		// Read numbers into 2D array
		try {
			file = new RandomAccessFile(new File("hundredNumbers.txt"), "r");
			while ( (temp = file.read()) != -1){
				if (temp == '\r'){
					i++;
					j=49;
					file.read();
				}else{
					numbers[i][j] = temp - '0';
					j--;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		// Add numbers
		int[] sum = new int[53];
		
		int carry = 0;
		
		for (int u=0;u<50;u++){
			sum[u] += carry;
			for (int v=0;v<100;v++){
				sum[u] += numbers[v][u];
			}
			carry = sum[u] / 10;
			sum[u] = sum[u] % 10;
		}
		
		sum[50] = carry%10;
		carry /= 10;
		
		sum[51] = carry%10;
		carry /= 10;
		
		if (carry > 9) System.out.println("Uh oh...!");
		sum[52] = carry;
		
		for (int u=51;u>=42;u--) System.out.print(sum[u]);
		
	}

}
