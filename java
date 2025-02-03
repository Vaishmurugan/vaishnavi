import java.util.*;
public class Main
{
	public static void main(String[] args) 
	{
	    Scanner sc=new Scanner(System.in);
	    int n,i,count=0;
	    n=sc.nextInt();
	    int arr[]=new int[n];
	    for(i=0;i<n;i++)
	    {
	        arr[i]=sc.nextInt();
	    }
	    for(i=0;i<n;i++)
	    {
	        if(arr[i]==0)
	        {
	            for(int j=i+1;j<n;j++)
	            {
	                if(arr[j]==1)
	                {
	                    count++;
	                }
	            }
	        }
	    }
		System.out.println(count);
	}
}
