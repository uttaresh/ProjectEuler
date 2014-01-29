import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;

public class maximumPathSum1 {

	static ArrayList<ArrayList<Integer>> triangle;
	static ArrayList<Long> sums;
	
	public static void main(String[] args) {

		triangle = new ArrayList<ArrayList<Integer>>();
		triangle.add(new ArrayList<Integer>());
		RandomAccessFile file = null;
		try {
			 file = new RandomAccessFile(new File("triangle.txt"),"rw");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		// Read in triangle structure from file to memory
		int temp=0;
		int current=0;
		int highestLevel = 0;
		try {
			while ((temp = file.read()) != -1){
				if (temp == ' ' || temp == '\r'){
						triangle.get(highestLevel).add(new Integer(current));
						current = 0;
					if (temp == '\r'){
						triangle.add(new ArrayList<Integer>());
						highestLevel++;
					}
				}else if (temp != '\n'){
					current = current*10 + temp - '0';
				}
			}
			triangle.get(highestLevel).add(new Integer(current));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		// Store sum totals from top to bottom in ArrayList
		sums = new ArrayList<Long>(); 
		findSums(0,0,0L);
		
		// Find largest sum
		Long largest=0L;
		for (Long s : sums){
			if (s > largest) largest = s;
		}
		
		System.out.println("largest sum: " + largest);
	}
	
	static void findSums(int level, int index, long sumSoFar){
		if (level >= triangle.size()){
			sums.add(new Long(sumSoFar));
		}else{
			findSums(level+1, index, (triangle.get(level).get(index)+sumSoFar));
			findSums(level+1, index+1, (triangle.get(level).get(index)+sumSoFar));
		}
	}
	

}
