public class anonymousObject {
    int object1;

    public void display(int n) {
        object1 = n;
        System.out.println(object1);
    }

    public static void main(String[] args) {
        anonymousObject.display(5);

    }
}
