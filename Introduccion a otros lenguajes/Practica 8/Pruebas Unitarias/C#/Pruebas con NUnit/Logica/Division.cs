public class Division {
    public static double Dividir(double a, double b) {
        if (b == 0) throw new DivideByZeroException("División por cero");
        return a / b;
    }
}