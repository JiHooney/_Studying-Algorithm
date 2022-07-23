package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ1436 {
	private static int n;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt( br.readLine() );
		
		int num = 666;
		int cnt = 1;
		
		while( cnt != n ) {
			num++;
			if( String.valueOf(num).contains("666") ) cnt++;
		}
		
		System.out.println( num );
	}
}