import tp2.lib.Painter;
import java.awt.Color;

public class Point {
    private double x;
    private double y;
    // Constructeur
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public void draw(Painter painter, Color color) {
        painter.addPoint(this.x, this.y, color);
    }
    public void drawLine(Point p, Painter painter, Color color) {
        painter.addLine(this.x, this.y, p.x, p.y, color);
    }
    public Point translate(double dx, double dy) {
        return new Point(this.x + dx, this.y + dy);
    }
    public Point rotate(double angle) {
        double radian = Math.toRadians(angle);
        double newX = this.x * Math.cos(radian) - this.y * Math.sin(radian);
        double newY = this.x * Math.sin(radian) + this.y * Math.cos(radian);
        return new Point(newX, newY);
    }
    public double getX() {
        return this.x;
    }
    public double getY() {
        return this.y;
    }
}
