package dataStructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ11866_1 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer( br.readLine() );
		int n = Integer.parseInt( st.nextToken() );
		int k = Integer.parseInt( st.nextToken() );
		
		Queue<Integer> q = new LinkedList<Integer>();
		
		for( int i=1; i<=n; i++ ) q.add( i );
		
		StringBuffer sb = new StringBuffer();
		sb.append( "<" );
		
		while( q.size() > 1 ) {
			for( int i=0; i<k-1; i++ ) q.offer( q.poll() );
			
			sb.append( q.poll() ).append( ", " );
		}
		
		sb.append( q.poll() ).append( ">" );
		System.out.println( sb );
	}
}