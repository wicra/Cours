import tp2.lib.Painter;
import java.awt.Color;

public class Roue {

    public static void dessinerRoue(Painter painter) {
        Point center = new Point(200, 200);
        int numBranches = 10; 
        double radius = 150;   

        double angleStep = 360.0 / numBranches;

        Point[] points = new Point[numBranches];

        for (int i = 0; i < numBranches; i++) {
            double angle = Math.toRadians(i * angleStep);  
            double x = center.getX() + radius * Math.cos(angle);
            double y = center.getY() + radius * Math.sin(angle);

            points[i] = new Point(x, y);
            center.drawLine(points[i], painter, Color.BLUE);
            points[i].draw(painter, Color.RED);
        }
        for (int i = 0; i < numBranches; i++) {
            Point p1 = points[i];
            Point p2 = points[(i + 1) % numBranches];
            p1.drawLine(p2, painter, Color.BLACK);
        }
    }
}
