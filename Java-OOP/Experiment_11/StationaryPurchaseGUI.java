import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class StationaryPurchaseGUI {
    public StationaryPurchaseGUI() {
        JFrame f = new JFrame("Stationary Purchase System");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLayout(new FlowLayout());
        JCheckBox n = new JCheckBox("Notebook @ 50"), p = new JCheckBox("Pen @ 30"), pl = new JCheckBox("Pencil @ 10");
        JButton b = new JButton("Order");
        f.add(n); f.add(p); f.add(pl); f.add(b);
        b.addActionListener(e -> {
            double t = 0;
            StringBuilder s = new StringBuilder();
            if (n.isSelected()) t += ask(f, "Notebook", 50, s);
            if (p.isSelected()) t += ask(f, "Pen", 30, s);
            if (pl.isSelected()) t += ask(f, "Pencil", 10, s);
            if (t > 0) {
                JOptionPane.showMessageDialog(f, s.toString() + "Total: " + t);
                JOptionPane.showMessageDialog(f, "Successfully Ordered!", "Alert", JOptionPane.INFORMATION_MESSAGE);
            }
        });
        f.setSize(400, 200);
        f.setVisible(true);
    }
    private double ask(JFrame f, String item, int price, StringBuilder s) {
        String qStr = JOptionPane.showInputDialog("Quantity for " + item + ":");
        int q = Integer.parseInt(qStr);
        s.append(item).append(" x").append(q).append(": ").append(q * price).append("\n");
        return q * price;
    }
    public static void main(String[] args) { new StationaryPurchaseGUI(); }
}
