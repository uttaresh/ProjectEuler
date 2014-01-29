
public class evenFib {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int sum=2;
		int r, rmin1, rmin2;
		rmin2=1;
		rmin1=2;
		r=3;
		while(r<=4000000){
			if((r&1)!=1) sum+=r;
			rmin2=rmin1;
			rmin1=r;
			r=rmin2+rmin1;
		}
		
		System.out.println(sum);
		
	}

}
