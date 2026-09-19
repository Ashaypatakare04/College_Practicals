import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class BouncingBall extends JFrame {
    public BouncingBall() {
        setTitle("Bouncing Ball");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        BallPanel panel = new BallPanel();
        add(panel);
        setVisible(true);
    }
    public static void main(String[] args) {
        new BouncingBall();
    }
}
class BallPanel extends JPanel implements Runnable, MouseListener {
    int x = 50, y = 50;
    int dx = 2, dy = 2;
    int size = 30;
    Thread t;
    BallPanel() {
        addMouseListener(this);
    }
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.fillOval(x, y, size, size);
    }
    public void run() {
        while (true) {
            x += dx;
            y += dy;
            if (x <= 0 || x >= getWidth() - size)
                dx = -dx;
            if (y <= 0 || y >= getHeight() - size)
                dy = -dy;
            repaint();
            try {
                Thread.sleep(10);
            } catch (Exception e) {}
        }
    }
    public void mousePressed(MouseEvent e) {
        if (t == null) {
            t = new Thread(this);
            t.start();
        }
    }
    public void mouseClicked(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
}
