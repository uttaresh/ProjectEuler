// Lattice paths
public class latticePaths {

	// dynamic programming
	static long[][] waysLUT = new long[21][21];
	
	public static void main(String[] args) {
		
		// init ways LUT
		for (int i=0;i<21;i++){
			for (int j=0;j<21;j++) waysLUT[i][j] = -1;
		}

		long start = System.nanoTime();
		long numWays = ways(20,20);
		long end = System.nanoTime();
		System.out.println("Routes in a 20x20 grid: " + numWays);
		System.out.println("Time taken: " + (end-start)/1000 + "." + (end-start)%1000 +"us");

	}
	
	static long ways(int width, int depth){
		
		if (waysLUT[width][depth] != -1) return waysLUT[width][depth];
		
		// Base case:
		if (width<=0 && depth<=0) return (waysLUT[width][depth] = 1);
		else if (width<=0) return (waysLUT[width][depth] =  ways(width,depth-1) );
		else if (depth<=0) return (waysLUT[width][depth] =  ways(width-1,depth) );

		return (waysLUT[width][depth] = (ways(width,depth-1) + ways(width-1,depth)));
	}
	

}
