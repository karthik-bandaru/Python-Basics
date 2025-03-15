
class Static{
    static int a=10;
    int b=20;
    @SuppressWarnings("static-access")
    public static void main(String args[])
    {
        Static t1=new Static();
        t1.a=80;
        t1.b=90;
        System.out.println(t1.a+".."+t1.b);      
    
        Static t2=new Static();
        System.out.println(t2.a+".."+t2.b);      

    }
}