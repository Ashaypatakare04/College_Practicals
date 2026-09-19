import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MouseCoordinatesGUI {
    public MouseCoordinatesGUI() {
        JFrame frame = new JFrame("Mouse Coordinates");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JLabel label = new JLabel("Move the mouse", SwingConstants.CENTER);
        frame.add(label);
        frame.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseMoved(MouseEvent e) {
                label.setText("X: " + e.getX() + ", Y: " + e.getY());
            }
        });
        frame.setSize(400, 300);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new MouseCoordinatesGUI(); }
}
