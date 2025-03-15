import java.util.*;
class student{
    public static void main(String args[])
    {
        String name;
        int age;
        String mail;
        float cgpa;
        long mblnum;
        Scanner sc=new Scanner(System.in);
        System.out.println("student details");  
        System.out.println("enter name");
        name=sc.nextLine();
        System.out.println("enter age");
        age=sc.nextInt();
        System.out.println("enter mail");
        mail=sc.next();
        System.out.println("enter cgpa");
        cgpa=sc.nextFloat();
        System.out.println("enter num");
        mblnum=sc.nextLong();
    
        System.out.println("name is:"+name +"\n Age is:"+age + "\n cgpa is"+cgpa +"\n mblnum is"+mblnum +"\n mail is " +mail);
        sc.close();
        
    }
}
