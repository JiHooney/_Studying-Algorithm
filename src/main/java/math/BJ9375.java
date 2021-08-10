package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BJ9375 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt( br.readLine() );
		
		int n = 0;
		String name;
		String type;
		int sum;
		StringTokenizer st;
		HashMap<String, Integer> hm = new HashMap<String, Integer>();
		while( t --> 0 ) {
			n = Integer.parseInt(br.readLine());
			for( int i=0; i<n; i++ ) {
				st = new StringTokenizer( br.readLine() );
				name = st.nextToken();
				type = st.nextToken();
				hm.put( type, hm.getOrDefault( type, 0 )+1 );
			}
			if( hm.size() == 1 ) sum = hm.size();
			else {
				sum = 0;
				for( String s : hm.keySet() ) {
					sum += hm.get( s );
				}
			}
			
			System.out.println( sum );
		}
	}
}