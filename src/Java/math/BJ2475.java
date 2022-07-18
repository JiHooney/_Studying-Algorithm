package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ2475 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int sum = 0;
		while( st.hasMoreElements() ) 
			sum += Math.pow( Integer.parseInt( st.nextToken() ), 2 );
		System.out.println( sum%10 );
	}
}