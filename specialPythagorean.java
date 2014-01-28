
public class specialPythagorean {

	public static void main(String[] args) {

		int x, y, z;
		int a=-1, b=-1, c=-1;
		
		for (x=1;x<=1000;x++){
			for (y=1;y<=(1000-x);y++){
				z = 1000 - x - y;
				if (x*x + y*y == z*z){
					a = x;
					b = y;
					c = z;
				}
			}
		}
		
		System.out.println("a: "+a+"  b: "+b+"  c: "+c);
		System.out.println("prod: " + (a*b*c));
	}

}
